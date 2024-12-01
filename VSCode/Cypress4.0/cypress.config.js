const { defineConfig } = require("cypress");

module.exports = defineConfig({
    chromeWebSecurity: false,
    experimentalModifyObstructiveThirdPartyCode: true,
    e2e: {
        spectPattern: 'cypress/e2e/**/*.cy.{js,jsx,ts,tsx}',
        setupNodeEvents(on, config) {
            // implement node event listeners here
        },
    },
});
