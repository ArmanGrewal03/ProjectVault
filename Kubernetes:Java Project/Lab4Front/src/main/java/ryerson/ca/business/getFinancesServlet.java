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
import ryerson.ca.business.getFinancesBusiness;
import ryerson.ca.lab3.Helper.SalesXML;
import ryerson.ca.lab3.Helper.Sales;

/**
 *
 * @author student
 */
@WebServlet(name = "getFinancesServlet", urlPatterns = {"/getFinancesServlet"})
public class getFinancesServlet extends HttpServlet {

   @Override
protected void doGet(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {
    String query = request.getParameter("query");
    
    getFinancesBusiness Business = new getFinancesBusiness();
    SalesXML products = Business.searchFinance(query);
    request.setAttribute("sales", products);
    request.getRequestDispatcher("view_finances.jsp").forward(request, response);
}
    }

  
 


