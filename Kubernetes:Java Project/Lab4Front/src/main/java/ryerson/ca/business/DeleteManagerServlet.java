package ryerson.ca.business;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(name = "DeleteManagerServlet", urlPatterns = {"/DeleteManagerServlet"})
public class DeleteManagerServlet extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // Retrieve form parameter
        String username = request.getParameter("username");

        // Call your business logic to delete the manager
        ManagerBusiness managerBusiness = new ManagerBusiness();
        boolean success = managerBusiness.deleteManagerByUsername(username);

        // Construct JavaScript to show pop-up notification
        String script = "<script>";
        if (success) {
            script += "alert('Manager Deleted successfully.');";
        } else {
            script += "alert('Failed to Delete manager. Please try again.');";
        }
        script += "window.location.href = 'manage_managers.jsp';"; // Redirect to manage_managers.jsp
        script += "</script>";

        // Write JavaScript to the response
        response.setContentType("text/html");
        response.getWriter().println(script);
    }

    @Override
    public String getServletInfo() {
        return "Short description";
    }
}
