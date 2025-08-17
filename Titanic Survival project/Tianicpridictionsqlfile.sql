CREATE DATABASE titanic_db;
USE titanic_db;

CREATE TABLE passengers (
    PassengerId INT PRIMARY KEY,
    Survived TINYINT,
    Pclass INT,
    Name VARCHAR(100),
    Sex VARCHAR(10),
    Age FLOAT,
    SibSp INT,
    Parch INT,
    Ticket VARCHAR(50),
    Fare FLOAT,
    Cabin VARCHAR(20),
    Embarked VARCHAR(1)
);
-- Remove null Ages and Fares
DELETE FROM passengers WHERE Age IS NULL OR Fare IS NULL;

-- Optional: Update missing Embarked or Cabin
UPDATE passengers SET Embarked = 'S' WHERE Embarked IS NULL;

select count(*) from passengers where Age is NULL;