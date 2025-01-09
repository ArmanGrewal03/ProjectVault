/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.business;

import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.Entity;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.Form;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.sql.Date;
import java.math.BigDecimal;


/**
 *
 * @author student
 */
public class SaleBusiness {
    public boolean updateSale(String storeID, String date, String salesAmount, String costAmount, String profit) {
        Client client = ClientBuilder.newClient();
        String updateweeklysales=System.getenv("updateweeklysales");

        WebTarget target = client.target("http://"+updateweeklysales+"/UpdateWeeklySales/webresources/sales/add");
        
        System.out.println("INSALESBUSINESS");
        Form form = new Form();
        form.param("storeID", storeID)
                .param("date", date)
                .param("salesAmount", salesAmount)
                .param("costAmount", costAmount)
                .param("profit", profit);

        Response response = target.request(MediaType.TEXT_HTML)
                .post(Entity.entity(form, MediaType.APPLICATION_FORM_URLENCODED));

        return response.getStatus() == Response.Status.OK.getStatusCode();
    }
    
}
