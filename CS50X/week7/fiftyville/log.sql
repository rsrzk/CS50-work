-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Context: CS50 duck stolen, took flight withh accomplice help. Took place 28 July 2021 on Humphrey Street.

-- Understanding the database structure
.schema

-- CREATE TABLE crime_scene_reports (
--     id INTEGER,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     street TEXT,
--     description TEXT,
--     PRIMARY KEY(id)
-- );
-- CREATE TABLE interviews (
--     id INTEGER,
--     name TEXT,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     transcript TEXT,
--     PRIMARY KEY(id)
-- );
-- CREATE TABLE atm_transactions (
--     id INTEGER,
--     account_number INTEGER,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     atm_location TEXT,
--     transaction_type TEXT,
--     amount INTEGER,
--     PRIMARY KEY(id)
-- );
-- CREATE TABLE bank_accounts (
--     account_number INTEGER,
--     person_id INTEGER,
--     creation_year INTEGER,
--     FOREIGN KEY(person_id) REFERENCES people(id)
-- );
-- CREATE TABLE airports (
--     id INTEGER,
--     abbreviation TEXT,
--     full_name TEXT,
--     city TEXT,
--     PRIMARY KEY(id)
-- );
-- CREATE TABLE flights (
--     id INTEGER,
--     origin_airport_id INTEGER,
--     destination_airport_id INTEGER,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     hour INTEGER,
--     minute INTEGER,
--     PRIMARY KEY(id),
--     FOREIGN KEY(origin_airport_id) REFERENCES airports(id),
--     FOREIGN KEY(destination_airport_id) REFERENCES airports(id)
-- );
-- CREATE TABLE passengers (
--     flight_id INTEGER,
--     passport_number INTEGER,
--     seat TEXT,
--     FOREIGN KEY(flight_id) REFERENCES flights(id)
-- );
-- CREATE TABLE phone_calls (
--     id INTEGER,
--     caller TEXT,
--     receiver TEXT,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     duration INTEGER,
--     PRIMARY KEY(id)
-- );
-- CREATE TABLE people (
--     id INTEGER,
--     name TEXT,
--     phone_number TEXT,
--     passport_number INTEGER,
--     license_plate TEXT,
--     PRIMARY KEY(id)
-- );
-- CREATE TABLE bakery_security_logs (
--     id INTEGER,
--     year INTEGER,
--     month INTEGER,
--     day INTEGER,
--     hour INTEGER,
--     minute INTEGER,
--     activity TEXT,
--     license_plate TEXT,
--     PRIMARY KEY(id)
-- );

-- To start with crime scene reports.
SELECT COUNT(*) FROM crime_scene_reports; -- 301 reports
SELECT COUNT(*) FROM interviews; -- 192 interviews
SELECT * FROM crime_scene_reports LIMIT 3; -- to understand structure. Will need to filter database by crime scene date and location

SELECT * FROM crime_scene_reports WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street';
-- Two logs:
-- (id: 295) Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
-- (id: 297) Littering took place at 16:36. No known witnesses.

-- To check out the 3 interviews
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;
-- | id  |  name   | year | month | day |                                                                                                                                                     transcript                                                                                                                                                      |
-- | 158 | Jose    | 2021 | 7     | 28  | “Ah,” said he, “I forgot that I had not seen you for some weeks. It is a little souvenir from the King of Bohemia in return for my assistance in the case of the Irene Adler papers.”                                                                                                                               |
-- | 159 | Eugene  | 2021 | 7     | 28  | “I suppose,” said Holmes, “that when Mr. Windibank came back from France he was very annoyed at your having gone to the ball.”                                                                                                                                                                                      |
-- | 160 | Barbara | 2021 | 7     | 28  | “You had my note?” he asked with a deep harsh voice and a strongly marked German accent. “I told you that I would call.” He looked from one to the other of us, as if uncertain which to address.                                                                                                                   |

-- | 161 | Ruth    | 2021 | 7     | 28  | Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away. If you have security footage from the bakery parking lot, you might want to look for cars that left the parking lot in that time frame.                                                          |
-- | 162 | Eugene  | 2021 | 7     | 28  | I don't know the thief's name, but it was someone I recognized. Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.                                                                                                 |
-- | 163 | Raymond | 2021 | 7     | 28  | As the thief was leaving the bakery, they called someone who talked to them for less than a minute. In the call, I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow. The thief then asked the person on the other end of the phone to purchase the flight ticket. |

-- | 191 | Lily    | 2021 | 7     | 28  | Our neighboring courthouse has a very annoying rooster that crows loudly at 6am every day. My sons Robert and Patrick took the rooster to a city far, far away, so it may never bother us again. My sons have successfully arrived in Paris.                                                                        |

