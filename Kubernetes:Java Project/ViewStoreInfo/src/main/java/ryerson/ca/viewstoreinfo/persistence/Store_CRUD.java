/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.viewstoreinfo.persistence;

import ryerson.ca.viewstoreinfo.helper.Store;

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
public class Store_CRUD {
    
     private static Connection getCon() throws SQLException {
        Connection con = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            String connection = System.getenv("DB_URL");
            //  String connection ="localhost:3306";
            con = DriverManager.getConnection("jdbc:mysql://" + connection
                    + "/LMS_STORE?allowPublicKeyRetrieval=true&useSSL=false", "root", "student");
            System.out.println("Connection established.");
        } catch (ClassNotFoundException e) {
            System.out.println("JDBC Driver not found");
            e.printStackTrace();
        }
        return con;
    }
     
    public List<Store> getAllStores() {
        List<Store> stores = new ArrayList<>();
        try (Connection con = getCon()) {
            String query = "SELECT * FROM STORE";
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery(query);
            
            while (rs.next()) {
                String storeName = rs.getString("storeName");
                String phoneNo = rs.getString("phoneNo");
                String street = rs.getString("street");
                String postalCode = rs.getString("postalCode");
                String city = rs.getString("city");
                int storeID = rs.getInt("storeID");
                Store store = new Store(storeName, phoneNo, street, postalCode, city, storeID);
                stores.add(store);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return stores;
    }
    
}
