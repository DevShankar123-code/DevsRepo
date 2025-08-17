
CREATE DATABASE IF NOT EXISTS Hospital_Patient_Care_Performance_Analysis;
USE Hospital_Patient_Care_Performance_Analysis;
select * from modified_healthcare_dataset;

-- Patient Demographics
SELECT Gender, COUNT(*) AS total_patients
FROM modified_healthcare_dataset
GROUP BY Gender;

-- Admission Trends
SELECT DATE_FORMAT("Date of Admission", '%Y-%m') AS Month, COUNT(*) AS Admissions
FROM modified_healthcare_dataset
GROUP BY Month
ORDER BY Month;

-- Most Common Diseases
SELECT "Medical Condition", COUNT(*) AS case_count
FROM modified_healthcare_dataset
GROUP BY "Medical Condition"
ORDER BY case_count DESC
LIMIT 10;

-- Bed Occupancy & Length of Stay
SELECT "Room Number", AVG("Length of Stay") AS "avg stay"
FROM modified_healthcare_dataset
GROUP BY "Room Number";

-- Department/Doctor Performance
SELECT Doctor, COUNT(*) AS patients_handled, AVG("Length of Stay") AS avg_recovery_days
FROM modified_healthcare_dataset
GROUP BY Doctor
ORDER BY patients_handled DESC;

-- Financial Analysis
SELECT 'Medical Condition', AVG ( 'Billing Amount') AS avg_cost
FROM modified_healthcare_dataset
GROUP BY 'Medical Condition'
ORDER BY avg_cost DESC;

-- Age Distribution by Range
SELECT
    CASE
        WHEN Age < 18 THEN '0-17'
        WHEN Age BETWEEN 18 AND 35 THEN '18-35'
        WHEN Age BETWEEN 36 AND 50 THEN '36-50'
        WHEN Age BETWEEN 51 AND 65 THEN '51-65'
        ELSE '66+'
    END AS age_group,
    COUNT(*) AS total
FROM modified_healthcare_dataset
GROUP BY age_group
ORDER BY total DESC;

-- 7. Seasonal Disease Patterns
SELECT 'Medical Condition',
       CASE
           WHEN MONTH('Date of Admission') IN (12,1,2) THEN 'Winter'
           WHEN MONTH('Date of Admission') IN (3,4,5) THEN 'Spring'
           WHEN MONTH('Date of Admission') IN (6,7,8) THEN 'Summer'
           ELSE 'Autumn'
       END AS season,
       COUNT(*) AS cases
FROM modified_healthcare_dataset
GROUP BY 'Medical Condition', season
ORDER BY cases DESC;

-- 8. Average Length of Stay per Disease
SELECT 'Medical Condition',
       ROUND(AVG('Length of Stay'), 2) AS avg_stay_days
FROM modified_healthcare_dataset
GROUP BY 'Medical Condition'
ORDER BY avg_stay_days DESC;

-- 9. Bed Occupancy per Room
SELECT 'Room Number',
       COUNT(*) AS patients_assigned,
       ROUND(AVG('Length of Stay'), 2) AS avg_stay
FROM modified_healthcare_dataset
GROUP BY 'Room Number'
ORDER BY patients_assigned DESC;

-- 10. Emergency vs Scheduled Admissions
SELECT 'Admission Type', COUNT(*) AS total
FROM modified_healthcare_dataset
GROUP BY 'Admission Type';

-- 11. Doctor Performance (Patient Load + Avg Recovery)
SELECT Doctor,
       COUNT(*) AS 'patients handled',
       ROUND(AVG('Length of Stay'), 2) AS avg_recovery_days
FROM modified_healthcare_dataset
GROUP BY Doctor
ORDER BY 'patients handled' DESC;

-- 12. Department Performance
SELECT Hospital AS Department,
       COUNT(*) AS 'Patients Handled',
       ROUND(AVG(`Length of Stay`), 2) AS 'Avg Recovery Days'
FROM modified_healthcare_dataset
GROUP BY Department
ORDER BY 'Patients Handled' DESC;

-- 13. Revenue per Department
SELECT Hospital AS Department,
       ROUND(SUM(`Billing Amount`), 2) AS 'Total Revenue'
FROM modified_healthcare_dataset
GROUP BY Department
ORDER BY 'Total Revenue' DESC;

-- 14. Average Cost per Disease
SELECT `Medical Condition`,
       ROUND(AVG(`Billing Amount`), 2) AS 'Avg Cost'
FROM modified_healthcare_dataset
GROUP BY `Medical Condition`
ORDER BY 'Avg Cost' DESC;

-- 15. Cost Efficiency (Cost per Day)
SELECT `Medical Condition`,
       ROUND(AVG(`Billing Amount` / `Length of Stay`), 2) AS 'Avg Cost Per Day'
FROM modified_healthcare_dataset
WHERE `Length of Stay` > 0
GROUP BY `Medical Condition`
ORDER BY 'Avg Cost Per Day' DESC;