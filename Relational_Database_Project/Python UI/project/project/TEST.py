from tkinter import ttk, messagebox
import oracledb
import tkinter as tk
from tkinter import messagebox
from tkinter import Label, Entry, Button, messagebox

class DentalClinicGUI:
        # Define a common style for buttons
    button_style = {'font': ('Helvetica', 14), 'padx': 10, 'pady': 5, 'width': 20, 'highlightthickness': 0}

    # Background colors for buttons
    button_colors = ['#3498db', '#2980b9']

    def __init__(self, master):
        self.master = master
        self.master.title("Dental Clinic Database Manager")
        self.master.geometry("800x800")
        self.master.configure(bg='#D6DBDF')



        
        username = "****"  
        password = "******"  
        host = "*****"  
        port = "*****"  
        service_name = "*****"  


        try:
            self.connection = oracledb.connect(
                user=username,
                password=password,
                dsn=f"{host}:{port}/{service_name}"
            )
            self.cursor = self.connection.cursor()

            # Create and place widgets
            self.label = tk.Label(self.master, text="Dental Clinic Database Manager", font=("Helvetica", 20), pady=20, bg='#D6DBDF')
            self.label.pack()

            button_font = ("Helvetica", 16)  

            self.button_drop_tables = tk.Button(self.master, text="Drop Tables", command=self.drop_tables,
                                               bg=self.button_colors[0],wraplength=400,width=40,height=2,font=button_font)
            self.button_drop_tables.pack(pady=10)
            self.set_button_style_on_hover(self.button_drop_tables, self.button_colors)

            self.button_create_table = tk.Button(self.master, text="Create Tables", command=self.create_table,
                                                bg=self.button_colors[0],wraplength=400,width=40,height=2,font=button_font)
            self.button_create_table.pack(pady=10)
            self.set_button_style_on_hover(self.button_create_table, self.button_colors)


            self.button_populate_table = tk.Button(self.master, text="Populate Tables", command=self.populate_table,
                                                bg=self.button_colors[0],wraplength=400,width=40,height=2,font=button_font)
            self.button_populate_table.pack(pady=10)
            self.set_button_style_on_hover(self.button_populate_table, self.button_colors)


            self.button_create_view = tk.Button(self.master, text="Create Views", command=self.create_view,
                                                bg=self.button_colors[0],wraplength=400,width=40,height=2,font=button_font)
            self.button_create_view.pack(pady=10)
            self.set_button_style_on_hover(self.button_create_view, self.button_colors)


            self.button_query_list = tk.Button(self.master, text="Query List", command=self.query_list,
                                                bg=self.button_colors[0],wraplength=400,width=40,height=2,font=button_font)
            self.button_query_list.pack(pady=10)
            self.set_button_style_on_hover(self.button_query_list, self.button_colors)



            self.button_add_entries_menu = tk.Button(self.master, text="Insert New Entries", command=self.add_entries_menu,
                                                bg=self.button_colors[0],wraplength=400,width=40,height=2,font=button_font)
            self.button_add_entries_menu.pack(pady=10)
            self.set_button_style_on_hover(self.button_add_entries_menu, self.button_colors)


            # Add more buttons as needed

        except oracledb.Error as e:
            messagebox.showerror("Error", f"Error connecting to the database: {e}")

    def set_button_style_on_hover(self, button, colors):
        button.bind("<Enter>", lambda e: button.configure(bg=colors[1]))
        button.bind("<Leave>", lambda e: button.configure(bg=colors[0]))



##################
    def rebuild_main_menu(self):
            # Clear the current content in the main window
            for widget in self.master.winfo_children():
                widget.destroy()
                self.master.geometry("800x800")

            button_font = ("Helvetica", 16)  

            # Add widgets for the "Drop Tables" menu
            label = tk.Label(self.master, text="Dental Clinic Database Manager", font=("Helvetica", 20), pady=20, bg='#D6DBDF')
            label.pack()
            self.button_style = {"font": ("Arial", 14)}


            q1_button = tk.Button(self.master, text="Drop Tables", command=self.drop_tables,
                                    bg=self.button_colors[0],wraplength=400,width=40,height=2,font=button_font)
            q1_button.pack(pady=10)
            self.set_button_style_on_hover(q1_button, [self.button_colors[1], self.button_colors[0]])




            q2_button = tk.Button(self.master, text="Create Tables", command=self.create_table,
                                    bg=self.button_colors[0],wraplength=400,width=40,height=2,font=button_font)
            q2_button.pack(pady=10)
            self.set_button_style_on_hover(q2_button, [self.button_colors[1], self.button_colors[0]])


            q3_button = tk.Button(self.master, text="Populate Tables", command=self.populate_table,
                                    bg=self.button_colors[0],wraplength=400,width=40,height=2,font=button_font)
            q3_button.pack(pady=10)
            self.set_button_style_on_hover(q3_button, [self.button_colors[1], self.button_colors[0]])


            q4_button = tk.Button(self.master, text="Create Views", command=self.create_view,
                                    bg=self.button_colors[0],wraplength=400,width=40,height=2,font=button_font)
            q4_button.pack(pady=10)
            self.set_button_style_on_hover(q4_button, [self.button_colors[1], self.button_colors[0]])


            q5_button = tk.Button(self.master, text="Query List", command=self.query_list,
                                    bg=self.button_colors[0],width=40,height=2,font=button_font)
            q5_button.pack(pady=10)
            self.set_button_style_on_hover(q5_button, [self.button_colors[1], self.button_colors[0]])

            q6_button = tk.Button(self.master, text="Insert New Entries", command=self.add_entries_menu,
                                    bg=self.button_colors[0],width=40,height=2,font=button_font)
            q6_button.pack(pady=10)
            self.set_button_style_on_hover(q6_button, [self.button_colors[1], self.button_colors[0]])


    def back_to_home(self):
        self.rebuild_main_menu()

