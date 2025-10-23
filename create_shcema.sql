DROP TABLE IF EXISTS students;
CREATE TABLE students(
    id              serial PRIMARY KEY,
    first_name      varchar(255) NOT NULL,
    last_name       varchar(255) NOT NULL,
    age             integer NOT NULL,
    grade             varchar(1) NOT NULL
);
SELECT * FROM students;