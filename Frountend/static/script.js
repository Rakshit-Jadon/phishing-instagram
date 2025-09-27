document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const inputs = document.querySelectorAll('input');
    const loginButton = document.querySelector('button[type="submit"]');

    function validateForm() {
        let isValid = true;
        inputs.forEach(input => {
            if (!input.value.trim()) {
                isValid = false;
            }
        });
        loginButton.disabled = !isValid;
    }

    inputs.forEach(input => {
        input.addEventListener('input', validateForm);
    });
});