######################





    def drop_tables(self):
        try:
            # Execute the SQL script to drop tables
            tables_to_drop = [
                "APPOINTMENTS",
                "DENTISTS",
                "INVENTORY",
                "INVOICES",
                "MEDICAL_RECORDS",
                "PATIENTS",
                "TREATMENTS"
            ]

            for table in tables_to_drop:
                drop_statement = f"DROP TABLE {table} CASCADE CONSTRAINTS"
                self.cursor.execute(drop_statement)

            self.connection.commit()
            messagebox.showinfo("Success", "All tables dropped successfully!")

        except oracledb.Error as e:
            messagebox.showerror("Error", f"Error dropping tables: {e}")
        

    def create_table(self):
        try:
            # SQL commands for creating tables and constraints
            create_commands = [
                """
                CREATE TABLE J255SING.APPOINTMENTS (
                    APPOINTMENT_ID NUMBER(*,0), 
                    DESCRIPTION VARCHAR2(1000 BYTE), 
                    DENTIST_ID NUMBER(*,0), 
                    PATIENT_ID NUMBER(*,0), 
                    DATETIME DATE
                ) TABLESPACE DBCOURSE
                """,

                """
                CREATE TABLE J255SING.DENTISTS (
                    DENTIST_ID NUMBER(*,0), 
                    EMAIL_ADDRESS VARCHAR2(500 BYTE), 
                    PHONE_NUMBER VARCHAR2(20 BYTE), 
                    NAME VARCHAR2(500 BYTE), 
                    SPECIALIZATION VARCHAR2(500 BYTE)
                ) TABLESPACE DBCOURSE
                """,

                """
                CREATE TABLE J255SING.INVENTORY (
                    INVENTORY_ID NUMBER(*,0), 
                    NAME_OF_ITEM VARCHAR2(500 BYTE), 
                    QUANTITY NUMBER(*,0), 
                    ITEM_CATEGORY_OR_TYPE VARCHAR2(1000 BYTE)
                ) TABLESPACE DBCOURSE
                """,

                """
                CREATE TABLE J255SING.INVOICES (
                    INVOICE_ID NUMBER(*,0), 
                    PATIENT_ID NUMBER(*,0), 
                    TREATMENT_ID NUMBER(*,0), 
                    PAYMENT_STATUS VARCHAR2(50 BYTE) DEFAULT 'Pending', 
                    PAYMENT_TYPE VARCHAR2(50 BYTE), 
                    COST NUMBER(9,2)
                ) TABLESPACE DBCOURSE
                """,

                """
                CREATE TABLE J255SING.MEDICAL_RECORDS (
                    MEDICAL_FILE_ID NUMBER(*,0), 
                    PATIENT_ID NUMBER(*,0)
                ) TABLESPACE DBCOURSE
                """,

                """
                CREATE TABLE J255SING.PATIENTS (
                    PATIENT_ID NUMBER(*,0), 
                    HEALTH_CARD_ID NUMBER(*,0), 
                    EMAIL_ADDRESS VARCHAR2(500 BYTE), 
                    INSURANCE_ID NUMBER(*,0), 
                    DATE_OF_BIRTH DATE, 
                    NAME VARCHAR2(500 BYTE), 
                    PHONE_NUMBER VARCHAR2(20 BYTE)
                ) TABLESPACE DBCOURSE
                """,

                """
                CREATE TABLE J255SING.TREATMENTS (
                    TREATMENT_ID NUMBER(*,0), 
                    COST NUMBER, 
                    DESCRIPTION VARCHAR2(1000 BYTE), 
                    NAME_OF_TREATMENT VARCHAR2(1000 BYTE), 
                    INVENTORY_INVENTORY_ID NUMBER(*,0)
                ) TABLESPACE DBCOURSE
                """,

                # Add other create table statements here

                # Constraints for Table APPOINTMENTS
                """
                ALTER TABLE J255SING.APPOINTMENTS ADD CONSTRAINT APPOINTMENTS_PK PRIMARY KEY (APPOINTMENT_ID)
                USING INDEX TABLESPACE DBCOURSE ENABLE
                """,

                """
                ALTER TABLE J255SING.APPOINTMENTS MODIFY (APPOINTMENT_ID NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.APPOINTMENTS MODIFY (DESCRIPTION NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.APPOINTMENTS MODIFY (DENTIST_ID NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.APPOINTMENTS MODIFY (PATIENT_ID NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.APPOINTMENTS MODIFY (DATETIME NOT NULL ENABLE)
                """,

                # Constraints for Table DENTISTS
                """
                ALTER TABLE J255SING.DENTISTS ADD CONSTRAINT DENTISTS_PK PRIMARY KEY (DENTIST_ID)
                USING INDEX TABLESPACE DBCOURSE ENABLE
                """,

                """
                ALTER TABLE J255SING.DENTISTS MODIFY (DENTIST_ID NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.DENTISTS MODIFY (EMAIL_ADDRESS NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.DENTISTS MODIFY (PHONE_NUMBER NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.DENTISTS MODIFY (NAME NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.DENTISTS MODIFY (SPECIALIZATION NOT NULL ENABLE)
                """,

                # Add other constraint statements here

                # Constraints for Table INVENTORY
                """
                ALTER TABLE J255SING.INVENTORY ADD CONSTRAINT INVENTORY_PK PRIMARY KEY (INVENTORY_ID)
                USING INDEX TABLESPACE DBCOURSE ENABLE
                """,

                """
                ALTER TABLE J255SING.INVENTORY MODIFY (INVENTORY_ID NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.INVENTORY MODIFY (NAME_OF_ITEM NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.INVENTORY MODIFY (QUANTITY NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.INVENTORY MODIFY (ITEM_CATEGORY_OR_TYPE NOT NULL ENABLE)
                """,

                # Constraints for Table INVOICES
                """
                ALTER TABLE J255SING.INVOICES ADD CONSTRAINT INVOICES_PK PRIMARY KEY (INVOICE_ID)
                USING INDEX TABLESPACE DBCOURSE ENABLE
                """,

                """
                ALTER TABLE J255SING.INVOICES MODIFY (INVOICE_ID NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.INVOICES MODIFY (PATIENT_ID NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.INVOICES MODIFY (TREATMENT_ID NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.INVOICES MODIFY (PAYMENT_STATUS NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.INVOICES MODIFY (PAYMENT_TYPE NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.INVOICES MODIFY (COST NOT NULL ENABLE)
                """,

                # Constraints for Table MEDICAL_RECORDS
                """
                ALTER TABLE J255SING.MEDICAL_RECORDS ADD CONSTRAINT MEDICAL_RECORDS_PK PRIMARY KEY (MEDICAL_FILE_ID)
                USING INDEX TABLESPACE DBCOURSE ENABLE
                """,

                """
                ALTER TABLE J255SING.MEDICAL_RECORDS MODIFY (MEDICAL_FILE_ID NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.MEDICAL_RECORDS MODIFY (PATIENT_ID NOT NULL ENABLE)
                """,

                # Constraints for Table PATIENTS
                """
                ALTER TABLE J255SING.PATIENTS ADD CONSTRAINT HEALTH_CARD UNIQUE (HEALTH_CARD_ID)
                USING INDEX TABLESPACE DBCOURSE ENABLE
                """,

                """
                ALTER TABLE J255SING.PATIENTS ADD CONSTRAINT INSURANCE_ID UNIQUE (INSURANCE_ID)
                USING INDEX TABLESPACE DBCOURSE ENABLE
                """,

                """
                ALTER TABLE J255SING.PATIENTS ADD CONSTRAINT PATIENTS_PK PRIMARY KEY (PATIENT_ID)
                USING INDEX TABLESPACE DBCOURSE ENABLE
                """,

                """
                ALTER TABLE J255SING.PATIENTS MODIFY (PATIENT_ID NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.PATIENTS MODIFY (HEALTH_CARD_ID NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.PATIENTS MODIFY (EMAIL_ADDRESS NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.PATIENTS MODIFY (INSURANCE_ID NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.PATIENTS MODIFY (DATE_OF_BIRTH NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.PATIENTS MODIFY (NAME NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.PATIENTS MODIFY (PHONE_NUMBER NOT NULL ENABLE)
                """,

                # Constraints for Table TREATMENTS
                """
                ALTER TABLE J255SING.TREATMENTS MODIFY (TREATMENT_ID NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.TREATMENTS MODIFY (COST NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.TREATMENTS MODIFY (DESCRIPTION NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.TREATMENTS MODIFY (NAME_OF_TREATMENT NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.TREATMENTS MODIFY (INVENTORY_INVENTORY_ID NOT NULL ENABLE)
                """,

                """
                ALTER TABLE J255SING.TREATMENTS ADD CONSTRAINT TREATMENTS_PK PRIMARY KEY (TREATMENT_ID)
                USING INDEX TABLESPACE DBCOURSE ENABLE
                """,

                # Add other constraint statements here

                # Ref Constraints for Table APPOINTMENTS
                """
                ALTER TABLE J255SING.APPOINTMENTS ADD CONSTRAINT APPOINTMENTS_DENTISTS_FK FOREIGN KEY (DENTIST_ID)
                    REFERENCES J255SING.DENTISTS (DENTIST_ID) ENABLE
                """,

                """
                ALTER TABLE J255SING.APPOINTMENTS ADD CONSTRAINT APPOINTMENTS_PATIENTS_FK FOREIGN KEY (PATIENT_ID)
                    REFERENCES J255SING.PATIENTS (PATIENT_ID) ENABLE
                """,

                # Add other ref constraint statements here

                # Ref Constraints for Table INVOICES
                """
                ALTER TABLE J255SING.INVOICES ADD CONSTRAINT INVOICES_PATIENTS_FK FOREIGN KEY (PATIENT_ID)
                    REFERENCES J255SING.PATIENTS (PATIENT_ID) ENABLE
                """,

                """
                ALTER TABLE J255SING.INVOICES ADD CONSTRAINT INVOICES_TREATMENTS_FK FOREIGN KEY (TREATMENT_ID)
                    REFERENCES J255SING.TREATMENTS (TREATMENT_ID) ENABLE
                """,

                # Add other ref constraint statements here

                # Ref Constraints for Table MEDICAL_RECORDS
                """
                ALTER TABLE J255SING.MEDICAL_RECORDS ADD CONSTRAINT MEDICAL_RECORDS_PATIENTS_FK FOREIGN KEY (PATIENT_ID)
                    REFERENCES J255SING.PATIENTS (PATIENT_ID) ENABLE
                """,

                # Add other ref constraint statements here

                # Ref Constraints for Table TREATMENTS
                """
                ALTER TABLE J255SING.TREATMENTS ADD CONSTRAINT TREATMENTS_INVENTORY_FK FOREIGN KEY (INVENTORY_INVENTORY_ID)
                    REFERENCES J255SING.INVENTORY (INVENTORY_ID) ENABLE
                """
            ]

            # Execute the SQL commands
            for command in create_commands:
                self.cursor.execute(command)
                self.connection.commit()  # Commit after each DDL statement

            messagebox.showinfo("Success", "Tables and Constraints created successfully!")

        except oracledb.Error as e:
            messagebox.showerror("Error", f"Error creating tables: {e}")

    def populate_table(self):
        try:
            # Insert data into the PATIENTS table
            insert_statements = [
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (1,1234567890,'john.doe@example.com',9876543210,to_date('90-01-15','RR-MM-DD'),'John Doe','555-555-5555')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (2,2345678901,'jane.smith@example.com',8765432101,to_date('85-03-20','RR-MM-DD'),'Jane Smith','555-555-5556')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (3,3456789012,'bob.johnson@example.com',7654321092,to_date('95-07-10','RR-MM-DD'),'Bob Johnson','555-555-5557')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (4,4567890123,'lisa.miller@example.com',6543210983,to_date('82-12-05','RR-MM-DD'),'Lisa Miller','555-555-5558')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (5,5678901234,'michael.wilson@example.com',5432109874,to_date('78-08-25','RR-MM-DD'),'Michael Wilson','555-555-5559')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (6,6789012345,'susan.brown@example.com',4321098765,to_date('92-04-30','RR-MM-DD'),'Susan Brown','555-555-5560')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (7,7890123456,'david.jones@example.com',3210987656,to_date('87-06-18','RR-MM-DD'),'David Jones','555-555-5561')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (8,8901234567,'sarah.jackson@example.com',2109876547,to_date('76-11-12','RR-MM-DD'),'Sarah Jackson','555-555-5562')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (9,9012345678,'chris.white@example.com',1098765438,to_date('98-03-02','RR-MM-DD'),'Chris White','555-555-5563')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (10,5555666555777,'patient50@example.com',5674548567856,to_date('95-12-10','RR-MM-DD'),'Ella Davis','555-555-5610')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (11,1122334455,'peter.thompson@example.com',9988776655,to_date('75-05-22','RR-MM-DD'),'Peter Thompson','555-555-5565')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (12,2233445566,'laura.martin@example.com',8877665544,to_date('94-01-19','RR-MM-DD'),'Laura Martin','555-555-5566')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (13,3344556677,'james.wilson@example.com',7766554433,to_date('83-07-14','RR-MM-DD'),'James Wilson','555-555-5567')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (14,4455667788,'mary.brown@example.com',6655443322,to_date('97-11-29','RR-MM-DD'),'Mary Brown','555-555-5568')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (15,5566778899,'matthew.evans@example.com',5544332211,to_date('79-04-01','RR-MM-DD'),'Matthew Evans','555-555-5569')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (16,6666777788,'linda.johnson@example.com',5555666777,to_date('91-08-11','RR-MM-DD'),'Linda Johnson','555-555-5570')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (17,7777888999,'andrew.smith@example.com',4444555666,to_date('86-12-26','RR-MM-DD'),'Andrew Smith','555-555-5571')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (18,8888999000,'jennifer.davis@example.com',3333444555,to_date('80-02-03','RR-MM-DD'),'Jennifer Davis','555-555-5572')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (19,9900001111,'mark.jones@example.com',2222333444,to_date('96-06-29','RR-MM-DD'),'Mark Jones','555-555-5573')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (20,111222,'susan.wilson@example.com',1111222333,to_date('84-10-16','RR-MM-DD'),'Susan Wilson','555-555-5574')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (21,1111222233,'daniel.miller@example.com',1234123412,to_date('77-03-07','RR-MM-DD'),'Daniel Miller','555-555-5575')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (22,2222333444,'karen.brown@example.com',2345234523,to_date('93-09-03','RR-MM-DD'),'Karen Brown','555-555-5576')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (23,3333444555,'robert.taylor@example.com',3456345634,to_date('81-01-10','RR-MM-DD'),'Robert Taylor','555-555-5577')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (24,4444555666,'nancy.johnson@example.com',4567456745,to_date('99-05-14','RR-MM-DD'),'Nancy Johnson','555-555-5578')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (25,5555666777,'william.davis@example.com',5678567856,to_date('88-07-23','RR-MM-DD'),'William Davis','555-555-5579')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (26,1111222333,'amanda.smith@example.com',1234123413,to_date('90-11-08','RR-MM-DD'),'Amanda Smith','555-555-5580')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (27,260002,'patient27@example.com',260027,to_date('90-06-20','RR-MM-DD'),'Emily Johnson','555-555-5636')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (28,260003,'patient28@example.com',260028,to_date('85-03-10','RR-MM-DD'),'Michael Davis','555-555-5637')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (29,260004,'patient29@example.com',260029,to_date('93-09-05','RR-MM-DD'),'Sarah Wilson','555-555-5638')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (30,260005,'patient30@example.com',260030,to_date('80-07-20','RR-MM-DD'),'David Brown','555-555-5639')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (31,260006,'patient31@example.com',260031,to_date('91-04-15','RR-MM-DD'),'Jennifer Lee','555-555-5640')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (32,260007,'patient32@example.com',260032,to_date('86-08-18','RR-MM-DD'),'Robert Martinez','555-555-5641')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (33,260008,'patient33@example.com',260033,to_date('94-01-25','RR-MM-DD'),'Karen Taylor','555-555-5642')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (34,260009,'patient34@example.com',260034,to_date('82-11-30','RR-MM-DD'),'William Anderson','555-555-5643')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (35,260010,'patient35@example.com',260035,to_date('97-05-05','RR-MM-DD'),'Linda Clark','555-555-5644')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (36,260011,'patient36@example.com',260036,to_date('84-10-12','RR-MM-DD'),'Joseph Garcia','555-555-5645')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (37,260012,'patient37@example.com',260037,to_date('96-02-28','RR-MM-DD'),'Susan Hernandez','555-555-5646')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (38,260013,'patient38@example.com',260038,to_date('89-12-15','RR-MM-DD'),'James Scott','555-555-5647')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (39,260014,'patient39@example.com',260039,to_date('98-08-22','RR-MM-DD'),'Nancy Allen','555-555-5648')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (40,260015,'patient40@example.com',260040,to_date('83-06-07','RR-MM-DD'),'Christopher King','555-555-5649')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (41,260016,'patient41@example.com',260041,to_date('92-03-24','RR-MM-DD'),'Margaret Rodriguez','555-555-5650')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (42,260017,'patient42@example.com',260042,to_date('81-09-10','RR-MM-DD'),'Daniel Wright','555-555-5651')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (43,260018,'patient43@example.com',260043,to_date('95-04-03','RR-MM-DD'),'Patricia Lewis','555-555-5652')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (44,465574321,'lauraaa.johnson@example.com',458654745,to_date('84-04-01','RR-MM-DD'),'Bob Johnson','555-555-5694')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (45,361328254,'patient500@example.com',568657856,to_date('95-11-16','RR-MM-DD'),'Elena Davis','555-555-5693')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (46,5458123,'jenniferrr.martin@example.com',123417823412,to_date('90-11-09','RR-MM-DD'),'Jenniferrrr Martin','555-555-5606')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (47,643215,'roberttt.davis@example.com',234523314523,to_date('87-12-07','RR-MM-DD'),'Robertttt Davis','555-555-5607')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (48,9654456,'emilyyy.wilson@example.com',3456354645634,to_date('95-02-24','RR-MM-DD'),'Emilyyyy Wilson','555-555-5608')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (49,465321,'lauraaa.johnson@example.com',4567465456745,to_date('84-04-12','RR-MM-DD'),'Lauraaaa Johnson','555-555-5609')",
"Insert into J255SING.PATIENTS (PATIENT_ID,HEALTH_CARD_ID,EMAIL_ADDRESS,INSURANCE_ID,DATE_OF_BIRTH,NAME,PHONE_NUMBER) values (50,3613254,'patient500@example.com',5678675567856,to_date('95-12-16','RR-MM-DD'),'Ella Davissss','555-555-5610')",



"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (916577,1)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (117588,2)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (985116,3)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (872205,4)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (828194,5)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (403188,6)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (485955,7)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (291069,8)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (615852,9)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (423866,10)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (404663,11)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (242850,12)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (256632,13)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (910842,14)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (390435,15)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (652301,16)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (683400,17)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (106240,18)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (882194,19)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (524486,20)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (145140,21)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (299465,22)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (500955,23)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (922901,24)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (878980,25)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (380975,26)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (700097,27)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (492093,28)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (152875,29)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (647446,30)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (674066,31)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (739974,32)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (892714,33)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (315380,34)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (538083,35)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (535148,36)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (786987,37)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (597493,38)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (177057,39)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (783764,40)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (477280,41)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (671076,42)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (664045,43)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (181595,44)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (392059,45)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (446565,46)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (699895,47)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (852536,48)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (217471,49)",
"Insert into J255SING.MEDICAL_RECORDS (MEDICAL_FILE_ID,PATIENT_ID) values (838091,50)",



"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (11,'dr.jackson@example.com','555-555-1011','Dr. Amanda Jackson','General Dentistry')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (12,'dr.roberts@example.com','555-555-1012','Dr. Christopher Roberts','Orthodontics')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (13,'dr.campbell@example.com','555-555-1013','Dr. Jessica Campbell','Pediatric Dentistry')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (14,'dr.phillips@example.com','555-555-1014','Dr. Kevin Phillips','Oral Surgery')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (15,'dr.anderson@example.com','555-555-1015','Dr. Melissa Anderson','Endodontics')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (16,'dr.lewis@example.com','555-555-1016','Dr. Richard Lewis','Periodontics')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (17,'dr.white@example.com','555-555-1017','Dr. Kimberly White','Prosthodontics')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (18,'dr.young@example.com','555-555-1018','Dr. Justin Young','General Dentistry')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (19,'dr.hall@example.com','555-555-1019','Dr. Laura Hall','Orthodontics')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (20,'dr.baker@example.com','555-555-1020','Dr. Daniel Baker','Oral Surgery')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (1,'dr.smith@example.com','555-555-1001','Dr. John Smith','General Dentistry')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (2,'dr.jones@example.com','555-555-1002','Dr. Sarah Jones','Orthodontics')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (3,'dr.wilson@example.com','555-555-1003','Dr. Michael Wilson','Periodontics')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (4,'dr.davis@example.com','555-555-1004','Dr. Jennifer Davis','Pediatric Dentistry')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (5,'dr.brown@example.com','555-555-1005','Dr. David Brown','Oral Surgery')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (6,'dr.evans@example.com','555-555-1006','Dr. Laura Evans','Endodontics')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (7,'dr.martin@example.com','555-555-1007','Dr. Joseph Martin','Prosthodontics')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (8,'dr.thompson@example.com','555-555-1008','Dr. Emily Thompson','Orthodontics')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (9,'dr.harris@example.com','555-555-1009','Dr. Mark Harris','General Dentistry')",
"Insert into J255SING.DENTISTS (DENTIST_ID,EMAIL_ADDRESS,PHONE_NUMBER,NAME,SPECIALIZATION) values (10,'dr.wilson@example.com','555-555-1010','Dr. Linda Wilson','Periodontics')",




"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (21,'Routine Checkup',1,40,to_date('23-11-26','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (22,'Orthodontic Consultation',2,39,to_date('23-11-29','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (23,'Periodontal Treatment',3,38,to_date('23-12-02','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (24,'Pediatric Checkup',4,37,to_date('23-12-05','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (25,'Oral Surgery Consultation',5,36,to_date('23-12-08','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (26,'Root Canal Procedure',6,35,to_date('23-12-11','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (27,'Denture Fitting',7,34,to_date('23-12-14','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (28,'Orthodontic Adjustment',8,33,to_date('23-12-17','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (29,'Routine Checkup',9,32,to_date('23-12-20','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (30,'Periodontal Surgery',10,31,to_date('23-12-23','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (31,'Orthodontic Checkup',1,30,to_date('23-12-26','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (32,'Pediatric Checkup',2,29,to_date('23-12-29','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (33,'Oral Surgery Consultation',3,28,to_date('24-01-01','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (34,'Root Canal Procedure',4,27,to_date('24-01-04','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (35,'Routine Checkup',5,26,to_date('24-01-07','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (36,'Orthodontic Adjustment',6,25,to_date('24-01-10','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (37,'Denture Fitting',7,24,to_date('24-01-13','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (38,'Periodontal Surgery',8,23,to_date('24-01-16','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (39,'Oral Surgery Consultation',9,22,to_date('24-01-19','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (40,'Root Canal Procedure',10,21,to_date('24-01-22','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (41,'Routine Checkup',1,20,to_date('24-01-25','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (42,'Orthodontic Consultation',2,19,to_date('24-01-28','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (43,'Periodontal Treatment',3,18,to_date('24-01-31','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (44,'Pediatric Checkup',4,17,to_date('24-02-03','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (45,'Oral Surgery Consultation',5,16,to_date('24-02-06','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (46,'Root Canal Procedure',6,15,to_date('24-02-09','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (47,'Denture Fitting',7,14,to_date('24-02-12','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (48,'Orthodontic Adjustment',8,13,to_date('24-02-15','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (49,'Routine Checkup',9,12,to_date('24-02-18','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (50,'Periodontal Surgery',10,11,to_date('24-02-21','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (1,'Routine Checkup',1,1,to_date('23-10-05','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (2,'Orthodontic Consultation',2,2,to_date('23-10-07','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (3,'Periodontal Treatment',3,3,to_date('23-10-10','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (4,'Pediatric Checkup',4,4,to_date('23-10-12','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (5,'Oral Surgery Consultation',5,5,to_date('23-10-15','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (6,'Root Canal Procedure',6,6,to_date('23-10-17','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (7,'Denture Fitting',7,7,to_date('23-10-20','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (8,'Orthodontic Adjustment',8,8,to_date('23-10-22','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (9,'Routine Checkup',9,9,to_date('23-10-25','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (10,'Periodontal Surgery',10,10,to_date('23-10-27','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (11,'Orthodontic Checkup',1,50,to_date('23-10-30','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (12,'Pediatric Checkup',2,49,to_date('23-11-02','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (13,'Oral Surgery Consultation',3,48,to_date('23-11-05','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (14,'Root Canal Procedure',4,47,to_date('23-11-08','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (15,'Routine Checkup',5,46,to_date('23-11-10','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (16,'Orthodontic Adjustment',6,45,to_date('23-11-13','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (17,'Denture Fitting',7,44,to_date('23-11-15','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (18,'Periodontal Surgery',8,43,to_date('23-11-18','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (19,'Oral Surgery Consultation',9,42,to_date('23-11-20','RR-MM-DD'))",
"Insert into J255SING.APPOINTMENTS (APPOINTMENT_ID,DESCRIPTION,DENTIST_ID,PATIENT_ID,DATETIME) values (20,'Root Canal Procedure',10,41,to_date('23-11-23','RR-MM-DD'))",




"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (1,'Dental Chair',5,'Dental Equipment')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (2,'Dental Instruments Set',10,'Dental Equipment')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (3,'X-Ray Machine',2,'Dental Equipment')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (4,'Dental Supplies Kit',25,'Dental Supplies')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (5,'Dental Chair Upholstery',8,'Dental Equipment')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (6,'Sterilization Equipment',3,'Dental Equipment')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (7,'Dental Imaging Software',5,'Dental Software')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (8,'Dental Masks',50,'Dental Supplies')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (9,'Dental Handpieces',15,'Dental Equipment')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (10,'Dental Chairside Table',12,'Dental Equipment')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (11,'Dental X-Ray Film',100,'Dental Supplies')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (12,'Dental Curing Light',8,'Dental Equipment')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (13,'Dental Loupes',20,'Dental Equipment')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (14,'Dental Autoclave',4,'Dental Equipment')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (15,'Dental Impression Trays',30,'Dental Supplies')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (16,'Dental Nitrous Oxide System',2,'Dental Equipment')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (17,'Dental Amalgamator',3,'Dental Equipment')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (18,'Dental Prophy Angles',50,'Dental Supplies')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (19,'Dental Apex Locator',6,'Dental Equipment')",
"Insert into J255SING.INVENTORY (INVENTORY_ID,NAME_OF_ITEM,QUANTITY,ITEM_CATEGORY_OR_TYPE) values (20,'Dental Ultrasonic Scaler',5,'Dental Equipment')",



"Insert into J255SING.TREATMENTS (TREATMENT_ID,COST,DESCRIPTION,NAME_OF_TREATMENT,INVENTORY_INVENTORY_ID) values (1,200,'Routine Dental Cleaning','Dental Cleaning',4)",
"Insert into J255SING.TREATMENTS (TREATMENT_ID,COST,DESCRIPTION,NAME_OF_TREATMENT,INVENTORY_INVENTORY_ID) values (2,500,'Tooth Extraction Procedure','Tooth Extraction',9)",
"Insert into J255SING.TREATMENTS (TREATMENT_ID,COST,DESCRIPTION,NAME_OF_TREATMENT,INVENTORY_INVENTORY_ID) values (3,350,'Orthodontic Consultation','Orthodontic Consultation',2)",
"Insert into J255SING.TREATMENTS (TREATMENT_ID,COST,DESCRIPTION,NAME_OF_TREATMENT,INVENTORY_INVENTORY_ID) values (4,600,'Root Canal Therapy','Root Canal',19)",
"Insert into J255SING.TREATMENTS (TREATMENT_ID,COST,DESCRIPTION,NAME_OF_TREATMENT,INVENTORY_INVENTORY_ID) values (5,250,'Dental Crown Placement','Dental Crown',6)",
"Insert into J255SING.TREATMENTS (TREATMENT_ID,COST,DESCRIPTION,NAME_OF_TREATMENT,INVENTORY_INVENTORY_ID) values (6,700,'Teeth Whitening Procedure','Teeth Whitening',14)",
"Insert into J255SING.TREATMENTS (TREATMENT_ID,COST,DESCRIPTION,NAME_OF_TREATMENT,INVENTORY_INVENTORY_ID) values (7,400,'Periodontal Treatment','Periodontal Treatment',3)",
"Insert into J255SING.TREATMENTS (TREATMENT_ID,COST,DESCRIPTION,NAME_OF_TREATMENT,INVENTORY_INVENTORY_ID) values (8,300,'Dental Filling Procedure','Dental Filling',8)",
"Insert into J255SING.TREATMENTS (TREATMENT_ID,COST,DESCRIPTION,NAME_OF_TREATMENT,INVENTORY_INVENTORY_ID) values (9,550,'Dental Implant Surgery','Dental Implant',1)",
"Insert into J255SING.TREATMENTS (TREATMENT_ID,COST,DESCRIPTION,NAME_OF_TREATMENT,INVENTORY_INVENTORY_ID) values (10,450,'Oral Surgery Consultation','Oral Surgery Consultation',13)",




"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (1,30,1,'Paid','Credit Card',200)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (2,27,2,'Paid','Cash',500)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (3,5,3,'Pending','Insurance',350)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (4,7,4,'Paid','Credit Card',600)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (5,49,5,'Paid','Cash',250)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (6,47,6,'Pending','Insurance',700)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (7,10,7,'Paid','Credit Card',400)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (8,47,8,'Paid','Cash',300)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (9,18,9,'Pending','Insurance',550)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (10,5,10,'Paid','Credit Card',450)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (11,11,4,'Paid','Credit Card',600)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (12,36,8,'Paid','Cash',300)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (13,24,10,'Pending','Insurance',450)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (14,29,1,'Paid','Credit Card',200)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (15,15,3,'Paid','Cash',350)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (16,40,5,'Pending','Insurance',250)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (17,19,7,'Paid','Credit Card',400)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (18,28,9,'Paid','Cash',550)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (19,14,1,'Pending','Insurance',200)",
"Insert into J255SING.INVOICES (INVOICE_ID,PATIENT_ID,TREATMENT_ID,PAYMENT_STATUS,PAYMENT_TYPE,COST) values (20,39,1,'Paid','Credit Card',200)",


            ]

            for insert_statement in insert_statements:
                self.cursor.execute(insert_statement)
                self.connection.commit()

            messagebox.showinfo("Success", "Data inserted into ALL tables successfully!")

        except oracledb.Error as e:
            messagebox.showerror("Error", f"Error inserting data into ALL tables: {e}")



    def create_view(self):
        try:
            
            create_commands = [
                """
                CREATE OR REPLACE FORCE VIEW "J255SING"."APPOINTMENT_INFO" ("APPOINTMENT_ID", "APPOINTMENT_DESCRIPTION", "APPOINTMENT_DATETIME", "PATIENT_NAME", "DENTIST_NAME", "MEDICAL_FILE_ID") AS 
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
                LEFT JOIN medical_records m ON p.patient_id = m.patient_id
                """,


                """
                CREATE OR REPLACE FORCE VIEW "J255SING"."INVENTORY_TREATMENT_INFO" ("INVENTORY_ID", "NAME_OF_ITEM", "NAME_OF_TREATMENT", "TREATMENT_COST") AS 
                SELECT
                    i.inventory_id,
                    i.name_of_item,
                    t.name_of_treatment,
                    t.cost AS treatment_cost
                FROM inventory i
                LEFT JOIN treatments t ON i.inventory_id = t.inventory_inventory_id
                """,


                """
                CREATE OR REPLACE FORCE VIEW "J255SING"."INVOICE_SUMMARY" ("INVOICE_ID", "PATIENT_NAME", "NAME_OF_TREATMENT", "PAYMENT_STATUS", "PAYMENT_TYPE", "COST") AS 
                SELECT
                    i.invoice_id,
                    p.name AS patient_name,
                    t.name_of_treatment,
                    i.payment_status,
                    i.payment_type,
                    i.cost
                FROM invoices i
                JOIN patients p ON i.patient_id = p.patient_id
                JOIN treatments t ON i.treatment_id = t.treatment_id
                """,

                """
                CREATE OR REPLACE FORCE VIEW "J255SING"."MEDICAL_RECORD_SUMMARY" ("MEDICAL_FILE_ID", "PATIENT_NAME", "DATE_OF_BIRTH", "PATIENT_EMAIL", "PATIENT_PHONE") AS 
                SELECT
                    m.medical_file_id,
                    p.name AS patient_name,
                    p.date_of_birth,
                    p.email_address AS patient_email,
                    p.phone_number AS patient_phone
                FROM medical_records m
                JOIN patients p ON m.patient_id = p.patient_id
                """,


            ]

            # Execute the SQL commands
            for command in create_commands:
                self.cursor.execute(command)
                self.connection.commit()  # Commit after each DDL statement

            messagebox.showinfo("Success", "Views created successfully!")

        except oracledb.Error as e:
            messagebox.showerror("Error", f"Error creating Views: {e}")

