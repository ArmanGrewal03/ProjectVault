/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.viewstoreinfo.business;

/**
 *
 * @author student
 */
import ryerson.ca.viewstoreinfo.helper.Store;
import ryerson.ca.viewstoreinfo.persistence.Store_CRUD;
import java.util.List;

public class VIewStoreInfoBusiness {

    public List<Store> getAllStores() {
        // Instantiate Store_CRUD
        Store_CRUD storeCRUD = new Store_CRUD();

        // Call getAllStores method to retrieve all stores from the database
        return storeCRUD.getAllStores();
    }

}
