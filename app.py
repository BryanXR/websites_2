from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_gesk():
    return '<h1>Bryan Valenzuela</h2>
    <img src="https://i0.wp.com/lamiradafotografia.es/wp-content/uploads/2014/07/simpson-rock.jpg" width="500" heigth="600">'


if __name__ == "__main__":
    app.run(debug = True)
