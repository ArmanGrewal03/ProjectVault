<%@ page import="ryerson.ca.business.SearchProductServlet" %>
<%@ page import="ryerson.ca.lab3.Helper.Product" %>
<%@ page import="ryerson.ca.lab3.Helper.ProductXML" %>
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
    <title>Search Product Inventory</title>
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
    </style>
</head>
<body>
    <div class="header">
        <h1>Search Product Inventory</h1>
    </div>
    <div class="content">
        <form id="searchForm" action="SearchProductServlet" method="get">
            <label for="query">Enter your search query:</label><br>
            <input type="text" id="query" name="query"><br><br>
            <button type="submit">Search</button>
        </form>
        <table id="searchResultsTable">
            <thead>
                <tr>
                    <th>Product ID</th>
                    <th>Product Name</th>
                    <th>Supplier Name</th>
                    <th>Price</th>
                    <th>Quantity</th>
                </tr>
            </thead>
            <tbody id="searchResultsBody">
                 <%-- Iterate over products and display them --%>
                <%
                    ProductXML products = (ProductXML)request.getAttribute("products");
                    if (products != null) {
                        for (Product product : products.getProducts()) {
                %>
                            <tr>
                                <td><%= product.getProductId() %></td>
                                <td><%= product.getProductName() %></td>
                                <td><%= product.getSupplier() %></td>
                                <td><%= product.getPrice() %></td>
                                <td><%= product.getQuantity() %></td>
                            </tr>
                <%
                        }
                    }
                %>
            </tbody>
        </table>
    </div>

    <script>
        // Example JavaScript to toggle table visibility based on search results
        // You may need to replace this with actual logic based on your application

        // Assuming searchResultsAvailable is a boolean indicating whether search results are available
        var searchResultsAvailable = true; // Set to true for demonstration

        var searchResultsTable = document.getElementById("searchResultsTable");

        if (searchResultsAvailable) {
            searchResultsTable.style.display = "table"; // Show the table
        } else {
            searchResultsTable.style.display = "none"; // Hide the table
        }
    </script>
</body>
</html>
<%
    } // End of if-else block for token authentication
%>