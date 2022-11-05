from flask import Flask, render_template, redirect, url_for, make_response, session
from models.quotes import get_user, edit_one_quote, delete_one_quote, insert_quote, render_quotes, select_one_quote
from models.database import sql_select
app = Flask(__name__)

app.config['SECRET_KEY'] = 'super secret key'


@app.route('/')
def index():
    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar')

    return render_template('index.html', user_avatar=user_avatar, user_name=user_name)

@app.route('/dashboard')
def dashboard():

    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar')

    all_quotes = render_quotes()

    return render_template('dashboard.html', all_quotes=all_quotes, user_name=user_name, user_avatar=user_avatar)

@app.route('/add_quote')
def add_quote():
    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar')

    return render_template('add_quote.html', user_name=user_name, user_avatar=user_avatar)

@app.route('/add_quote_action', methods=['POST'])
def add_quote_action():

    insert_quote()

    return redirect(url_for('dashboard'))

@app.route('/delete_quote/<id>')
def delete_quote(id):

    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar')

    quote = select_one_quote(id)

    return render_template('delete_quote.html', quote=quote, user_name=user_name, user_avatar=user_avatar)

@app.route('/delete_quote_action/<id>', methods=['POST'])
def delete_quote_action(id):
    delete_one_quote(id)

    return redirect(url_for('dashboard'))

@app.route('/edit_quote/<id>')
def edit_quote(id):

    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar')

    quote = select_one_quote(id)
    return render_template('edit_quote.html', quote=quote, user_name=user_name, user_avatar=user_avatar)

@app.route('/edit_quote_action/<id>', methods=['POST'])
def edit_quote_action(id):
    edit_one_quote(id)

    return redirect(url_for('dashboard'))

@app.route('/log_in')
def log_in():

    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar')

    return render_template('log_in.html', user_name=user_name, user_avatar=user_avatar)

@app.route('/log_in_action', methods=['POST'])
def log_in_action():

    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar')

    user = get_user()

    if user == [] or user == 'Unknown':
        return render_template('log_in.html', user_name=user_name, user_avatar=user_avatar)

    response = make_response(redirect(url_for('dashboard')))

    session['user_name'] = user[1]
    session['user_id'] = user[0]
    session['user_avatar'] = user[3]

    return response

@app.route('/log_out_action')
def log_out_action():
    response = redirect('/')
    response.delete_cookie('session')

    return response
    
if __name__ == '__main__':
    # Import the variables from the .env file
    from dotenv import load_dotenv
    # Start the server

app.run(debug=True)
