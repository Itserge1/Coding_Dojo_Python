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

#5
SELECT countries.name, countries.surface_area, countries.population FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000;

#6
SELECT countries.name, countries.government_form, countries.capital , countries.life_expectancy FROM countries
WHERE countries.government_form = "Constitutional Monarchy" AND countries.capital > 200 AND countries.life_expectancy > 75.0;

#7
SELECT countries.name, cities.name, cities.district, cities.population
FROM cities 
JOIN countries ON countries.id = cities.country_id
WHERE countries.name = "Argentina" AND cities.district = "Buenos Aires" AND cities.population > 500000;

#8
SELECT countries.region, COUNT(countries.name) AS total_countries FROM countries 
GROUP BY countries.region
ORDER BY total_countries DESC