#################################################################
#Queries List

    def main_menu(self):
        try:
            for widget in self.master.winfo_children():
                widget.destroy()
                self.master.geometry("800x800")

            label = tk.Label(self.master, text="Invoice and Treatment Details: Patient data, Treatment Costs, and Payment Status", font=("Helvetica", 14), pady=20,bg='#D6DBDF')
            label.pack()


            query = """
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
            JOIN treatments t ON i.treatment_id = t.treatment_id
            """

            self.cursor.execute(query)

            # Fetch the column names
            columns = [desc[0] for desc in self.cursor.description]

            # Create a new Frame within the current window
            result_frame = tk.Frame(self.master)
            result_frame.pack(expand=True, fill='both')

            # Create a treeview widget for displaying the table with a scroll bar
            tree = ttk.Treeview(result_frame, columns=columns, show='headings', selectmode='browse')
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=100)

            # Create a vertical scroll bar
            scroll_y = ttk.Scrollbar(result_frame, orient="vertical", command=tree.yview)
            scroll_y.pack(side="right", fill="y")

            tree.configure(yscrollcommand=scroll_y.set, show="headings", selectmode='browse')

            # Insert data into the treeview
            for row in self.cursor.fetchall():
                tree.insert("", "end", values=row)

            tree.pack(expand=True, fill='both')

            back_button = tk.Button(self.master, text="Back to Query List", command=self.query_list,
                                    bg="#3498db", fg="black", font=("Arial", 14), relief=tk.FLAT)
            back_button.pack(pady=10)

        except oracledb.DatabaseError as e:
            messagebox.showerror("Error", f"Error connecting to the database or executing the query: {e}")


    def main_menu2(self):

        
        try:
            for widget in self.master.winfo_children():
                widget.destroy()
                self.master.geometry("800x800")

            # Add widgets for the "Drop Tables" menu
            label = tk.Label(self.master, text="Patient Unpaid Invoices Summary: Tracking Pending Payments by Patient and Insurance ID", font=("Helvetica", 14), pady=20,bg='#D6DBDF')
            label.pack()
            self.button_style = {"font": ("Arial", 14)}

            # Connect to the Oracle database

            # Execute the SQL query
            query = """
            SELECT
            p.name AS patient_name,
            p.insurance_id,
            SUM(CASE WHEN i.payment_status = 'Pending' THEN i.cost ELSE 0 END) AS total_unpaid_invoices
            FROM patients p
            LEFT JOIN invoices i ON p.patient_id = i.patient_id
            LEFT JOIN treatments t ON i.treatment_id = t.treatment_id
            GROUP BY p.name, p.insurance_id
            """

            self.cursor.execute(query)

            # Fetch the column names
            columns = [desc[0] for desc in self.cursor.description]

            # Create a new Frame within the current window
            result_frame = tk.Frame(self.master)
            result_frame.pack(expand=True, fill='both')

            # Create a treeview widget for displaying the table
            tree = ttk.Treeview(result_frame, columns=columns, show='headings')
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=100)

            # Create a vertical scroll bar
            scroll_y = ttk.Scrollbar(result_frame, orient="vertical", command=tree.yview)
            scroll_y.pack(side="right", fill="y")

            tree.configure(yscrollcommand=scroll_y.set, show="headings", selectmode='browse')
            # Insert data into the treeview
            for row in self.cursor.fetchall():
                tree.insert("", "end", values=row)

            tree.pack(expand=True, fill='both')

            back_button = tk.Button(self.master, text="Back to Query List", command=self.query_list,
                                    bg="#3498db", fg="black", font=("Arial", 14), relief=tk.FLAT)
            back_button.pack(pady=10)

        except oracledb.DatabaseError as e:
            messagebox.showerror("Error", f"Error connecting to the database or executing the query: {e}")


    def main_menu3(self):
        try:
            for widget in self.master.winfo_children():
                widget.destroy()
                self.master.geometry("800x800")

            # Add widgets for the "Drop Tables" menu
            label = tk.Label(self.master, text="Dentist Appointments by Day of Week: Weekly Appointments and Dentist Assignments", font=("Helvetica", 14), pady=20,bg='#D6DBDF')
            label.pack()
            self.button_style = {"font": ("Arial", 14)}
            # Connect to the Oracle database

            # Execute the SQL query
            query = """
            SELECT
            TO_CHAR(a.datetime, 'DY') AS day_of_week,
            COUNT(*) AS number_of_appointments,
            d.name AS dentist_name
            FROM appointments a
            JOIN patients p ON a.patient_id = p.patient_id
            JOIN dentists d ON a.dentist_id = d.dentist_id
            GROUP BY TO_CHAR(a.datetime, 'DY'), d.name
            ORDER BY TO_CHAR(a.datetime, 'DY')
            """

            self.cursor.execute(query)

            # Fetch the column names
            columns = [desc[0] for desc in self.cursor.description]

            # Create a new Frame within the current window
            result_frame = tk.Frame(self.master)
            result_frame.pack(expand=True, fill='both')

            # Create a treeview widget for displaying the table
            tree = ttk.Treeview(result_frame, columns=columns, show='headings')
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=100)

            # Create a vertical scroll bar
            scroll_y = ttk.Scrollbar(result_frame, orient="vertical", command=tree.yview)
            scroll_y.pack(side="right", fill="y")

            tree.configure(yscrollcommand=scroll_y.set, show="headings", selectmode='browse')

            # Insert data into the treeview
            for row in self.cursor.fetchall():
                tree.insert("", "end", values=row)

            tree.pack(expand=True, fill='both')

            back_button = tk.Button(self.master, text="Back to Query List", command=self.query_list,
                                    bg="#3498db", fg="black", font=("Arial", 14), relief=tk.FLAT)
            back_button.pack(pady=10)

        except oracledb.DatabaseError as e:
            messagebox.showerror("Error", f"Error connecting to the database or executing the query: {e}")

