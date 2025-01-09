/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.inventorysearch.Helper;

/**
 *
 * @author student
 */

import java.util.ArrayList;
import java.util.List;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlElementWrapper;
import javax.xml.bind.annotation.XmlRootElement;
import ryerson.ca.inventorysearch.Helper.Product;

@XmlRootElement(name = "products")
@XmlAccessorType (XmlAccessType.FIELD)
       public class ProductXML{
     @XmlElement(name="product")
           private ArrayList<Product> products;
           
           
           public List<Product>getProducts(){
               return products;
               
           }
          public  ProductXML(){
               
               
           }
           public void setProduct(ArrayList<Product> ps){
               products = ps;
               
           }
           
       }