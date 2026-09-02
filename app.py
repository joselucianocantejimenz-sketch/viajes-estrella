from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><meta name='viewport' content='width=device-width, initial-scale=1'>
    <style>
    body{font-family:Arial;text-align:center;background:#FFF8E1;padding:15px}
    h1{color:#FF6600}
    .card{background:white;padding:15px;border-radius:12px;margin:10px;box-shadow:0 2px 5px #ccc}
    .btn{background:#25D366;color:white;padding:15px 25px;text-decoration:none;border-radius:10px;font-size:20px;display:inline-block;margin-top:15px}
    </style>
    </head>
    <body>
    <h1>⭐ VIAJES ESTRELLA ⭐</h1>
    <h2>Buctzotz, Yucatán</h2>
    <div class='card'><h3>🚌 Mérida $150</h3><p>Todos los días 6am</p></div>
    <div class='card'><h3>🏖️ Cancún $600</h3><p>Lunes y Viernes</p></div>
    <div class='card'><h3>🔺 Chichén Itzá $300</h3><p>Sábados y Domingos</p></div>
    <a class='btn' href='https://wa.me/529861234567'>📲 Reservar por WhatsApp</a>
    </body>
    </html>
    """
