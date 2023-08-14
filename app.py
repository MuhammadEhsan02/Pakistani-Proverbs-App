from flask import Flask, render_template
import random

app = Flask(__name__)

proverbs_data = [
    {"proverb": "Darya kinare ek makan", "explanation": "A house by the riverbank."},
    {"proverb": "Dil ka rasta pet se ho ke jata hai", "explanation": "The path to the heart is through the stomach."},
    {"proverb": "Jitni lambi chaadar ho, utna pair pasara ho", "explanation": "Stretch your legs only as much as your blanket allows."},
    {"proverb": "Mitti pao bhaata naan", "explanation": "Bread made with dirty hands."},
    {"proverb": "Chor ki daarhi mein tinka", "explanation": "A thorn in the beard of a thief."},
    {"proverb": "Jab miyan biwi raazi, to kya karega qazi", "explanation": "When the husband and wife agree, what can the judge do?"},
    {"proverb": "Chaar din ki chandni phir andheri raat", "explanation": "A brief period of happiness followed by darkness."},
    {"proverb": "Bandar kya jaane adrak ka swad", "explanation": "What does a monkey know about the taste of ginger? (A fool does not appreciate the value of something)"},
    {"proverb": "Jaisa des, waisa bhesh", "explanation": "When in Rome, do as the Romans do."},
    {"proverb": "Jhoot ke paon nahi hote", "explanation": "Lies have no legs."},
    {"proverb": "Neki kar dariya mein daal", "explanation": "Do good and throw it into the river (without expecting anything in return)."},
    {"proverb": "Kahan raja bhoj, kahan gangu teli", "explanation": "As different as chalk and cheese."},
    {"proverb": "Baagh mein chhora, kuye mein sona", "explanation": "A thief in the garden, gold in the well (a situation with hidden treasures)."},
    {"proverb": "Duniya daari aur darvesh ki chaadar", "explanation": "The world's ways and the saint's cloak (opposite ways of living)."},
    {"proverb": "Ghar ki murgi daal barabar", "explanation": "One doesn't value what's easily available."},
    {"proverb": "Andhon mein kana raja", "explanation": "In the land of the blind, the one-eyed man is king."},
    {"proverb": "Bhains ke aage been bajana", "explanation": "Playing the flute to a buffalo (wasting effort on an unappreciative audience)."},
    {"proverb": "Ghar ki murghi dal barabar", "explanation": "The home-cooked chicken is equivalent to lentils (we often fail to appreciate what's easily available)."},
    {"proverb": "Ghar ki murgi dal barabar", "explanation": "A homely hen is equivalent to lentils (things that are familiar might not seem exciting)."},
    {"proverb": "Ab pachhtaye kya hot jab chidiya chug gayi khet", "explanation": "What's the use of regretting now, when the bird has eaten the harvest?"},
    {"proverb": "Ek myan mein do talwarein nahi reh sakti", "explanation": "Two swords cannot be in one scabbard (two incompatible things/people cannot coexist)."},
    {"proverb": "Jaisa des, waisa bhes", "explanation": "A person adopts the ways of the place they live."},
    {"proverb": "Laato ke bhoot, baato se nahi maante", "explanation": "Spirits of kicks, don't get convinced by words."},
    {"proverb": "Laaton ke bhoot baaton se nahi maante", "explanation": "Spirits of kicks, don't listen to words."},
    {"proverb": "Chaar din ki chandni, phir andheri raat", "explanation": "A brief period of happiness followed by darkness."},
    {"proverb": "Loha lohe ko kaat ta hai", "explanation": "Iron cuts iron (like seeks like)."},
    {"proverb": "Har qadam par khushi", "explanation": "Happiness at every step."},
    {"proverb": "Har chamakne wale cheez sona nahi hoti", "explanation": "Not everything that shines is gold."},
    {"proverb": "Jaise ko taisa", "explanation": "As you sow, so shall you reap."},
    {"proverb": "Doosron ko pehchane bina khud ko pehchano", "explanation": "Know yourself before judging others."},
    {"proverb": "Nek raah mein andhera", "explanation": "There's darkness on the path of righteousness."},
    {"proverb": "Chup kar jao varna mian bana doonga", "explanation": "Shut up, or I'll make you look bad."},
    {"proverb": "Chor chor mausere bhai", "explanation": "Thieves are of the same feather."},
    {"proverb": "Jitni chadar ho utne pair failane chahiye", "explanation": "Stretch your legs according to the length of the blanket."},
    {"proverb": "Jaisi karni waisi bharni", "explanation": "As you sow, so shall you reap."},
    {"proverb": "Chor ki daadhi mein tinka", "explanation": "A thorn in a thief's beard."},
    {"proverb": "Ghar ki baat ghar mein reh jati hai", "explanation": "What happens at home, stays at home."},
    {"proverb": "Sona lagna bhi sona hai", "explanation": "Even getting gold to fall on you is a golden experience."},
    {"proverb": "Andher nagri, chaupat raja; take ser bhaji, take ser khaja", "explanation": "In a dark kingdom, there's a weak ruler; he takes a ser (small coin) as tax, and gives a ser of leafy greens and a ser of sweets."},
    {"proverb": "Sone ki chidiya", "explanation": "The golden bird (a metaphor for prosperity)."},
    {"proverb": "Bada ho to aisa ho", "explanation": "If you're going to be great, be like this."},
    {"proverb": "Bandar kya jaane adrak ka swad", "explanation": "What does a monkey know of the taste of ginger?"},
    {"proverb": "Bhains ke aage been bajana", "explanation": "Playing the flute to a buffalo."},
    {"proverb": "Bhais ke aage been bajana", "explanation": "Playing the flute to a buffalo."},
    {"proverb": "Dukh me sumiran sab kare, sukh me kare na koi", "explanation": "In sorrow, everyone remembers God; in happiness, no one does."},
    {"proverb": "Mitti mein sona", "explanation": "Gold in the soil (hidden treasure)."},
    {"proverb": "Neki kar dariya mein daal", "explanation": "Do good and cast it into the river (without expecting returns)."},
    {"proverb": "Ped ke niche kaala saanp", "explanation": "A black snake under a tree (a hidden danger)."},
    {"proverb": "Raja ka beta raja nahi banega", "explanation": "A king's son will not become a king."},
    {"proverb": "Raja ka beta raja nahi hota", "explanation": "A king's son is not necessarily a king."},
    {"proverb": "Sapne me raaja", "explanation": "A king in dreams (referring to an unrealistic fantasy)."},
    {"proverb": "Ungli ke nache to gaana bhi baj jaata hai", "explanation": "When the finger dances, the song also plays."},
    {"proverb": "Ungli ke nache to taali bhi baj jaati hai", "explanation": "When the finger dances, even the applause happens."},
    {"proverb": "Ungli ke nache to taali bhi baj jaata hai", "explanation": "When the finger dances, even the applause happens."},
    {"proverb": "Uski raai ka sikka khota hai", "explanation": "The coin of his opinion is of no value."},
    {"proverb": "Waqt se pehle aur kismat se zyada kisika nahi hota", "explanation": "No one can achieve more than what is destined and before its time."},

]

@app.route('/')
def home():
    proverb = random.choice(proverbs_data)
    return render_template('home.html', proverb=proverb['proverb'], explanation=proverb['explanation'])

@app.route('/get_random_proverb')
def get_random_proverb():
    proverb = random.choice(proverbs_data)
    return {'proverb': proverb['proverb'], 'explanation': proverb['explanation']}

if __name__ == '__main__':
    app.run(debug=True)
