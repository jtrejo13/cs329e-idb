Cypress.on('uncaught:exception', (err, runnable) => {
    // prevent uncaught assertion errors when loading each page
    return false
})

describe('Testing navbar links', function() {
    beforeEach(function () {
        // visit the homepage before each test
        cy.visit('/')
    })

    it('test home scroll to top', function() {
        cy.scrollTo(0,500)
        cy.get('.navbar-brand').click()
        cy.wait(500)
        cy.window({ timeout: 10000 }).then(($window) => {
            expect($window.scrollY).to.be.closeTo(0, 100);
        })
    })

    it('test artists', function() {
        // cy.on('uncaught:exception', (err, runnable) => {
        //     expect(err.message).to.include('This error originated from your application code')
        //
        //     // using mocha's async done callback to finish
        //     // this test so we prove that an uncaught exception
        //     // was thrown
        //     done()
        //
        //     // return false to prevent the error from
        //     // failing this test
        //     return false
        // })
        cy.get(':nth-child(1) > .nav-link').click()
        cy.url().should('eq', 'http://localhost:8000/artists')
    })

    it('test albums', function() {
        cy.get(':nth-child(2) > .nav-link').click()
        cy.url().should('eq', 'http://localhost:8000/albums')
    })

    it('test songs', function() {
        cy.get(':nth-child(3) > .nav-link').click()
        cy.url().should('eq', 'http://localhost:8000/songs')
    })

    it('test team', function() {
        cy.get(':nth-child(4) > .nav-link').click()
        cy.url().should('eq', 'http://localhost:8000/')
    })

    it('test about and home', function() {
        cy.get(':nth-child(5) > .nav-link').click()
        cy.url().should('eq', 'http://localhost:8000/about')

        cy.get('.navbar-brand').click()
        cy.url().should('eq', 'http://localhost:8000/')
    })
})