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
import ryerson.ca.lab3.Helper.Manager;
import ryerson.ca.lab3.Helper.ManagerXML;

@WebServlet("/ManageManagersServlet")
public class ManageManagersServlet extends HttpServlet {

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Fetch managers from the backend
        ManagerBusiness managerBusiness = new ManagerBusiness();
        ManagerXML managers = managerBusiness.getAllManagers();
        
        request.setAttribute("managers", managers);
        
        request.getRequestDispatcher("manage_managers.jsp").forward(request, response);
        

    }

}