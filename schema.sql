DROP TABLE IF EXISTS quotes;

CREATE TABLE quotes (
    id SERIAL PRIMARY KEY,
    content VARCHAR(120),
    mood TEXT,
    image_url TEXT
)