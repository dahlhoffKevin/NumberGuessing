// JavaScript function to reset the game
function restartGame() {
    document.getElementById('number').value = ''; // Clear guessing number input
    document.getElementById('number').placeholder = 'Guess number!!'; // Restore placeholder
  }

  // Placeholder removal and restoration for playerNameInput
  function removePlaceholderPlayerName() {
    document.getElementById('playerNameInput').placeholder = '';
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

  function restartGame() {
    // Redirect to the Flask route to restart the game
    window.location.href = "/clear";
}