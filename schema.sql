DROP TABLE IF EXISTS users, quotes;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    password TEXT,
    avatar TEXT,
    description TEXT,
    isAdmin BOOLEAN
);

CREATE TABLE quotes (
    id SERIAL PRIMARY KEY,
    content VARCHAR(120),
    mood TEXT,
    image_url TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id)
        REFERENCES users(id)
)
