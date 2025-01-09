package ryerson.ca.updatesales.business;

import ryerson.ca.updatesales.persistence.SALES_CRUD;
import ryerson.ca.updatesales.helper.Sales;
import java.math.BigDecimal;
import java.io.IOException;

/**
 *
 * @author student
 */
public class UpdateSalesBusiness {
    
      public boolean insertSale(String storeID, String date, String salesAmount, String costAmount, String profit) {
    // Create a Sales object
    Sales sale = new Sales(storeID, date, salesAmount, costAmount, profit);
    
    // Instantiate SALES_CRUD or your database access class for sales
    SALES_CRUD salesCRUD = new SALES_CRUD();
    
    // Call addSales method to insert the sale into the database
    boolean saleAdded = salesCRUD.addSales(sale);
    
    // Send message if sale was added successfully
    if (saleAdded) {
        try {
            Messaging.sendmessage("ADD:"+storeID+":"+date+":"+salesAmount+":"+costAmount+":"+profit);
        } catch (IOException e) {
            System.err.println("Error sending message: " + e.getMessage());
        }
    }
    
    return saleAdded;
}

}