-- Relevant transcripts are 161 to 1163
-- Within 10 mins of theft, Ruth saw thief got into car in bakey parking lot and drove away. TODO: Check security footage from 10.15am till 10.25am
-- Eugene recognised thief. Saw thief before going to Emma's bakery, saw thief withdrawing money from Leggett Street ATM. TODO: Check ATM transactions before 10.15am
-- Raymond saw thief called someone and spoke for less than a minute. Heard they planned to take earliest flight out of Fiftyville tomorrow. Asked accomplice to buy ticket. TODO: Check flights and who bought them

-- Bakery security logs
SELECT * from bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >=15 AND minute <= 25;

-- I now have a list of license plates I can use to filter the people database
SELECT * from people WHERE license_plate IN (SELECT license_plate from bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >=15 AND minute <= 25);
-- |   id   |  name   |  phone_number  | passport_number | license_plate |
-- +--------+---------+----------------+-----------------+---------------+
-- | 221103 | Vanessa | (725) 555-4692 | 2963008352      | 5P2BI95       |
-- | 243696 | Barry   | (301) 555-4174 | 7526138472      | 6P58WS2       |
-- | 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
-- | 398010 | Sofia   | (130) 555-0289 | 1695452385      | G412CB7       |
-- | 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
-- | 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
-- | 560886 | Kelsey  | (499) 555-9472 | 8294398571      | 0NTHK55       |
-- | 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |

-- I can now cross reference this with the call logs and flight database


-- Looking into ATM transactions, unfortunately database does not have time of transactions
SELECT * FROM atm_transactions
    JOIN bank_accounts
    ON atm_transactions.account_number = bank_accounts.account_number
    JOIN people
    ON bank_accounts.person_id = people.id
    WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location LIKE '%Leggett Street%';
-- | id  | account_number | year | month | day |  atm_location  | transaction_type | amount | account_number | person_id | creation_year |   id   |  name   |  phone_number  | passport_number | license_plate |
-- +-----+----------------+------+-------+-----+----------------+------------------+--------+----------------+-----------+---------------+--------+---------+----------------+-----------------+---------------+
-- | 267 | 49610011       | 2021 | 7     | 28  | Leggett Street | withdraw         | 50     | 49610011       | 686048    | 2010          | 686048 | Bruce   | (367) 555-5533 | 5773159633      | 94KL13X       |
-- | 275 | 86363979       | 2021 | 7     | 28  | Leggett Street | deposit          | 10     | 86363979       | 948985    | 2010          | 948985 | Kaelyn  | (098) 555-1164 | 8304650265      | I449449       |
-- | 336 | 26013199       | 2021 | 7     | 28  | Leggett Street | withdraw         | 35     | 26013199       | 514354    | 2012          | 514354 | Diana   | (770) 555-1861 | 3592750733      | 322W7JE       |
-- | 269 | 16153065       | 2021 | 7     | 28  | Leggett Street | withdraw         | 80     | 16153065       | 458378    | 2012          | 458378 | Brooke  | (122) 555-4581 | 4408372428      | QX4YZN3       |
-- | 264 | 28296815       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     | 28296815       | 395717    | 2014          | 395717 | Kenny   | (826) 555-1652 | 9878712108      | 30G67EN       |
-- | 288 | 25506511       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     | 25506511       | 396669    | 2014          | 396669 | Iman    | (829) 555-5269 | 7049073643      | L93JTIZ       |
-- | 246 | 28500762       | 2021 | 7     | 28  | Leggett Street | withdraw         | 48     | 28500762       | 467400    | 2014          | 467400 | Luca    | (389) 555-5198 | 8496433585      | 4328GD8       |
-- | 266 | 76054385       | 2021 | 7     | 28  | Leggett Street | withdraw         | 60     | 76054385       | 449774    | 2015          | 449774 | Taylor  | (286) 555-6063 | 1988161715      | 1106N58       |
-- | 313 | 81061156       | 2021 | 7     | 28  | Leggett Street | withdraw         | 30     | 81061156       | 438727    | 2018          | 438727 | Benista | (338) 555-6650 | 9586786673      | 8X428L0       |

-- Can find those that match license plate numbers from security footage
SELECT * FROM atm_transactions
    JOIN bank_accounts
    ON atm_transactions.account_number = bank_accounts.account_number
    JOIN people
    ON bank_accounts.person_id = people.id
    WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location LIKE '%Leggett Street%'
    AND license_plate IN (SELECT license_plate from bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >=15 AND minute <= 25);
