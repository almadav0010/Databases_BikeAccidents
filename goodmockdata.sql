INSERT INTO 'Bicycle' Values
('B001', 'Giant', 0, 0, 5),
('B005', 'Giant', 0, 0, 3),
('B002', 'Trek', 1, 0, 2),
('B003', 'Specialized', 0, 1, 4),
('B004', 'Cannondale', 0, 0, 6)
;

INSERT INTO 'Cyclist' Values
(361738163, 25, 1),
(361738161, 30, 0),
(361738169, 22, 1),
(361738160, 28, 0),
(361738121, 35, 1)
;

INSERT INTO 'DownfallType' Values
(1, 'Rain'),
(2, 'Snow'),
(3, 'Hail'),
(4, 'Sleet'),
(5, 'Fog'),
(6, 'Drizzle');

INSERT INTO 'ReasonType' Values
(1, 'Slippery road'),
(2, 'Poor visibility'),
(3, 'Mechanical failure'),
(4, 'Human error'),
(5, 'Animal crossing')
;

INSERT INTO 'RoadType' Values
(1, 'Asphalt', 5),
(2, 'Concrete', 6),
(3, 'Gravel', 4),
(4, 'Dirt', 3),
(5, 'Cobblestone', 2);

INSERT INTO 'BicycleOwnership' Values
(1, 361738163, 'B001'),
(2, 361738169, 'B002'),
(3, 361738160, 'B003'),
(4, 361738121, 'B004'),
(5, 361738161, 'B005')
;

INSERT INTO 'Location' Values
(1, 'Amsterdam', 'Damrak', 7, 1),
(2, 'Rotterdam', 'Coolsingel', 6, 2),
(3, 'Utrecht', 'Oudegracht', 5, 3),
(4, 'Eindhoven', 'Stratumseind', 4, 4),
(5, 'Groningen', 'Vismarkt', 3, 5)
;