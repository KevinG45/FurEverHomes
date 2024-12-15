
create database FurEverHomes_db;
USE FurEverHomes_db;
CREATE TABLE Animal (
    Animal_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Animal_Type ENUM('DOG', 'CAT', 'HAMSTER') NOT NULL,
    Age TEXT NOT NULL,
    Gender ENUM('MALE', 'FEMALE') NOT NULL,
    Breed VARCHAR(255),
    Health_Issues TEXT,
    Adoption_Status ENUM('AVAILABLE', 'ADOPTED') NOT NULL DEFAULT 'AVAILABLE',
    Description TEXT,
    Image_Path VARCHAR(255) DEFAULT 'images/default.jpg'
);

CREATE TABLE User (
    User_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Phone_Number VARCHAR(20) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL
);

CREATE TABLE Adoption_Application (
    Application_ID INT PRIMARY KEY AUTO_INCREMENT,
    User_ID INT,
    Animal_ID INT,
    Application_Date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Status ENUM('AVAILABLE', 'ADOPTED') NOT NULL DEFAULT 'AVAILABLE',
    FOREIGN KEY (User_ID) REFERENCES User(User_ID),
    FOREIGN KEY (Animal_ID) REFERENCES Animal(Animal_ID)
);
CREATE TABLE Donations (
    Donation_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL DEFAULT 'Anonymous',
    email varchar(255) not null,
    Amount DECIMAL(10, 2) NOT NULL,
    phone_number VARCHAR(15) not null,
    Payment_Method ENUM('CREDIT CARD', 'DEBIT CARD', 'UPI', 'NET BANKING') NOT NULL,
    Donation_Date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE Volunteers (
    Volunteer_ID INT PRIMARY KEY AUTO_INCREMENT,
    User_ID INT NOT NULL,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Phone_Number VARCHAR(20) NOT NULL UNIQUE,
    Age INT NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Camp_Location ENUM('KORMANGALA', 'MARTHAHALLI', 'HOSA ROAD'),
    Image_Path VARCHAR(255) DEFAULT 'images/default.jpg',
    FOREIGN KEY (User_ID) REFERENCES User(User_ID)
);
CREATE TABLE Admin (
    Admin_ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL
);

INSERT INTO Animal (Animal_ID, Name, Animal_Type, Age, Gender, Breed, Health_Issues, Adoption_Status, Description, Image_Path)
VALUES
(1, 'Bruno', 'DOG', '6 years 3 months', 'MALE', 'Labrador', 'Skin allergies', 'AVAILABLE', 'Friendly and energetic, loves playing fetch.', 'images/bruno.jpg'),
(2, 'Ace', 'DOG', '1 year 8 months', 'MALE', 'Indie', NULL, 'ADOPTED', 'Playful and affectionate, good with kids.', 'images/ace.jpg'),
(3, 'Sheru', 'DOG', '5 years 1 month', 'MALE', 'Rottweiler', NULL, 'AVAILABLE', 'Protective and loyal, perfect guard dog.', 'images/sheru.jpeg'),
(4, 'Scooby', 'DOG', '4 years', 'MALE', 'Indie', NULL, 'AVAILABLE', 'Calm, enjoys quiet walks and lounging.', 'images/coco.jpg'),
(5, 'Maximus', 'DOG', '8 months', 'MALE', 'Dachshund', NULL, 'AVAILABLE', 'Very playful, loves company and long walks.', 'images/maximus.jpg'),
(6, 'Coco', 'DOG', '6 years', 'MALE', 'Indie', 'Arthritis', 'AVAILABLE', 'Cute and friendly, loves to be pampered.', 'images/newdog.jpg'),
(7, 'Cherry', 'DOG', '2 years 5 months', 'FEMALE', 'Pomeranian', NULL, 'ADOPTED', 'Intelligent and energetic, needs active play.', 'images/cherry.jpeg'),
(8, 'Cookie', 'DOG', '4 years 7 months', 'FEMALE', 'Indie', 'Mild joint pain', 'ADOPTED', 'Loyal and protective, requires daily exercise.', 'images/cookie.jpg'),
(9, 'Bella', 'DOG', '5 years', 'FEMALE', 'Labrador', NULL, 'AVAILABLE', 'Friendly, loves water, good with children.', 'images/bella.jpeg'),
(10, 'Tuffy', 'DOG', '1 year 10 months', 'MALE', 'Pomeranian', NULL, 'AVAILABLE', 'Small but lively, loves attention.', 'images/tuffy.jpeg');

INSERT INTO Animal (Animal_ID, Name, Animal_Type, Age, Gender, Breed, Health_Issues, Adoption_Status, Description, Image_Path)
VALUES
(11, 'Mishka', 'CAT', '3 months', 'FEMALE', 'Indie', NULL, 'AVAILABLE', 'Loves cuddles, purrs constantly when held.', 'images/cats2indianbreed.jpg'),
(12, 'Noir', 'CAT', '1 year', 'FEMALE', 'Bombay cat', NULL, 'ADOPTED', 'A sleek beauty with a gentle temperament, perfect for first-time owners.', 'images/cats2bombaycat.jpg'),
(13, 'Oscar', 'CAT', '1 year 5 months', 'MALE', 'American Shorthair', 'Sensitive stomach requiring special diet.', 'AVAILABLE', 'A goofy and playful companion who loves belly rubs.', 'images/cats3americanshorthair.jpg'),
(14, 'Fluffy', 'CAT', '1 year', 'MALE', 'Persian', NULL, 'AVAILABLE', 'Quiet and reserved, enjoys relaxing in cozy corners.', 'images/cats2persiancat.jpg'),
(15, 'Max', 'CAT', '8 months', 'MALE', 'Indie', NULL, 'ADOPTED', 'Sociable and loves interacting with people and other cats.', 'images/cats3indianbreed.jpg'),
(16, 'Ruby', 'CAT', '3 years', 'FEMALE', 'Indie', 'Mild joint stiffness that improves with regular exercise.', 'AVAILABLE', 'Playful and loves exploring small nooks. A bundle of energy with a curious mind.', 'images/cats8indianbreed.jpg'),
(17, 'Snowy', 'CAT', '8 months', 'FEMALE', 'Persian', 'Prone to watery eyes and needs regular cleaning.', 'AVAILABLE', 'Beautiful and calm, adores grooming sessions and soft cushions.', 'images/cats3persiancat.jpg'),
(18, 'Shadow', 'CAT', '2 years', 'MALE', 'Bombay cat', NULL, 'AVAILABLE', 'Jet-black coat and a playful personality, loves to chase shadows.', 'images/cats3bombaycat.jpg'),
(19, 'Ash', 'CAT', '1 month', 'MALE', 'American Shorthair', NULL, 'ADOPTED', 'Energetic and loves to play with strings and laser lights.', 'images/cats2americanshorthair.jpg'),
(20, 'Ginger', 'CAT', '1 year 7 months', 'FEMALE', 'Indie', NULL, 'AVAILABLE', 'Gentle and calm, perfect for families with kids.', 'images/cats5indianbreed.jpg');

INSERT INTO Animal (Animal_ID, Name, Animal_Type, Age, Gender, Breed, Health_Issues, Adoption_Status, Description, Image_Path)
VALUES
(21, 'Nibbles', 'HAMSTER', '1 year 2 months', 'MALE', 'Golden Hamster', 'Prone to dental issues', 'AVAILABLE', 'Loves chewing and exploring tunnels.', 'images/goldenhamster3.jpeg'),
(22, 'Pudding', 'HAMSTER', '2 years', 'FEMALE', 'Winter White Hamster', NULL, 'AVAILABLE', 'Adorable and loves to roll in sand baths.', 'images/winterwhitedwarf1.jpeg'),
(23, 'Biscuit', 'HAMSTER', '8 months', 'MALE', 'Roborovski', 'Sensitive to bright light', 'AVAILABLE', 'Small and quick, enjoys wheel running.', 'images/roborovski1.jpeg'),
(24, 'Peanut', 'HAMSTER', '1 year 4 months', 'FEMALE', 'Russian Campbell', 'Mild obesity', 'AVAILABLE', 'Sociable and enjoys group settings.', 'images/russiancampell.jpeg'),
(25, 'Muffin', 'HAMSTER', '3 years', 'FEMALE', 'Golden Hamster', NULL, 'ADOPTED', 'Very friendly and enjoys being cuddled.', 'images/goldenhamster.jpg'),
(26, 'Snickers', 'HAMSTER', '6 months', 'MALE', 'Roborovski', 'Minor joint stiffness', 'AVAILABLE', 'Tiny and full of energy.', 'images/roborovski2.jpeg'),
(27, 'Daisy', 'HAMSTER', '2 years 3 months', 'FEMALE', 'Winter White Hamster', 'Eye irritation', 'ADOPTED', 'Quiet and calm, loves burrowing.', 'images/winterwhitedwarf2.jpeg'),
(28, 'Choco', 'HAMSTER', '1 year', 'MALE', 'Russian Campbell', NULL, 'AVAILABLE', 'Friendly and loves exploring new places.', 'images/russiancambell.jpeg'),
(29, 'Ginger', 'HAMSTER', '2 years', 'FEMALE', 'Golden Hamster', 'Susceptible to heat stress', 'AVAILABLE', 'Cheerful and loves sunflower seeds.', 'images/goldenhamster2.jpeg'),
(30, 'Cinnamon', 'HAMSTER', '10 months', 'MALE', 'Roborovski', NULL, 'AVAILABLE', 'Fast and playful, perfect for hamster races.', 'images/roborovski1.jpeg'),
(31, 'Pip', 'HAMSTER', '1 year 1 month', 'MALE', 'Winter White Hamster', 'Prone to dry skin', 'ADOPTED', 'Sweet and shy, enjoys running in the wheel.', 'images/winterwhitedwarf.jpeg'),
(32, 'Hazel', 'HAMSTER', '1 year 6 months', 'FEMALE', 'Golden Hamster', NULL, 'AVAILABLE', 'Charming and loves to interact with humans.', 'images/goldenhamster3.jpeg'),
(33, 'Coco', 'HAMSTER', '2 years', 'FEMALE', 'Russian Campbell', 'Sensitive digestion', 'AVAILABLE', 'Curious and enjoys climbing structures.', 'images/russiancampell.jpeg'),
(34, 'Taffy', 'HAMSTER', '3 years 2 months', 'MALE', 'Golden Hamster', NULL, 'AVAILABLE', 'Fluffy and loves nesting materials.', 'images/goldenhamster.jpg'),
(35, 'Sugar', 'HAMSTER', '7 months', 'FEMALE', 'Winter White Hamster', 'Mild respiratory issues', 'ADOPTED', 'Playful and loves soft bedding.', 'images/winterwhitedwarf2.jpeg'),
(36, 'Toffee', 'HAMSTER', '1 year 3 months', 'MALE', 'Roborovski', NULL, 'AVAILABLE', 'Loves running and exploring new toys.', 'images/roborovski2.jpeg'),
(37, 'Luna', 'HAMSTER', '2 years 5 months', 'FEMALE', 'Russian Campbell', 'Frequent shedding', 'AVAILABLE', 'Affectionate and loves treats.', 'images/russiancambell.jpeg'),
(38, 'Twix', 'HAMSTER', '8 months', 'MALE', 'Golden Hamster', 'Occasional sneezing', 'AVAILABLE', 'Energetic and loves to tunnel.', 'images/goldenhamster2.jpeg'),
(39, 'Maple', 'HAMSTER', '3 years', 'FEMALE', 'Winter White Hamster', NULL, 'AVAILABLE', 'Gentle and enjoys quiet environments.', 'images/winterwhitedwarf1.jpeg'),
(40, 'Sunny', 'HAMSTER', '1 year', 'FEMALE', 'Roborovski', NULL, 'AVAILABLE', 'Quick and lively, great for active owners.', 'images/roborovski1.jpeg');


INSERT INTO Animal (Animal_ID, Name, Animal_Type, Age, Gender, Breed, Health_Issues, Adoption_Status, Description, Image_Path)
VALUES
(41, 'Buddy', 'DOG', '2 years', 'MALE', 'Labrador', 'Hip dysplasia', 'AVAILABLE', 'Gentle and loves playing in the park.', 'images/ace.jpg'),
(42, 'Duke', 'DOG', '1 year 6 months', 'MALE', 'Rottweiler', NULL, 'AVAILABLE', 'Protective and highly loyal, a perfect guard dog.', 'images/sheru.jpeg'),
(43, 'Barney', 'DOG', '4 years', 'FEMALE', 'Indie', NULL, 'ADOPTED', 'Friendly and calm, enjoys quiet walks.', 'images/scooby.jpg'),
(44, 'Lola', 'DOG', '1 year 3 months', 'FEMALE', 'Pomeranian', 'Prone to skin allergies', 'AVAILABLE', 'Lively and loves to cuddle.', 'images/tuffy.jpeg'),
(45, 'Jack', 'DOG', '3 years', 'MALE', 'Labrador', NULL, 'AVAILABLE', 'Energetic and great with kids.', 'images/bruno.jpg'),
(46, 'Zoe', 'DOG', '2 years 7 months', 'FEMALE', 'Indie', 'Mild joint stiffness', 'AVAILABLE', 'Quiet and affectionate, loves lounging around.', 'images/bella.jpeg'),
(47, 'Max', 'DOG', '6 months', 'MALE', 'Dachshund', NULL, 'ADOPTED', 'Tiny and playful, enjoys long walks.', 'images/maximus.jpg'),
(48, 'Daisy', 'DOG', '5 years', 'FEMALE', 'Pomeranian', NULL, 'AVAILABLE', 'Charming and active, loves attention.', 'images/cherry.jpeg'),
(49, 'Charlie', 'DOG', '1 year', 'MALE', 'Labrador', 'Sensitive stomach', 'ADOPTED', 'Friendly and social, loves outdoor activities.', 'images/bruno.jpg'),
(50, 'Coco', 'DOG', '4 years 6 months', 'MALE', 'Rottweiler', 'Prone to mild arthritis', 'AVAILABLE', 'Loyal and protective, enjoys guarding the house.', 'images/sheru.jpeg');


INSERT INTO Animal (Animal_ID, Name, Animal_Type, Age, Gender, Breed, Health_Issues, Adoption_Status, Description, Image_Path)
VALUES
(51, 'Snowball', 'CAT', '1 year', 'FEMALE', 'Persian', 'Prone to watery eyes', 'AVAILABLE', 'Graceful and calm, loves grooming sessions.', 'images/cats3persiancat.jpg'),
(52, 'Shadow', 'CAT', '2 years 5 months', 'MALE', 'Bombay cat', NULL, 'ADOPTED', 'Jet-black coat and a playful personality.', 'images/cats3bombaycat.jpg'),
(53, 'Mittens', 'CAT', '7 months', 'FEMALE', 'Indie', NULL, 'AVAILABLE', 'Charming and playful, loves small spaces.', 'images/cats2indianbreed.jpg'),
(54, 'Simba', 'CAT', '1 year 3 months', 'MALE', 'American Shorthair', 'Sensitive digestion', 'AVAILABLE', 'Cheerful and loves belly rubs.', 'images/cats2americanshorthair.jpg'),
(55, 'Luna', 'CAT', '3 years', 'FEMALE', 'Persian', NULL, 'ADOPTED', 'Fluffy and affectionate, enjoys lounging on soft cushions.', 'images/cats3persiancat.jpg'),
(56, 'Oliver', 'CAT', '1 year 7 months', 'MALE', 'Bombay cat', 'Mild respiratory issues', 'AVAILABLE', 'Loves to chase shadows and play with strings.', 'images/cats2bombaycat.jpg'),
(57, 'Cleo', 'CAT', '8 months', 'FEMALE', 'Indie', NULL, 'AVAILABLE', 'Lively and curious, enjoys exploring new spaces.', 'images/cats5indianbreed.jpg'),
(58, 'Smokey', 'CAT', '2 years', 'MALE', 'American Shorthair', NULL, 'AVAILABLE', 'Quiet and gentle, loves being held.', 'images/cats3americanshorthair.jpg'),
(59, 'Peaches', 'CAT', '4 years', 'FEMALE', 'Persian', 'Occasional sneezing', 'ADOPTED', 'A fluffy bundle of love, adores being pampered.', 'images/cats3persiancat.jpg'),
(60, 'Leo', 'CAT', '1 year 5 months', 'MALE', 'Bombay cat', NULL, 'AVAILABLE', 'Sleek and friendly, loves spending time with humans.', 'images/cats2bombaycat.jpg');



INSERT INTO User (User_ID, Name, Email, Phone_Number, Password)
VALUES
(1, 'Alice Green', 'alice.green@example.com', '9876543210', 'alice2024'),
(2, 'Liam Carter', 'liam.carter@example.com', '8765432109', 'liamSecure'),
(3, 'Mia Reed', 'mia.reed@example.com', '7654321098', 'mia@pass'),
(4, 'Noah Blake', 'noah.blake@example.com', '6543210987', 'noah123'),
(5, 'Emma Hill', 'emma.hill@example.com', '5432109876', 'emma_secure'),
(6, 'Ethan Fox', 'ethan.fox@example.com', '4321098765', 'ethanPass'),
(7, 'Sophia Dean', 'sophia.dean@example.com', '3210987654', 'sophiaRocks'),
(8, 'Logan Price', 'logan.price@example.com', '2109876543', 'logan_001'),
(9, 'Ava Scott', 'ava.scott@example.com', '1987654321', 'avaSecure'),
(10, 'Jack Hayes', 'jack.hayes@example.com', '9876501234', 'jack456');



ALTER TABLE Adoption_Application
DROP COLUMN Status;

INSERT INTO Adoption_Application (Application_ID, User_ID, Animal_ID, Application_Date)
VALUES
-- Applications for Adopted Animals
(1, 3, 2, '2024-12-05 10:30:00'),  -- Ace (Dog, ADOPTED)
(2, 5, 7, '2024-12-06 14:00:00'),  -- Cherry (Dog, ADOPTED)
(3, 6, 8, '2024-12-06 16:30:00'),  -- Cookie (Dog, ADOPTED)
(4, 7, 12, '2024-12-07 09:15:00'), -- Noir (Cat, ADOPTED)
(5, 8, 15, '2024-12-06 16:30:00'), -- Max (Cat, ADOPTED)
(6, 9, 19, '2024-12-07 11:15:00'), -- Ash (Cat, ADOPTED)
(7, 10, 25, '2024-12-07 13:00:00'), -- Muffin (Hamster, ADOPTED)
(8, 3, 27, '2024-12-05 12:45:00'), -- Daisy (Hamster, ADOPTED)
(9, 4, 31, '2024-12-06 10:15:00'), -- Pip (Hamster, ADOPTED)
(10, 5, 35, '2024-12-06 14:30:00'), -- Sugar (Hamster, ADOPTED)
(11, 6, 43, '2024-12-07 09:00:00'), -- Bella (Dog, ADOPTED)
(12, 7, 47, '2024-12-07 10:45:00'), -- Max (Dog, ADOPTED)
(13, 8, 49, '2024-12-07 11:30:00'), -- Charlie (Dog, ADOPTED)
(14, 9, 52, '2024-12-07 13:15:00'), -- Shadow (Cat, ADOPTED)
(15, 10, 55, '2024-12-07 14:00:00'), -- Luna (Cat, ADOPTED)
(16, 3, 59, '2024-12-07 14:30:00'), -- Peaches (Cat, ADOPTED)

-- Applications for Selected Available Animals
(17, 4, 1, '2024-12-05 15:00:00'),  -- Bruno (Dog, AVAILABLE)
(18, 5, 3, '2024-12-06 11:30:00'),  -- Sheru (Dog, AVAILABLE)
(19, 6, 9, '2024-12-06 18:00:00'),  -- Bella (Dog, AVAILABLE)
(20, 7, 13, '2024-12-07 08:30:00'), -- Oscar (Cat, AVAILABLE)
(21, 8, 16, '2024-12-07 09:45:00'), -- Ruby (Cat, AVAILABLE)
(22, 9, 22, '2024-12-07 10:15:00'), -- Pudding (Hamster, AVAILABLE)
(23, 10, 26, '2024-12-07 11:00:00'), -- Snickers (Hamster, AVAILABLE)
(24, 3, 40, '2024-12-07 11:45:00'); -- Sunny (Hamster, AVAILABLE)


-- Inserting volunteers based on random users from the User table

INSERT INTO Volunteers (User_ID, Name, Email, Phone_Number, Age, Address, Camp_Location, Image_Path)
SELECT User_ID, Name, Email, Phone_Number, 30, '123 Main St', 'KORMANGALA', 'images/volunteer1.jpg'
FROM User
WHERE User_ID = 2;  -- Liam Carter

INSERT INTO Volunteers (User_ID, Name, Email, Phone_Number, Age, Address, Camp_Location, Image_Path)
SELECT User_ID, Name, Email, Phone_Number, 28, '456 Oak St', 'MARTHAHALLI', 'images/volunteer2.jpg'
FROM User
WHERE User_ID = 5;  -- Emma Hill

INSERT INTO Volunteers (User_ID, Name, Email, Phone_Number, Age, Address, Camp_Location, Image_Path)
SELECT User_ID, Name, Email, Phone_Number, 25, '789 Pine St', 'HOSA ROAD', 'images/volunteer3.jpg'
FROM User
WHERE User_ID = 7;  -- Sophia Dean

INSERT INTO Volunteers (User_ID, Name, Email, Phone_Number, Age, Address, Camp_Location, Image_Path)
SELECT User_ID, Name, Email, Phone_Number, 35, '101 Maple St', 'KORMANGALA', 'images/volunteer4.jpg'
FROM User
WHERE User_ID = 9;  -- Ava Scott

Insert into admin values(1,'Kevin','kev@gmail.com','qwerty1234'),
(2,'Simran','simran@gmail.com','1234qwerty'),
(3,'Shradha','shradha@gmail.com','asdfgh7890');



INSERT INTO Donations (Name, email, Amount, phone_number, Payment_Method) VALUES
('John Doe', 'johndoe@example.com', 500.00, '9876543210', 'CREDIT CARD'),
('Jane Smith', 'janesmith@example.com', 750.50, '8765432109', 'DEBIT CARD'),
('Anonymous', 'anonymous1@example.com', 1000.00, '7654321098', 'UPI'),
('Michael Johnson', 'michael.johnson@example.com', 2575.00, '6543210987', 'NET BANKING'),
('Emily Brown', 'emilybrown@example.com', 2000.00, '5432109876', 'CREDIT CARD'),
('Anonymous', 'anonymous2@example.com', 1500.00, '4321098765', 'UPI'),
('Sarah Davis', 'sarahdavis@example.com', 3000.00, '3210987654', 'DEBIT CARD'),
('David Wilson', 'davidwilson@example.com', 800.00, '2109876543', 'CREDIT CARD'),
('Anna Moore', 'annamoore@example.com', 1205.50, '1098765432', 'NET BANKING'),
('Anonymous', 'anonymous3@example.com', 600.00, '9876012345', 'DEBIT CARD'),
('James Taylor', 'jamestaylor@example.com', 5000.00, '8765012345', 'UPI'),
('Olivia Anderson', 'oliviaanderson@example.com', 400.00, '7654012345', 'NET BANKING'),
('Anonymous', 'anonymous4@example.com', 900.00, '6543012345', 'CREDIT CARD'),
('Liam Martinez', 'liammartinez@example.com', 2500.00, '5432012345', 'DEBIT CARD'),
('Sophia Garcia', 'sophiagarcia@example.com', 350.00, '4321012345', 'UPI');


CREATE TABLE dogadoptform (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    pet_type ENUM('Dog', 'Cat', 'Hamster') NOT NULL,
    reason TEXT NOT NULL
);
ALTER TABLE dogadoptform
ADD COLUMN address TEXT NOT NULL;

INSERT INTO dogadoptform(name, email, phone_number, pet_type, reason, address) 
VALUES 
('John Doe', 'johndoe@example.com', '+911234567890', 'Dog', 'I want to provide a loving home.', '123 Main Street, Delhi, India'),
('Jane Smith', 'janesmith@example.com', '+919876543210', 'Cat', 'Looking for a companion.', '456 Park Avenue, Bangalore, India'),
('Emily Brown', 'emilybrown@example.com', '9876543210', 'Hamster', 'My kids want a small pet to care for.', '789 Green Road, Mumbai, India'),
('Michael Johnson', 'michaelj@example.com', '+919123456789', 'Dog', 'Always wanted a dog to adopt.', '101 Sunset Blvd, Hyderabad, India'),
('Sophia White', 'sophiaw@example.com', '9123456789', 'Cat', 'Looking for a cat to keep me company.', '303 Oak Street, Chennai, India');

ALTER TABLE Donations
DROP COLUMN Donation_Date;

