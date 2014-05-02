document.onkeydown = checkKey;

function checkKey(e) {
    e = e || window.event;

    var map = {
      38: 0, // Up
      39: 1, // Right
      40: 2, // Down
      37: 3, // Left
      75: 0, // Vim up
      76: 1, // Vim right
      74: 2, // Vim down
      72: 3, // Vim left
      87: 0, // W
      68: 1, // D
      83: 2, // S
      65: 3  // A
    };

    if (e.keyCode == '38') {
        alert map[e.keyCode];
        // up arrow
    }
    else if (e.keyCode == '40') {
        // down arrow
    }
}
