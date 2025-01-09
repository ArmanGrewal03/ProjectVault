SELECT
    i.invoice_id,
    i.patient_id,
    i.treatment_id,
    t.name_of_treatment,
    i.payment_status,
    i.payment_type,
    i.cost
FROM (
    SELECT
        i.invoice_id,
        i.patient_id,
        i.treatment_id,
        i.payment_status,
        i.payment_type,
        i.cost,
        ROWNUM AS rn
    FROM
        invoices i
    WHERE
        i.payment_status = 'Paid'
) i
JOIN
    treatments t
ON
    i.treatment_id = t.treatment_id
WHERE
    i.rn <= 10;