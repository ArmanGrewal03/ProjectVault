/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.lab3.Helper;
/**
 *
 * @author student
 */
public class userInfo {
    
    private String phoneNo;
    private String username;
    private String password;
    private String firstName; // Added
    private String lastName;  // Added
    private String street;    // Added

    public userInfo(String firstName, String lastName, String street, String phoneNo, String username, String password) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.street = street;
        this.phoneNo = phoneNo;
        this.username = username;
        this.password = password; 
    }

    // Getters
    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public String getStreet() {
        return street;
    }

    public String getPhoneNo() {
        return phoneNo;
    }

    public String getUsername() {
        return username;
    }

    
}
