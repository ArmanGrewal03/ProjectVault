/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.getsales.persistence;

/**
 *
 * @author student
 */
import java.sql.Connection;
import java.sql.SQLException;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.HashSet;
import java.util.Set;
import ryerson.ca.getsales.helper.Sales;

public class Finance_CRUD {
   private static Connection getCon() throws SQLException {
        Connection con = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            String connection = System.getenv("DB_URL");
            //  String connection ="localhost:3306";
            con = DriverManager.getConnection("jdbc:mysql://" + connection
                    + "/LMS_SALES?allowPublicKeyRetrieval=true&useSSL=false", "root", "student");
            System.out.println("Connection established.");
        } catch (ClassNotFoundException e) {
            System.out.println("JDBC Driver not found");
            e.printStackTrace();
        }
        return con;
    }

public static Set<Sales> getSalesByStoreId(String storeId) {
        Set<Sales> sales = new HashSet<>();
        try {
            Connection connection = getCon();
            String sqlQuery = "SELECT * FROM LMS_SALES.SALES WHERE storeID = ?";
            PreparedStatement preparedStatement = connection.prepareStatement(sqlQuery);
            preparedStatement.setString(1, storeId);
            ResultSet resultSet = preparedStatement.executeQuery();
            while (resultSet.next()) {
                String updateId = resultSet.getString("updateID");
                String date = resultSet.getString("Date");
                String salesAmount = resultSet.getString("salesAmount");
                String costAmount = resultSet.getString("costAmount");
                String profit = resultSet.getString("profit");
                Sales sale = new Sales(storeId, date, salesAmount, costAmount, profit);
                sales.add(sale);
            }
            connection.close();
        } catch (Exception e) {
            System.out.println("Error fetching sales for store ID " + storeId + ": " + e.getMessage());
        }
        return sales;
    }
public boolean addSales(Sales sales) {
    try (Connection con = getCon()) {
        String query = "INSERT INTO LMS_SALES.SALES (storeID, Date, salesAmount, costAmount, profit) VALUES (?, ?, ?, ?, ?)";
        PreparedStatement ps = con.prepareStatement(query);
        ps.setString(1, sales.getStoreID());
        ps.setString(2, sales.getDate());
        ps.setString(3, sales.getSalesAmount());
        ps.setString(4, sales.getCostAmount());
        ps.setString(5, sales.getProfit());

        System.out.println("Executing SQL statement: " + ps.toString());

        int rowsInserted = ps.executeUpdate();
        return rowsInserted > 0;
    } catch (SQLException e) {
        e.printStackTrace();
        return false;
    }
}
}