describe('Login and Case Management Test', () => {
    before(() => {
        // Visit the initial login page
        cy.visit('https://satu-sim.intranet.pajak.go.id/login');

        // Handle SSL certificate error if present
        cy.get('#details-button', { timeout: 10000 }).click();
        cy.get('#proceed-link').click();
    });

    it('should log in and perform case management actions', () => {
        const supervisorLto = 'evelinsarmauli.siagian';
        const password = 'Pajak123';
        const caseTypeIdentifier = 'Travel Ban Request';
        const taxpayer = '0747779825024000';
        const informationSource = 'Information source';
        const officerId = '199511252016121002';

        // Perform login
        cy.get('input[name="username"]').type(supervisorLto);
        cy.get('input[name="password"]').type(password);
        cy.get('button[type="submit"]').click();

        // Visit the new page
        cy.visit('https://ctas-qa.intranet.pajak.go.id/');

        // Handle SSL certificate error if present
        cy.get('#details-button', { timeout: 10000 }).click();
        cy.get('#proceed-link').click();

        // Interact with case management elements
        cy.xpath('//*[@id="4"]').click();
        cy.xpath('//a[@href="/case-management/en-US/case-creation"]').click();

        // Select case type
        cy.get('#CaseTypeIdentifier').click();
        cy.xpath('/html/body/csm-root/div/ui-coretax-one-column-layout/div/div/div/csm-case-creation/div/csm-case-creation-form/form/div[1]/div/p-dropdown/div/p-overlay/div/div/div/div[1]/div/input')
            .type(caseTypeIdentifier);
        cy.xpath(`//span[.="${caseTypeIdentifier}"]`).click();

        // Fill in case details
        cy.get('#Taxpayer').click();
        cy.get('#ObjectPermitNumber').type(taxpayer);
        cy.get('.p-button-label').click();
        cy.xpath('//*[@id="CaseInvolvement"]/div/span').click();
        cy.xpath(`//span[.="${informationSource}"]`).click();
        cy.xpath("//button[.='Save']").click();

        // Wait for and click on General Information
        cy.xpath("//a[.='General Information']").click();

        // Extract case number
        cy.xpath("//h1[@class='ng-star-inserted']").invoke('text').as('caseNumber');

        // Perform routing actions
        cy.xpath("//a[.='Routing']").click();
        cy.get('#nextStep').click();

        // Handle iframe
        cy.get('iframe#connector-0', { timeout: 10000 }).then($iframe => {
            const iframeBody = $iframe.contents().find('body');
            cy.wrap(iframeBody).find('(//div//table//thead//tr[2]//th[3]//input)[1]').type(officerId);
            cy.wrap(iframeBody).find('span').contains('Add').click();
        });

        cy.get('#nextStep').click();

        // Log off and log in with a different user
        cy.wait(10000);
        cy.xpath("//a[.='Log off']").click();

        const taxOfficerLtoUsername = 'wawan.nurprayogi';

        cy.get('input[name="username"]').type(taxOfficerLtoUsername);
        cy.get('input[name="password"]').type(password);
        cy.get('button[type="submit"]').click();

        // Navigate to My Due Cases and search for the case number
        cy.xpath("//ul[@class='navbar-nav mr-auto scrollmenu ng-star-inserted']/li[@class='nav-item p-0 ng-star-inserted']/a[contains(.,'Case Management')]").click();
        cy.xpath("//a[.='My Due Cases']").click();
        cy.get('#filterCaseNumber .p-inputtext').type(`${this.caseNumber}{enter}`);

        cy.get('#SelectButton').click();
    });
});
