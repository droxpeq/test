CREATE DATABASE task2db;
CREATE TABLE person (
    person_id SERIAL PRIMARY KEY,
    last_name VARCHAR(50) NOT NULL CHECK (last_name ~ '^[А-Яа-я-]+$'),
    first_name VARCHAR(50) NOT NULL CHECK (first_name ~ '^[А-Яа-я-]+$'),
    middle_name VARCHAR(50) CHECK (middle_name ~ '^[А-Яа-я]+$'),
    gender BOOLEAN NOT NULL,
    birth_date DATE NOT NULL,
    house_number SMALLINT NOT NULL CHECK (house_number BETWEEN 1 AND 300)
);

CREATE TABLE animal (
    animal_id SERIAL PRIMARY KEY,
    owner_id INT NOT NULL REFERENCES person(person_id) ON DELETE CASCADE,
    nickname VARCHAR(50) NOT NULL CHECK (nickname ~ '^[А-Яа-я]+$'),
    species VARCHAR(50) NOT NULL CHECK (species ~ '^[А-Яа-я]+$'),
    gender BOOLEAN NOT NULL,
    birth_date DATE NOT NULL,
    registration_datetime TIMESTAMP NOT NULL,
    description TEXT NOT NULL
);


INSERT INTO person (last_name, first_name, middle_name, gender, birth_date, house_number)
VALUES
('Романов', 'Николай', 'Александрович', FALSE, '18.05.1868', 45),
('Петрова', 'Мария', 'Ивановна', TRUE, '17.09.1968', 78),
('Старков', 'Эдуард', 'Сергеевич', FALSE, '08.07.1969', 12),
('Кузнецова', 'Ольга', 'Дмитриевна', TRUE, '28.03.1973', 134),
('Смирнов', 'Лев', 'Владимирович', FALSE, '08.12.1991', 200);

INSERT INTO animal (owner_id, nickname, species, gender, birth_date, registration_datetime, description)
VALUES
(1, 'Булка', 'Кошка', TRUE, '16.12.2023', '03.02.2025 10:30:00', 'Белая с черным пятном на лице'),
(2, 'Патрик', 'Кот', FALSE, '05.07.2022', '23.02.2020 11:00:00', 'Рыжий, пушистый, агрессивный'),
(3, 'Шарик', 'Собака', FALSE, '26.09.2017', '13.01.2025 09:15:00', 'Характер скверный, не женат'),
(4, 'Прасковья', 'Корова', TRUE, '13.10.2020', '03.03.2025 08:45:00', 'Черно-белая, бодливая'),
(5, 'Маруся', 'Корова', TRUE, '03.12.2021', '07.02.2025 07:30:00', 'Рыжая, спокойная');