#############
    def main_menu4(self):
        try:
            for widget in self.master.winfo_children():
                widget.destroy()
                self.master.geometry("800x800")

            # Add widgets for the "Drop Tables" menu
            label = tk.Label(self.master, text="Find Patients Who Received Expensive Treatments", font=("Helvetica", 14), pady=20,bg='#D6DBDF')
            label.pack()
            self.button_style = {"font": ("Arial", 14)}
            # Connect to the Oracle database

            # Execute the SQL query
            query = """
            SELECT p.name AS PatientName, SUM(t.cost) AS TotalTreatmentCost
            FROM patients p
            INNER JOIN invoices i ON p.patient_id = i.patient_id
            INNER JOIN treatments t ON i.treatment_id = t.treatment_id
            GROUP BY p.name
            HAVING SUM(t.cost) > 500
            """

            self.cursor.execute(query)

            # Fetch the column names
            columns = [desc[0] for desc in self.cursor.description]

            # Create a new Frame within the current window
            result_frame = tk.Frame(self.master)
            result_frame.pack(expand=True, fill='both')

            # Create a treeview widget for displaying the table
            tree = ttk.Treeview(result_frame, columns=columns, show='headings')
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=100)

            # Insert data into the treeview
            for row in self.cursor.fetchall():
                tree.insert("", "end", values=row)

            # Create a vertical scroll bar
            scroll_y = ttk.Scrollbar(result_frame, orient="vertical", command=tree.yview)
            scroll_y.pack(side="right", fill="y")

            tree.configure(yscrollcommand=scroll_y.set, show="headings", selectmode='browse')

            tree.pack(expand=True, fill='both')

            back_button = tk.Button(self.master, text="Back to Query List", command=self.query_list,
                                    bg="#3498db", fg="black", font=("Arial", 14), relief=tk.FLAT)
            back_button.pack(pady=10)

        except oracledb.DatabaseError as e:
            messagebox.showerror("Error", f"Error connecting to the database or executing the query: {e}")


    def main_menu5(self):
        try:
            for widget in self.master.winfo_children():
                widget.destroy()
                self.master.geometry("800x800")

            # Add widgets for the "Drop Tables" menu
            label = tk.Label(self.master, text="Find Patients Who Haven't Received Treatments", font=("Helvetica", 14), pady=20,bg='#D6DBDF')
            label.pack()
            self.button_style = {"font": ("Arial", 14)}
            # Connect to the Oracle database

            # Execute the SQL query
            query = """
            SELECT p.name AS PatientName
            FROM patients p
            MINUS
            SELECT DISTINCT p.name AS PatientName
            FROM patients p
            INNER JOIN invoices i ON p.patient_id = i.patient_id
            """

            self.cursor.execute(query)

            # Fetch the column names
            columns = [desc[0] for desc in self.cursor.description]

            # Create a new Frame within the current window
            result_frame = tk.Frame(self.master)
            result_frame.pack(expand=True, fill='both')

            # Create a treeview widget for displaying the table
            tree = ttk.Treeview(result_frame, columns=columns, show='headings')
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=100)

            # Create a vertical scroll bar
            scroll_y = ttk.Scrollbar(result_frame, orient="vertical", command=tree.yview)
            scroll_y.pack(side="right", fill="y")

            tree.configure(yscrollcommand=scroll_y.set, show="headings", selectmode='browse')

            # Insert data into the treeview
            for row in self.cursor.fetchall():
                tree.insert("", "end", values=row)

            tree.pack(expand=True, fill='both')

            back_button = tk.Button(self.master, text="Back to Query List", command=self.query_list,
                                    bg="#3498db", fg="black", font=("Arial", 14), relief=tk.FLAT)
            back_button.pack(pady=10)

        except oracledb.DatabaseError as e:
            messagebox.showerror("Error", f"Error connecting to the database or executing the query: {e}")



    def main_menu6(self):
        try:
            for widget in self.master.winfo_children():
                widget.destroy()
                self.master.geometry("800x800")

            # Add widgets for the "Drop Tables" menu
            label = tk.Label(self.master, text="Find Patients Who Have Received Treatments", font=("Helvetica", 14), pady=20,bg='#D6DBDF')
            label.pack()
            self.button_style = {"font": ("Arial", 14)}
            # Connect to the Oracle database

            # Execute the SQL query
            query = """
            SELECT p.name AS PatientName
            FROM patients p
            WHERE EXISTS (
                SELECT 1
                FROM invoices i
                WHERE p.patient_id = i.patient_id
            )
            """

            self.cursor.execute(query)

            # Fetch the column names
            columns = [desc[0] for desc in self.cursor.description]

            # Create a new Frame within the current window
            result_frame = tk.Frame(self.master)
            result_frame.pack(expand=True, fill='both')

            # Create a treeview widget for displaying the table
            tree = ttk.Treeview(result_frame, columns=columns, show='headings')
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=100)

            # Create a vertical scroll bar
            scroll_y = ttk.Scrollbar(result_frame, orient="vertical", command=tree.yview)
            scroll_y.pack(side="right", fill="y")

            tree.configure(yscrollcommand=scroll_y.set, show="headings", selectmode='browse')

            # Insert data into the treeview
            for row in self.cursor.fetchall():
                tree.insert("", "end", values=row)

            tree.pack(expand=True, fill='both')

            back_button = tk.Button(self.master, text="Back to Query List", command=self.query_list,
                                    bg="#3498db", fg="black", font=("Arial", 14), relief=tk.FLAT)
            back_button.pack(pady=10)

        except oracledb.DatabaseError as e:
            messagebox.showerror("Error", f"Error connecting to the database or executing the query: {e}")


    def main_menu7(self):
        try:
            for widget in self.master.winfo_children():
                widget.destroy()
                self.master.geometry("800x800")

            # Add widgets for the "Drop Tables" menu
            label = tk.Label(self.master, text="Combine Most Recent Appointments for Patients and Dentists", font=("Helvetica", 14), pady=20,bg='#D6DBDF')
            label.pack()
            self.button_style = {"font": ("Arial", 14)}
            # Connect to the Oracle database

            # Execute the SQL query
            query = """
            WITH RecentAppointments AS (
                SELECT a.appointment_id, a.description, a.datetime, 'Patient' AS UserType, p.name AS UserName
                FROM appointments a
                JOIN patients p ON a.patient_id = p.patient_id
                WHERE a.datetime = (SELECT MAX(datetime) FROM appointments WHERE patient_id = a.patient_id)
                UNION
                SELECT a.appointment_id, a.description, a.datetime, 'Dentist' AS UserType, d.name AS UserName
                FROM appointments a
                JOIN dentists d ON a.dentist_id = d.dentist_id
                WHERE a.datetime = (SELECT MAX(datetime) FROM appointments WHERE dentist_id = a.dentist_id)
            )
            SELECT appointment_id, description, datetime, UserType, UserName
            FROM RecentAppointments
            ORDER BY datetime DESC
            """

            self.cursor.execute(query)

            # Fetch the column names
            columns = [desc[0] for desc in self.cursor.description]

            # Create a new Frame within the current window
            result_frame = tk.Frame(self.master)
            result_frame.pack(expand=True, fill='both')

            # Create a treeview widget for displaying the table
            tree = ttk.Treeview(result_frame, columns=columns, show='headings')
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=100)

            # Create a vertical scroll bar
            scroll_y = ttk.Scrollbar(result_frame, orient="vertical", command=tree.yview)
            scroll_y.pack(side="right", fill="y")

            tree.configure(yscrollcommand=scroll_y.set, show="headings", selectmode='browse')

            # Insert data into the treeview
            for row in self.cursor.fetchall():
                tree.insert("", "end", values=row)

            tree.pack(expand=True, fill='both')

            back_button = tk.Button(self.master, text="Back to Query List", command=self.query_list,
                                    bg="#3498db", fg="black", font=("Arial", 14), relief=tk.FLAT)
            back_button.pack(pady=10)

        except oracledb.DatabaseError as e:
            messagebox.showerror("Error", f"Error connecting to the database or executing the query: {e}")


    def main_menu8(self):
        try:
            for widget in self.master.winfo_children():
                widget.destroy()
                self.master.geometry("800x800")

            # Add widgets for the "Drop Tables" menu
            label = tk.Label(self.master, text="Count Appointments for Each Dentist", font=("Helvetica", 14), pady=20,bg='#D6DBDF')
            label.pack()
            self.button_style = {"font": ("Arial", 14)}
            # Connect to the Oracle database

            # Execute the SQL query
            query = """
            SELECT d.name AS DentistName, COUNT(a.appointment_id) AS AppointmentCount
            FROM dentists d
            LEFT JOIN appointments a ON d.dentist_id = a.dentist_id
            GROUP BY d.name
            ORDER BY AppointmentCount DESC
            """

            self.cursor.execute(query)

            # Fetch the column names
            columns = [desc[0] for desc in self.cursor.description]

            # Create a new Frame within the current window
            result_frame = tk.Frame(self.master)
            result_frame.pack(expand=True, fill='both')

            # Create a treeview widget for displaying the table
            tree = ttk.Treeview(result_frame, columns=columns, show='headings')
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=100)

            # Create a vertical scroll bar
            scroll_y = ttk.Scrollbar(result_frame, orient="vertical", command=tree.yview)
            scroll_y.pack(side="right", fill="y")

            tree.configure(yscrollcommand=scroll_y.set, show="headings", selectmode='browse')


            # Insert data into the treeview
            for row in self.cursor.fetchall():
                tree.insert("", "end", values=row)

            tree.pack(expand=True, fill='both')


            back_button = tk.Button(self.master, text="Back to Query List", command=self.query_list,
                                    bg="#3498db", fg="black", font=("Arial", 14), relief=tk.FLAT)
            back_button.pack(pady=10)


        except oracledb.DatabaseError as e:
            messagebox.showerror("Error", f"Error connecting to the database or executing the query: {e}")

