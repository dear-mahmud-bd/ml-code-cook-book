CREATE DATABASE  IF NOT EXISTS `random-database`;
USE `random-database`;

CREATE TABLE IF NOT EXISTS Person (
    Id INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender VARCHAR(10),
    Country VARCHAR(50),
    Age INT,
    DateOfBirth DATE
);

INSERT INTO Person (Id, FirstName, LastName, Gender, Country, Age, DateOfBirth)
VALUES
(1, 'Dulce', 'Abril', 'Female', 'United States', 32, '2017-10-15'),
(2, 'Mara', 'Hashimoto', 'Female', 'Great Britain', 25, '2016-08-16'),
(3, 'Philip', 'Gent', 'Male', 'France', 36, '2015-05-21'),
(4, 'Kathleen', 'Hanner', 'Female', 'United States', 25, '2017-10-15'),
(5, 'Nereida', 'Magwood', 'Female', 'United States', 58, '2016-08-16'),
(6, 'Gaston', 'Brumm', 'Male', 'United States', 24, '2015-05-21'),
(7, 'Etta', 'Hurn', 'Female', 'Great Britain', 56, '2017-10-15'),
(8, 'Earlean', 'Melgar', 'Female', 'United States', 27, '2016-08-16'),
(9, 'Vincenza', 'Weiland', 'Female', 'United States', 40, '2015-05-21');
