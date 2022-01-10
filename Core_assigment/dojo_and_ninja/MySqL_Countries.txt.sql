SELECT * FROM tweets;

SELECT * FROM tweets 
WHERE id = 3 OR id = 5
ORDER BY id DESC;

SELECT * FROM tweets 
WHERE  tweet LIKE "%e" OR tweet LIKE "%y" OR tweet LIKE "t%" 
LIMIT 2,4;

UPDATE twitter.users SET
first_name  = "jonn"
WHERE id = 5;

UPDATE twitter.tweets SET
tweet = "cool day"
WHERE id = 17; 

DELETE FROM tweets 
WHERE id = 17;   