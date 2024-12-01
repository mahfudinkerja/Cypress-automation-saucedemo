describe('template spec', () => {
    it('passes', () => {
        // cy.viewport(1024, 1500);
        cy.on('uncaught:exception', (err, runnable) => {
            // Handle the exception here (e.g., log it)
            return false; // Prevent Cypress from failing the test
        });
        cy.visit('https://ctas-qa1.intranet.pajak.go.id/home/',
        )
        cy.get('#username').type('admin')
        cy.get('#password').type('R7!sXw2F')
        cy.get('.btn-brand').click()

        cy.get('#4').click()
        cy.contains('New Case').click({ force: true })
        cy.get('#CaseTypeIdentifier').type('Travel')

        cy.contains('[aria-label="Travel Ban Request"]', 'Travel Ban Request').click() // more than 1 options
        cy.get('#Taxpayer').click()
        cy.get('#ObjectPermitNumber').type('1091031210914608')
        cy.get('.p-button-label').click()
        cy.get('#CaseInvolvement').type('Information Source')
        cy.contains('Save').click()

        cy.get('#311').click()
        cy.get('#nextStep').click()
        // cy.wait(15000)

        cy.frameLoaded('#connector-0');

        // Officer Assignment
        cy.get('iframe[class="connector-iframe"]').then(($iframe) => {
            const $body = $iframe.contents({ force: true }).find('body');
            // cy.wrap($body).find('.ng-star-inserted').children('.ng-tns-c87-9>input:first').type('IZAZI MUBAROK')
            cy.wrap($body).find('.p-inputtext[type=text]').eq(1).type('WAWAN NURPRAYOGI')
            cy.wrap($body).contains('Add').click()
            // cy.wrap($body).find('.pi-filter-slash').eq(2).click()
            // cy.wrap($body).find('.p-inputtext[type=text]').eq(1).type('TEGUH HARIYONO')
            // cy.wrap($body).contains('Add').click()
        });
        cy.get('#nextStep').click()


    })
})