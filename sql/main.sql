CREATE TABLE IF NOT EXISTS Player(
    PlayerId TEXT NOT NULL PRIMARY KEY,
    Playername TEXT,
    MailAdress TEXT,
    Password TEXT
);

CREATE TABLE IF NOT EXISTS Game(
    GameId TEXT NOT NULL PRIMARY KEY,
    PlayerId TEXT NOT NULL,
    NumberOfAttempts INT,
    FOREIGN KEY(PlayerId) REFERENCES Player(PlayerId)
);
