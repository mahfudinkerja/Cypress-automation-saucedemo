/// <reference types="Cypress" />
describe('This is my first Cypress on 4.0', () => {
    it('passes', () => {
        cy.viewport(720, 1380);
        cy.visit('https://parabank.parasoft.com/parabank/index.htm')
        cy.get("input[name='username']").type('userok')
        cy.get("input[name='password']").type('1q2w3e4r5t6y')
        cy.get(':nth-child(5) > .button').click()

        cy.get('tbody > :nth-child(1) > :nth-child(1) > a').click()
        cy.get('#month').select('February')
        cy.get('#transactionType').select('Debit')
        cy.get(':nth-child(3) > :nth-child(2) > .button').click()




















    })
})