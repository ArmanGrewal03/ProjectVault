/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.getsales.business;

/**
 *
 * @author student
 */
import ryerson.ca.getsales.helper.SalesXML;
import static java.lang.System.in;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlElementWrapper;
import javax.xml.bind.annotation.XmlRootElement;
import ryerson.ca.getsales.helper.Sales;
import ryerson.ca.getsales.persistence.Finance_CRUD;

/**
 *
 * @author student
 */
public class SearchBusiness {
       public SalesXML getProductsByQuery(String query){
       Set<Sales> sales = Finance_CRUD.getSalesByStoreId(query);
       SalesXML ps = new SalesXML();
       ps.setSales(new ArrayList<>(sales));
       return ps;
    }
       
       public boolean insertSale(String storeID, String date, String salesAmount, String costAmount, String profit) {
        // Create a Sales object
        Sales sale = new Sales(storeID, date, salesAmount, costAmount, profit);
        
        // Instantiate Sales_CRUD or your database access class for sales
        Finance_CRUD salesCRUD = new Finance_CRUD();
        
        // Call addSales method to insert the sale into the database
        return salesCRUD.addSales(sale);
    }
    }
