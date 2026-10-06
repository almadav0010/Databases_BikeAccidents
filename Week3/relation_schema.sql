/*
create comman for all tables based on our ER diagram.
it differs from the ER by connecting Accident and Location (ER did not list the column, but noted the relation)
Changed the name of the junction table of Bicycle and Cyclist from BicycleCyclist to BicycleOwnership
*/


-- MockdataGood.AccidentType definition
CREATE TABLE IF NOT EXISTS AccidentType (
  accdentTypeID int PRIMARY KEY AUTO_INCREMENT,
  type varchar(100) NOT NULL,
    weather_effect_score int DEFAULT 5 CHECK (weather_effect_score BETWEEN 1 AND 10) -- how much does weather, like low light effect the certain accident type, like bike with bike/bike with car. 5 is average
);

-- MockdataGood.Bicycle definition
CREATE TABLE IF NOT EXISTS Bicycle (
  serial_num varchar(12) PRIMARY KEY,
  brand varchar(50) DEFAULT NULL, -- Longest bike brand name is 27 characters long:Kona Humuhumunukunukuapua'a, set maximum length to 50
  ebike tinyint(1) DEFAULT NULL,
  fatbike tinyint(1) DEFAULT NULL,
  age int DEFAULT NULL
);
  
-- MockdataGood.Cyclist definition
CREATE TABLE IF NOT EXISTS Cyclist (
  BSN int PRIMARY KEY,
  age int DEFAULT NULL,
  helmet_usually TINYINT DEFAULT FALSE -- most dutch people dont wear helmet so a false assumption is reasonable
);

-- MockdataGood.DownfallType definition
CREATE TABLE IF NOT EXISTS DownfallType (
  downfallTypeID int PRIMARY KEY AUTO_INCREMENT,
  type varchar(100) NOT NULL
);

-- MockdataGood.ReasonType definition
CREATE TABLE IF NOT EXISTS ReasonType (
  reasonTypeID int PRIMARY KEY AUTO_INCREMENT,
  type varchar(100) NOT NULL
);

-- MockdataGood.RoadType definition
CREATE TABLE IF NOT EXISTS RoadType (
  roadTypeID int PRIMARY KEY AUTO_INCREMENT,
  type varchar(100) NOT NULL,
  rain_effect_score int(10) DEFAULT 5 CHECK(rain_effect_score BETWEEN 1 and 10)  -- 5 is average, if no data was added we assume average
);

-- MockdataGood.BicycleOwnership definition
CREATE TABLE IF NOT EXISTS BicycleOwnership (
  bicycleCyclistID int PRIMARY KEY AUTO_INCREMENT,
  cyclist int NOT NULL REFERENCES Cyclist (BSN),
  bike varchar(12) NOT NULL REFERENCES Bicycle (serial_num)
);

-- MockdataGood.Location definition
CREATE TABLE IF NOT EXISTS Location (
  placeID int PRIMARY KEY AUTO_INCREMENT,
  /*longest city name we found is 27 letters: Westerhaar-Vriezenveensewijk, but we made upper bound 50 to not crash in any situation*/
  city varchar(50) NOT NULL, 
  street varchar(100) NOT NULL, -- in intersections always the street the biker at fault was coming from
  road_quality_score int(10) DEFAULT NULL CHECK(road_quality_score BETWEEN 1 and 10),
  road_type int DEFAULT NULL REFERENCES RoadType (roadTypeID)
);

-- MockdataGood.Accident definition
CREATE TABLE IF NOT EXISTS Accident (
  ID int PRIMARY KEY AUTO_INCREMENT,
  time datetime DEFAULT NULL,
  type int DEFAULT NULL REFERENCES AccidentType (accdentTypeID),
  reason int DEFAULT NULL REFERENCES ReasonType (reasonTypeID),
  downfall int DEFAULT NULL REFERENCES DownfallType (downfallTypeID),
  location int DEFAULT NULL REFERENCES Location (placeID),
  temperature smallint DEFAULT NULL,
  road_wet tinyint(1) DEFAULT NULL,
  bron_id bigint UNIQUE,
    severity varchar(20) DEFAULT NULL,
    speed_limit smallint,
    urban tinyint(1),
    light int
);

-- MockdataGood.CyclistAccident definition
CREATE TABLE IF NOT EXISTS CyclistAccident (
  cyclistAccidentID int PRIMARY KEY AUTO_INCREMENT,
  cyclist int NOT NULL REFERENCES Cyclist (BSN),
  accident int NOT NULL REFERENCES Accident (ID),
  serial_num varchar(12) DEFAULT NULL REFERENCES Bicycle (serial_num),
  lethal tinyint(1) DEFAULT NULL,
  at_fault tinyint(1) DEFAULT 0 -- without data we assume person isnt at fault
);
