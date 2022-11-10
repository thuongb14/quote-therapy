from flask import Flask, render_template, redirect, url_for, make_response, session
from models.quotes import render_profile_quotes, get_profile_user, get_cookie, set_cookie_session, get_user, change_profile_info, render_user_quotes, check_sign_up, check_log_in, edit_one_quote, delete_one_quote, insert_quote, render_quotes, select_one_quote


app = Flask(__name__)

app.config['SECRET_KEY'] = 'super secret key'

@app.route('/')
def index():
    user_cookie = get_cookie()

    return render_template('index.html', user_cookie=user_cookie)

@app.route('/dashboard')
def dashboard():
    user_cookie = get_cookie()

    all_quotes = render_quotes()

    return render_template('dashboard.html', all_quotes=all_quotes, user_cookie=user_cookie)

@app.route('/add_quote')
def add_quote():
    user_cookie = get_cookie()

    return render_template('add_quote.html', user_cookie=user_cookie)

@app.route('/add_quote_action', methods=['POST'])
def add_quote_action():
    insert_quote()

    return redirect(url_for('dashboard'))

@app.route('/delete_quote/<id>')
def delete_quote(id):
    user_cookie = get_cookie()

    quote = select_one_quote(id)

    return render_template('delete_quote.html', quote=quote, user_cookie=user_cookie)

@app.route('/delete_quote_action/<id>', methods=['POST'])
def delete_quote_action(id):
    delete_one_quote(id)

    return redirect(url_for('dashboard'))

@app.route('/edit_quote/<id>')
def edit_quote(id):
    user_cookie = get_cookie()

    quote = select_one_quote(id)
    
    return render_template('edit_quote.html', quote=quote, user_cookie=user_cookie)

@app.route('/edit_quote_action/<id>', methods=['POST'])
def edit_quote_action(id):
    edit_one_quote(id)

    return redirect(url_for('dashboard'))

@app.route('/log_in')
def log_in():
    user_cookie = get_cookie()

    return render_template('log_in.html', user_cookie=user_cookie)

@app.route('/log_in_action', methods=['POST'])
def log_in_action():
    user = check_log_in()

    user_cookie = get_cookie()

    if user == [] or user == 'Invalid Password':
        return render_template('log_in.html', user=user, user_cookie=user_cookie)
    else:
        response = make_response(redirect('/'))
        # # response.set_cookie('user_name', user[2])
        set_cookie_session(user)

        return response

@app.route('/log_out_action')
def log_out_action():
    response = redirect('/')
    response.delete_cookie('session')

    return response

@app.route('/about')
def about():
    user_cookie = get_cookie()

    return render_template('about.html',user_cookie=user_cookie)
    

@app.route('/sign_up')
def sign_up():
    user_cookie = get_cookie()

    return render_template('sign_up.html', user_cookie=user_cookie)
    
@app.route('/sign_up_action', methods=['POST'])
def sign_up_action():
    user = check_sign_up()

    user_cookie = get_cookie()

    if user == 'Email has been used':
        return render_template('sign_up.html', user_cookie=user_cookie, user=user)
    else:
        response = redirect('/log_in')
        return response

@app.route('/profile/<id>')
def profile(id):
    user_cookie = get_cookie()

    quotes = render_user_quotes()
    return render_template('profile.html', quotes=quotes, user_cookie=user_cookie)

@app.route('/edit_profile_info/<user_id>')
def edit_profile_info(user_id):
    user_cookie = get_cookie()

    return render_template('edit_profile_info.html', user_cookie=user_cookie)

@app.route('/edit_profile_info_action/<user_id>', methods=['POST'])
def edit_profile_info_action(user_id):
    user_cookie = get_cookie()

    change_profile_info(user_id)

    response = make_response(redirect('/'))

    user = get_user(user_cookie['user_email'])

    response.delete_cookie('session')

    set_cookie_session(user)

    return response

@app.route('/user_profile/<id>')
def user_profile(id):
    user_cookie = get_cookie()

    user = get_profile_user(id)

    quotes = render_profile_quotes(id)

    return render_template('user_profile.html', quotes=quotes, user_cookie=user_cookie, user=user)


if __name__ == '__main__':
    # Import the variables from the .env file
    # Start the server
    app.run(debug=True)