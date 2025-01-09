<%@ page import="ryerson.ca.lab3.Helper.StoreXML" %>
<%@ page import="ryerson.ca.lab3.Helper.Store" %>
<%@ page import="ryerson.ca.business.GetStoresServlet" %>
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
    <title>View Store Information</title>
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
        .fetch-managers-btn,
        .view-finances-btn { /* Added .view-finances-btn */
            background-color: #8a5cb8;
            color: white;
            padding: 10px 15px;
            text-decoration: none;
            border-radius: 5px;
            transition: background-color 0.3s;
            margin-bottom: 10px;
        }
        .add-manager-btn:hover,
        .fetch-managers-btn:hover,
        .view-finances-btn:hover { /* Added .view-finances-btn:hover */
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
        <h1>View Store Information</h1>
    </div>
    <div class="content">
        <table>
            <thead>
                <tr>
                    <th>Store Name</th>
                    <th>Phone No</th>
                    <th>Street</th>
                    <th>Postal Code</th>
                    <th>City</th>
                    <th>Store ID</th>
                </tr>
            </thead>
            <tbody>
                <%
                    StoreXML stores = (StoreXML)request.getAttribute("stores");
                    if (stores != null) {
                        for (Store store : stores.getStores()) {
                %>
                            <tr>
                                <td><%= store.getStoreName() %></td>
                                <td><%= store.getPhoneNo() %></td>
                                <td><%= store.getStreet() %></td>
                                <td><%= store.getPostalCode() %></td>
                                <td><%= store.getCity() %></td>
                                <td><%= store.getStoreID() %></td>
                                <td>
                <%
                        }
                    }
                %>
            </tbody>
        </table>
        <div class="action-buttons">
            <form action="GetStoresServlet" method="get"> 
                <input type="submit" value="Fetch Stores" class="fetch-managers-btn">
            </form> 
            <form action="view_finances.jsp">
                <input type="submit" value="View Finances" class="view-finances-btn">
            </form>
        </div>
    </div>
</body>
</html>
<%
    } // End of if-else block for token authentication
%>
