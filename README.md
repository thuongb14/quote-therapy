# Quote Therapy
Simple project to share & look for cheerup quotes. The project was created for General Assembly SEI course.

## Table of contents
* [Preview](#preview)
* [Description](#description)
* [Technologies](#technologies)
* [Project Planning](#project-planning)


## Preview

## Description
Quote Therapy is a website to share and look for quotes that can help you to cheerup. But does only quote enough to cheer you up? Music has long been known to help people to heal, so each quote shared will be categorised with a different mood and each mood will have a different Lofi track for you to listen to and relax. How you feel matters and Quote Therapy exists to help you cope up with stress and negative thoughts.

## Technologies
* Javascript
* Python (Flask, Jinja, Psycopg2)
* PostgreSQL

## Project Planning
Quote Therapy follows CRUD functions: Create, Read, Update and Delete. With Jinja template, all pages follow a base template to represent fixed header and footer.
### Home Page
Elements in home page:
* Logo
* Log in & Sign up buttons
* Website introduction

### Dashboard
Elements in dashboard:
* Add quote button (available when user logs in)
* Edit & Delete quote button (right now, these buttons are available for all users, planning to make users can only edit & delete the quote that they shared and only admin can have access to edit and delete all quotes)
* Audio control for each quote - The tracks are fetched from Spotify API, but can only play the preview version which is for 29 seconds.
* Image click to show details of the quote.

## About Us:




