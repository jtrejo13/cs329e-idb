Cypress.on('uncaught:exception', (err, runnable) => {
    // prevent uncaught assertion errors when loading each page
    return false
})

describe('Test Artists Page', function() {
    beforeEach(function() {
        // visit page before each test
        cy.visit('/artists')
    })

    it('Test jinja2 blocks', function() {
        // check for elements in the head, nav, body, and footer
        cy.get('head')
        cy.get('nav')
        cy.get('.search-bar')
        cy.get('footer')
    })

    it('Test search selector', function() {
        // select each option and test it's value
        cy.get('.change-input')
            .select('all')
            .should('have.value', 'all')
            .select('Artist')
            .should('have.value', '0')
            .select('Origin')
            .should('have.value', '1')
            .select('Genre')
            .should('have.value', '2')
            .select('Start')
            .should('have.value', '3')
            .select('Latest release')
            .should('have.value', '4')
    })

    it('Test pager selector', function() {
        // select 10 and check its value
        cy.get('.pagesize')
            .select('10')
            .should('have.value', '10')
        // confirm pagedisplay is updated
        cy.get('.pagedisplay').should(($span) => {
            const textArr = $span.text().split(' ')
            expect(textArr).to.have.lengthOf(6)
            expect(textArr[2]).to.eq('10')
        })
        // select 20 and check its value
        cy.get('.pagesize')
            .select('20')
            .should('have.value', '20')
        // confirm pagedisplay is updated
        cy.get('.pagedisplay').should(($span) => {
            const textArr = $span.text().split(' ')
            expect(textArr).to.have.lengthOf(6)
            expect(textArr[2]).to.eq('20')
        })
        // select all rows and check its value
        cy.get('.pagesize')
            .select('All Rows')
            .should('have.value', 'all')
        // confirm pagedisplay is updated
        cy.get('.pagedisplay').should(($span) => {
            const textArr = $span.text().split(' ')
            expect(textArr).to.have.lengthOf(6)
            expect(textArr[2]).to.eq(textArr[4])
        })
    })

    it('Test pager buttons', function() {
        // test page size 10
        cy.get('.pagesize').select('10')
        cy.get('.pagedisplay').should('contain', '1 to 10')
        cy.get('.next').click()
        cy.get('.pagedisplay').should('contain', '11 to 20')
        cy.get('.prev').click()
        cy.get('.pagedisplay').should('contain', '1 to 10')
        // after clicking last, show that pagedisplay is on last page
        cy.get('.last').click()
        cy.get('.pagedisplay').should(($span) => {
            const textArr = $span.text().split(' ')
            expect(textArr).to.have.lengthOf(6)
            expect(textArr[2]).to.eq(textArr[4])
        })
        // after clicking first, show that pagedisplay is on first page
        cy.get('.first').click()
        cy.get('.pagedisplay').should('contain', '1 to 10')
    })

    // test search results

    // test reset
})