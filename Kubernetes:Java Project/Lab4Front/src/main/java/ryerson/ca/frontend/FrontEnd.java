/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.io.IOException;
import java.util.Date;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import javax.crypto.SecretKey; // For SecretKey
import io.jsonwebtoken.Claims; // For Claims
import io.jsonwebtoken.Jws; // For Jws
import io.jsonwebtoken.JwtException; // For JwtException
import javax.servlet.http.Cookie;


import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.security.Keys; // Added import statement
import ryerson.ca.lab3.Persistance.Regional_CRUD;
import ryerson.ca.lab3.Persistance.Employee_CRUD;
import ryerson.ca.lab3.Persistance.Manager_CRUD;
import ryerson.ca.lab3.Helper.userInfo;

@WebServlet(name = "FrontEnd", urlPatterns = {"/frontend"})
public class FrontEnd extends HttpServlet {
    private static final long serialVersionUID = 1L;

    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String username = request.getParameter("username");
        String password = request.getParameter("password");

        Regional_CRUD regCrud = new Regional_CRUD();
        Employee_CRUD empCrud = new Employee_CRUD();
        Manager_CRUD manCrud = new Manager_CRUD();

        userInfo reg = null;

        // Check if the user is a regional manager
        reg = regCrud.readRegionalManager(username, password);
        if (reg != null) {
            // Generate JWT token
            String jwtToken = Jwts.builder().setSubject(username).setIssuedAt(new Date())
                    .setExpiration(new Date(System.currentTimeMillis() + 86400000)) 
                    .signWith(Keys.secretKeyFor(SignatureAlgorithm.HS256)) 
                    .compact();
            HttpSession session = request.getSession();
            Cookie jwtCookie = new Cookie("auth_token", jwtToken);
            response.addCookie(jwtCookie); // Add token as cookie
            session.setAttribute("user", reg);
            request.getRequestDispatcher("regional_home.jsp").forward(request, response);
            return;
        }

        // Check if the user is an employee
        reg = empCrud.readEmployee(username, password);
        if (reg != null) {
            // Generate JWT token
            String jwtToken = Jwts.builder().setSubject(username).setIssuedAt(new Date())
                    .setExpiration(new Date(System.currentTimeMillis() + 86400000)) // 24 hours
                    .signWith(Keys.secretKeyFor(SignatureAlgorithm.HS256)) // Using secure key generation
                    .compact();
            HttpSession session = request.getSession();
            Cookie jwtCookie = new Cookie("auth_token", jwtToken);
            session.setAttribute("jwtToken", jwtToken);
            response.addCookie(jwtCookie); // Add token as cookie
            session.setAttribute("user", reg);
            request.getRequestDispatcher("employee_home.jsp").forward(request, response);
            return;
        }

        // Check if the user is a manager
        reg = manCrud.readManager(username, password);
        if (reg != null) {
            // Generate JWT token
            String jwtToken = Jwts.builder().setSubject(username).setIssuedAt(new Date())
                    .setExpiration(new Date(System.currentTimeMillis() + 86400000)) // 24 hours
                    .signWith(Keys.secretKeyFor(SignatureAlgorithm.HS256)) // Using secure key generation
                    .compact();
            HttpSession session = request.getSession();
            Cookie jwtCookie = new Cookie("auth_token", jwtToken);
            session.setAttribute("jwtToken", jwtToken);
            response.addCookie(jwtCookie); // Add token as cookie
            request.getRequestDispatcher("manager_home.jsp").forward(request, response);
            return;
        }

        // If none of the above conditions match, forward to login_fail.html
        request.getRequestDispatcher("login_fail.html").forward(request, response);
    }
    public boolean isJwtAuthentic(String jwtToken) {
        // Ideally, retrieve your secretKey from a secure location.
        SecretKey secretKey = Keys.secretKeyFor(SignatureAlgorithm.HS256);
        
        try {
            // Parse the token. If it's not valid, an exception will be thrown
            Jws<Claims> claims = Jwts.parserBuilder()
                    .setSigningKey(secretKey)
                    .build()
                    .parseClaimsJws(jwtToken);
            
            // Here you can also check claims.getBody().getExpiration() to see if the token is expired
            // and perform any other checks you require for your application
            
            // If we get to this point, the token is valid
            return true;
        } catch (JwtException e) {
            // If any exception is caught, the token is considered invalid
            return false;
        }
    }
}
