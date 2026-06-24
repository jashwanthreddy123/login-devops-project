CREATE TABLE users
(
 id SERIAL PRIMARY KEY,
 email VARCHAR(100),
 password VARCHAR(100)
);


INSERT INTO users(email,password)
VALUES
('admin@gmail.com','12345');
