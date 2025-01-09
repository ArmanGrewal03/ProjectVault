SET PAGESIZE 100
SET LINESIZE 150
TTITLE "Orthodontic Specialists Directory: A-Z Order and Names starting with Dr";
COLUMN dentist_id FORMAT 99999
COLUMN email_address FORMAT A30
COLUMN phone_number FORMAT A20
COLUMN name FORMAT A30
COLUMN specialization FORMAT A20
SELECT DISTINCT dentist_id, email_address, phone_number, name, specialization
FROM dentists
WHERE specialization = 'Orthodontics' AND name LIKE 'Dr%'
ORDER BY name ASC;





SET PAGESIZE 100
SET LINESIZE 150
TTITLE "Upcoming Appointments with a specific dentist: Sorted by Date and Time:";
COLUMN appointment_id FORMAT 99999
COLUMN description FORMAT A30
COLUMN dentist_id FORMAT 99999
COLUMN patient_id FORMAT 99999
COLUMN datetime FORMAT A20
SELECT DISTINCT *
FROM appointments
WHERE dentist_id = 1
ORDER BY datetime ASC;





SET PAGESIZE 100
SET LINESIZE 150
TTITLE "Adult Patients: Sorted by Name and Date of Birth:";
COLUMN patient_id FORMAT 99999
COLUMN name FORMAT A30
COLUMN date_of_birth FORMAT A13
SELECT DISTINCT patient_id, name, TO_CHAR(date_of_birth, 'YYYY-MM-DD') AS date_of_birth
FROM patients
WHERE date_of_birth > TO_DATE('1990-01-01', 'YYYY-MM-DD')
ORDER BY name ASC;





SET PAGESIZE 100
SET LINESIZE 150
TTITLE "Medical Records Sorted by Age";
COLUMN medical_file_id FORMAT 999999
COLUMN patient_id FORMAT 99999
SELECT *
FROM medical_records
WHERE patient_id IN (
    SELECT patient_id
    FROM patients
    WHERE EXTRACT(YEAR FROM date_of_birth) > 1995
)
ORDER BY (
    SELECT date_of_birth
    FROM patients
    WHERE patients.patient_id = medical_records.patient_id
) ASC;






SET PAGESIZE 100
SET LINESIZE 150
TTITLE "Inventory Summary by Category: Total Quantities:";
COLUMN item_category_or_type FORMAT A30
COLUMN total_quantity FORMAT 999,999
SELECT item_category_or_type, SUM(quantity) AS total_quantity
FROM inventory
GROUP BY item_category_or_type
ORDER BY total_quantity DESC;





SET PAGESIZE 100
SET LINESIZE 150
TTITLE "High-Cost Treatments: Sorted by Descending Cost:";
COLUMN treatment_id FORMAT 99999
COLUMN cost FORMAT 999,999.99
COLUMN description FORMAT A30
COLUMN name_of_treatment FORMAT A30
COLUMN inventory_inventory_id FORMAT 99999
SELECT DISTINCT *
FROM treatments
WHERE cost > 350
ORDER BY cost DESC;





SET PAGESIZE 100
SET LINESIZE 150
TTITLE "Unpaid Invoices: Total Costs Grouped by Patients, Highest to Lowest:";
COLUMN patient_id FORMAT 99999
COLUMN total_cost FORMAT 999,999.99
SELECT patient_id, SUM(cost) AS total_cost
FROM invoices
WHERE payment_status != 'Paid'
GROUP BY patient_id
ORDER BY total_cost DESC;





