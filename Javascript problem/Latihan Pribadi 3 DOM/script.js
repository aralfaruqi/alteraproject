function validation() {
    let username = document.form.name.value;
    if(username=="") { 
        alert("Username tidak boleh kosong !");
        document.form.name.focus();
        return false; 
    }

    let password = document.form.password.value;
    if(password=="") { 
        alert("Password tidak boleh kosong !");
        document.form.password.focus();
        return false; 
    }

    let confirmPassword = document.form.confirmPassword.value;
    if(confirmPassword=="") { 
        alert("Password confirmation tidak boleh kosong !");
        document.form.confirmPassword.focus();
        return false; 
    }

    let email = document.form.email.value;
    if(email=="") { 
        alert("Email tidak boleh kosong !");
        document.form.email.focus();
        return false; 
    }

    let confirmEmail = document.form.confirmEmail.value;
    if(confirmEmail=="") { 
        alert("Email confirmation tidak boleh kosong !");
        document.form.confirmEmail.focus();
        return false; 
    }

    if(password != confirmPassword) {
        alert("Password tidak sama !");
        document.form.confirmPassword.focus();
        return false;
    }

    if(email != confirmEmail) {
        alert("Email tidak sama !");
        document.form.confirmEmail.focus();
        return false;
    }
}