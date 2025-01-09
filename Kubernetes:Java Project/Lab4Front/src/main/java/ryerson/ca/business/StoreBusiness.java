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
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.MediaType;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Unmarshaller;
import org.apache.commons.io.IOUtils;
import ryerson.ca.lab3.Helper.StoreXML;

public class StoreBusiness {

    public StoreXML getAllStores() throws IOException {
        try {
            Client client = ClientBuilder.newClient();
            String viewstoreinfo=System.getenv("viewstoreinfo");
            WebTarget target = client.target("http://"+viewstoreinfo+"/ViewStoreInfo/webresources/stores/here");
            InputStream is = target.request(MediaType.APPLICATION_XML).get(InputStream.class);
            String xml = IOUtils.toString(is, "utf-8");
            
            JAXBContext jaxbContext = JAXBContext.newInstance(StoreXML.class);
            Unmarshaller unmarshaller = jaxbContext.createUnmarshaller();
            StoreXML stores = (StoreXML) unmarshaller.unmarshal(new StringReader(xml));

            return stores;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}