describe('template spec', () => {
    it('passes', () => {
        cy.on('uncaught:exception', (err, runnable) => {
            // Handle the exception here (e.g., log it)
            return false; // Prevent Cypress from failing the test
        });
        cy.visit('https://ctas-qa1.intranet.pajak.go.id/home/',
        )
        cy.get('#username').type('admin')
        cy.get('#password').type('Pajak123')
        cy.get('.btn-brand').click()

        cy.get('#4').click()
        cy.contains('New Case').click({ force: true })
        cy.get('#CaseTypeIdentifier').type('Travel')

        cy.contains('[aria-label="Travel Ban Request"]', 'Travel Ban Request').click() // mengatasi lebih dari 1 option
        cy.get('#Taxpayer').click()
        cy.get('#ObjectPermitNumber').type('1091031210914608')
        cy.get('.p-button-label').click()
        cy.get('#CaseInvolvement').type('Information Source')
        cy.contains('Save').click()

        cy.get('#311').click()
        cy.get('#nextStep').click()

        cy.get('#connector-0').then(($iframe) => {
            // Ensure the iframe is fully loaded
            const iframeBody = $iframe.contents().find('body');

            // Interact with elements inside the iframe
            cy.wrap(iframeBody)
                .find('.ng-star-inserted')
                .type('199511252016121002');

            cy.wrap(iframeBody)
                .find('span')
                .contains('Add')
                .click();


        })
    })
})