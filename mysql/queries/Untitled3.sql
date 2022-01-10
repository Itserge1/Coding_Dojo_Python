SELECT *
FROM users
LEFT JOIN tweets
ON users.id = tweets.user_id
WHERE users.id = 1;

SELECT tweets.tweet
FROM users
LEFT JOIN tweets
ON users.id = tweets.user_id
WHERE users.id = 1;

SELECT first_name, tweet
FROM users
LEFT JOIN faves
ON users.id = faves.user_id
LEFT JOIN tweets
ON faves.tweet_id = tweets.id
WHERE users.id = 2;

SELECT first_name, tweet
FROM users
LEFT JOIN faves
ON users.id = faves.user_id
LEFT JOIN tweets
ON faves.tweet_id = tweets.id
WHERE users.id = 1 OR users.id = 2;

SELECT users.first_name as followed, users2.first_name as follower
FROM users
LEFT JOIN follows
ON users.id = follows.followed_id
LEFT JOIN users as users2
ON users2.id = follows.follower_id
WHERE users.id = 1;