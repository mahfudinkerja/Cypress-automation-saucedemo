describe('template spec', () => {
    it('passes', () => {
        cy.on('uncaught:exception', (err, runnable) => {
            // Handle the exception here (e.g., log it)
            return false; // Prevent Cypress from failing the test
        });
        cy.visit('https://tpportal-qa1.intranet.pajak.go.id/',
        )
        cy.get('#Username').type('1091031210914608')
        cy.get('#password').type('Poiuy09876%')
        cy.get('button[name="button"]').click();


        // cy.get('#4').click()
        // cy.contains('New Case').click({ force: true })
        // cy.get('#CaseTypeIdentifier').type('Travel Ban Request')
        // cy.contains('Travel Ban Request').click()
        // cy.get('#Taxpayer').click()
        // cy.get('#ObjectPermitNumber').type('1091031210914608')
        // cy.get('.p-button-label').click()
        // cy.get('#CaseInvolvement').type('Information Source')
        // cy.contains('Save').click()












    })
})


