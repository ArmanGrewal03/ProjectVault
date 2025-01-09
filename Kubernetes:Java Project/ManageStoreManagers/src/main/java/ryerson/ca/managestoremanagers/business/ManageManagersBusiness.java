/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.managestoremanagers.business;

/**
 *
 * @author student
 */
import ryerson.ca.managestoremanagers.helper.Manager;
import ryerson.ca.managestoremanagers.persistence.Manager_CRUD;
import java.util.List;
import java.util.ArrayList;

public class ManageManagersBusiness {
    
    public boolean insertManager(String firstName, String lastName, String city, String postalCode, String street, String phoneNo, String username, String password) {
        // Create a Manager object
        Manager manager = new Manager(firstName, lastName, 999999, city, postalCode, street, phoneNo, username, password);
        
        // Instantiate Manager_CRUD
        Manager_CRUD managerCRUD = new Manager_CRUD();
        
        // Call addManager method to insert the manager into the database
        return managerCRUD.addManager(manager);
    }
    
    public List<Manager> getAllManagers() {
        // Instantiate Manager_CRUD
        Manager_CRUD managerCRUD = new Manager_CRUD();

        // Call getAllManagers method to retrieve all managers from the database
        return managerCRUD.getAllManagers();
    }
    
    public boolean deleteManagerByUsername(String username) {
        // Instantiate Manager_CRUD
        Manager_CRUD managerCRUD = new Manager_CRUD();

        // Call removeManager method to delete the manager by username
        return managerCRUD.removeManager(username);
    }
    
    public boolean updateManager(int managerID, String username, String firstName, String lastName, String city, String postalCode, String street, String phoneNo, String password) {
        // Create a Manager object with updated information
        Manager updatedManager = new Manager(firstName, lastName, managerID, city, postalCode, street, phoneNo, username, password);
        System.out.println("made manager");
        
        // Instantiate Manager_CRUD
        Manager_CRUD managerCRUD = new Manager_CRUD();
        
        // Call updateManager method to update the manager in the database
        return managerCRUD.updateManager(updatedManager);
    }

}
