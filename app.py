from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "<h1>VIAJES ESTRELLA Buctzotz</h1><p>Merida $150 | Cancun $600 | Chichen Itza $300</p><p><a href='https://wa.me/529861234567'>WhatsApp para reservar</a></p>"
