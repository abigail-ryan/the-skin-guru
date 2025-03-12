document.addEventListener('DOMContentLoaded', function() {
    const phoneNumberInput = document.getElementById('id_phone_number');
    const errorMessageElement = document.getElementById('phone-number-error');

    phoneNumberInput.addEventListener('blur', function (event) {
        validatePhoneNumber(event.target);
    });

    function validatePhoneNumber(input) {
        const phoneNumber = input.value.replace(/\D/g, '');
        
        if (phoneNumber.length < 10 || phoneNumber.length > 15) {
            input.classList.add('is-invalid');
            errorMessageElement.textContent = 'Phone number must be between 10 and 15 digits.';
            return false;
        } else {
            input.classList.remove('is-invalid');
            errorMessageElement.textContent = '';
            return true;
        }
    }

    document.getElementById('payment-form').addEventListener('submit', function(event) {
        if (!validatePhoneNumber(phoneNumberInput)) {
            event.preventDefault();
            phoneNumberInput.focus();
        }
    });
});