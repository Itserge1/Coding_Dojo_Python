#1
SELECT countries.name,languages.language,languages.percentage
FROM languages
JOIN countries ON countries.id = languages.country_id
WHERE language = "Slovene"
ORDER BY languages.percentage DESC;

#2
SELECT countries.name, COUNT(cities.name) as city_count
FROM countries
JOIN cities ON countries.id  = country_id
GROUP BY countries.name
ORDER BY city_count DESC;

#3

SELECT cities.name, cities.population, cities.country_id
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.country_id DESC;

#4
SELECT countries.name, languages.language, languages.percentage
FROM languages
JOIN countries ON languages.country_id =  countries.id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;






