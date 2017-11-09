$(function(){
    $("table").tablesorter({
	theme: 'blue',
	sortList: [[0,0], [1,0]],
	widgets: ['zebra'],
    });
    $("table").tablesorterPager({
	container: $("#pager"),
    });
});