-- | id  | account_number | year | month | day |  atm_location  | transaction_type | amount | account_number | person_id | creation_year |   id   | name  |  phone_number  | passport_number | license_plate |
-- +-----+----------------+------+-------+-----+----------------+------------------+--------+----------------+-----------+---------------+--------+-------+----------------+-----------------+---------------+
-- | 267 | 49610011       | 2021 | 7     | 28  | Leggett Street | withdraw         | 50     | 49610011       | 686048    | 2010          | 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
-- | 336 | 26013199       | 2021 | 7     | 28  | Leggett Street | withdraw         | 35     | 26013199       | 514354    | 2012          | 514354 | Diana | (770) 555-1861 | 3592750733      | 322W7JE       |
-- | 288 | 25506511       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     | 25506511       | 396669    | 2014          | 396669 | Iman  | (829) 555-5269 | 7049073643      | L93JTIZ       |
-- | 246 | 28500762       | 2021 | 7     | 28  | Leggett Street | withdraw         | 48     | 28500762       | 467400    | 2014          | 467400 | Luca  | (389) 555-5198 | 8496433585      | 4328GD8       |



-- Checking call logs for calls less than a minute

SELECT * from phone_calls
    WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;
-- | id  |     caller     |    receiver    | year | month | day | duration |
-- +-----+----------------+----------------+------+-------+-----+----------+
-- | 221 | (130) 555-0289 | (996) 555-8899 | 2021 | 7     | 28  | 51       |
-- | 224 | (499) 555-9472 | (892) 555-8872 | 2021 | 7     | 28  | 36       |
-- | 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       |
-- | 251 | (499) 555-9472 | (717) 555-1342 | 2021 | 7     | 28  | 50       |
-- | 254 | (286) 555-6063 | (676) 555-6554 | 2021 | 7     | 28  | 43       |
-- | 255 | (770) 555-1861 | (725) 555-3243 | 2021 | 7     | 28  | 49       |
-- | 261 | (031) 555-6622 | (910) 555-3251 | 2021 | 7     | 28  | 38       |
-- | 279 | (826) 555-1652 | (066) 555-9701 | 2021 | 7     | 28  | 55       |
-- | 281 | (338) 555-6650 | (704) 555-2131 | 2021 | 7     | 28  | 54       |

-- Will now cross check both caller and receiver numbers with any of our suspects


SELECT * FROM atm_transactions
    JOIN bank_accounts
    ON atm_transactions.account_number = bank_accounts.account_number
    JOIN people
    ON bank_accounts.person_id = people.id
    WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location LIKE '%Leggett Street%'
    AND license_plate IN (SELECT license_plate from bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >=15 AND minute <= 25)
    AND
        (
            phone_number IN
                (
                    SELECT caller from phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60
                )
            OR
            phone_number IN
                (
                    SELECT caller from phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60
                )
        )
    ;

-- | id  | account_number | year | month | day |  atm_location  | transaction_type | amount | account_number | person_id | creation_year |   id   | name  |  phone_number  | passport_number | license_plate |
-- +-----+----------------+------+-------+-----+----------------+------------------+--------+----------------+-----------+---------------+--------+-------+----------------+-----------------+---------------+
-- | 267 | 49610011       | 2021 | 7     | 28  | Leggett Street | withdraw         | 50     | 49610011       | 686048    | 2010          | 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |
-- | 336 | 26013199       | 2021 | 7     | 28  | Leggett Street | withdraw         | 35     | 26013199       | 514354    | 2012          | 514354 | Diana | (770) 555-1861 | 3592750733      | 322W7JE       |

-- Important to also know who Bruce and Diana called
SELECT * from phone_calls
    JOIN people
    ON phone_calls.receiver = people.phone_number
    WHERE caller IN
    (
        SELECT phone_number FROM atm_transactions
            JOIN bank_accounts
            ON atm_transactions.account_number = bank_accounts.account_number
            JOIN people
            ON bank_accounts.person_id = people.id
            WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location LIKE '%Leggett Street%'
            AND license_plate IN (SELECT license_plate from bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >=15 AND minute <= 25)
            AND
                (
                    phone_number IN
                        (
                            SELECT caller from phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60
                        )
                    OR
                    phone_number IN
                        (
                            SELECT caller from phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60
                        )
                )
    )
    AND year = 2021 AND month = 7 AND day = 28 AND duration < 60
