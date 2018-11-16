(function () {
	"use strict";

	var treeviewMenu = $('.app-menu');

	// Toggle Sidebar
	$('[data-toggle="sidebar"]').click(function(event) {
		event.preventDefault();
		var $app = $('.app');
		$app.toggleClass('sidenav-toggled');
		var value = $app.hasClass('sidenav-toggled');
		Cookies.set('sidenav-toggled', value, {expires: 30});
	});
	/*
	$(window).ready(function() {
		if(Cookies.get('sidenav-toggled') != 'true') {
			$('.app').removeClass('sidenav-toggled');
		}
	});
	*/
	

	// Activate sidebar treeview toggle
	$("[data-toggle='treeview']").click(function(event) {
		event.preventDefault();
		if(!$(this).parent().hasClass('is-expanded')) {
			treeviewMenu.find("[data-toggle='treeview']").parent().removeClass('is-expanded');
		}
		$(this).parent().toggleClass('is-expanded');
	});

	// Set initial active toggle
	$("[data-toggle='treeview.'].is-expanded").parent().toggleClass('is-expanded');

	//Activate bootstrip tooltips
	$("[data-toggle='tooltip']").tooltip();

})();
