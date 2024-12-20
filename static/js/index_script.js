let isElectron;

// Detect if running in Electron or a web environment
(function detectEnvironment() {
    isElectron = typeof window !== 'undefined' && window.process && window.process.versions.electron;
    console.log("Operating Environment", isElectron);
})();

document.addEventListener("DOMContentLoaded", function() {
    // Set the hidden input field for isElectron
    const isElectronInput = document.getElementById("isElectron");
    if (isElectronInput) {
        isElectronInput.value = isElectron; // Set the hidden field to true/false
    }

    // Function to encrypt the password before submitting the login form
    function encryptPassword() {
        const username = document.querySelector('input[name="username"]').value; // Capture the username
        const password = document.querySelector('input[name="password"]').value;
        const secretKey = "monty"; // Ensure you use a secure method to handle this key
        const iv = CryptoJS.enc.Hex.parse('000102030405060708090A0B0C0D0E0F');  // Example fixed IV
        const key = CryptoJS.enc.Utf8.parse(secretKey);

        // Encrypt the password
        const encrypted = CryptoJS.AES.encrypt(password, key, { iv: iv }).toString();

        // Replace the raw password field with the encrypted password before submission
        document.querySelector('input[name="password"]').value = encrypted;
    }

    // Attach the function to the login form submission
    const loginForm = document.getElementById("login-form");
    if (loginForm) {
        loginForm.addEventListener("submit", function(event) {
            encryptPassword(); // Encrypt the password before form submission
        });
    }
});

