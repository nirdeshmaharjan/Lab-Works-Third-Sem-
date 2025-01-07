import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class PortfolioApp {

    public static void main(String[] args) {
        // Create frame for the portfolio
        JFrame frame = new JFrame("Portfolio");
        frame.setSize(600, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        // Set layout manager
        frame.setLayout(new BorderLayout());

        // Create a panel for the navigation menu
        JPanel navPanel = new JPanel();
        navPanel.setLayout(new GridLayout(1, 4)); // 4 sections in the menu
        JButton infoButton = new JButton("Personal Info");
        JButton skillsButton = new JButton("Skills");
        JButton projectsButton = new JButton("Projects");
        JButton contactButton = new JButton("Contact");

        // Add buttons to the navigation panel
        navPanel.add(infoButton);
        navPanel.add(skillsButton);
        navPanel.add(projectsButton);
        navPanel.add(contactButton);

        // Create a text area to display content
        JTextArea contentArea = new JTextArea();
        contentArea.setEditable(false);
        
        // Create the content panel to hold the text area
        JPanel contentPanel = new JPanel();
        contentPanel.setLayout(new BorderLayout());
        contentPanel.add(new JScrollPane(contentArea), BorderLayout.CENTER);

        // Add navigation and content panels to the frame
        frame.add(navPanel, BorderLayout.NORTH);
        frame.add(contentPanel, BorderLayout.CENTER);

        // Personal Info Content
        String personalInfo = "Name: John Doe\nAge: 25\nLocation: New York\n\nA passionate Java developer.";

        // Skills Content
        String skills = "Languages: Java, Python, JavaScript\nFrameworks: Spring, Angular\nTools: Git, Docker, Jenkins";

        // Projects Content
        String projects = "Project 1: Portfolio Website (Java Swing)\nProject 2: E-commerce Platform (Spring Boot)\nProject 3: Personal Blog (React, Node.js)";

        // Contact Content
        String contactInfo = "Email: john.doe@example.com\nPhone: (123) 456-7890\nLinkedIn: linkedin.com/in/johndoe";

        // Event listeners for buttons
        infoButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                contentArea.setText(personalInfo);
            }
        });

        skillsButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                contentArea.setText(skills);
            }
        });

        projectsButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                contentArea.setText(projects);
            }
        });

        contactButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                contentArea.setText(contactInfo);
            }
        });

        // Set default content when the application starts
        contentArea.setText(personalInfo);

        // Make the frame visible
        frame.setVisible(true);
    }
}
