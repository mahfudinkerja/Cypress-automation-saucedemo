describe('template spec', () => {
    it('passes', () => {
        cy.viewport(1020, 1020);
        cy.on('uncaught:exception', (err, runnable) => {
            // Handle the exception here (e.g., log it)
            return false; // Prevent Cypress from failing the test
        });
        cy.visit('https://ctas-qa.intranet.pajak.go.id/home/en-US/',
        )
        cy.get('#username').type('admin')
        cy.get('#password').type('R7!sXw2F')
        cy.get('.btn-brand').click()

        // cy.get('#1').click()
        cy.contains('Registrasi').click()
        cy.contains('Identitas Wajib Pajak').click({ force: true })

        cy.get('.is-invalid > .p-dropdown-label').click()
        cy.get('#pr_id_9_list > :nth-child(2) > .p-ripple').click()


        // Choose Taxpayer Pop-up
        cy.get('.p-inputgroup > #TIN').click()
        cy.get('#ObjectPermitNumber').type('2171075002739002')
        cy.get('div.ng-star-inserted > .p-element.ng-star-inserted > .p-ripple').click()

        cy.get('#p-panel-1-content > .p-panel-content > :nth-child(1) > .col-sm-9 > .form-control-sm').click()
        cy.get('#Bank > .p-inputwrapper > .col-sm-12 > .p-dropdown-label').type('PT BANK JAGO TBK')
        cy.contains('PT BANK JAGO TBK').click({ force: true })










    })
})