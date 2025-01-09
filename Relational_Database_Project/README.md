# Dental Clinic Database Management System

## INTRODUCTION

Efficient data management is pivotal in ensuring smooth operations and delivering quality care. A **Dental Clinic Database Management System (DBMS)** is a comprehensive solution designed to support the specific needs of a dentist's office, streamlining the various processes that occur on a daily basis. Unlike generic healthcare database systems, this DBMS caters to the unique requirements of dental clinics.

This database, combined with a **Graphical User Interface (GUI)**, will handle the frequent updates and management tasks that are common in clinics. It will also provide the ability to view and interact with data in an efficient manner. Key functionalities include managing patient information, scheduling appointments, tracking patient records, managing inventory supplies, and handling invoices. Furthermore, the system will allow for easy querying to obtain precise and relevant information, enabling the clinic to optimize operations, improve patient care, and enhance revenue management.

### Core Features of the DBMS

- **Patient Management**: Store and retrieve detailed patient information such as contact details, health card number, insurance, and treatment history.
- **Appointments Scheduling**: Maintain an appointment schedule linked to patients and dentists.
- **Medical Records**: Access patient-specific medical records for treatment history.
- **Inventory Management**: Track supplies and their usage.
- **Treatment and Invoices**: Manage treatments performed and generate associated invoices.
- **Data Querying**: Run queries to get specific information, improving decision-making and operational efficiency.

---

## **Database Tables**

### 1. **Patients Table**
- **Cardinality**: 
  - 1-M (One-to-Many) relationship with **Appointments**.
  - 1-1 (One-to-One) relationship with **Medical Records**.
  - 1-M (One-to-Many) relationship with **Invoices**.

| Field Name       | Description                             | Data Type     |
|------------------|-----------------------------------------|---------------|
| Patient ID       | Unique patient number (Primary Key)     | Integer       |
| Health Card ID   | Unique health card number               | Integer       |
| Name             | Patient’s first and last name           | Varchar2(500) |
| Email Address    | Patient's email address                 | Varchar2(500) |
| Phone Number     | Patient's phone number                  | Varchar2(20)  |
| Date of Birth    | Patient's Date of Birth                 | Date          |
| Insurance ID     | Unique insurance number                | Integer       |

### 2. **Appointments Table**
- **Cardinality**:
  - M-1 (Many-to-One) relationship with **Patients**.
  - M-1 (Many-to-One) relationship with **Dentists**.

| Field Name       | Description                             | Data Type     |
|------------------|-----------------------------------------|---------------|
| Appointment ID   | Unique appointment number (Primary Key) | Integer       |
| Date & Time      | Date and time of appointment            | Date          |
| Description      | Description of the exam being performed | Varchar2(1000)|
| Dentist ID       | Foreign key to **Dentists** table       | Integer       |
| Patient ID       | Foreign key to **Patients** table       | Integer       |

### 3. **Dentists Table**
- **Cardinality**:
  - 1-M (One-to-Many) relationship with **Appointments**.

| Field Name       | Description                             | Data Type     |
|------------------|-----------------------------------------|---------------|
| Dentist ID       | Unique dentist number (Primary Key)     | Integer       |
| Name             | Dentist's first and last name           | Varchar2(500) |
| Specialization   | Dentist’s specialization (e.g., Orthodontist) | Varchar2(20) |
| Email Address    | Dentist's email address                 | Varchar2(500) |
| Phone Number     | Dentist’s phone number                  | Varchar2(500) |

### 4. **Treatments Table**
- **Cardinality**:
  - 1-M (One-to-Many) relationship with **Inventory**.
  - M-1 (Many-to-One) relationship with **Invoices**.

| Field Name       | Description                             | Data Type     |
|------------------|-----------------------------------------|---------------|
| Treatment ID     | Unique treatment number (Primary Key)   | Integer       |
| Name             | Name of treatment (e.g., filling, root canal) | Varchar2(1000)|
| Description      | Brief description of the procedure      | Varchar2(1000)|
| Cost             | Cost of the procedure                   | Number(9,2)   |
| Inventory ID     | Foreign key to **Inventory** table      | Integer       |

