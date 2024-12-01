describe('template spec', () => {
    it('passes', () => {
        cy.viewport(1024, 1800);
        cy.on('uncaught:exception', (err, runnable) => {
            // Handle the exception here (e.g., log it)
            return false; // Prevent Cypress from failing the test
        });
        cy.visit('https://tpportal-qa1.intranet.pajak.go.id/',)
        cy.get('#Username').type('admin')
        cy.get('#password').type('R7!sXw2F')
        cy.get('.btn-brand').click()

        cy.get('#776').click()
        cy.contains('Tax Borne by Government Water Company Request').click({ force: true })
        cy.contains('Create New interest Compensation Request').click({ force: true })
        cy.contains('Permohonan PPh DTP atas Penghasilan Tertentu PDAM').click({ force: true })
        cy.contains('Buat Permohonan PPh DTP atas Penghasilan Tertentu PDAM').click()

        cy.get('#CorrespondenceDocumentNo-input').clear().type('OK1')
        cy.get('#input-BudgetYear').clear().type('2024')
        cy.get('#input-TaxYear').clear().type('2024')

        cy.wait(20000)
        cy.contains('0011280682123000').should('be.visible')
        cy.contains('JL SISINGAMANGARAJA NO.1, KOTA MEDAN, SUMATERA UTARA 20212', { timeout: 30000 }).should('be.visible')


        // Bank Account Details
        cy.get('#BankAccountNo-input').type('123000123')
        cy.get('#BankAccountName-input').type('Payment Tester')
        cy.get('#BankName-input').type('BANK JAGO')
        cy.get('#BankBranch-input').type('HEHEHHE')

        // Financial Statement in IDR
        cy.get('#number-OperatingRevenues').type('1000000')
        cy.get('#number-OperatingExpenses').type('5000')

        cy.get('#number-OtherIncomeOtherThanWriteOffStateReceivable').type('2000000')
        cy.get('#number-IncomeFromWriteOffStateReceivable').type('400000')
        cy.get('#number-OtherExpenses').type('3000000')
        cy.get('#number-FiscalCorrection').type('5000000')
        cy.get('#number-LossCompensation').type('600000')
        cy.get('#number-TaxDueIncludingIncomeFromWriteOffStateReceivable').type('400000')
        cy.get('#number-TaxDueExcludingIncomeFromWriteOffStateReceivable').type('50000')

        // //Signer Identity
        // cy.get('#City-input').type('Jakarta')
        // cy.get('#SignersName-input').type('Tukang Signer')

        // cy.get(".p-checkbox-box").click()


        // // cy.xpath("//li[.='KO DJP']")
        // cy.get('#select-SignerProvider').click()
        // cy.get('[aria-label="KO DJP"]').click()

        // cy.get('#input-SignerNik', { force: true }).type('3305202311840002')
        // cy.get('#SignerPassword-input').type('Pajak123')
        // // cy.wait(15000)
        // cy.get('[arialabel="Sign"]').click()

        // // form signed

        // cy.get('#82').click()
        // // cy.wait(10000)
        // cy.contains('Tax Borne by Government Water Company Request').click({ force: true })

        // cy.xpath("//tbody[@class='p-element p-datatable-tbody']/tr[1]//button[@id='EditButton']").click()
        // cy.get('[arialabel="Submit"]').click()

        // cy.wait(15000)
        // // cy.xpath("//button[@class='btn btn-link']").click()

        // cy.visit('https://ctas-qa1.intranet.pajak.go.id/home/')
        // cy.get('#username').type('admin')
        // cy.get('#password').type('Pajak123')
        // cy.get('.btn-brand').click()

        // cy.get('#4').click()
        // cy.contains('All Cases').click({ force: true })
        // cy.wait(20000)

        // cy.get('[class="p-inputtext p-component p-element ng-star-inserted"]').eq(3).type('Tax Borne by Government Water Company{enter}')
        // cy.xpath("//th[.='Created']").click()
        // cy.wait(5000)
        // cy.xpath("//th[.='Created']").click()
        // // cy.wait(5000) 
        // cy.get('.p-datatable-tbody > tr:nth-of-type(1) #SelectButton').click()

        // cy.get('#311').click()

        // cy.frameLoaded('#connector-0')
        // cy.get('iframe[class="connector-iframe"]').then(($iframe) => {
        //     const $body = $iframe.contents({ force: true }).find('body')
        //     cy.wait(15000)
        //     cy.wrap($body).find('[class="p-element p-fluid ng-tns-c87-9 ng-star-inserted"]').type('AZIVA RUSLINA')
        //     cy.wrap($body).contains('Add').click()
        // });
        // cy.get('#nextStep').click()

        // cy.wait(20000)

        // cy.frameLoaded('#connector-0')
        // cy.get('iframe[class="connector-iframe"]').then(($iframe) => {
        //     const $body = $iframe.contents({ force: true }).find('body')
        //     cy.wait(20000)
        //     cy.get('#id="ReceiptNumber-input"').type('MANTAP01')

        //     cy.wrap($body).find('[icon="pi pi-calendar"]') // Sesuaikan selector sesuai dengan elemen datepicker
        //     const date = '05-10-2024'; // YYYY-MM-DD format
        //     cy.wrap($body).find('input').eq(6).type(date); // Isi tanggal ke dalam input datepicker
        // });





























    })
})