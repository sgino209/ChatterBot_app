#import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

bot = ChatBot("Candice")

trainer = ListTrainer(bot)
trainer.train([
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
])
trainer.train([
    "שלום",
    "היי",
    "מה שלומך?",
    "בסדר גמור",
    "טוב לשמוע",
    "תודה",
    "אין בעד מה"
])

#trainer = ChatterBotCorpusTrainer(bot)
#trainer.train("chatterbot.corpus.english")


@app.route("/")
def home():    
    return render_template("home.html") 

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 
if __name__ == "__main__":    
    app.run()