;
-- | id  |     caller     |    receiver    | year | month | day | duration |   id   |  name  |  phone_number  | passport_number | license_plate |
-- +-----+----------------+----------------+------+-------+-----+----------+--------+--------+----------------+-----------------+---------------+
-- | 233 | (367) 555-5533 | (375) 555-8161 | 2021 | 7     | 28  | 45       | 864400 | Robin  | (375) 555-8161 | NULL            | 4V16VO0       | called by Bruce
-- | 255 | (770) 555-1861 | (725) 555-3243 | 2021 | 7     | 28  | 49       | 847116 | Philip | (725) 555-3243 | 3391710505      | GW362R6       | called by Diana



-- Last place to look would be the flights. Chheck earliest flights the next day

-- understanding airports table
SELECT * FROM airports;

-- Finding potential flights
SELECT * FROM flights
    JOIN airports
    ON flights.destination_airport_id = airports.id
    WHERE flights.origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
    AND year = 2021 AND month = 7 AND day = 29
    ORDER BY hour, minute;
-- | id | origin_airport_id | destination_airport_id | year | month | day | hour | minute | id | abbreviation |              full_name              |     city      |
-- +----+-------------------+------------------------+------+-------+-----+------+--------+----+--------------+-------------------------------------+---------------+
-- | 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     | 4  | LGA          | LaGuardia Airport                   | New York City |
-- | 43 | 8                 | 1                      | 2021 | 7     | 29  | 9    | 30     | 1  | ORD          | O'Hare International Airport        | Chicago       |
-- | 23 | 8                 | 11                     | 2021 | 7     | 29  | 12   | 15     | 11 | SFO          | San Francisco International Airport | San Francisco |
-- | 53 | 8                 | 9                      | 2021 | 7     | 29  | 15   | 20     | 9  | HND          | Tokyo International Airport         | Tokyo         |
-- | 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      | 6  | BOS          | Logan International Airport         | Boston        |

SELECT * FROM flights
    JOIN airports
    ON flights.destination_airport_id = airports.id
    JOIN passengers
    ON flights.id = passengers.flight_id
    JOIN people
    ON passengers.passport_number = people.passport_number
    WHERE flights.origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
    AND year = 2021 AND month = 7 AND day = 29
    AND
    (
        passengers.passport_number IN
        (
            -- accomplice
            SELECT passport_number from phone_calls
                JOIN people
                ON phone_calls.receiver = people.phone_number
                WHERE caller IN
                (
                    SELECT phone_number FROM atm_transactions
                        JOIN bank_accounts
                        ON atm_transactions.account_number = bank_accounts.account_number
                        JOIN people
                        ON bank_accounts.person_id = people.id
                        WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location LIKE '%Leggett Street%'
                        AND license_plate IN (SELECT license_plate from bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >=15 AND minute <= 25)
                        AND
                            (
                                phone_number IN
                                    (
                                        SELECT caller from phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60
                                    )
                                OR
                                phone_number IN
                                    (
                                        SELECT caller from phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60
                                    )
                            )
                )
                AND year = 2021 AND month = 7 AND day = 28 AND duration < 60
        )
        OR
        passengers.passport_number IN
        (
            -- thief
            SELECT passport_number FROM atm_transactions
                JOIN bank_accounts
                ON atm_transactions.account_number = bank_accounts.account_number
                JOIN people
                ON bank_accounts.person_id = people.id
                WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location LIKE '%Leggett Street%'
                AND license_plate IN (SELECT license_plate from bakery_security_logs WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute >=15 AND minute <= 25)
                AND
                    (
                        phone_number IN
                            (
                                SELECT caller from phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60
                            )
                        OR
                        phone_number IN
                            (
                                SELECT caller from phone_calls WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60
                            )
                    )
        )
    );
-- | id | origin_airport_id | destination_airport_id | year | month | day | hour | minute | id | abbreviation |          full_name          |     city      | flight_id | passport_number | seat |   id   | name  |  phone_number  | passport_number | license_plate |
-- +----+-------------------+------------------------+------+-------+-----+------+--------+----+--------------+-----------------------------+---------------+-----------+-----------------+------+--------+-------+----------------+-----------------+---------------+
-- | 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      | 6  | BOS          | Logan International Airport | Boston        | 18        | 3592750733      | 4C   | 514354 | Diana | (770) 555-1861 | 3592750733      | 322W7JE       |
-- | 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     | 4  | LGA          | LaGuardia Airport           | New York City | 36        | 5773159633      | 4A   | 686048 | Bruce | (367) 555-5533 | 5773159633      | 94KL13X       |


-- Double checking that accomplices are not on the above flights
SELECT * FROM flights
   ...>     JOIN airports
   ...>     ON flights.destination_airport_id = airports.id
   ...>     JOIN passengers
   ...>     ON flights.id = passengers.flight_id
   ...>     JOIN people
   ...>     ON passengers.passport_number = people.passport_number
   ...>     WHERE flights.origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville')
   ...>     AND year = 2021 AND month = 7 AND day = 29
   ...>     AND (flights.id = 18 OR flights.id = 36);
