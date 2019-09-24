SELECT tblFN.Company_Code AS CC, tblFN.Founder AS FN FROM COMPANY AS tblFN;
/*
SELECT tblCC.COMPANY_CODE AS CC, COUNT(tblLM.LEAD_MANAGER_CODE) AS LM, 0 AS SM, 0 AS MM, 0 AS EE  FROM COMPANY AS tblCC LEFT JOIN LEAD_MANAGER AS tblLM ON tblCC.COMPANY_CODE = tblLM.COMPANY_CODE GROUP BY tblCC.COMPANY_CODE

SELECT tblCC.COMPANY_CODE AS CC,  0 AS LM, COUNT(tblSM.SENIOR_MANAGER_CODE) AS SM, 0 AS MM, 0 AS EE  FROM COMPANY AS tblCC LEFT JOIN SENIOR_MANAGER AS tblSM ON tblCC.COMPANY_CODE = tblSM.COMPANY_CODE GROUP BY tblCC.COMPANY_CODE

SELECT tblCC.COMPANY_CODE AS CC, 0 AS LM, 0 AS SM, COUNT(tblMM.MANAGER_CODE) AS MM, 0 AS EE  FROM COMPANY AS tblCC LEFT JOIN MANAGER AS tblMM ON tblCC.COMPANY_CODE = tblMM.COMPANY_CODE GROUP BY tblCC.COMPANY_CODE

SELECT tblCC.COMPANY_CODE AS CC, 0 AS LM, 0 AS SM, 0 AS MM, COUNT(tblEE.EMPLOYEE_CODE) AS EE  FROM COMPANY AS tblCC LEFT JOIN EMPLOYEE AS tblEE ON tblCC.COMPANY_CODE = tblEE.COMPANY_CODE GROUP BY tblCC.COMPANY_CODE

*/
SELECT tblcon.CC, tblFN.FN,  SUM(tblcon.LM) AS LM, SUM(tblcon.SM) AS SM, SUM(tblcon.MM) AS MM, SUM(tblcon.EE) AS EE FROM (SELECT tblCC.COMPANY_CODE AS CC, COUNT(DISTINCT tblLM.LEAD_MANAGER_CODE) AS LM, 0 AS SM, 0 AS MM, 0 AS EE  FROM COMPANY AS tblCC INNER JOIN LEAD_MANAGER AS tblLM ON tblCC.COMPANY_CODE = tblLM.COMPANY_CODE GROUP BY tblCC.COMPANY_CODE UNION SELECT tblCC.COMPANY_CODE AS CC,  0 AS LM, COUNT(DISTINCT tblSM.SENIOR_MANAGER_CODE) AS SM, 0 AS MM, 0 AS EE  FROM COMPANY AS tblCC INNER JOIN SENIOR_MANAGER AS tblSM ON tblCC.COMPANY_CODE = tblSM.COMPANY_CODE GROUP BY tblCC.COMPANY_CODE UNION SELECT tblCC.COMPANY_CODE AS CC, 0 AS LM, 0 AS SM, COUNT(DISTINCT tblMM.MANAGER_CODE) AS MM, 0 AS EE  FROM COMPANY AS tblCC INNER JOIN MANAGER AS tblMM ON tblCC.COMPANY_CODE = tblMM.COMPANY_CODE GROUP BY tblCC.COMPANY_CODE UNION SELECT tblCC.COMPANY_CODE AS CC, 0 AS LM, 0 AS SM, 0 AS MM, COUNT(DISTINCT tblEE.EMPLOYEE_CODE) AS EE  FROM COMPANY AS tblCC INNER JOIN EMPLOYEE AS tblEE ON tblCC.COMPANY_CODE = tblEE.COMPANY_CODE GROUP BY tblCC.COMPANY_CODE) AS tblcon INNER JOIN (SELECT Company_Code AS FN_CC, Founder AS FN FROM COMPANY) AS tblFN ON tblcon.cc = tblFN.FN_CC GROUP BY tblcon.CC, tblFN.FN ORDER BY tblcon.CC;
