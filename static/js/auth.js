function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch("/auth/login/", {
        method: "POST",
        body: new URLSearchParams({
            "username": username,
            "password": password,
        }),
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        if (data.success) location.reload();
    });
}

function logoutUser() {
    fetch("/auth/logout/", {
        method: "POST",
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message);
        if (data.success) location.reload();
    });
}