#######################################################

    def query_list(self):
        # Clear the current content in the main window
            for widget in self.master.winfo_children():
                widget.destroy()
                self.master.geometry("800x800")

            # Add widgets for the "Drop Tables" menu
            label = tk.Label(self.master, text="Query Menu", font=("Helvetica", 20), pady=20, bg='#D6DBDF')
            label.pack()
            self.button_style = {"font": ("Arial", 14)}




            q1_button = tk.Button(self.master, text="Invoice and Treatment Details: Patient data, Treatment Costs, and Payment Status", command=self.main_menu,
                                    bg=self.button_colors[0],wraplength=400,width=50,height=2,**self.button_style)
            q1_button.pack(pady=10)
            self.set_button_style_on_hover(q1_button, [self.button_colors[1], self.button_colors[0]])




            q2_button = tk.Button(self.master, text="Patient Unpaid Invoices Summary: Tracking Pending Payments by Patient and Insurance ID", command=self.main_menu2,
                                    bg=self.button_colors[0],wraplength=400,width=50,height=2,**self.button_style)
            q2_button.pack(pady=10)
            self.set_button_style_on_hover(q2_button, [self.button_colors[1], self.button_colors[0]])




            q3_button = tk.Button(self.master, text="Dentist Appointments by Day of Week: Counting Weekly Appointments and Dentist Assignments", command=self.main_menu3,
                                    bg=self.button_colors[0],wraplength=400,width=50,height=3,**self.button_style)
            q3_button.pack(pady=10)
            self.set_button_style_on_hover(q3_button, [self.button_colors[1], self.button_colors[0]])


