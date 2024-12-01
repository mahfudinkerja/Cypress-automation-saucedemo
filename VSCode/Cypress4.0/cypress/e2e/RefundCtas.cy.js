/// <reference types="Cypress" />
describe('RefundFom013', () => {
    it('passes', () => {
        cy.viewport(2024, 1700);
        cy.on('uncaught:exception', (err, runnable) => {
            // Handle the exception here (e.g., log it)
            return false; // Prevent Cypress from failing the test
        });
        cy.visit('https://ctas-qa.intranet.pajak.go.id/',
        )
        cy.get('#username').type('admin')
        cy.get('#password').type('R7!sXw2F')
        cy.get('.btn-brand').click()

        cy.get("a[id='776']").click()
        cy.get('#ul-776 > :nth-child(10) > .dropdown-item')
            .click({ force: true })

        // Manual Payment Creation===================================//
        cy.get("tbody tr[class='ng-untouched ng-pristine ng-invalid ng-star-inserted'] td:nth-child(3) input:nth-child(1)").type("2171075002739002")
        cy.get(':nth-child(4) > .form-control').should('be.visible')

        cy.get('.col-md-12').click()
        cy.get(':nth-child(6) > ui-dropdown > .p-inputwrapper > .col-sm-12 > .p-dropdown-label').click()
        cy.get(':nth-child(2) > .p-ripple').click()

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

        cy.get('.col-md-12').click()
        cy.get('#776').click()

        // Refund Form013===================================//
        cy.contains('Formulir Permohonan Pengembalian Kelebihan Pembayaran Pajak').click({ force: true })
        cy.get('#CorrespondenceLetter-input').type('Refund Form013 MD')
        cy.wait(5000)
        cy.get('#select-Channel > .col-sm-12 > .p-dropdown-label').click()
        cy.wait(5000)
        cy.get('#pr_id_16_list > :nth-child(1) > .p-ripple').click()

        cy.get(':nth-child(1) > .form-group > .col-sm-9 > .p-inputgroup > .p-button-warn').click()
        cy.get('#ObjectPermitNumber').type('2171075002739002')
        cy.get('.p-element.ng-star-inserted > .p-ripple').click()

        cy.get('#TaxpayerEmail-input').type('testing@email.com')

        cy.get('#select-RefundSubject > .col-sm-12 > .p-dropdown-label').click()
        cy.get(':nth-child(2) > .p-ripple > .ng-star-inserted').click()
        cy.wait(5000)
        cy.get('#p-panel-7-content > .p-panel-content > coretax-form-grid-offline.ng-star-inserted > .overflowx-auto > .justify-content-between > a')
            .should('be.visible')
            .click()
        cy.get('#p-panel-16-content > .p-panel-content > coretax-form-lookup.ng-star-inserted > .form-group > .col-sm-9 > .p-inputgroup > .p-button-warn').click()
        cy.get('.p-datatable-tbody > :nth-child(1) > :nth-child(4)', { timeout: 10000 }).should('be.visible')
        cy.get('[name="TransactionDateGridColumn1"]').click()
        cy.get('.p-datatable-tbody > :nth-child(1) > :nth-child(4)', { timeout: 10000 }).should('be.visible')
        cy.get('[name="TransactionDateGridColumn1"]').click()
        cy.get(':nth-child(1) > [style="text-align: left; min-width: 130px;"] > #SetActive').click()
        cy.get('.form-group > .row > #undefined').click()
        // cy.get('#p-panel-11-content > .p-panel-content > coretax-form-lookup.ng-star-inserted > .form-group > .col-sm-9 > .p-inputgroup > .p-button-warn').click()
        // cy.get('#SetActive').click()

        // cy.get(':nth-child(3) > div.ng-star-inserted > .form-group > div.col-sm-6 > .grid > .p-element').selectFile("/Users/mymac/Downloads/Document Upload/4.MD Documents Upload.pdf")

        cy.xpath("//coretax-form-upload-with-file-storage[1]//div[1]//div[1]//div[1]//div[1]//button[1]")
            .selectFile("/Users/mymac/Downloads/Document Upload/4.MD Documents Upload.pdf")



        // cy.get("body > pmnt-root:nth-child(1) > div:nth-child(1) > ui-coretax-one-column-layout:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > pmnt-refund-transfer-review-request:nth-child(2) > pmntshr-request-refund-transfer-review-form:nth-child(1) > coretax-dynamic-generated-form-with-controls:nth-child(1) > form:nth-child(2) > div:nth-child(6) > p-panel:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > coretax-form-upload-with-file-storage:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(1)").selectFile




















    })
})