describe('template spec', () => {
    it('passes', () => {
        cy.viewport(2020, 2100);
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


        cy.get('#CaseTypeIdentifier').type('Pajak Ditanggung Pemerintah (DTP)')
        // cy.contains('Pajak Ditanggung Pemerintah (DTP)').click()
        cy.get('.p-element.ng-star-inserted > .p-ripple').click()
        // cy.get('#Taxpayer').click()
        // cy.get('#ObjectPermitNumber').type('5103066311960003')
        // cy.get('.p-button-label.ng-star-inserted').eq(0).click()
        // cy.get('#CaseInvolvement').click()
        // cy.contains('Subyek kasus').click()
        // cy.get('.ng-tns-c67-10.form-control.form-control-sm.p-calendar').type('06-11-2024')
        cy.get('.btn.btn-primary.btn-sm').eq(0).click()
        cy.get('#311').click()
        cy.contains('Alur Kasus').click({ force: true })

        // cy.get('.p-button-label').eq(4).click()
        cy.wait(10000)

        cy.get('iframe[class="connector-iframe"]').then(($iframe) => {
            const $body = $iframe.contents({ force: true }).find('body');
            cy.wrap($body).find('.p-inputtext[type=text]').eq(1).type('AZIVA RUSLINA')
            cy.wrap($body).contains('Tambah').click()
        });
        cy.get('#nextStep').click()

        // 








    })
})