###############################################
            q4_button = tk.Button(self.master, text="Find Patients Who Received Expensive Treatments", command=self.main_menu4,
                                    bg=self.button_colors[0],wraplength=400,width=50,height=2,**self.button_style)
            q4_button.pack(pady=10)
            self.set_button_style_on_hover(q4_button, [self.button_colors[1], self.button_colors[0]])



            q5_button = tk.Button(self.master, text="Find Patients Who Haven't Received Treatments", command=self.main_menu5,
                                    bg=self.button_colors[0],wraplength=400,width=50,height=2,**self.button_style)
            q5_button.pack(pady=10)
            self.set_button_style_on_hover(q5_button, [self.button_colors[1], self.button_colors[0]])


            q6_button = tk.Button(self.master, text="Find Patients Who Have Received Treatments", command=self.main_menu6,
                                    bg=self.button_colors[0],wraplength=400,width=50,height=2,**self.button_style)
            q6_button.pack(pady=10)
            self.set_button_style_on_hover(q6_button, [self.button_colors[1], self.button_colors[0]])


            q7_button = tk.Button(self.master, text="Combine Most Recent Appointments for Patients and Dentists", command=self.main_menu7,
                                    bg=self.button_colors[0],wraplength=400,width=50,height=2,**self.button_style)
            q7_button.pack(pady=10)
            self.set_button_style_on_hover(q7_button, [self.button_colors[1], self.button_colors[0]])


            q8_button = tk.Button(self.master, text="Count Appointments for Each Dentist", command=self.main_menu8,
                                    bg=self.button_colors[0],wraplength=400,width=50,height=2,**self.button_style)
            q8_button.pack(pady=10)
            self.set_button_style_on_hover(q8_button, [self.button_colors[1], self.button_colors[0]])

            back_button = tk.Button(self.master, text="Back to Main Menu", command=self.back_to_home,                  ##########    NEEDS FIXING
                                    bg="#3498db", fg="black", font=("Arial", 14), relief=tk.FLAT)
            back_button.pack(pady=10)
