SELECT FORMAT(((SELECT MAX(TOP_HALF.LAT_N) FROM( SELECT TOP 50 PERCENT ROW_NUMBER() OVER(ORDER BY LAT_N) AS ROWNUM, LAT_N FROM STATION ORDER BY ROW_NUMBER() OVER(ORDER BY LAT_N)) AS TOP_HALF) + (SELECT MIN  (BOTTOM_HALF.LAT_N) FROM( SELECT TOP 50 PERCENT ROW_NUMBER() OVER(ORDER BY LAT_N) AS ROWNUM, LAT_N FROM STATION ORDER BY ROW_NUMBER() OVER(ORDER BY LAT_N DESC)) AS BOTTOM_HALF) ) /2 ,'##.####') AS LAT_N_MEDIAN
