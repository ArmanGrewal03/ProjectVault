/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.managestoremanagers.helper;

/**
 *
 * @author student
 */
public class Manager {
    
    private String firstName;
    private String lastName;
    private int managerID;
    private String city;
    private String postalCode;
    private String street;
    private String phoneNo;
    private String username;
    private String password;

    // Constructor
    public Manager(String firstName, String lastName, int managerID, String city, String postalCode, String street, String phoneNo, String username, String password) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.managerID = managerID;
        this.city = city;
        this.postalCode = postalCode;
        this.street = street;
        this.phoneNo = phoneNo;
        this.username = username;
        this.password = password;
    }
    
    public Manager(){
        
    }

    // Getters and Setters
    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public int getManagerID() {
        return managerID;
    }

    public void setManagerID(int managerID) {
        this.managerID = managerID;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getPostalCode() {
        return postalCode;
    }

    public void setPostalCode(String postalCode) {
        this.postalCode = postalCode;
    }

    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public String getPhoneNo() {
        return phoneNo;
    }

    public void setPhoneNo(String phoneNo) {
        this.phoneNo = phoneNo;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}

