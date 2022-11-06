from flask import Flask, render_template, redirect, url_for, make_response, session
from models.quotes import check_sign_up, check_log_in, edit_one_quote, delete_one_quote, insert_quote, render_quotes, select_one_quote
app = Flask(__name__)

app.config['SECRET_KEY'] = 'super secret key'


@app.route('/')
def index():
    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar', 'Unknown')
    user_id = session.get('user_id')


    return render_template('index.html', user_id=user_id, user_name=user_name, user_avatar=user_avatar)

@app.route('/dashboard')
def dashboard():

    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar', 'Unknown')
    user_isAdmin = session.get('user_isAdmin')
    user_id = session.get('user_id')


    all_quotes = render_quotes()

    return render_template('dashboard.html',user_id=user_id, all_quotes=all_quotes, user_isAdmin=user_isAdmin, user_name=user_name, user_avatar=user_avatar)

@app.route('/add_quote')
def add_quote():
    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar')
    user_id = session.get('user_id')

    return render_template('add_quote.html', user_id=user_id, user_name=user_name, user_avatar=user_avatar)

@app.route('/add_quote_action', methods=['POST'])
def add_quote_action():

    insert_quote()

    return redirect(url_for('dashboard'))

@app.route('/delete_quote/<id>')
def delete_quote(id):

    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar', 'Unknown')
    user_isAdmin = session.get('user_isAdmin')
    user_id = session.get('user_id')

    quote = select_one_quote(id)

    return render_template('delete_quote.html', user_id=user_id, quote=quote, user_isAdmin=user_isAdmin, user_name=user_name, user_avatar=user_avatar)

@app.route('/delete_quote_action/<id>', methods=['POST'])
def delete_quote_action(id):
    delete_one_quote(id)

    return redirect(url_for('dashboard'))

@app.route('/edit_quote/<id>')
def edit_quote(id):

    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar', 'Unknown')
    user_isAdmin = session.get('user_isAdmin')
    user_id = session.get('user_id')

    quote = select_one_quote(id)
    return render_template('edit_quote.html', user_id=user_id, quote=quote, user_isAdmin=user_isAdmin, user_name=user_name, user_avatar=user_avatar)

@app.route('/edit_quote_action/<id>', methods=['POST'])
def edit_quote_action(id):
    edit_one_quote(id)

    return redirect(url_for('dashboard'))

@app.route('/log_in')
def log_in():

    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar', 'Unknown')
    user_isAdmin = session.get('user_isAdmin')

    return render_template('log_in.html', user_name=user_name, user_avatar=user_avatar, user_isAdmin=user_isAdmin)

@app.route('/log_in_action', methods=['POST'])
def log_in_action():

    user = check_log_in()

    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar', 'Unknown')
    user_isAdmin = session.get('user_isAdmin')
    user_id = session.get('user_id')


    if user == [] or user == 'Invalid Password':
        return render_template('log_in.html', user_id=user_id, user=user, user_name=user_name, user_avatar=user_avatar, user_isAdmin=user_isAdmin)
    else:
        response = make_response(redirect('/'))
        # # response.set_cookie('user_name', user[2])
        session['user_name'] = user[1]
        session['user_id'] = user[0]
        session['user_avatar'] = user[4]
        session['user_isAdmin'] = user[5]
        return response

@app.route('/log_out_action')
def log_out_action():
    response = redirect('/')
    response.delete_cookie('session')

    return response

@app.route('/about')
def about():
    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar')
    user_id = session.get('user_id')

    return render_template('about.html', user_id=user_id, user_name=user_name, user_avatar=user_avatar)
    

@app.route('/sign_up')
def sign_up():
    
    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar')
    user_id = session.get('user_id')

    return render_template('sign_up.html', user_id=user_id, user_name=user_name, user_avatar=user_avatar)
    
@app.route('/sign_up_action', methods=['POST'])
def sign_up_action():
    user = check_sign_up()

    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar')
    user_id = session.get('user_id')


    if user == 'Email has been used':
        return render_template('sign_up.html',  user_id=user_id, user_name=user_name, user_avatar=user_avatar, user=user)
    else:
        response = redirect('/log_in')
        return response

@app.route('/profile/<id>')
def profile(id):
    user_name = session.get('user_name', 'Unknown')
    user_avatar = session.get('user_avatar')
    user_id = session.get('user_id')

    return render_template('profile.html', user_id=user_id, user_name=user_name, user_avatar=user_avatar)

if __name__ == '__main__':
    # Import the variables from the .env file
    from dotenv import load_dotenv
    # Start the server

app.run(debug=True)
