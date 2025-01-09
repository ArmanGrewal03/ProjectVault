/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.getsales.helper;

/**
 *
 * @author student
 */
import java.util.List;
import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement(name = "sales")
public class SalesXML {
    
    @XmlElement(name="sale")
    private List<Sales> saleList;
    
    public List<Sales> getSales() {
        return saleList;
    }

    public void setSales(List<Sales> sales) {
        this.saleList = sales;
    }
    
    public SalesXML() {
        // Required for JAXB
    }
    
}
