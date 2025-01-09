/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.business;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import ryerson.ca.business.SaleBusiness;
import java.sql.Date;
import java.math.BigDecimal;

/**
 *
 * @author student
 */
@WebServlet("/UpdateSalesServlet")
public class UpdateSalesServlet extends HttpServlet {

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Retrieve form parameters
       String storeID = request.getParameter("storeID");
    String date = request.getParameter("date");
    String salesAmount = request.getParameter("salesAmount");
    String costAmount = request.getParameter("costAmount");
    String profit = request.getParameter("profit");

        // Call your business logic to update the sale
        SaleBusiness saleBusiness = new SaleBusiness();
        boolean success = saleBusiness.updateSale(storeID, date, salesAmount, costAmount, profit);
        

        // Construct JavaScript to show pop-up notification
        String script = "<script>";
        if (success) {
            script += "alert('Sale updated successfully.');";
        } else {
            script += "alert('Failed to update sale. Please try again.');";
        }
        script += "window.location.href = 'update_sales.jsp';"; 
        script += "</script>";

        // Write JavaScript to the response
        response.setContentType("text/html");
        response.getWriter().println(script);
    }
}
