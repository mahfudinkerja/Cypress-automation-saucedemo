/// <reference types="Cypress" />
import { faker } from '@faker-js/faker';

// Define a constant object to hold all the CSS selectors used in the tests
const SELECTORS = {
    usernameInput: '[name="user-name"]', // Selector for the username input field
    passwordInput: '[id="password"]', // Selector for the password input field
    loginButton: '[id="login-button"]', // Selector for the login button
    errorMessage: '[data-test="error"]', // Selector for the error message display

    cartButton: '.btn_action', // Selector for the cart action button
    menuButton: 'Open Menu', // Text for the menu button
    productButton: '.pricebar > .btn_primary', // Selector for the product add-to-cart button

    firstNameInput: '[data-test="firstName"]', // Selector for the first name input field in checkout
    lastNameInput: '[data-test="lastName"]', // Selector for the last name input field in checkout
    postalCodeInput: '[data-test="postalCode"]', // Selector for the postal code input field in checkout
    continueButton: 'CONTINUE', // Text for the continue button
    logoutButton: 'Logout', // Text for the logout button
    appLogo: '.app_logo' // Selector for the application logo
};

describe('Sauce Demo Application', () => {
    // This block runs before each test in the context
    beforeEach(() => {
        cy.viewport(1100, 1200); // Set the viewport size for the tests
        cy.visit('https://www.saucedemo.com/v1/index.html'); // Navigate to the Sauce Demo application
    });

    context('Login Scenarios', () => {

        // Helper function to perform login with given credentials
        const login = (username, password) => {
            cy.get(SELECTORS.usernameInput).type(username); // Type the username
            cy.get(SELECTORS.passwordInput).type(password); // Type the password
            cy.get(SELECTORS.loginButton).click(); // Click the login button
        };

        it('should display error for incorrect user', () => {
            // Attempt to log in with an incorrect username
            login('incorrect_user', 'secret_sauce');
            // Verify that the correct error message is displayed
            cy.get(SELECTORS.errorMessage)
                .should('have.text', 'Epic sadface: Username and password do not match any user in this service');
        });

        it('should display error for locked out user', () => {
            // Attempt to log in with a locked-out user
            login('locked_out_user', 'secret_sauce');
            // Verify that the correct error message is displayed
            cy.get(SELECTORS.errorMessage)
                .should('have.text', 'Epic sadface: Sorry, this user has been locked out.');
        });

        it('should log in with problem user', () => {
            // Attempt to log in with a user that has a problem
            login('problem_user', 'secret_sauce');
        });

        it('should log in with performance glitch user', () => {
            // Attempt to log in with a performance glitch user
            login('performance_glitch_user', 'secret_sauce');
        });

        it('should log in with standard user and complete purchase', () => {
            // Attempt to log in with the standard user
            login('standard_user', 'secret_sauce');

            // Add multiple items to the cart by clicking the add-to-cart button for each product
            for (let i = 1;
                i <= 6; i++) {
                cy.get(`:nth-child(${i}) > ${SELECTORS.productButton}`).click(); // Click the add-to-cart button for each product
            }
            // Verify that the app logo is visible, indicating successful login
            cy.get(SELECTORS.appLogo).should('be.visible');

            // Navigate to the cart page
            cy.visit('https://www.saucedemo.com/v1/cart.html');
            cy.get(SELECTORS.cartButton).click(); // Click the cart action button

            // Fill in the checkout form with random data using Faker.js
            cy.get(SELECTORS.firstNameInput).type(faker.person.firstName()); // Type a random first name
            cy.get(SELECTORS.lastNameInput).type(faker.person.lastName()); // Type a random last name
            cy.get(SELECTORS.postalCodeInput).type(faker.location.zipCode()); // Type a random postal code

            // Click the continue button to proceed with the checkout
            cy.contains(SELECTORS.continueButton).click();

            // Click the cart action button to finalize the purchase
            cy.get(SELECTORS.cartButton).scrollIntoView().click(); // Scroll to the cart button and click it

            // Open the menu to log out
            cy.contains(SELECTORS.menuButton).click(); // Click the menu button
            cy.contains(SELECTORS.logoutButton).click(); // Click the logout button to log out of the application
        });
    });
});