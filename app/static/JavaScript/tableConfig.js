$(function(){
    $("table").tablesorter({
	theme: 'blue',
	sortList: [[0,0], [1,0]],
	widgets: ['zebra', 'filter'],
	widgetOptions:{
	    filter_external: '.search'
	}
    });
    $("table").tablesorterPager({
	container: $("#pager"),
    });
});

