 package ryerson.ca.business;

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

import ryerson.ca.lab3.Helper.Product;
import ryerson.ca.lab3.Helper.ProductXML;
import ryerson.ca.lab3.Helper.Supplier;

/**
 *
 * @author student
 */
public class ProductBusiness {
	public static ProductXML searchProducts(String query) {
    	try {
            
       	Client client = ClientBuilder.newClient();
        String searchinventory=System.getenv("searchinventory");
        	WebTarget target = client.target("http://"+searchinventory+"/SearchInventory/webresources/search/")
                                 	.path(query); // Append query as path parameter
        	InputStream is = target.request(MediaType.APPLICATION_XML).get(InputStream.class);
        	String xml = IOUtils.toString(is, "utf-8");
        	JAXBContext jaxbContext = JAXBContext.newInstance(ProductXML.class);
        	Unmarshaller unmarshaller = jaxbContext.createUnmarshaller();
        	ProductXML product = (ProductXML) unmarshaller.unmarshal(new StringReader(xml));
        	return product;
    	} catch (IOException e) {
        	e.printStackTrace();
        	return null;
    	} catch (JAXBException e) {
        	e.printStackTrace();
        	return null;
}
	}
}