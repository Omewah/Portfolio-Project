// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function() {
    // Get the register button element
    var registerButton = document.getElementById("registerButton");

    // Add a click event listener to the register button
    registerButton.addEventListener("click", function() {
        // Get the flash message element
        var flashMessage = document.getElementById("flashMessage");

        // Toggle the visibility of the flash message
        flashMessage.style.display = "block";
    });
});
