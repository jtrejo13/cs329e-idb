$(function(){
    $("table").tablesorter({
	theme: 'blue',
	sortList: [[0,0], [1,0]],
	widgets: ['zebra', 'filter'],
	widgetOptions:{
	    filter_external: '.search',
	    filter_columnFilters: false,
	    filter_reset: '.reset',
	    filter_ignoreCase: true,
	    filter_liveSearch: true,
	    filter_searchDelay: 100,
	}
    });

    
    $("table").tablesorterPager({
	container: $("#pager"),
    });

    $('select').change(function(){
	// modify the search input data-column value (swap "0" or "all")
	$('.selectable').attr( 'data-column', $(this).val() );
	// update external search inputs
	$.tablesorter.filter.bindSearch( $table, $('.search'), false );
    });
});

