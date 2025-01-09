
package ryerson.ca.updatesales.persistence;

import ryerson.ca.updatesales.helper.Sales;
import java.sql.Connection;
import java.sql.*;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import java.util.ArrayList;

/**
 *
 * @author student
 */
public class SALES_CRUD {
    
    private static Connection getCon() throws SQLException {
        Connection con = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            String connection = System.getenv("DB_URL");
            //  String connection ="localhost:3306";
            con = DriverManager.getConnection("jdbc:mysql://" + connection
                    + "/LMS_ADD_SALES?allowPublicKeyRetrieval=true&useSSL=false", "root", "student");
            System.out.println("Connection established.");
        } catch (ClassNotFoundException e) {
            System.out.println("JDBC Driver not found");
            e.printStackTrace();
        }
        return con;
    }
    
  public boolean addSales(Sales sales) {
    try (Connection con = getCon()) {
        String query = "INSERT INTO LMS_ADD_SALES.SALES (storeID, Date, salesAmount, costAmount, profit) VALUES (?, ?, ?, ?, ?)";
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


    

