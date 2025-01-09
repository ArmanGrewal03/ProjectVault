/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.managestoremanagers.helper;

import javax.xml.bind.annotation.*;
import java.util.ArrayList;
import java.util.List;
import ryerson.ca.managestoremanagers.helper.Manager;

@XmlRootElement(name = "managers")
@XmlAccessorType(XmlAccessType.FIELD)
public class ManagerXML {

    @XmlElement(name = "manager")
    private List<Manager> managers;

    public List<Manager> getManagers() {
        return managers;
    }
    

public ManagerXML() {

}

    public ManagerXML(List <Manager> managers) {
        this.managers = managers;
    }

    public void setManagers(List<Manager> managers) {
        this.managers = managers;
    }
}

