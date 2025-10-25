#Coaching Session 2 Assignment

##Overview

Following details:

i) Steps on creating db connection, importing csv data into dBeaver. This serve as a guide for fellow classmates who are still struggling.

ii) My DML script and answers to the assignment  questions.

iii) Several comments along the way, to serve as a future reference for myself as well as to facilitate fellow classmates in their learning journey  or offer their input on my solutions.

Happy leaning and coding everyone!

### Creating dB and importing

1. Start up dBeaver app, click on "New Database Connection"

2. Select DuckDB -> Create -> <desired folder you want to store your db>

3. Test connection -> click Finish

4. Open New SQL Script
   (Side Note) For me, I tend to create several SQL for sake of organising my lines of codes. I rename them as "DDL, DML, Queries, Import_Export" for ease of identification.

5. (Optional) Type:

```SQL
CREATE SCHEMA vgsales
```
For me, I just use the default schema (ie main)

6. Type the following to create table and import data.

```SQL
CREATE TABLE vgsales AS SELECT * FROM read_csv_auto ('<vgsales.csv file pathname>', HEADER = TRUE);
```

### Answering Questions

1. Which 5 games have the highest global sales? What do they have in common?

```SQL
DESCRIBE main.vgsales;

SELECT vg.RANK, vg.Name, vg.Global_Sales
FROM main.vgsales vg
ORDER BY vg.Global_Sales DESC
LIMIT 5;
```

Answer- Wii Sports, Super Mario Bros., Mario Kart Wii, Wii Sports Resort, Pokemon Red/Pokemon Blue
(Note: The first line DESCRIBE shows the table already has a ranking. So you can already answer the question.)

2. Calculate total sales by genre. Which genre generates the most revenue globally?

```SQL
SELECT vg.Genre, sum(vg.Global_Sales) AS Total_Global_Sales
FROM main.vgsales vg
GROUP BY vg.Genre
ORDER by Total_Global_sales DESC;
```

Answer - Action

3. Find the average sales per game for each platform. Which platforms have the highest average?

```SQL
SELECT vg.Platform, vg.Name, AVG(vg.Global_Sales) AS average_sales
FROM main.vgsales vg
GROUP BY vg.Platform, vg.Name
ORDER BY average_sales DESC;
```

Answer - Wii and NES hold the top 3 spots.

4. Which publisher has released the most games? Do they also have the highest total sales?

```SQL
SELECT vg.Publisher, COUNT (*) AS number_of_games, SUM(vg.Global_Sales) AS total_sales,
RANK() OVER (ORDER BY total_sales DESC)
FROM main.vgsales vg
GROUP BY vg.Publisher
ORDER BY number_of_games  DESC;
```

Answer -Electronic Arts released the most games. Electronic Arts sales volume ranked 2. Nintendo had the highest game volume sales with just 703 games released.

5. For games released after 2010, which genre dominated each region (NA, EU, JP)?

```SQL
SELECT DISTINCT(year)
FROM main.vgsales vg;
--Finding what is causing the yeart to be VARCHAR instead of interger

WITH games_after_2010 AS (
SELECT vg.Genre, vg.NA_Sales, vg.EU_sales, vg.JP_Sales,
CASE
	WHEN vg.Year ~'^[0-9]+$' THEN CAST(vg.Year AS INT)
	ELSE NULL
	END AS converted_year
FROM main.vgsales vg

	-- ~ means "matching", ^ refers to start of expression, 
	-- + means there can be reoccurence of the numbers, $ means end of expression
	-- if we want to find cells that do not match we add "!" (ie !~'^[0-9]+$')
)
SELECT Genre, SUM(NA_Sales) AS NA_region, SUM(EU_Sales) AS EU_region, SUM(JP_Sales) AS JP_region
FROM games_after_2010
WHERE converted_year > 2010
GROUP BY Genre;
```

Notes - 
1. Previously had problems handling the main.year column as it data is VARCHAR data type. Using DISTINCT function to find out what is causing the problem.

2. Using the CASE function to convert the problematic cell to NULL and rest to integer for processing.

3. Using CTL and sub-query to do a comparison

Answer - NA_region - Action , EU_region - Action, JP_region - Role-Playing

6. Calculate the percentage of global sales that each region contributes. Which region is most important?

```SQL

SELECT 
	ROUND(SUM(vg.NA_Sales)/SUM(vg.Global_Sales),2) AS NA_region,
	ROUND(SUM(vg.EU_Sales)/SUM(vg.Global_Sales),2) AS EU_region,
	ROUND(SUM(vg.JP_Sales)/SUM(vg.Global_Sales),2) AS JP_region
FROM main.vgsales vg;
```

Answer - North America region takes up the highest share of game sales volume

7. Find games where Japanese sales exceed North American sales. What patterns do you notice about genre or publisher

```SQL
WITH JP_v_NA AS(
	SELECT vg.Genre, vg.Publisher, vg.Name,
	SUM(vg.JP_Sales) AS JP_Sales, SUM(vg.NA_Sales) AS NA_Sales
	FROM main.vgsales vg
	WHERE JP_Sales > NA_Sales
	GROUP BY vg.Name, vg.Genre, vg.Publisher
)
SELECT Genre, Publisher, Name, JP_Sales, NA_Sales
FROM JP_v_NA
ORDER BY JP_Sales DESC;
```

Notes - I am unable to create a table to display "trends/patterns". The work done for second part of the question was manual.

Answer -  Role-Playing holds significant popularity among Japanes with Nintendo being the go-to platform.

END