describe('template spec', () => {
    it('passes', () => {
        cy.on('uncaught:exception', (err, runnable) => {
            // Handle the exception here (e.g., log it)
            return false; // Prevent Cypress from failing the test
        });
        cy.visit('https://shopee.co.id/')
        // cy.get('[class="cHPMhq"]').click()
        // cy.get('[name="loginKey"]').type('mahfudcovra@gmail.com')
        // cy.get('[name="password"]').type('passwordShopee8!')
        // cy.get('[class="vvOL40 iesrPs AsFRg8 qCI4rz ZKayWA AnY7KS"]').click()

        cy.get('.eQpFX_').click()
        cy.wait(10000)
        cy.visit('https://id.shp.ee/YitRxWb')
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()
        cy.xpath("//button[@class='btn btn-solid-primary btn--l YuENex']").click()






    })
})