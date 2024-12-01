describe('template spec', () => {
    it('passes', () => {
        cy.viewport(1024, 1700);
        cy.visit('https://www.saucedemo.com')
        cy.get('[data-test="username"]').type('standard_user')
        cy.get('[data-test="password"]').type('secret_sauce')
        cy.get('[data-test="login-button"]').click()

    })
})