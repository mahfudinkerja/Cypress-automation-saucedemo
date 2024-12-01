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


        cy.get('#CaseTypeIdentifier').type('Pajak Ditanggung Pemerintah (DTP)')
        cy.get('.p-element.ng-star-inserted > .p-ripple').click()

        cy.get('.btn.btn-primary.btn-sm').eq(0).click()


        cy.get('[arialabel="Number"]')
        // cy.get("cy.get('csm-case-overview.ng-star-inserted > .row > :nth-child(2)')").type('{cmd}c')
        cy.get('#311').click()
        cy.contains('Alur Kasus').click({ force: true })

        cy.wait(10000)
        // Assign Oficer
        cy.get('iframe[class="connector-iframe"]').then(($iframe) => {
            const $body = $iframe.contents({ force: true }).find('body');
            cy.wrap($body).find('.p-inputtext[type=text]').eq(1).type('AZIVA RUSLINA')
            cy.wrap($body).contains('Tambah').click()
        });
        cy.get('#nextStep').click()

        cy.get('.ml-3').click()
        cy.get('#username').type('aziva.ruslina')
        cy.get('#password').type('Pajak123')
        cy.get('.btn-brand').click()

        cy.get('#4').click()
        cy.contains('Manajemen Kasus').click({ force: true })
        cy.contains('Kasus Jatuh Tempo').click({ force: true })
        cy.wait(15000);
        cy.get('[name="CreatedDateGridColumn10"]').click()
        cy.wait(10000);
        cy.get('[name="CreatedDateGridColumn10"]').click()
        cy.get(':nth-child(1) > [style="text-align: left; min-width: 130px;"] > #SelectButton').click()

        // cy.get("cy.get('csm-case-overview.ng-star-inserted > .row > :nth-child(2)')").type('{cmd}v')












    })
})