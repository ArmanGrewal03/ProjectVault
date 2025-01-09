/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ryerson.ca.business;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import ryerson.ca.lab3.Helper.Store;
import ryerson.ca.lab3.Helper.StoreXML;

/**
 *
 * @author student
 */
@WebServlet(name = "GetStoresServlet", urlPatterns = {"/GetStoresServlet"})
public class GetStoresServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Fetch stores from the backend
        StoreBusiness storeBusiness = new StoreBusiness();
        StoreXML stores = storeBusiness.getAllStores();
        
        request.setAttribute("stores", stores);
        
        request.getRequestDispatcher("view_store_info.jsp").forward(request, response);
    }

}
