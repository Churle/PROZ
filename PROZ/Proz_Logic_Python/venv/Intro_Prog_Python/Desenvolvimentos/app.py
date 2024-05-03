from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Desenvolvimento_5.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

# Configuração para servir arquivos estáticos (CSS, JS, imagens, etc.)
app.static_folder = 'static'

@app.route('/')
def index():
    return render_template('seu_arquivo_html.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('seu_arquivo_html.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)


