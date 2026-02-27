CREATE DATABASE aryan;

USE aryan;

CREATE TABLE gofish(
name VARCHAR(50),
turns_taken_to_win INT,
winner VARCHAR(50)
);

CREATE TABLE handcricket(
name VARCHAR(50),
player_score INT,
computer_score INT,
winner VARCHAR(50)
);

CREATE TABLE quizs(
name VARCHAR(50),
genre VARCHAR(50),
difficulty VARCHAR(50),
score INT
);

CREATE TABLE typings(
player1 VARCHAR(50),
player2 VARCHAR(50),
time_taken_first_player FLOAT,
time_taken_second_player FLOAT,
winner_time FLOAT,
winner VARCHAR(50)
);