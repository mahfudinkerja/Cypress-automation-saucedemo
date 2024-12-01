describe('template spec', () => {
    it('passes', () => {
        cy.viewport(1800, 1800);
        cy.on('uncaught:exception', (err, runnable) => {
            // Handle the exception here (e.g., log it)
            return false; // Prevent Cypress from failing the test
        });
        cy.visit('https://ctas-qa.intranet.pajak.go.id/',
        )
        cy.get('#username').type('admin')
        cy.get('#password').type('R7!sXw2F')
        cy.get('.btn-brand').click()

        cy.get('#776').click()
        cy.xpath("//a[.='Perekaman Data Pembayaran Manual']").click({ force: true })

        cy.get(':nth-child(3) > .form-control').type('1091031210913878')
        cy.get('.col-md-12').click()
        cy.get(':nth-child(6) > ui-dropdown > .p-inputwrapper > .col-sm-12 > .p-dropdown-trigger').type('Pembayaran Tunai')
        cy.get(':nth-child(8) > .p-inputwrapper > .col-sm-12 > .p-dropdown-label').type('411618-100 Setoran untuk Deposit Pajak')
        cy.contains('411618-100 Setoran untuk Deposit Pajak').click()
        cy.get(':nth-child(9) > .p-inputwrapper > .col-sm-12 > .p-dropdown-label').type('Januari - Desember 2024')
        cy.contains('Januari - Desember 2024').click()
        cy.get(':nth-child(12) > ui-dropdown > .p-inputwrapper > .col-sm-12 > .p-dropdown-label').type('Rupiah Indonesia')
        cy.contains('Rupiah Indonesia').click()
        cy.get('.p-button-warn > .p-button-icon').click()
        cy.get(':nth-child(1) > .p-button-label').click()
        cy.get('#Amount0').type('50000123')
        cy.get(':nth-child(15) > .form-control').type('ok gas')
        cy.get('.py-2 > .btn').click()
        cy.get('.p-2 > .btn').click()













    })
})