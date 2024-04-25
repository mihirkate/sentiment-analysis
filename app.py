from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
import bcrypt


app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def main():
    if request.method == "POST":
        inp = request.form.get("inp")
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(inp)
        if score["neg"] > 0.1:
            return render_template('home.html', message = "Negative 🙁")
        elif score["pos"] > 0.1:
            return render_template('home.html', message = "Positive 😊")
        else:
            return render_template('home.html', message = "Nuteral 😐")
    return render_template("home.html")





if __name__ == "__main__":
    app.run(debug=True, port=8000)