function setNavigation() {
    let current_location = location.pathname.split('/')[1];
    if (current_location === "") {
    	document.getElementById('homenav').className = "active";
    	return;
    }
    var nav = document.getElementById('topnav'),
        menu_items = nav.getElementsByTagName('a');
    for (let i = 0, len = menu_items.length; i < len; i++) {
      if (menu_items[i].getAttribute("href").indexOf(current_location) !== -1) {
        menu_items[i].className = "active";
      }
    }
  }
  setNavigation()
