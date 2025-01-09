/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.lab3.Persistance;

import ryerson.ca.lab3.Helper.userInfo;

import java.sql.Connection;
import java.sql.*;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

/**
 *
 * @author student
 */
public class Manager_CRUD {
    private Connection getCon() {
   Connection con = null;
   try {
       Class.forName("com.mysql.cj.jdbc.Driver");
       String connection = System.getenv("DB_URL2");
            //  String connection ="localhost:3306";
            con = DriverManager.getConnection("jdbc:mysql://" + connection
                    + "/LMS?allowPublicKeyRetrieval=true&useSSL=false", "root", "student");
       System.out.println("Connection established.");
   }catch (ClassNotFoundException e){
       System.out.println("JDBC Driver not found");
       e.printStackTrace();
   } catch (SQLException e) {
       System.out.println("Connection failed.");
       e.printStackTrace();
   }
   return con;
}

   
   
public userInfo readManager(String username, String password) {
    userInfo x = null;
	try (Connection con = getCon()) {
    	String q = "SELECT * FROM MANAGER WHERE username = ? AND password = ?";
    	PreparedStatement ps = con.prepareStatement(q);
    	ps.setString(1, username);
    	ps.setString(2, password);
    	ResultSet rs = ps.executeQuery();
    	if (rs.next()) {
        	x = new userInfo(
                	rs.getString("firstName"),
                	rs.getString("lastName"),
                	rs.getString("street"),
                	rs.getString("phoneNo"),
                	username,
                	password
        	);
    	}
        rs.close();
        ps.close();
        con.close();
        return x;
	} catch (SQLException e) {
    	System.out.println(e);
	}
        return null;
  
}
    
}
