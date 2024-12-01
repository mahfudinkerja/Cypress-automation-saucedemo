const { defineConfig } = require('cypress');

module.exports = defineConfig({
    e2e: {
        pageLoadTimeout: 120000, // Tunggu hingga 2 menit
        defaultCommandTimeout: 10000, // Timeout default untuk perintah lainnya
    },
});
