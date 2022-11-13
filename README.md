# Quotes Therapy
Simple project to share & look for cheerup quotes. The project was created for General Assembly SEI course.

## Table of contents
* [Preview](#preview)
* [Description](#description)
* [Technologies](#technologies)
* [Project Planning](#project-planning)

## Preview
https://quotetherapy.herokuapp.com/

## Description
Quote Therapy is a website to share and look for quotes that can help you to cheerup. But does only quote enough to cheer you up? Music has long been known to help people to heal, so each quote shared will be categorised with a different mood and each mood will have a different Lofi track for you to listen to and relax. How you feel matters and Quote Therapy exists to help you cope up with stress and negative thoughts.

## Technologies
* Javascript
* Python (Flask, Jinja, Psycopg2)
* PostgreSQL

## Project Planning
Quote Therapy follows CRUD functions: Create, Read, Update and Delete. With Jinja template, all pages follow a base template to represent fixed header and footer.

### Functions:
* Sign up & Log in to be able to Add, Edit and Delete own quotes.
* Users assigned as admin can have access to Edit & Delete all quotes.
* Audio control for each quote - The tracks are fetched from Spotify API, but can only play the preview version which is for 29 seconds.
* Image click to show details of the quote (track name, artist, name of user who posted the quote)
* Users can edit their personal information on profile page and keep track of their shared quotes.
* Users can visit other users' profile

### Things can be updated:
* 'Like' function
* Sort quote by: newest, oldest
* Follow another user



