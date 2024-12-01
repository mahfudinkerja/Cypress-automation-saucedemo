describe('template spec', () => {
    it('passes', () => {
        cy.visit('https://www.instagram.com')
        cy.contains('Log In').click()
        cy.contains('Phone number, username, or email').type('mahfud')
        cy.contains('Password').type('passwordIg8!')
        cy.get('button[type="submit"]').click()






    })
})