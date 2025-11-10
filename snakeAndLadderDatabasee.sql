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
('sc08250078dc', 'Jaden', 0),
('si0625000085dc', 'JadenThe', 0),
('m-9020566', 'Player3', 0),
('playerid', 'Player4', 0);