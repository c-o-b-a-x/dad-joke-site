import requests
from flask import Flask,render_template,request

app=Flask(__name__)



@app.route("/")
def home():
        return render_template("home.html")

@app.route("/joke", methods=["GET", "POST"])
def joke():
    mood_message = None
    joke = None
    error = None
    moods = ["Chill", "Bored", "Moody", "Aggressive", "Sad", "Focused"]

    if request.method == "POST":
        mood = request.form.get("mood")
        
        if mood == "Bored":
            mood_message = "You look so bored — Have a joke"
        if mood == "Chill":
            mood_message = "You're really chill today, just vibing."
        if mood == "Moody":
            mood_message = "Everything will be okay, here have a joke to cheer you up."
        if mood == "Aggressive":
            mood_message = "Seems you're in an aggressive mood, maybe this joke can calm you down."
        if mood == "Sad":
            mood_message = "Here, have a joke to cheer you up."
        if mood == "Focused":
            mood_message = "Hopefully this joke doesn't make you lose focus!"

 

        api_url = "https://icanhazdadjoke.com/"
        headers = {"Accept": "application/json"}
        response = requests.get(api_url, headers=headers)
        
        if response.status_code == 200:
            joke = response.json().get("joke")
        else:
            error = "Couldn't find a joke at this time, sorry :("

    return render_template("joke.html", error=error, moods=moods, joke=joke, mood_message=mood_message)

@app.route("/search", methods=["GET", "POST"])
def search_joke():
        joke=None
        term=None
        error=None
        jokes=""
        if request.method == "POST":
                term = request.form.get("search")
                api_url = f"https://icanhazdadjoke.com/search?term={term}"
                headers = {"Accept": "application/json"}
                response = requests.get(api_url, headers=headers)
                if response.status_code == 200:
                        jokes = response.json().get("results")
                else:
                     error="Couldnt get your joke, either try again with a different term or try again later "
        return render_template("search.html",jokes=jokes,error=error,joke=joke)



if __name__ == "__main__":
        app.run(debug=True)