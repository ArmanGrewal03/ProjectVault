/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.getsales.endpoint;

/**
 *
 * @author student
 */
import java.io.StringWriter;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.Produces;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.POST;
import javax.ws.rs.FormParam;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Marshaller;
import ryerson.ca.getsales.business.SearchBusiness;
import ryerson.ca.getsales.helper.SalesXML;

@Path("/sales")
public class StoreSaleResource {

    @Context
    private UriInfo context;

    public StoreSaleResource() {
    }
    @POST
    @Produces(MediaType.TEXT_HTML)
    @Path("new/add")
    public String addSale(
            @FormParam("storeID") String storeID,
            @FormParam("date") String dateStr,
            @FormParam("salesAmount") String salesAmountStr,
            @FormParam("costAmount") String costAmountStr,
            @FormParam("profit") String profitStr) 
    {
        try {
            SearchBusiness service = new SearchBusiness();
            // Call the business logic to add the sale
            boolean inserted = service.insertSale(storeID, dateStr, salesAmountStr, costAmountStr, profitStr);

            if (inserted) {
                return "Sale Inserted Successfully";
            } else {
                return "Failed to Insert Sale";
            }
        } catch (IllegalArgumentException e) {
            // Handle invalid input data
            return "Invalid input data";
        }
    }
    @Path("/{storeID}")
    @GET
    @Produces(MediaType.APPLICATION_XML + ";charset=utf-8")
    public String getXml(@PathParam("storeID") String storeID) {
        SearchBusiness search = new SearchBusiness();
        SalesXML sales = search.getProductsByQuery(storeID);

        JAXBContext jaxbContext;
        try {
            jaxbContext = JAXBContext.newInstance(SalesXML.class);
            Marshaller jaxbMarshaller = jaxbContext.createMarshaller();
            jaxbMarshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
            StringWriter sw = new StringWriter();
            jaxbMarshaller.marshal(sales, sw);
            return sw.toString();
        } catch (JAXBException ex) {
            Logger.getLogger(StoreSaleResource.class.getName()).log(Level.SEVERE, null, ex);
            return "An error has occurred.";
        }
    }
}