from flask import Flask, request, render_template, redirect
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    conn = psycopg2.connect('dbname=quotes')
    cur = conn.cursor()

    cur.execute('SELECT content, image_url, mood FROM quotes')

    results = cur.fetchall()
    
    all_quotes = []

    for row in results:
        content, image_url, mood = row
        quote = {'content': content, 'image_url': image_url, 'mood' : mood}
        all_quotes.append(quote)
    
    conn.commit()

    cur.close()

    conn.close()

    return render_template('dashboard.html', all_quotes=all_quotes)

@app.route('/add_quote')
def add_quote():
    return render_template('add_quote.html')

@app.route('/add_quote_action', methods=['POST'])
def add_quote_action():
    conn = psycopg2.connect('dbname=quotes')
    cur = conn.cursor()

    content = request.form.get('content')
    image_url = request.form.get('image')
    mood = request.form.get('mood')

    cur.execute('INSERT INTO quotes(content, image_url, mood) VALUES (%s, %s, %s)', [content, image_url, mood])
        
    conn.commit()

    cur.close()

    conn.close()

    return redirect('/')
    

app.run(debug=True)
