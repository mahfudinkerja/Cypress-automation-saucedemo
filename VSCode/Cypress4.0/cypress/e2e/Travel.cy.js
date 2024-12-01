describe('template spec', () => {
    it('passes', () => {
        cy.viewport(1900, 2110);

        cy.on('uncaught:exception', (err, runnable) => {
            // Handle the exception here (e.g., log it)
            return false; // Prevent Cypress from failing the test
        });
        cy.visit('https://ctas-qa.intranet.pajak.go.id/home/en-US/',
        )
        cy.get('#username').type('mochamad.amin2')
        cy.get('#password').type('Pajak123')
        cy.get('.btn-brand').click()

        cy.get('#4').click()
        cy.contains('Manajemen Kasus').click({ force: true })
        cy.contains('Kasus Baru').click({ force: true })


        cy.get('#CaseTypeIdentifier')
            .click()
            .type('Pajak Ditanggung Pemerintah (DTP)', { delay: 200 })
        cy.get('.p-element.ng-star-inserted > .p-ripple').click()

        cy.get('.btn.btn-primary.btn-sm').eq(0).click()








    })
})