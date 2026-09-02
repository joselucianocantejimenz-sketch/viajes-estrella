from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html><head><meta name='viewport' content='width=device-width, initial-scale=1'>
    <style>
    body{font-family:Arial;text-align:center;background:#f0f8ff;padding:20px}
    h1{color:#ff6600;font-size:32px}
    .btn{background:#25D366;color:white;padding:18px 30px;text-decoration:none;border-radius:12px;font-size:22px;display:inline-block;margin:15px}
    </style>
    </head><body>
    <h1>⭐ VIAJES ESTRELLA</h1>
    <h2>Buctzotz, Yucatán</h2>
    <p>Salidas a Mérida, Cancún y Chichén Itzá</p>
    <p><b>¡Tu agencia de confianza!</b></p>
    <a class='btn' href='https://wa.me/529991234567'>WhatsApp</a>
    </body></html>
    """

if __name__ == '__main__':
    app.run()
