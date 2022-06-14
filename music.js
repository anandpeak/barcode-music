let readline = require("readline");
var player = require('play-sound')(opts = {})

readline.emitKeypressEvents(process.stdin);

process.stdin.on("keypress", (ch, key) => {
  console.log('got "keypress"', ch, key);

  if (key && key.sequence == "a") {
    player.play('sounds/beat1.mp3', function(err){
        if (err) throw err
      })
  }

});

process.stdin.setRawMode(true);
process.stdin.resume();