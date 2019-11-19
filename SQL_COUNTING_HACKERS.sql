USE DESKTOP_ADV
--SELECT DISTINCT submission_date FROM Submissions

DECLARE @sub_date DATE
SET @sub_date = N'2016-03-01'
SELECT tblFour.submission_date, COUNT(tblFour.hacker_count) AS Count_Reg_Hacker  FROM 
	(SELECT @sub_date AS submission_date, COUNT(tblOne.hacker_id) AS hacker_count  FROM 
		(SELECT DISTINCT submission_date, hacker_id FROM Submissions WHERE Submissions.submission_date <= @sub_date GROUP BY submission_date, hacker_id) AS tblOne GROUP BY tblOne.hacker_id HAVING ((COUNT(tblOne.hacker_id) IN (SELECT MAX(tblThree.Max_Hacker_Count) FROM 
			(SELECT tblTwo.hacker_id, MAX(tblTwo.hacker_count) AS Max_Hacker_Count FROM 
				(SELECT @sub_date AS submission_date, tblOne.hacker_id, COUNT(tblOne.hacker_id) AS hacker_count  FROM 
					(SELECT DISTINCT submission_date, hacker_id FROM Submissions WHERE Submissions.submission_date <= @sub_date GROUP BY submission_date, hacker_id) AS tblOne GROUP BY tblOne.hacker_id) AS tblTwo GROUP BY tblTwo.hacker_id) AS tblThree)))) AS tblFour GROUP BY tblFour.submission_date


SELECT tblxFour.submission_date, tblxFour.hacker_id, Hackers.name FROM (SELECT tblxThree.submission_date, MIN(tblxThree.hacker_id) AS hacker_id FROM 
	(SELECT tblxTwo.submission_date, tblxTwo.hacker_id, tblxTwo.hacker_submissions FROM 
		(SELECT tblxOne.submission_date, tblxOne.hacker_id, (tblxOne.hacker_submissions) FROM 
			(SELECT DISTINCT @sub_date as submission_date, hacker_id, COUNT(hacker_id) AS hacker_submissions FROM Submissions GROUP BY submission_date, hacker_id HAVING (Submissions.submission_date = @sub_date)) AS tblxOne GROUP BY tblxOne.submission_date, tblxOne.hacker_id, tblxOne.hacker_submissions) AS tblxTwo GROUP BY tblxTwo.submission_date, tblxTwo.hacker_id, tblxTwo.hacker_submissions  HAVING (((tblxTwo.hacker_submissions) IN 
				(SELECT MAX(tblxOne.hacker_submissions) FROM (SELECT DISTINCT @sub_date as submission_date, hacker_id, COUNT(hacker_id) AS hacker_submissions FROM Submissions GROUP BY submission_date, hacker_id HAVING (Submissions.submission_date = @sub_date)) AS tblxOne)))) AS tblxThree GROUP BY tblxThree.submission_date) AS tblxFour INNER JOIN Hackers ON tblxFour.hacker_id = Hackers.hacker_id 


SELECT DISTINCT Submissions.submission_date, tblFive.Count_Reg_Hacker, tblxFive.hacker_id,  tblxFive.name FROM (Submissions LEFT JOIN (SELECT tblFour.submission_date, COUNT(tblFour.hacker_count) AS Count_Reg_Hacker  FROM 
	(SELECT @sub_date AS submission_date, COUNT(tblOne.hacker_id) AS hacker_count  FROM 
		(SELECT DISTINCT submission_date, hacker_id FROM Submissions WHERE Submissions.submission_date <= @sub_date GROUP BY submission_date, hacker_id) AS tblOne GROUP BY tblOne.hacker_id HAVING ((COUNT(tblOne.hacker_id) IN (SELECT MAX(tblThree.Max_Hacker_Count) FROM 
			(SELECT tblTwo.hacker_id, MAX(tblTwo.hacker_count) AS Max_Hacker_Count FROM 
				(SELECT @sub_date AS submission_date, tblOne.hacker_id, COUNT(tblOne.hacker_id) AS hacker_count  FROM 
					(SELECT DISTINCT submission_date, hacker_id FROM Submissions WHERE Submissions.submission_date <= @sub_date GROUP BY submission_date, hacker_id) AS tblOne GROUP BY tblOne.hacker_id) AS tblTwo GROUP BY tblTwo.hacker_id) AS tblThree)))) AS tblFour GROUP BY tblFour.submission_date) AS tblFive ON Submissions.submission_date = tblFive.submission_date) LEFT JOIN 
					( SELECT tblxFour.submission_date, tblxFour.hacker_id, Hackers.name FROM (SELECT tblxThree.submission_date, MIN(tblxThree.hacker_id) AS hacker_id FROM 
	(SELECT tblxTwo.submission_date, tblxTwo.hacker_id, tblxTwo.hacker_submissions FROM 
		(SELECT tblxOne.submission_date, tblxOne.hacker_id, (tblxOne.hacker_submissions) FROM 
			(SELECT DISTINCT @sub_date as submission_date, hacker_id, COUNT(hacker_id) AS hacker_submissions FROM Submissions GROUP BY submission_date, hacker_id HAVING (Submissions.submission_date = @sub_date)) AS tblxOne GROUP BY tblxOne.submission_date, tblxOne.hacker_id, tblxOne.hacker_submissions) AS tblxTwo GROUP BY tblxTwo.submission_date, tblxTwo.hacker_id, tblxTwo.hacker_submissions  HAVING (((tblxTwo.hacker_submissions) IN 
				(SELECT MAX(tblxOne.hacker_submissions) FROM (SELECT DISTINCT @sub_date as submission_date, hacker_id, COUNT(hacker_id) AS hacker_submissions FROM Submissions GROUP BY submission_date, hacker_id HAVING (Submissions.submission_date = @sub_date)) AS tblxOne)))) AS tblxThree GROUP BY tblxThree.submission_date) AS tblxFour INNER JOIN Hackers ON tblxFour.hacker_id = Hackers.hacker_id  ) AS tblxFive ON Submissions.submission_date = tblxFive.submission_date