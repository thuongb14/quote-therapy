from .database import sql_write, sql_select
import os
from flask import request

CLOUDINARY_CLOUD = os.environ.get('CLOUDINARY_CLOUD')
CLOUDINARY_API_KEY = os.environ.get('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET = os.environ.get('CLOUDINARY_API_SECRET')

import cloudinary
import cloudinary.uploader

cloudinary.config(
    cloud_name = CLOUDINARY_CLOUD,
    api_key = CLOUDINARY_API_KEY,
    api_secret = CLOUDINARY_API_SECRET,
)

def insert_quote():
    content = request.form.get('content')
    mood = request.form.get('mood')
    image_url = request.files['image']

    #upload to cloudinary
    response = cloudinary.uploader.upload(image_url, filename=image_url.filename)
    image_url = response['secure_url']

    return sql_write('INSERT INTO quotes(content, image_url, mood) VALUES (%s, %s, %s)', [content, image_url, mood])

def render_quotes():
    results = sql_select('SELECT id, content, image_url, mood FROM quotes ORDER BY id')
    
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
    


