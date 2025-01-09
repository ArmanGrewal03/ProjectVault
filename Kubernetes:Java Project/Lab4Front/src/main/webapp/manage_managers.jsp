<%@ page import="ryerson.ca.business.AddManagerServlet" %>
<%@ page import="ryerson.ca.business.ManageManagersServlet" %>
<%@ page import="ryerson.ca.business.DeleteManagerServlet" %>
<%@ page import="ryerson.ca.lab3.Helper.Manager" %>
<%@ page import="ryerson.ca.lab3.Helper.ManagerXML" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" isErrorPage="false" %>
<%
    // Initialize token variable
    String token = null;

    // Check for the auth_token cookie directly within the scriptlet
    Cookie[] cookies = request.getCookies();
    if (cookies != null) {
        for (Cookie cookie : cookies) {
            if ("auth_token".equals(cookie.getName())) {
                token = cookie.getValue();
                break;
            }
        }
    }

    if (token == null || token.isEmpty()) { // If token is not present or empty, redirect to index.html
        response.sendRedirect("index.html");
    } else { // Proceed only if the token exists and is not empty
%>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Manage Store Managers</title>
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
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .content {
            display: flex;
            justify-content: center;
            padding-top: 20px;
            flex-direction: column;
            align-items: center;
        }
        table {
            width: 80%;
            max-width: 1000px;
            border-collapse: collapse;
            background-color: #fff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        th, td {
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #8a5cb8;
            color: white;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        .action-links a {
            color: #8a5cb8;
            text-decoration: none;
            padding: 4px 6px;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        .action-links a:hover {
            background-color: #7a4ca0;
            color: white;
        }
        .add-manager-btn,
        .fetch-managers-btn {
            background-color: #8a5cb8;
            color: white;
            padding: 10px 15px;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s;
            margin-bottom: 10px;
        }
        .add-manager-btn:hover,
        .fetch-managers-btn:hover {
            background-color: #7a4ca0;
        }
        .content > a {
            margin: 20px;
            align-self: flex-start;
        }
        .add-button-container {
            display: flex;
            justify-content: center;
        }
        .action-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .action-buttons button {
            background-color: #ff5050;
            color: white;
            padding: 8px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .action-buttons button:hover {
            background-color: #cc0000;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Manage Store Managers</h1>
    </div>
    <div class="content">
        <table>
            <thead>
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>City</th>
                    <th>Postal Code</th>
                    <th>Street</th>
                    <th>Phone Number</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <%-- Iterate over managers and display them --%>
                <%
                    ManagerXML managers = (ManagerXML)request.getAttribute("managers");
                    if (managers != null) {
                        for (Manager manager : managers.getManagers()) {
                %>
                            <tr>
                                <td><%= manager.getFirstName() %></td>
                                <td><%= manager.getLastName() %></td>
                                <td><%= manager.getCity() %></td>
                                <td><%= manager.getPostalCode() %></td>
                                <td><%= manager.getStreet() %></td>
                                <td><%= manager.getPhoneNo() %></td>
                                <td>
                                    
                                    <form action="DeleteManagerServlet" method="post">
                                        <input type="hidden" name="username" value="<%= manager.getUsername() %>">
                                        <button type="submit">Delete</button>
                                    </form>
                                </td>
                            </tr>
                <%
                        }
                    }
                %>
            </tbody>
        </table>
        <form action="ManageManagersServlet" method="get"> 
            <input type="submit" value="Fetch Managers" class="fetch-managers-btn">
        </form> 
        <h2>Add Manager</h2>
        <div class="add-button-container">
            <form action="AddManagerServlet" method="post">
                <label for="firstName">First Name:</label><br>
                <input type="text" id="firstName" name="firstName" required><br><br>
                
                <label for="lastName">Last Name:</label><br>
                <input type="text" id="lastName" name="lastName" required><br><br>
                
                <label for="city">City:</label><br>
                <input type="text" id="city" name="city" required><br><br>
                
                <label for="postalCode">Postal Code:</label><br>
                <input type="text" id="postalCode" name="postalCode" required><br><br>
                
                <label for="street">Street:</label><br>
                <input type="text" id="street" name="street" required><br><br>
                
                <label for="phoneNo">Phone Number:</label><br>
                <input type="text" id="phoneNo" name="phoneNo" required><br><br>
                
                <label for="username">Username:</label><br>
                <input type="text" id="username" name="username" required><br><br>
                
                <label for="password">Password:</label><br>
                <input type="password" id="password" name="password" required><br><br>

                <button type="submit" class="add-manager-btn">Add Manager</button>
            </form>
        </div>
    </div>
</body>
</html>
<%
    } // End of if-else block for token authentication
%>
