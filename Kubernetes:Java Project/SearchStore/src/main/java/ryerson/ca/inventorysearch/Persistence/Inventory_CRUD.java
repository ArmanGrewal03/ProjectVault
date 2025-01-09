/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.inventorysearch.Persistence;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.HashSet;
import java.util.Set;
import ryerson.ca.inventorysearch.Helper.Product;
import ryerson.ca.inventorysearch.Helper.Supplier;

/**
 *
 * @author student
 */
public class Inventory_CRUD {
    private static Connection getConnection() {
    Connection con = null;
    try {
        Class.forName("com.mysql.cj.jdbc.Driver");
         String connection = System.getenv("DB_URL");
            //  String connection ="localhost:3306";
            con = DriverManager.getConnection("jdbc:mysql://" + connection
                    + "/LMS_INVENTORY?allowPublicKeyRetrieval=true&useSSL=false", "root", "student");
        System.out.println("Database connection established.");
     } catch (Exception e) {
            System.out.println(e);
        }
        return con;
    }



    public static Set<Product> searchForProducts(String query) {
        Set<Product> products = new HashSet<>();
        try {
            Connection connection = getConnection();
            String sqlQuery = "SELECT * FROM inventory WHERE product_name LIKE \"" + query + "\";";
            System.out.println(sqlQuery);
            PreparedStatement preparedStatement = connection.prepareStatement(sqlQuery);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()) {
                String product_Id = resultSet.getString("product_id");
                String product_Name = resultSet.getString("product_name");
                String supplier = resultSet.getString("supplier_name");
                double price = resultSet.getDouble("price");
                int quantity = resultSet.getInt("quantity");
                Product product = new Product(product_Id, product_Name, supplier, price, quantity);
                products.add(product);
            }
            connection.close();
        } catch (Exception e) {
            System.out.println("Error searching for products: " + e);
        }
        System.out.println("Number of products found: " + products.size());
        return products;
    }
}
