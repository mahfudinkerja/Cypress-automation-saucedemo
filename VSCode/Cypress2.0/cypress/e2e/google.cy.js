describe('template spec', () => {
    it('passes', () => {
        cy.viewport(2020, 2100);
        cy.on('uncaught:exception', (err, runnable) => {
            // Handle the exception here (e.g., log it)
            return false; // Prevent Cypress from failing the test
        });
        cy.visit('https://www.google.com')
        cy.xpath("//textarea[@id='APjFqb']").type('nasi goreng{enter}')
        cy.xpath("//h3[.='Resep aneka Nasi Goreng praktis dan mudah dibuat ...']").click()





        // cy.xpath("").click()
        // cy.xpath("//input[@id='amount']").type(1000123)








    })
})