/*SELECT * FROM (SELECT contest_id FROM dbo.Contests) AS myContests LEFT OUTER JOIN (SELECT contest_id FROM dbo.Colleges) AS myColleges ON myContests.contest_id=myColleges.contest_id
*/

SELECT myContests.contest_id, myContests.hacker_id, myContests.name, SUM(myColleges.total_submissions) AS [total submissions], SUM(myColleges.total_accepted_submissions) AS [total accepted submissions], SUM(myColleges.total_views) AS [total views], SUM(myColleges.total_unique_views) AS [total unique views] FROM ( SELECT * FROM (SELECT Contests.contest_id, Contests.hacker_id, Contests.name, Colleges.college_id FROM Contests LEFT OUTER JOIN Colleges ON Contests.contest_id = Colleges.contest_id GROUP BY Contests.contest_id, Contests.hacker_id, Contests.name, Colleges.college_id) AS vHackerDetail   ) AS myContests LEFT OUTER JOIN ( SELECT * FROM (SELECT qryViewSubmissions.college_id, SUM(qryViewSubmissions.[sum of total_submissions]) AS total_submissions, SUM(qryViewSubmissions.[sum of total_accepted_submissions]) AS total_accepted_submissions, SUM(qryViewSubmissions.[sum of total_views]) AS total_views, SUM(qryViewSubmissions.[sum of total_unique_views]) AS total_unique_views FROM (SELECT Challenges.college_id, IIF(SUM(Submission_Stats.total_submissions) IS NULL,0,SUM(Submission_Stats.total_submissions)) AS [sum of total_submissions], IIF(SUM(Submission_Stats.total_accepted_submissions) IS NULL,0,SUM(Submission_Stats.total_accepted_submissions)) AS [sum of total_accepted_submissions], 0 AS [sum of total_views], 0 AS [sum of total_unique_views] FROM Challenges LEFT OUTER JOIN Submission_Stats ON Challenges.challenge_id = Submission_Stats.challenge_id GROUP BY Challenges.college_id UNION SELECT  Challenges.college_id, 0 AS [sum of total_submissions], 0 AS [sum of total_accepted_submissions], IIF(SUM(View_Stats.total_views) IS NULL,0,SUM(View_Stats.total_views)) AS [sum of total_views], IIF(SUM(View_Stats.total_unique_views) IS NULL,0,SUM(View_Stats.total_unique_views)) AS [sum of total_unique_views] FROM  Challenges LEFT OUTER JOIN View_Stats ON Challenges.challenge_id = View_Stats.challenge_id GROUP BY Challenges.college_id) AS qryViewSubmissions GROUP BY qryViewSubmissions.college_id) AS vHackerStats) AS myColleges ON myContests.college_id=myColleges.college_id GROUP BY  myContests.contest_id, myContests.hacker_id, myContests.name HAVING (SUM(myColleges.total_submissions)+SUM(myColleges.total_accepted_submissions)+SUM(myColleges.total_views)+SUM(myColleges.total_unique_views))>0

/*
SELECT * FROM (
SELECT        dbo.Contests.contest_id, dbo.Contests.hacker_id, dbo.Contests.name, dbo.Colleges.college_id
FROM            dbo.Contests LEFT OUTER JOIN
                         dbo.Colleges ON dbo.Contests.contest_id = dbo.Colleges.contest_id
GROUP BY dbo.Contests.contest_id, dbo.Contests.hacker_id, dbo.Contests.name, dbo.Colleges.college_id) AS vHackerDetail


SELECT * FROM (
SELECT qryViewSubmissions.college_id,
SUM(qryViewSubmissions.[sum of total_submissions]) AS total_submissions, SUM(qryViewSubmissions.[sum of total_accepted_submissions]) AS total_accepted_submissions,
SUM(qryViewSubmissions.[sum of total_views]) AS total_views, SUM(qryViewSubmissions.[sum of total_unique_views]) AS total_unique_views
FROM (SELECT        dbo.Challenges.college_id, IIF(SUM(dbo.Submissions_Stats.total_submissions) IS NULL,0,SUM(dbo.Submissions_Stats.total_submissions)) AS [sum of total_submissions],
                     IIF(SUM(dbo.Submissions_Stats.total_accepted_submissions) IS NULL,0,SUM(dbo.Submissions_Stats.total_accepted_submissions)) AS [sum of total_accepted_submissions], 0 AS [sum of total_views], 0 AS [sum of total_unique_views]
FROM            dbo.Challenges LEFT OUTER JOIN
                         dbo.Submissions_Stats ON dbo.Challenges.challenge_id = dbo.Submissions_Stats.challenge_id
GROUP BY dbo.Challenges.college_id
UNION
SELECT        dbo.Challenges.college_id, 0 AS [sum of total_submissions], 0 AS [sum of total_accepted_submissions], IIF(SUM(dbo.View_Stats.total_views) IS NULL,0,SUM(dbo.View_Stats.total_views)) AS [sum of total_views],
                     IIF(SUM(dbo.View_Stats.total_unique_views) IS NULL,0,SUM(dbo.View_Stats.total_unique_views)) AS [sum of total_unique_views]
FROM            dbo.Challenges LEFT OUTER JOIN
                         dbo.View_Stats ON dbo.Challenges.challenge_id = dbo.View_Stats.challenge_id
GROUP BY dbo.Challenges.college_id) AS qryViewSubmissions GROUP BY qryViewSubmissions.college_id) AS vHackerStats
*/
