/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.managestoremanagers.endpoint;

import java.io.StringWriter;

import ryerson.ca.managestoremanagers.business.ManageManagersBusiness;
import ryerson.ca.managestoremanagers.helper.Manager;
import ryerson.ca.managestoremanagers.helper.ManagerXML;

import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.ws.rs.Consumes;
import javax.ws.rs.Produces;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PUT;
import javax.ws.rs.POST;
import javax.ws.rs.core.MediaType;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.io.StringWriter;
import java.io.StringReader;
import javax.ws.rs.core.Context;
import javax.ws.rs.core.UriInfo;
import javax.xml.bind.JAXBContext;
import javax.xml.bind.JAXBException;
import javax.xml.bind.Marshaller;
import javax.xml.bind.Unmarshaller;
/**
 *
 * @author student
 */

@Path("/managers")
public class ManageResource {
    @Context
    private UriInfo context;

    /**
     * Creates a new instance of SearchResource
     */
    
    private ManageManagersBusiness service = new ManageManagersBusiness();
    
    public ManageResource() {
    }
    
    @POST
    @Produces(MediaType.TEXT_HTML)
    @Path("/update")
    public String updateManager(
            @FormParam("managerID") int managerID,
            @FormParam("username") String username,
            @FormParam("firstName") String firstName,
            @FormParam("lastName") String lastName,
            @FormParam("city") String city,
            @FormParam("postalCode") String postalCode,
            @FormParam("street") String street,
            @FormParam("phoneNo") String phoneNo,
            @FormParam("password") String password) 
    {
        System.out.println("HERE"+username);
        ManageManagersBusiness manage = new ManageManagersBusiness();
        boolean updated = manage.updateManager(managerID, username, firstName, lastName, city, postalCode, street, phoneNo,password);
        if (updated) {
            return "Manager Updated Successfully";
        } else {
            return "Failed to Update Manager";
        }
    }
    
    @POST
    @Path("/delete")
    @Produces(MediaType.TEXT_HTML)
    public String deleteManager(@FormParam("username") String username) {
        // Call your business logic to delete the manager
        ManageManagersBusiness manage = new ManageManagersBusiness();
        boolean deleted = manage.deleteManagerByUsername(username);

        if (deleted) {
            return "deleted successfully";
        } else {
            return"Manager not found";
        }
    }

    
    // Fetches all managers
@GET
@Produces(MediaType.APPLICATION_XML)
@Path("/here")
public Response getManagers() {
    try {
        // Assuming you have a method in AppointmentService to get all managers
        // Replace 'getAllManagers()' with the actual method call
        ManagerXML managers = new ManagerXML(service.getAllManagers());
        
        // Marshalling the ManagersXML object to XML format
        JAXBContext jaxbContext = JAXBContext.newInstance(ManagerXML.class);
        Marshaller jaxbMarshaller = jaxbContext.createMarshaller();
        jaxbMarshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
        
        StringWriter sw = new StringWriter();
        jaxbMarshaller.marshal(managers, sw);
        
        // Returning the XML representation of managers in the response
        return Response.ok(sw.toString()).build();
    } catch (JAXBException e) {
        e.printStackTrace();
        return Response.status(Response.Status.INTERNAL_SERVER_ERROR).entity("Error processing request").build();
    }
}

    @POST
    @Produces(MediaType.TEXT_HTML)
    @Path("add")
    public String addManager(
            @FormParam("firstName") String firstName,
            @FormParam("lastName") String lastName,
            @FormParam("city") String city,
            @FormParam("postalCode") String postalCode,
            @FormParam("street") String street,
            @FormParam("phoneNo") String phoneNo,
            @FormParam("username") String username,
            @FormParam("password") String password) 
    {
        ManageManagersBusiness manage = new ManageManagersBusiness();
        boolean inserted = manage.insertManager(firstName, lastName, city, postalCode, street, phoneNo, username, password);
        if (inserted) {
            return "Manager Inserted Successfully";
        } else {
            return "Failed to Insert Manager";
        }
    }

    
}