-- | id | origin_airport_id | destination_airport_id | year | month | day | hour | minute | id | abbreviation |          full_name          |     city      | flight_id | passport_number | seat |   id   |   name    |  phone_number  | passport_number | license_plate |
-- +----+-------------------+------------------------+------+-------+-----+------+--------+----+--------------+-----------------------------+---------------+-----------+-----------------+------+--------+-----------+----------------+-----------------+---------------+
-- | 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      | 6  | BOS          | Logan International Airport | Boston        | 18        | 2835165196      | 9C   | 788911 | Gloria    | (973) 555-3809 | 2835165196      | O010420       |
-- | 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      | 6  | BOS          | Logan International Airport | Boston        | 18        | 6131360461      | 2C   | 253397 | Kristina  | (918) 555-2946 | 6131360461      | P743G7C       |
-- | 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      | 6  | BOS          | Logan International Airport | Boston        | 18        | 3231999695      | 3C   | 757606 | Douglas   | (491) 555-2505 | 3231999695      | 1FW4EUJ       |
-- | 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      | 6  | BOS          | Logan International Airport | Boston        | 18        | 3592750733      | 4C   | 514354 | Diana     | (770) 555-1861 | 3592750733      | 322W7JE       |
-- | 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      | 6  | BOS          | Logan International Airport | Boston        | 18        | 2626335085      | 5D   | 952462 | Christian | NULL           | 2626335085      | 6CV51G1       |
-- | 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      | 6  | BOS          | Logan International Airport | Boston        | 18        | 6117294637      | 6B   | 542503 | Michael   | (529) 555-7276 | 6117294637      | HOD8639       |
-- | 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      | 6  | BOS          | Logan International Airport | Boston        | 18        | 2996517496      | 7A   | 682850 | Ethan     | (594) 555-6254 | 2996517496      | NAW9653       |
-- | 18 | 8                 | 6                      | 2021 | 7     | 29  | 16   | 0      | 6  | BOS          | Logan International Airport | Boston        | 18        | 3915621712      | 8D   | 769190 | Charles   | (427) 555-0556 | 3915621712      | R12SA4D       |
-- | 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     | 4  | LGA          | LaGuardia Airport           | New York City | 36        | 7214083635      | 2A   | 953679 | Doris     | (066) 555-9701 | 7214083635      | M51FA04       |
-- | 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     | 4  | LGA          | LaGuardia Airport           | New York City | 36        | 1695452385      | 3B   | 398010 | Sofia     | (130) 555-0289 | 1695452385      | G412CB7       |
-- | 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     | 4  | LGA          | LaGuardia Airport           | New York City | 36        | 5773159633      | 4A   | 686048 | Bruce     | (367) 555-5533 | 5773159633      | 94KL13X       |
-- | 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     | 4  | LGA          | LaGuardia Airport           | New York City | 36        | 1540955065      | 5C   | 651714 | Edward    | (328) 555-1152 | 1540955065      | 130LD9Z       |
-- | 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     | 4  | LGA          | LaGuardia Airport           | New York City | 36        | 8294398571      | 6C   | 560886 | Kelsey    | (499) 555-9472 | 8294398571      | 0NTHK55       |
-- | 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     | 4  | LGA          | LaGuardia Airport           | New York City | 36        | 1988161715      | 6D   | 449774 | Taylor    | (286) 555-6063 | 1988161715      | 1106N58       |
-- | 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     | 4  | LGA          | LaGuardia Airport           | New York City | 36        | 9878712108      | 7A   | 395717 | Kenny     | (826) 555-1652 | 9878712108      | 30G67EN       |
-- | 36 | 8                 | 4                      | 2021 | 7     | 29  | 8    | 20     | 4  | LGA          | LaGuardia Airport           | New York City | 36        | 8496433585      | 7B   | 467400 | Luca      | (389) 555-5198 | 8496433585      | 4328GD8       |

-- Between the two suspects, Bruce and Diana, it appears that Bruce is the likely suspect due to the earlier flight time but it does not feel conclusive. Will do some extra homework and view Bruce's and Robin's bank transactions

SELECT * FROM atm_transactions
    JOIN bank_accounts
    ON atm_transactions.account_number = bank_accounts.account_number
    JOIN people
    ON bank_accounts.person_id = people.id
    WHERE people.id = 686048 OR people.id = 864400;
-- This did not bring about any interesting information

-- Double checked the interview statements. They wanted the earliest flight out of Fiftyville and Bruce is on the earliest flight.