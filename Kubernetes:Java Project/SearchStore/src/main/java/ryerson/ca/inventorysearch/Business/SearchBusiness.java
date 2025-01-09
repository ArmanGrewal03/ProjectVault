/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.inventorysearch.Business;

import ryerson.ca.inventorysearch.Helper.ProductXML;
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
import ryerson.ca.inventorysearch.Helper.Product;
import ryerson.ca.inventorysearch.Persistence.Inventory_CRUD;

/**
 *
 * @author student
 */
public class SearchBusiness {
       public ProductXML getProductsByQuery(String query){
       Set<Product> products = Inventory_CRUD.searchForProducts(query);
       ProductXML ps = new ProductXML();
       ps.setProduct(new ArrayList<>(products));
       return ps;
    }
    }
    
      

