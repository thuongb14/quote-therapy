from .database import sql_write, sql_select
from flask import request, session

import os
import bcrypt
import cloudinary
import cloudinary.uploader

CLOUDINARY_CLOUD = os.environ.get('CLOUDINARY_CLOUD')
CLOUDINARY_API_KEY = os.environ.get('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET = os.environ.get('CLOUDINARY_API_SECRET')


cloudinary.config(
    cloud_name = CLOUDINARY_CLOUD,
    api_key = CLOUDINARY_API_KEY,
    api_secret = CLOUDINARY_API_SECRET,
)

def insert_quote():
    user_id = session.get('user_id')

    content = request.form.get('content')
    mood = request.form.get('mood')
    image_url = request.files['image']

    #upload to cloudinary
    response = cloudinary.uploader.upload(image_url, filename=image_url.filename)
    image_url = response['secure_url']

    return sql_write('INSERT INTO quotes(content, image_url, mood, user_id) VALUES (%s, %s, %s, %s)', [content, image_url, mood, user_id])

def render_quotes():
    results = sql_select('SELECT id, content, image_url, mood FROM quotes ORDER BY id DESC')
    
    all_quotes = []

    for row in results:
        id, content, image_url, mood = row
        quote = {'id':id,'content': content, 'image_url': image_url, 'mood' : mood}
        all_quotes.append(quote)

    return all_quotes

def select_one_quote(id):
    results = sql_select('SELECT id, content from quotes WHERE id = %s', [id])

    for row in results:
        id, content = row
        quote = {'id': id,'content': content}
    return quote

def delete_one_quote(id):
    return sql_write('DELETE FROM quotes WHERE id = %s', [id])

def edit_one_quote(id):
    content = request.form.get('content')
    mood = request.form.get('mood')
    image_url = request.files['image']

    #upload to cloudinary
    response = cloudinary.uploader.upload(image_url, filename=image_url.filename)
    image_url = response['secure_url']

    return sql_write('UPDATE quotes SET content = %s, image_url = %s, mood= %s WHERE id = %s', [content, image_url, mood, id])
    
def get_user(email):
    results = sql_select('SELECT id, name, email, password, avatar, isAdmin FROM users WHERE email = %s', [email])
    if results == []:
        user = []
    else:
        for row in results:
            id, name, email, password, avatar, isAdmin = row
            user = [id, name, email, password, avatar, isAdmin]
        print(user[5])
    return user

def check_log_in():
    email = request.form.get('email')
    password = request.form.get('password')
    user = get_user(email) #get info from sql
    if user == []:
        return user
    else:
        valid = bcrypt.checkpw(password.encode(), user[3].encode()) #check pw input hash with data
        if not valid:
            return 'Invalid Password'
        else:
            return user

def check_sign_up():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password') 
    avatar = request.files['avatar']
    password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    response = cloudinary.uploader.upload(avatar)
    avatar = response['secure_url']

    all_emails = []

    results = sql_select('SELECT email FROM users')

    for row in results:
        item = row[0]
        all_emails.append(item)

    if email in all_emails:
        return 'Email has been used'
    else:
        return sql_write('INSERT INTO users (name, email,  password, avatar) VALUES (%s, %s, %s, %s)', [name, email, password_hash, avatar])

def render_user_quotes():
    user_id = session.get('user_id')
    results = sql_select('SELECT quotes.id, image_url, content FROM quotes INNER JOIN users ON quotes.user_id = users.id WHERE quotes.user_id = %s',[user_id])
    all_quotes = []
    for row in results:
        id, image_url, content = row
        quote = {'id': id, 'image_url': image_url,'content': content}
        all_quotes.append(quote)
    return all_quotes


