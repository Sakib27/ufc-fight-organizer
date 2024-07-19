CREATE TABLE Users (
    UserID VARCHAR(9) PRIMARY KEY,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Username VARCHAR(50) UNIQUE NOT NULL,
    Full_Name VARCHAR(100) NOT NULL,
    HashedPW VARCHAR(255) NOT NULL,
    dob DATE NOT NULL,
    UserType VARCHAR(50) NOT NULL
);

CREATE TABLE Fighters (
    UserID VARCHAR(9) PRIMARY KEY REFERENCES Users(UserID),
    Nationality VARCHAR(50),
    Weight INTEGER,
    Height INTEGER,
    Gender VARCHAR(50),
    Salary NUMERIC(9,2)
);

CREATE TABLE Admins (
    UserID VARCHAR(9) PRIMARY KEY REFERENCES Users(UserID),
    Salary NUMERIC(9,2)
);

CREATE TABLE Staff (
    UserID VARCHAR(9) PRIMARY KEY REFERENCES Users(UserID),
    Salary NUMERIC(9,2)
);

CREATE TABLE Attendees (
    UserID VARCHAR(9) PRIMARY KEY REFERENCES Users(UserID)
);

CREATE TABLE Venues (
    VenueID VARCHAR(9) PRIMARY KEY,
    Name VARCHAR(100),
    Address VARCHAR(100),
    Contact_Information VARCHAR(50),
    Capacity INTEGER
);

CREATE TABLE Events (
    EventID VARCHAR(9) PRIMARY KEY,
    FighterID1 VARCHAR(9) REFERENCES Users(UserID) NOT NULL,
    FighterID2 VARCHAR(9) REFERENCES Users(UserID) NOT NULL,
    WeightClass VARCHAR(50),
    EventDate DATE NOT NULL,
    Time TIME(0),
    Location VARCHAR(50) REFERENCES Venues(VenueID)
);

CREATE TABLE Sponsors (
    SponsorID VARCHAR(9),
    Name VARCHAR(100),
    Amount NUMERIC(9,2),
    EventID VARCHAR(9) REFERENCES Events(EventID),
    PRIMARY KEY (SponsorID, EventID)
);

CREATE TABLE Results (
    EventID VARCHAR(9) REFERENCES Events(EventID) PRIMARY KEY,
    WinnerID VARCHAR(9) REFERENCES Users(UserID) NOT NULL,
    LoserID VARCHAR(9) REFERENCES Users(UserID) NOT NULL,
    Strikes INTEGER,
    Round INTEGER,
    Method VARCHAR(100)
);

CREATE TABLE Tickets (
    TicketID VARCHAR(20),
    EventID VARCHAR(9) REFERENCES Events(EventID),
    AttendeeID VARCHAR(9) REFERENCES Attendees(UserID),
    TicketType VARCHAR(20),
    Price NUMERIC(6,2),
    PRIMARY KEY(TicketID, EventID)
);

CREATE TABLE Shifts (
    UserID VARCHAR(9) REFERENCES Users(UserID),
    EventID VARCHAR(9) REFERENCES Events(EventID),
    StartTime TIME(0),
    EndTime TIME(0),
    PRIMARY KEY (UserID, EventID)
);

CREATE OR REPLACE FUNCTION check_shift_time() 
RETURNS TRIGGER AS $$
BEGIN
    -- Check if the event has already happened
    IF NEW.StartTime < NOW() THEN
        RAISE EXCEPTION 'Cannot set a shift for an event that has already happened.';
    END IF;
    
    -- Check if the shift is less than 72 hours away
    IF NEW.StartTime < (SELECT EventDate + NEW.StartTime::TIME - INTERVAL '72 hours' 
                        FROM Events WHERE EventID = NEW.EventID) THEN
        RAISE EXCEPTION 'Cannot set a shift for a staff member less than 72 hours before the event.';
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER before_shift_insert
BEFORE INSERT ON Shifts
FOR EACH ROW
EXECUTE FUNCTION check_shift_time();