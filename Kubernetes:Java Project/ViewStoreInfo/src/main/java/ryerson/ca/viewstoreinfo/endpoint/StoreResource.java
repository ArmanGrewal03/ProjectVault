package ryerson.ca.viewstoreinfo.endpoint;

import ryerson.ca.viewstoreinfo.helper.StoreXML;
import ryerson.ca.viewstoreinfo.business.VIewStoreInfoBusiness;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.io.StringWriter;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Marshaller;

@Path("/stores")
public class StoreResource {
    @Context
    private UriInfo context;
    
    private VIewStoreInfoBusiness storeService = new VIewStoreInfoBusiness ();

    // Method to fetch all stores
    @GET
    @Produces(MediaType.APPLICATION_XML)
    @Path("/here")
    public Response getStores() {
        try {
            // Assuming you have a method in StoreService to get all stores
            // Replace 'getAllStores()' with the actual method call
            StoreXML stores = new StoreXML(storeService.getAllStores());

            // Marshalling the StoreXML object to XML format
            JAXBContext jaxbContext = JAXBContext.newInstance(StoreXML.class);
            Marshaller jaxbMarshaller = jaxbContext.createMarshaller();
            jaxbMarshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);

            StringWriter sw = new StringWriter();
            jaxbMarshaller.marshal(stores, sw);

            // Returning the XML representation of stores in the response
            return Response.ok(sw.toString()).build();
        } catch (JAXBException e) {
            e.printStackTrace();
            return Response.status(Response.Status.INTERNAL_SERVER_ERROR).entity("Error processing request").build();
        }
    }
}

