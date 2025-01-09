package ryerson.ca.business;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import ryerson.ca.business.ManagerBusiness;

@WebServlet("/AddManagerServlet")
public class AddManagerServlet extends HttpServlet {

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Retrieve form parameters
        String firstName = request.getParameter("firstName");
        String lastName = request.getParameter("lastName");
        String city = request.getParameter("city");
        String postalCode = request.getParameter("postalCode");
        String street = request.getParameter("street");
        String phoneNo = request.getParameter("phoneNo");
        String username = request.getParameter("username");
        String password = request.getParameter("password");
        
        System.out.println(firstName);

        // Call your business logic to add the manager
        ManagerBusiness managerBusiness = new ManagerBusiness();
        boolean success = managerBusiness.addManager(firstName, lastName, city, postalCode, street, phoneNo, username, password);

        // Construct JavaScript to show pop-up notification
        String script = "<script>";
        if (success) {
            script += "alert('Manager added successfully.');";
        } else {
            script += "alert('Failed to add manager. Please try again.');";
        }
        script += "window.location.href = 'manage_managers.jsp';"; // Redirect to manage_managers.jsp
        script += "</script>";

        // Write JavaScript to the response
        response.setContentType("text/html");
        response.getWriter().println(script);
    }
}
