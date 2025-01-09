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
import javax.xml.bind.JAXBException;


import ryerson.ca.lab3.Helper.Product;
import ryerson.ca.lab3.Helper.ProductXML;
import ryerson.ca.lab3.Helper.Supplier;


/**
 *
 * @author student
 */
@WebServlet(name = "SearchProductServlet", urlPatterns = {"/SearchProductServlet"})
public class SearchProductServlet extends HttpServlet {

   @Override
protected void doGet(HttpServletRequest request, HttpServletResponse response)
        throws ServletException, IOException {
    String query = request.getParameter("query");
    
    ProductBusiness productBusiness = new ProductBusiness();
    ProductXML products = productBusiness.searchProducts(query);
    request.setAttribute("products", products);
    request.getRequestDispatcher("stock_product_info.jsp").forward(request, response);
}


    /**
     * Handles the HTTP <code>POST</code> method.
     *
     * @param request servlet request
     * @param response servlet response
     * @throws ServletException if a servlet-specific error occurs
     * @throws IOException if an I/O error occurs
     */
    
    @Override
    public String getServletInfo() {
        return "Short description";
    }// </editor-fold>

}
