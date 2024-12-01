describe('template spec', () => {
    it('passes', () => {
        cy.viewport(1624, 1700);
        cy.on('uncaught:exception', (err, runnable) => {
            // Handle the exception here (e.g., log it)
            return false; // Prevent Cypress from failing the test
        });
        cy.visit('https://ctas-qa.intranet.pajak.go.id/',
        )
        cy.get('#username').type('admin')
        cy.get('#password').type('R7!sXw2F')
        cy.get('.btn-brand').click()

        cy.get('#4').click()
        cy.contains('Kasus Baru').click()
        cy.get('#CaseTypeIdentifier > .col-sm-12 > .p-dropdown-label').type('Pajak Ditanggung Pemerintah (DTP)')
        cy.get('.p-ripple > .ng-star-inserted').click()
        cy.get('#Taxpayer').click()
        cy.get('#ObjectPermitNumber').type('1091031210913878')
        cy.get('.p-element.ng-star-inserted > .p-ripple').click()
        cy.get('[type="submit"]').click()





    })
})