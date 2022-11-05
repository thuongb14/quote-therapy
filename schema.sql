DROP TABLE IF EXISTS quotes, users;

CREATE TABLE quotes (
    id SERIAL PRIMARY KEY,
    content VARCHAR(120),
    mood TEXT,
    image_url TEXT
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    avatar TEXT
)