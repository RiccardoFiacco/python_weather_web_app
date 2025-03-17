from flask import Flask, render_template, request, redirect
#importiamo la classe Flask, una funzione che renderizza l'html nel browser, oggetto che fa il parsing dei dati in ingresso e ne da l'accesso tramite un ggetto globale
from weather import get_current_weather
from waitress import serve

app = Flask(__name__) #rende la nostra app un app Flask
# inizializza un'istanza dell'applicazione Flask dandola a app 
# che verrà usato per definire le rotte, gestire richieste e configurare l'app.

@app.route("/")#crea una route per la homepage
@app.route("/index")#crea una route alternativa per la stessa funzione, http://localhost:xxxx/index funziona lo stesso
def index():
    return render_template(
        "index.html"
    )

@app.route("/weather")
def get_weather():
    city = request.args.get('city') #prende le info dal form con quel nome
    try:
        data = get_current_weather(city) #prendo i dati dalla funzione in weather.py
        
        return render_template(
          "weather.html",
          title = data["name"],
          weather_data = data
        )
    except:
       return redirect("/ErrorPage",code=302)

@app.route("/ErrorPage")
def error():
    return "an error occourred😥"



if __name__ == "__main__": #se esguiamo direttamente, dal file, il codice eseguiremo una versione in console
   serve(app, host="0.0.0.0", port=8000)