/* SLIDER */

var counter = 2;
setInterval(function() {
    document.getElementById('radio' + counter).checked = true;
    counter++;
    if(counter > 2) {
        counter = 1;
    }
}, 5000);