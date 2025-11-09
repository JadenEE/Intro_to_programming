CREATE DATABASE IF NOT EXISTS snakeAndLadderDatabase;
USE snakeAndLadderDatabase;

CREATE TABLE IF NOT EXISTS players (
    playerId VARCHAR(20) PRIMARY KEY,
    name VARCHAR(255),
    wins VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS games (
    gameId VARCHAR(20) PRIMARY KEY,
    roundCount INT,
    winner VARCHAR(255),
    runnerUp VARCHAR(255),
    secondRunnerUp VARCHAR(255)
);

INSERT IGNORE INTO players (playerId, name, wins) VALUES
('P01', 'Player1', 0),
('P02', 'Player2', 0),
('P03', 'Player3', 0),
('P04', 'Player4', 0);