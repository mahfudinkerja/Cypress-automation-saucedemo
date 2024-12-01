/// <reference types="Cypress" />
import { faker } from '@faker-js/faker';

describe('This is my first Cypress on 4.0', () => {
    it('passes', () => {
        cy.viewport(720, 1380); // untuk setengah layar
        // cy.viewport(1224, 1380);

        cy.visit('https://parabank.parasoft.com/parabank/index.htm')
        cy.get('#loginPanel > :nth-child(3) > a').click()

        cy.get("input[id = 'customer.firstName']").type(faker.person.firstName())
        cy.get("input[id = 'customer.lastName']").type(faker.person.lastName())
        cy.get("input[id = 'customer.address.street']").type(faker.location.street())
        cy.get("input[id = 'customer.address.city']").type(faker.location.city())
        cy.get("input[id = 'customer.address.state']").type(faker.location.state())
        cy.get("input[id = 'customer.address.zipCode']").type(faker.location.zipCode())
        cy.get("input[id = 'customer.phoneNumber']").type(faker.phone.number())
        cy.get("input[id = 'customer.ssn']").type(faker.finance.accountNumber())

        // cy.get("input[id = 'customer.username']").type(faker.internet.username())
        cy.get("input[id = 'customer.username']").type('userok')
        cy.get("input[id = 'customer.password']").type('1q2w3e4r5t6y')
        cy.get("#repeatedPassword").type('1q2w3e4r5t6y')
        cy.get("input[value='Register']").click()
        // for duplicate
        // cy.get("span[id='customer.username.errors']").should('have.text', 'This username already exists.')













    })
})