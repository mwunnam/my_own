function open() {
  const loginPopup = document.getElementById('login_popup');
  fetch('login.html')
    .then(response => response.text())
    .then(htmlContent => {
        loginPopup.innerHTML = htmlContent;
        });
    .catch(error => {
        console.error('Error fetching login form: ' error);
        }
        }

}
