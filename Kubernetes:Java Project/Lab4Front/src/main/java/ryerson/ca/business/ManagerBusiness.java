/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.business;


/**
 *
 * @author student
 */

import java.io.IOException;
import java.io.InputStream;
import java.io.StringReader;
import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.Form;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import org.apache.commons.io.IOUtils;

import ryerson.ca.lab3.Helper.Manager;
import ryerson.ca.lab3.Helper.ManagerXML;

public class ManagerBusiness {
    
    public static boolean deleteManagerByUsername(String username) {
        Client client = ClientBuilder.newClient();
        String managestoremanagers=System.getenv("managestoremanagers");
        WebTarget target = client.target("http://"+managestoremanagers+"/ManageStoreManagers/webresources/managers/delete");
        Form form = new Form();
        form.param("username", username);
                
        Response response = target.request(MediaType.TEXT_HTML)
                .post(Entity.entity(form, MediaType.APPLICATION_FORM_URLENCODED));
        
        return response.getStatus() == Response.Status.OK.getStatusCode();
    }
    
    
    public static ManagerXML getAllManagers() throws IOException {
        try{
        Client client = ClientBuilder.newClient();
        String managestoremanagers=System.getenv("managestoremanagers");
        WebTarget target = client.target("http://"+managestoremanagers+"/ManageStoreManagers/webresources/managers/here");
        InputStream is = target.request(MediaType.APPLICATION_XML).get(InputStream.class);
        String xml = IOUtils.toString(is, "utf-8");
        JAXBContext jaxbContext = JAXBContext.newInstance(ManagerXML.class);
            Unmarshaller unmarshaller = jaxbContext.createUnmarshaller();
            ManagerXML manager = (ManagerXML) unmarshaller.unmarshal(new StringReader(xml));

            return manager;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
    
    


    public static boolean addManager(String firstName, String lastName, String city, String postalCode, String street, String phoneNo, String username, String password) {
        Client client = ClientBuilder.newClient();
        String managestoremanagers=System.getenv("managestoremanagers");
        WebTarget target = client.target("http://"+managestoremanagers+"/ManageStoreManagers/webresources/managers/add");
        Form form = new Form();
        form.param("firstName", firstName)
            .param("lastName", lastName)
            .param("city", city)
            .param("postalCode", postalCode)
            .param("street", street)
            .param("phoneNo", phoneNo)
            .param("username", username)
            .param("password", password);
        
        System.out.println("managerBusiness"+firstName);
        
        Response response = target.request(MediaType.TEXT_HTML)
                .post(Entity.entity(form, MediaType.APPLICATION_FORM_URLENCODED));
        
        return response.getStatus() == Response.Status.OK.getStatusCode();
    }

   

    private static ManagerXML managersXmlToObjects(String xml) {
        JAXBContext jaxbContext;
        try {
            jaxbContext = JAXBContext.newInstance(ManagerXML.class);
            Unmarshaller jaxbUnmarshaller = jaxbContext.createUnmarshaller();
            return (ManagerXML) jaxbUnmarshaller.unmarshal(new StringReader(xml));
        } catch (JAXBException e) {
            e.printStackTrace();
        }
        return null;
    }

    // Add private methods for XML conversion if needed for update and delete operations
    
}
