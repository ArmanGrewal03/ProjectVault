SELECT
    i.invoice_id,
    i.patient_id,
    i.treatment_id,
    t.name_of_treatment,
    i.payment_status,
    i.payment_type,
    i.cost
FROM
    invoices i
JOIN
    treatments t
ON
    i.treatment_id = t.treatment_id
WHERE
    i.payment_status = 'Paid'
FETCH FIRST 10 ROWS ONLY;

