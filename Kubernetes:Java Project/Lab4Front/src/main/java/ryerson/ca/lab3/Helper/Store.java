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
 public class Store {
    
    private String storeName;
    private String phoneNo;
    private String street;
    private String postalCode;
    private String city;
    private int storeID;

    // Constructor
    public Store(String storeName, String phoneNo, String street, String postalCode, String city, int storeID) {
        this.storeName = storeName;
        this.phoneNo = phoneNo;
        this.street = street;
        this.postalCode = postalCode;
        this.city = city;
        this.storeID = storeID;
    }
    
    public Store(){
        
    }

    // Getters and Setters
    public String getStoreName() {
        return storeName;
    }

    public void setStoreName(String storeName) {
        this.storeName = storeName;
    }

    public String getPhoneNo() {
        return phoneNo;
    }

    public void setPhoneNo(String phoneNo) {
        this.phoneNo = phoneNo;
    }

    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public String getPostalCode() {
        return postalCode;
    }

    public void setPostalCode(String postalCode) {
        this.postalCode = postalCode;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public int getStoreID() {
        return storeID;
    }

    public void setStoreID(int storeID) {
        this.storeID = storeID;
    }
}

