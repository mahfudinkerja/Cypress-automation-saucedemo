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
        cy.get('#ul-776 > :nth-child(1) > .dropdown-item').click()
        cy.get('#ObjectPermitNumber').type('1091031210913878')
        cy.get('.p-button-label').click()
        cy.get('#Next').click()
        cy.get('#TaxTypeTaxPayment > .form-control > .p-dropdown-label').type('411128-402 PPh Final Pasal 4 (2) atas Pengalihan Hak Tanah dan/atau Bangunan')
        cy.contains('411128-402 PPh Final Pasal 4 (2) atas Pengalihan Hak Tanah dan/atau Bangunan').click()
        cy.get('#TaxPeriod > .form-control > .p-dropdown-label').type('Oktober 2024')
        cy.contains('Oktober 2024').click()
        cy.get('#lnb-sector-rural > .p-radiobutton > .p-radiobutton-box').click()
        cy.get('#TaxObjectNumber').type('123123123123122312')
        cy.get('#TaxObjectAddress').type('Direktorat Jenderal Pajak, Kementerian Keuangan Republik Indonesia Jl.Jenderal Gatot Subroto No. 40 Jakarta 12190 Indonesia')
        cy.get('#Province > .p-inputwrapper > .col-sm-12 > .p-dropdown-label').type('DKI Jakarta')
        cy.contains('DKI Jakarta').click()
        cy.get('#CityMunicipality > .p-inputwrapper > .col-sm-12 > .p-dropdown-label').type('KOTA ADM. JAKARTA PUSAT')
        cy.contains('KOTA ADM. JAKARTA PUSAT').click()
        cy.get('#District > .p-inputwrapper > .col-sm-12 > .p-dropdown-label').type('CEMPAKA PUTIH')
        cy.contains('CEMPAKA PUTIH').click()
        cy.get('#SubDistrict > .p-inputwrapper > .col-sm-12 > .p-dropdown-label').type('CEMPAKA PUTIH TIMUR')
        cy.contains('CEMPAKA PUTIH TIMUR').click()
        cy.get('#Next > .p-button-label').click()

        cy.get('#AmountInput').type('1000123')
        cy.get('#Remarks').type('Mantep Abis')
        cy.get('.col-md-12').click()
        // cy.get('#Download\ Billing\ Code').click()
        // cy.get('#Download\ Billing\ Code').click()
        // cy.get('Download Billing Code').click()
        // cy.contains('Unduh Kode Billing').click()


















    })
})