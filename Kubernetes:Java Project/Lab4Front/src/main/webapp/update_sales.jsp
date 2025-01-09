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
    } 
%>
<!DOCTYPE html>
<html>
<head>
    <title>Update Finances</title>
    <meta charset="UTF-8">
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #e6e8f0;
            font-family: 'Arial', sans-serif;
        }
        .container {
            width: 50%;
            margin: 50px auto;
            background-color: #ffffff;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        label {
            display: block;
            margin-bottom: 10px;
        }
        input[type="text"],
        input[type="date"] {
            width: calc(100% - 20px);
            padding: 8px;
            margin-bottom: 20px;
        }
        button[type="submit"] {
            background-color: #8a5cb8;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button[type="submit"]:hover {
            background-color: #7a4ca0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Add Finances</h2>
        <form action="UpdateSalesServlet" method="post">
            <label for="storeID">Store ID:</label><br>
            <input type="text" id="storeID" name="storeID" required><br>
            
            <label for="date">Date:</label><br>
            <input type="date" id="date" name="date" required><br>
            
            <label for="salesAmount">Sales Amount:</label><br>
            <input type="text" id="salesAmount" name="salesAmount" required><br>
            
            <label for="costAmount">Cost Amount:</label><br>
            <input type="text" id="costAmount" name="costAmount" required><br>
            
            <label for="profit">Profit:</label><br>
            <input type="text" id="profit" name="profit" required><br>
            
            <button type="submit">Add Weekly Sale</button>
        </form>
    </div>
</body>
</html>
