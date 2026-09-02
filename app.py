from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return """
    <html><head><meta name='viewport' content='width=device-width, initial-scale=1'>
    <style>body{font-family:Arial;text-align:center;background:#FFF8E1;padding:15px}h1{color:#FF6600}.card{background:white;padding:15px;border-radius:12px;margin:10px}.btn{background:#25D366;color:white;padding:15px 25px;text-decoration:none;border-radius:10px;font-size:20px;display:inline-block}</style>
    </head><body>
    <h1>⭐ VIAJES ESTRELLA ⭐</h1><h2>Buctzotz, Yucatan</h2>
    <div class='card'><h3>Merida $150</h3><p>Todos los dias 6am</p></div>
    <div class='card'><h3>Cancun $600</h3><p>Lunes y Viernes</p></div>
    <div class='card'><h3>Chichen Itza $300</h3><p>Sabados y Domingos</p></div>
    <a class='btn' href='https://wa.me/529861234567'>Reservar WhatsApp</a>
    </body></html>
    """
