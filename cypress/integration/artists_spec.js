// Cypress.on('uncaught:exception', (err, runnable) => {
//     // prevent uncaught assertion errors when loading each page
//     return false
// })

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
            var textArr = $span.text().split(' ')
            expect(textArr).to.have.lengthOf(6)
            expect(textArr[2]).to.eq('10')
        })
        // select 20 and check its value
        cy.get('.pagesize')
            .select('20')
            .should('have.value', '20')
        // confirm pagedisplay is updated
        cy.get('.pagedisplay').should(($span) => {
            var textArr = $span.text().split(' ')
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
        cy.get('.pagedisplay').should('contain', '1 – 10')
        cy.get('.next').click()
        cy.get('.pagedisplay').should('contain', '11 – 20')
        cy.get('.prev').click()
        cy.get('.pagedisplay').should('contain', '1 – 10')
        // after clicking last, show that pagedisplay is on last page
        cy.get('.last').click()
        cy.get('.pagedisplay').should(($span) => {
            var textArr = $span.text().split(' ')
            expect(textArr).to.have.lengthOf(6)
            expect(textArr[2]).to.eq(textArr[4])
        })
        // after clicking first, show that pagedisplay is on first page
        cy.get('.first').click()
        cy.get('.pagedisplay').should('contain', '1 – 10')
    })

    it('Test search \'ap\'', function() {
        // first search for 'ap'
        cy.get('.search')
            .type('ap')
        // test pagedisplay length and correct rows
        cy.get('.pagedisplay').should(($span) => {
            var textArr = $span.text().split(' ')
            expect(textArr).to.have.lengthOf(8)
            expect(textArr[4]).to.eq('14')
        })
        // ensure each visible row contains 'ap' (case-insensitive)
        cy.get('tbody > tr:visible').then(($tr) => {
            expect($tr).to.have.lengthOf(10)
            cy.wrap($tr).each(($row) => {
                cy.wrap($row).contains(/ap/i)
            })
        })

        // next page
        cy.get('.next').click()
        // ensure each row contains 'ap' (case-insensitive)
        cy.get('tbody > tr:visible').then(($tr) => {
            expect($tr).to.have.lengthOf(4)
            cy.wrap($tr).each(($row) => {
                cy.wrap($row).contains(/ap/i)
            })
        })

        // change input selector to genre
        cy.get('.change-input').select('Genre')
        cy.get('.search').type('ap')
        // ensure each genre contains 'ap' (case-insensitive)
        cy.wait(100)
        cy.get('tbody > tr:visible > :nth-child(3)').then(($tr) => {
            expect($tr).to.have.lengthOf(4)
            cy.wrap($tr).each(($row) => {
                cy.wrap($row).contains(/ap/i)
            })
        })

        // test reset
        cy.get('.reset').click()
        cy.get('.pagedisplay').should(($span) => {
            var textArr = $span.text().split(' ')
            expect(textArr).to.have.lengthOf(6)
            expect(textArr[4]).to.eq('67')
        })
    })

    it('Test column sorting', function() {
        // test name column
        // ensure that the first row comes before the second and last alphabetically
        cy.get('tbody > tr > :nth-child(1) > a').then(($rows) => {
            cy.wrap($rows[0].text).should('be.lte', $rows[1].text)
            cy.wrap($rows[1].text).should('be.lte', $rows[2].text)
            cy.wrap($rows[2].text).should('be.lte', $rows[$rows.length-1].text)
        })
        // click name column head
        cy.get('[data-column="0"] > .tablesorter-header-inner').click()
        // ensure order is opposite
        cy.get('tbody > tr > :nth-child(1) > a').then(($rows) => {
            cy.wrap($rows[0].text).should('be.gte', $rows[1].text)
            cy.wrap($rows[1].text).should('be.gte', $rows[2].text)
            cy.wrap($rows[2].text).should('be.gte', $rows[$rows.length-1].text)
        })

        // test origin column
        // cy.get('.pagesize').select('All Rows')
        // click origin column head
        cy.get('[data-column="1"] > .tablesorter-header-inner').click()
        // ensure order is opposite
        cy.get('tbody > tr > :nth-child(2)').then(($rows) => {
            cy.wrap($rows[0].innerHTML).should('be.gte', $rows[1].innerHTML)
            cy.wrap($rows[1].innerHTML).should('be.gte', $rows[2].innerHTML)
            cy.wrap($rows[2].innerHTML).should('be.gte', $rows[$rows.length-1].innerHTML)
        })
        // click origin column head
        cy.get('[data-column="1"] > .tablesorter-header-inner').click()
        // ensure order is opposite
        cy.get('tbody > tr > :nth-child(2)').then(($rows) => {
            cy.wrap($rows[0].innerHTML).should('be.lte', $rows[1].innerHTML)
            cy.wrap($rows[1].innerHTML).should('be.lte', $rows[2].innerHTML)
            // last rows contain blank origin
            //cy.wrap($rows[2].innerHTML).should('be.lte', $rows[$rows.length-1].innerHTML)
        })
    })
})