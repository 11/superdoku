const sample = [
    "6------7------5-2------1---362----81--96-----71--9-4-5-2---651---78----345-------",
    "685329174971485326234761859362574981549618732718293465823946517197852643456137298"
  ];

  window.onload = function() {
    //run game on click of button "play"
    document.querySelector('.play_btn').addEventListener('click', playGame);
    //playGame();
  }

  function playGame() {
    let board;
    board = sample[0];
    generateBoard(board);
  }

  //create sudoku board
  function generateBoard(board) {
      console.log(board);
    clearBoard();

    for(let i = 0; i < 81; i++){
        //create 81 tiles as tparagraphs
        let tile = document.createElement("p");

        //change delimiter based on character used
        // if number exists in location, populate text w/ number.
        if(board.charAt(i) != "-"){
            tile.textContent = board.charAt(i);
        } else{
            //listen for click of tile, then change paragraph to text field in tile for user input.
            tile = document.createElement("p");
            tile.textContent = " ";
        }

        //add tile class to tiles
        tile.classList.add('number-tile');

        //add tile to board
        document.querySelector('.sudoku-board').appendChild(tile);
    }
  }

  //clear board
  function clearBoard() {
    let tiles = document.querySelectorAll('.number-tile');

    for(let i = 0; i < tiles.length; i++){
        tiles[i].remove();
    }
  }