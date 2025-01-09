<%@ page contentType="text/html; charset=UTF-8" %>
<%@ page import="ryerson.ca.lab3.Helper.userInfo" %>
<!DOCTYPE html>
<html lang="en">
<head>
   <title>Employee Dashboard</title>
   <style>
    body {
        margin: 0;
        padding: 0;
        background-color: #e6e8f0;
        font-family: 'Arial', sans-serif;
    }
    .header {
        text-align: center;
        padding: 20px;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0,0,0,0);
    }
    .header img {
        max-width: 120px;
        margin-bottom: 14px;
    }
    .dashboard-container {
        display: flex;
        padding-top: 20px;
        align-items: center;
        flex-direction: column;
    }
    .dashboard-options {
        background: #ffffff;
        padding: 40px;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0);
        width: 100%;
        max-width: 400px;
        text-align: center;
        margin-top: 20px;
    }
    .dashboard-options h2 {
        margin-bottom: 24px;
        color: #373737;
        font-size: 24px;
    }
    .dashboard-options a {
        display: block;
        padding: 12px 10px;
        border: none;
        border-radius: 9px;
        background-color: #8a5cb8;
        color: white;
        font-size: 18px;
        text-decoration: none;
        margin: 10px 0;
        transition: background-color 0.3s ease;
    }
    .dashboard-options a:hover {
        background-color: #7a4ca0;
    }
   </style>
</head>
<body>
   <div class="header">
    <img src="resources/logo.png" alt="Store Logo">
    <% 
    userInfo user = (userInfo) session.getAttribute("user");
    String name = user.getFirstName();
    out.println("<h1>Welcome, " + name + " to the Employee Dashboard</h1>");  
    %>
   </div>
   <div class="dashboard-container">
    <div class="dashboard-options">
        <h2>Management Options</h2>
        <a href="update_sales.jsp">Update Weekly Sales</a>
        <a href="stock_product_info.jsp">Access/Stock Product Information</a>
    </div>
   </div>
</body>
</html>
