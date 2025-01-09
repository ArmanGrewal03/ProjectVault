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
import javax.xml.bind.annotation.*;
import java.util.ArrayList;
import java.util.List;

@XmlRootElement(name = "stores")
@XmlAccessorType(XmlAccessType.FIELD)
public class StoreXML {

    @XmlElement(name = "store")
    private List<Store> stores;

    public List<Store> getStores() {
        return stores;
    }

    public StoreXML() {
        this.stores = new ArrayList<>();
    }

    public StoreXML(List<Store> stores) {
        this.stores = stores;
    }

    public void setStores(List<Store> stores) {
        this.stores = stores;
    }
}
