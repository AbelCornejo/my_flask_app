from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi Primer App en Docker <3 </title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #fff;
                border-radius: 5px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                text-align: center;
                color: #333;
            }
            p {
                text-align: center;
                color: #666;
                font-size: 18px;
            }
            .footer {
                text-align: center;
                color: #999;
                margin-top: 30px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bienvenid@s a Mi App - Volumen 4
            </h1>
            <p>¡Gracias por visitar nuestra página! Esperamos que disfrutes de tu estancia.</p>
        </div>
        <div class="footer">
            <p>© 2024 Abel Cornejo Rojas. Todos los derechos reservados.</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
