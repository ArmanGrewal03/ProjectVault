CREATE VIEW appointment_info AS
SELECT
    a.appointment_id,
    a.description AS appointment_description,
    a.datetime AS appointment_datetime,
    p.name AS patient_name,
    d.name AS dentist_name,
    m.medical_file_id
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN dentists d ON a.dentist_id = d.dentist_id
LEFT JOIN medical_records m ON p.patient_id = m.patient_id;




CREATE VIEW invoice_summary AS
SELECT
    i.invoice_id,
    p.name AS patient_name,
    t.name_of_treatment,
    i.payment_status,
    i.payment_type,
    i.cost
FROM invoices i
JOIN patients p ON i.patient_id = p.patient_id
JOIN treatments t ON i.treatment_id = t.treatment_id;





CREATE VIEW medical_record_summary AS
SELECT
    m.medical_file_id,
    p.name AS patient_name,
    p.date_of_birth,
    p.email_address AS patient_email,
    p.phone_number AS patient_phone
FROM medical_records m
JOIN patients p ON m.patient_id = p.patient_id;




CREATE VIEW inventory_treatment_info AS
SELECT
    i.inventory_id,
    i.name_of_item,
    t.name_of_treatment,
    t.cost AS treatment_cost
FROM inventory i
LEFT JOIN treatments t ON i.inventory_id = t.inventory_inventory_id;






SELECT
    i.invoice_id,
    p.name AS patient_name,
    p.insurance_id,
    t.name_of_treatment,
    i.cost AS treatment_cost,
    i.payment_status,
    i.payment_type
FROM invoices i
JOIN patients p ON i.patient_id = p.patient_id
JOIN treatments t ON i.treatment_id = t.treatment_id;






 SELECT
    p.name AS patient_name,
    p.insurance_id,
    SUM(CASE WHEN i.payment_status = 'Pending' THEN i.cost ELSE 0 END) AS total_unpaid_invoices
FROM patients p
LEFT JOIN invoices i ON p.patient_id = i.patient_id
LEFT JOIN treatments t ON i.treatment_id = t.treatment_id
GROUP BY p.name, p.insurance_id;





SELECT
    TO_CHAR(a.datetime, 'DY') AS day_of_week,
    COUNT(*) AS number_of_appointments,
    d.name AS dentist_name
FROM appointments a
JOIN patients p ON a.patient_id = p.patient_id
JOIN dentists d ON a.dentist_id = d.dentist_id
GROUP BY TO_CHAR(a.datetime, 'DY'), d.name
ORDER BY TO_CHAR(a.datetime, 'DY');
