# Store Chain Database Management System
![website](https://github.com/user-attachments/assets/e54a27fc-24f4-471f-9dfe-b3e4dcee5034)
## Project Description

The objective of this project is to create and implement a database management system designed for the operations of a store chain. The goal of the database management system is to allow for ease of access to relevant information regarding each store’s products and employees. This will hopefully allow for effective data management and accessibility for managers, employees, and regional managers of the store chain. 

Fundamentally, the system will be built to manage enormous amounts of data centered primarily around employee histories and product details. It will function as a central repository for vital operational and commercial knowledge. 

![use-case-diagram](https://github.com/user-attachments/assets/c3d8ad14-f40e-4e1b-9e23-eade95101f31)


### Key Features

The store database management system will offer user-friendly interfaces and functions for simple navigation and product information administration. It will be a vital tool for the employees and managers of any store chain. 

- **Inventory Management**: Employees will have access to resources needed to ensure effective inventory management and customer service. The system will allow employees to check stock levels, revise prices, and update product descriptions. 
- **Improved Efficiency**: This will be invaluable as employees replenish shelves or answer customer questions, ultimately improving the efficiency of the store chain and boosting profits.
- **Product Management**: Managers will have full access to the product database, ensuring the correctness and consistency of product prices and stock levels across all store locations.
- **Employee Management**: Managers will also have access to employee information, helping them manage employee profiles and ensuring smooth operations. This will minimize miscommunication and scheduling conflicts.
- **Data Analytics**: Managers will be better equipped to identify trends, seize opportunities, and address problems head-on, promoting excellence and continuous improvement in retail operations.
- **Customized Recommendations**: By using data analytics, the system will provide tailored recommendations, promotions, and incentives to enhance customer engagement and loyalty.
- **Customer Satisfaction**: The store chain will be able to offer fair prices on sought-after products, driving repeat business and long-term success. For example, related goods can be suggested based on previous purchases, or loyal customers can be offered targeted discounts.


# Microservice General Descriptions

## 1. Frontend - User Authentication Microservice (Lab4Front)

This microservice handles the user authentication aspect of the program. The authentication is done through the use of **JSON Web Tokens (JWT)**. It communicates with every other microservice and ensures that any request made is authenticated beforehand to avoid any potential security risks. The communication is handled by **REST API endpoints**, allowing for synchronous communication between the frontend microservice and every other microservice currently implemented.

This microservice also manages the user login page, where it authenticates whether the login information entered by the user is valid or not. Depending on the result, it redirects the user to the appropriate page.

## 2. Backend - ManageStoreManagers Microservice

This microservice lets users (regional managers, in this context) manage the store manager database. Users can add, update, or delete manager information from the database.

It contains **REST API endpoints** that allow for communication with other microservices, making the process of navigating through the manager database and modifying data much easier for users.

## 3. Backend - SearchStore Microservice

This microservice enables users to search through the inventory of each store within the store chain. Users can submit queries to the inventory database to gather information about the quantity, price, and supplier of each product.

It contains **REST API endpoints** that allow the microservice to communicate with other microservices, namely the frontend, enabling users to view the information.

# Website with K8's

![K8](https://github.com/user-attachments/assets/5d2f70f1-5ba0-4e39-a67f-61fe8f4c0f0f)

![website](https://github.com/user-attachments/assets/c502f93f-4776-4553-a516-5c51fc489386)


