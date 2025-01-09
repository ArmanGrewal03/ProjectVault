package ryerson.ca.updatesales.endpoint;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import java.math.BigDecimal;
import java.sql.Date;
import ryerson.ca.updatesales.business.UpdateSalesBusiness;

@Path("/sales")
public class SalesResource {

    private UpdateSalesBusiness service = new UpdateSalesBusiness();

    public SalesResource() {
    }

    @POST
    @Produces(MediaType.TEXT_HTML)
    @Path("/add")
    public String addSale(
            @FormParam("storeID") String storeID,
            @FormParam("date") String dateStr,
            @FormParam("salesAmount") String salesAmountStr,
            @FormParam("costAmount") String costAmountStr,
            @FormParam("profit") String profitStr) 
    {
        try {
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
}