### 5. **Inventory Table**
- **Cardinality**:
  - M-1 (Many-to-One) relationship with **Treatments**.

| Field Name       | Description                             | Data Type     |
|------------------|-----------------------------------------|---------------|
| Inventory ID     | Unique inventory number (Primary Key)   | Integer       |
| Name             | Name of item (e.g., dental instruments) | Varchar2(500) |
| Quantity         | Quantity of items in stock              | Integer       |
| Item Category    | Category of item (e.g., consumables, medications) | Varchar2(1000) |

### 6. **Invoices Table**
- **Cardinality**:
  - 1-M (One-to-Many) relationship with **Treatments**.
  - M-1 (Many-to-One) relationship with **Patients**.

| Field Name       | Description                             | Data Type     |
|------------------|-----------------------------------------|---------------|
| Invoice ID       | Unique invoice number (Primary Key)     | Integer       |
| Patient ID       | Foreign key to **Patients** table       | Integer       |
| Treatment ID     | Foreign key to **Treatments** table     | Integer       |
| Payment Type     | Payment type (e.g., Cash, Credit, Debit)| Varchar2(50)  |
| Payment Status   | Payment status (e.g., Paid, Unpaid)     | Varchar2(50)  |
| Cost             | Total cost of the treatment             | Number(9,2)   |

### 7. **Medical Records Table**
- **Cardinality**:
  - M-1 (Many-to-One) relationship with **Patients**.

| Field Name       | Description                             | Data Type     |
|------------------|-----------------------------------------|---------------|
| Medical File ID  | Unique medical record number (Primary Key) | Integer     |
| Patient ID       | Foreign key to **Patients** table       | Integer       |

---

## **Data Integrity and Referential Integrity**

In a dental clinic setting, it is essential to maintain the integrity of sensitive information. To ensure data quality, certain constraints are implemented:

- **Entity Integrity**: 
  - **Primary Keys** such as `Patient ID` and `Dentist ID` must be unique and cannot be duplicated.
  - Attributes like `Specialization` or `Item Category` can have duplicates, as they are not critical to uniquely identify a record.

- **Referential Integrity**: 
  - **Foreign Keys** establish relationships between tables, ensuring that each record in a child table corresponds to a valid record in the parent table. For example:
    - The `Patient ID` in **Appointments**, **Invoices**, and **Medical Records** refers to the `Patient ID` in the **Patients Table**.
    - The `Treatment ID` in **Invoices** refers to the `Treatment ID` in the **Treatments Table**.

---

## **Data Queries and JOINs**

To present data effectively and to avoid redundancy, **JOINs** are used. Since foreign keys exist in the tables, they can be referenced across multiple tables. This allows the merging of related data from different tables into a single query result.

- **Example 1**: Retrieving detailed patient appointment information:
  - Use a JOIN between **Appointments** and **Patients** to get patient details along with appointment information.

- **Example 2**: Generating invoices with associated treatments:
  - Use a JOIN between **Invoices**, **Treatments**, and **Patients** to create a comprehensive invoice with patient details and treatment costs.

---

## **Entity Relationship Diagram (ERD)**

Below is the **Entity Relationship Diagram (ERD)** created to meet the requirements for the Dental Clinic Database Management System:

![image](https://github.com/user-attachments/assets/f36e8ad7-3b66-430d-a9cd-8b92ec2e0bae)


---

## Conclusion

The Dental Clinic Database Management System streamlines clinic operations by centralizing patient information, appointment scheduling, treatment management, and inventory tracking. By utilizing structured tables with well-defined relationships and enforcing data integrity, the system ensures efficient and secure management of clinic data, ultimately contributing to improved patient care and optimized clinic operations.
