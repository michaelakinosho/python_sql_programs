SELECT d.Name AS 'Doctor', p.Name AS 'Professor', s.Name AS 'Singer', a.Name AS 'Actor'
FROM 
(SELECT Name, Row_number() over(order by name) as num FROM Occupations WHERE Occupation = 'Doctor') d full join 
(SELECT Name, Row_number() over(order by name) as num FROM Occupations WHERE Occupation = 'Professor') p on d.num = p.num full join 
(SELECT Name, Row_number() over(order by name) as num FROM Occupations WHERE Occupation = 'Singer') s on d.num = s.num or p.num = s.num full join 
(SELECT Name, Row_number() over(order by name) as num FROM Occupations WHERE Occupation = 'Actor') a on d.num = a.num or p.num = a.num or s.num = a.num;

