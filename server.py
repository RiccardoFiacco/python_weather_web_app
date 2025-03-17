from flask import Flask, render_template, request 
#importiamo la classe Flask, una funzione che renderizza l'html nel browser, oggetto che fa il parsing dei dati in ingresso e ne da l'accesso tramite un ggetto globale
from weather import get_current_weather

app = Flask(__name__) #rende la nostra app un app Flask
# inizializza un'istanza dell'applicazione Flask dandola a app 
# che verrà usato per definire le rotte, gestire richieste e configurare l'app.

@app.route("/")#crea una route per la homepage
@app.route("/index")#crea una route alternativa per la stessa funzione, http://localhost:xxxx/index funziona lo stesso
def index():
    return "hi"


if __name__ == "__main__": #se esguiamo direttamente, dal file, il codice eseguiremo una versione in console
   app.run(host="0.0.0.0", port=8000)