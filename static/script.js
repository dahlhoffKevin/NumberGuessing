// JavaScript function to reset the game
function restartGame() {
    document.getElementById('playerNameInput').value = ''; // Clear player name input
    document.getElementById('number').value = ''; // Clear guessing number input
    document.getElementById('number').placeholder = 'Guess number!!'; // Restore placeholder
    document.getElementById('playerNameInput').placeholder = 'Player name...';
  }

  // Placeholder removal and restoration for playerNameInput
  function removePlaceholderPlayerName() {
    document.getElementById('playerNameInput').placeholder = '';
  }

  function restorePlaceholderPlayerName() {
    document.getElementById('playerNameInput').placeholder = 'Player name...';
  }

  // Placeholder removal and restoration for guessing number input
  function removePlaceholder() {
    document.getElementById('number').placeholder = '';
  }

  function restorePlaceholder() {
    document.getElementById('number').placeholder = 'Guess number!!';
  }

  function validateNumberInput() {
    const input = document.getElementById('number');
    input.value = input.value.replace(/[^0-9]/g, ''); // Only allow digits
  }