######################################

    def add_entries_menu(self):
        # Create a new window for the menu

        for widget in self.master.winfo_children():
            widget.destroy()
            self.master.geometry("800x800")

        # Add widgets for the "Drop Tables" menu
        label = tk.Label(self.master, text="Select Table", font=("Helvetica", 20), pady=20, bg='#D6DBDF')
        label.pack()
        self.button_style = {"font": ("Arial", 14)}

        # Add buttons for each table with corresponding commands
        tables = ["PATIENTS", "MEDICAL_RECORDS", "DENTISTS", "APPOINTMENTS", "INVENTORY", "TREATMENTS", "INVOICES"]

        for table_name in tables:
            button = tk.Button(self.master, text=f"Add Entries to {table_name}", command=lambda t=table_name: self.add_entries(t),
                            bg=self.button_colors[0], wraplength=400, width=50, height=2, **self.button_style)
            button.pack(pady=5)

        back_button = tk.Button(self.master, text="Back to Main Menu", command=self.back_to_home,
                                bg="#3498db", fg="black", font=("Arial", 14), relief=tk.FLAT)
        back_button.pack(pady=10)

    def add_entries(self, table_name):
        # Get the columns for the selected table (you can fetch this from your database metadata)
        # For demonstration purposes, I'm using a simple dictionary.
        columns_dict = {
            "PATIENTS": ["PATIENT_ID", "HEALTH_CARD_ID", "EMAIL_ADDRESS", "INSURANCE_ID", "DATE_OF_BIRTH", "NAME",
                        "PHONE_NUMBER"],
            "MEDICAL_RECORDS": ["MEDICAL_FILE_ID", "PATIENT_ID"],
            "DENTISTS": ["DENTIST_ID", "EMAIL_ADDRESS", "PHONE_NUMBER", "NAME", "SPECIALIZATION"],
            "APPOINTMENTS": ["APPOINTMENT_ID", "DESCRIPTION", "DENTIST_ID", "PATIENT_ID", "DATETIME"],
            "INVENTORY": ["INVENTORY_ID", "NAME_OF_ITEM", "QUANTITY", "ITEM_CATEGORY_OR_TYPE"],
            "TREATMENTS": ["TREATMENT_ID", "COST", "DESCRIPTION", "NAME_OF_TREATMENT", "INVENTORY_INVENTORY_ID"],
            "INVOICES": ["INVOICE_ID", "PATIENT_ID", "TREATMENT_ID", "PAYMENT_STATUS", "PAYMENT_TYPE", "COST"],
        }

        # Check if the window has been destroyed
        if not self.master or not self.master.winfo_exists():
            print("Window has been destroyed. Handle this situation appropriately.")
            return

        # Destroy existing widgets in the window
        for widget in self.master.winfo_children():
            widget.destroy()

        self.master.geometry("800x800")

        # Add widgets for the "Drop Tables" menu
        label = tk.Label(self.master, text=table_name, font=("Helvetica", 20), pady=20, bg='#D6DBDF')
        label.pack()
        self.button_style = {"font": ("Arial", 14)}

        # Labels and Entry widgets for each field
        labels = columns_dict[table_name]
        entries = []

        for i, label_text in enumerate(labels):
            label = tk.Label(
                self.master,
                text=label_text,
                font=("Helvetica", 14),
                fg="black",
                bg='#D6DBDF',
                padx=10,
                pady=5,
                relief="solid"
            )
            label.pack(pady=10, padx=10)

            entry = tk.Entry(self.master)
            entry.pack(pady=5)
            entries.append(entry)

        # Add a button to execute the add_to_sql function
        add_button = tk.Button(self.master, text="Add Entry",
                            command=lambda win=self.master: self.add_to_sql(win, table_name, labels, entries),
                            bg=self.button_colors[0], wraplength=400, width=50, height=2, font=("Arial", 14))
        add_button.pack(pady=10)

        # Add a back button
        back_button = tk.Button(self.master, text="Back to Entries Menu", command=self.add_entries_menu,
                                bg="#3498db", fg="black", font=("Arial", 14), relief=tk.FLAT)
        back_button.pack(pady=10)

    def initialize_database_connection(self):
        
        username = "j255sing"  
        password = "10249933"  
        host = "oracle12c.scs.ryerson.ca"  
        port = "1521"  
        service_name = "orcl12c"  

        try:
            self.connection = oracledb.connect(
                user=username,
                password=password,
                dsn=f"{host}:{port}/{service_name}"
            )
            self.cursor = self.connection.cursor()

        except oracledb.Error as e:
            messagebox.showerror("Error", f"Error connecting to the database: {e}")

    def add_to_sql(self, entry_window, table_name, labels, entries):

        values = [entry.get() if entry.get() else 'NULL' for entry in entries]

        # Construct the SQL query with parameterized values
        sql_query = f"INSERT INTO J255SING.{table_name} ({', '.join(labels)}) VALUES ({', '.join([':%d' % (i + 1) for i in range(len(values))])})"

        try:
            # Execute the SQL query with parameterized values
            self.cursor.execute(sql_query, values)
            self.connection.commit()

            # Inform the user about the successful addition
            messagebox.showinfo("Success", f"Entry added to {table_name}")

            # Open the add entries menu before destroying the entry window
            self.add_entries_menu()


        except Exception as e:
            # Handle database errors and inform the user
            messagebox.showerror("Error", f"Error adding entry to {table_name}: {str(e)}")


##########################################


if __name__ == "__main__":
    root = tk.Tk()
    app = DentalClinicGUI(root)
    root.mainloop()
