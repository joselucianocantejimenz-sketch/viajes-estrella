from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html><head><meta name='viewport' content='width=device-width, initial-scale=1'>
    <style>
    body{font-family:Arial;text-align:center;background:#f0f8ff;padding:20px}
    h1{color:#ff6600;font-size:32px}
    .btn{background:#25D366;color:white;padding:18px 30px;text-decoration:none;border-radius:12px;font-size:22px;display:inline-block;margin-top:20px}
    </style>
    </head><body>
    <h1>🌟 VIAJES ESTRELLA</h1>
    <h2>Buctzotz, Yucatan</h2>
    <p>Salidas a Merida, Cancun y Chichen Itza</p>
    <p><b>¡Tu agencia de confianza!</b></p>
    <a class='btn' href='https://wa.me/529910000000'>📲 Cotiza por WhatsApp</a>
    <p style='margin-top:40px'>Llamanos hoy</p>
    </body></html>
    """
