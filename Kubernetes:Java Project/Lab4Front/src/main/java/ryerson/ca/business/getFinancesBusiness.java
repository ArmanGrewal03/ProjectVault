/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.business;

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

import ryerson.ca.lab3.Helper.SalesXML;
import ryerson.ca.lab3.Helper.Sales;

public class getFinancesBusiness {

    public static SalesXML searchFinance(String query) {
    try {
        if (query == null || query.isEmpty()) {
            // Handle the case where query is null or empty
            return null;
        }
        
        Client client = ClientBuilder.newClient();
        String getsales=System.getenv("getsales");
        WebTarget target = client.target("http://"+getsales+"/GetSales/webresources/sales/")
                .path(query); // Append query as path parameter
        InputStream is = target.request(MediaType.APPLICATION_XML).get(InputStream.class);
        String xml = IOUtils.toString(is, "utf-8");
        JAXBContext jaxbContext = JAXBContext.newInstance(SalesXML.class);
        Unmarshaller unmarshaller = jaxbContext.createUnmarshaller();
        SalesXML sale = (SalesXML) unmarshaller.unmarshal(new StringReader(xml));
        return sale;
    } catch (IOException e) {
        e.printStackTrace();
        return null;
    } catch (JAXBException e) {
        e.printStackTrace();
        return null;
    }
}
}
