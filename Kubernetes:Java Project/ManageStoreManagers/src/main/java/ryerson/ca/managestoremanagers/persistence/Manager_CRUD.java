package ryerson.ca.managestoremanagers.persistence;

import ryerson.ca.managestoremanagers.helper.Manager;

import java.sql.Connection;
import java.sql.*;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import java.util.ArrayList;

public class Manager_CRUD {
    
    private static final String GET_ALL_MANAGERS_QUERY = "SELECT * FROM MANAGER";
    
    private static Connection getCon() throws SQLException {
        
        
        Connection con = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            String connection = System.getenv("DB_URL");
            con = DriverManager.getConnection("jdbc:mysql://" + connection
                    + "/LMS_MANAGER?allowPublicKeyRetrieval=true&useSSL=false", "root", "student");
            System.out.println("Connection established.");
        } catch (ClassNotFoundException e) {
            System.out.println("JDBC Driver not found");
            e.printStackTrace();
        }
        return con;
    }

    public boolean addManager(Manager manager) {
        try (Connection con = getCon()) {
            String query = "INSERT INTO MANAGER (firstName, lastName, city, postalCode, street, phoneNo, username, password) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
            PreparedStatement ps = con.prepareStatement(query);
            ps.setString(1, manager.getFirstName());
            ps.setString(2, manager.getLastName());
            ps.setString(3, manager.getCity());
            ps.setString(4, manager.getPostalCode());
            ps.setString(5, manager.getStreet());
            ps.setString(6, manager.getPhoneNo());
            ps.setString(7, manager.getUsername());
            ps.setString(8, manager.getPassword());
            
            System.out.println("Executing SQL statement: " + ps.toString());

            int rowsInserted = ps.executeUpdate();
            ps.close(); // Close PreparedStatement
            return rowsInserted > 0;
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }

 public boolean removeManager(String managerID) {
    try (Connection con = getCon()) {
        String query = "DELETE FROM MANAGER WHERE username = ?";
        PreparedStatement ps = con.prepareStatement(query);
        ps.setString(1, managerID);

        // Print the SQL statement being executed
        System.out.println("Executing SQL statement: " + ps.toString());

        int rowsDeleted = ps.executeUpdate();
        ps.close(); // Close PreparedStatement
        return rowsDeleted > 0;
    } catch (SQLException e) {
        e.printStackTrace();
        return false;
    }
}
    
    
   public List<Manager> getAllManagers() {
        List<Manager> managers = new ArrayList<>();
        try (Connection con = getCon();
             PreparedStatement ps = con.prepareStatement(GET_ALL_MANAGERS_QUERY);
             ResultSet rs = ps.executeQuery()) {

            while (rs.next()) {
                Manager manager = new Manager();
                manager.setManagerID(rs.getInt("managerID"));
                manager.setFirstName(rs.getString("firstName"));
                manager.setLastName(rs.getString("lastName"));
                manager.setCity(rs.getString("city"));
                manager.setPostalCode(rs.getString("postalCode"));
                manager.setStreet(rs.getString("street"));
                manager.setPhoneNo(rs.getString("phoneNo"));
                manager.setUsername(rs.getString("username"));
                manager.setPassword(rs.getString("password"));
                managers.add(manager);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return managers;
    }
   
   public boolean updateManager(Manager updatedManager) {
        try (Connection con = getCon()) {
            String query = "UPDATE MANAGER SET firstName = ?, lastName = ?, city = ?, postalCode = ?, street = ?, phoneNo = ?, username = ?, password = ? WHERE managerID = ?";
            PreparedStatement ps = con.prepareStatement(query);
            ps.setString(1, updatedManager.getFirstName());
            ps.setString(2, updatedManager.getLastName());
            ps.setString(3, updatedManager.getCity());
            ps.setString(4, updatedManager.getPostalCode());
            ps.setString(5, updatedManager.getStreet());
            ps.setString(6, updatedManager.getPhoneNo());
            ps.setString(7, updatedManager.getUsername());
            ps.setString(8, updatedManager.getPassword());
            ps.setInt(9, updatedManager.getManagerID()); 

       
            System.out.println("Executing SQL statement: " + ps.toString());

            int rowsUpdated = ps.executeUpdate();
            ps.close(); 
            return rowsUpdated > 0;
        } catch (SQLException e) {
            e.printStackTrace();
            return false;
        }
    }

}

