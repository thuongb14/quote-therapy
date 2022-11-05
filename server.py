from flask import Flask, render_template, redirect, url_for
from models.quotes import delete_one_quote, insert_quote, render_quotes, select_one_quote
from models.database import sql_select
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():

    all_quotes = render_quotes()

    return render_template('dashboard.html', all_quotes=all_quotes)

@app.route('/add_quote')
def add_quote():
    return render_template('add_quote.html')

@app.route('/add_quote_action', methods=['POST'])
def add_quote_action():

    insert_quote()

    return redirect(url_for('dashboard'))

@app.route('/delete_quote/<id>')
def delete_quote(id):
    quote = select_one_quote(id)

    return render_template('delete_quote.html', quote=quote)

@app.route('/delete_quote_action/<id>', methods=['POST'])
def delete_quote_action(id):
    delete_one_quote(id)

    return redirect(url_for('dashboard'))

    
if __name__ == '__main__':
    # Import the variables from the .env file
    from dotenv import load_dotenv
    # Start the server

app.run(debug=True)
