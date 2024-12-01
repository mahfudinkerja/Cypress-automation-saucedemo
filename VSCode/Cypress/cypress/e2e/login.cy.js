describe('template spec', () => {

    it('passes', () => {
        cy.on('uncaught:exception', (err, runnable) => {
            // Handle the exception here (e.g., log it)
            return false; // Prevent Cypress from failing the test
        });

        cy.visit('https://ctas-qa1.intranet.pajak.go.id/home/', {
            failOnStatusCode: false,
            redirect: 'manual'
        })
    })
})