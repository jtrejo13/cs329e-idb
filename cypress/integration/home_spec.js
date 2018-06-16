describe('Test home page content', function() {
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

    it('test portfolio', function() {
        cy.get('.portfolio-link').then(($links) => {
            // There should be 6 elements
            cy.wrap($links).should('have.length', 6)
                // Each element should have an img
                .each(($el) => {
                    cy.wrap($el).find('img')
                })
        })
    })

    it('test team', function() {
        cy.get('.team-member').then(($links) => {
            // There should be 5 elements
            cy.wrap($links).should('have.length', 5)
                .each(($el) => {
                    // Each element should have an img, p, h4, ul
                    cy.wrap($el).find('img')
                    cy.wrap($el).find('p')
                    cy.wrap($el).find('h4')
                    cy.wrap($el)
                        .find('ul')
                        .children('li')
                        .should(($li) => {
                            expect($li).to.have.length.lte(2)
                    })
                })
        })
    })
})