function login() {
  let u = document.getElementById("user").value;
  let p = document.getElementById("pass").value;

  if (u === "admin" && p === "admin") {
    document.getElementById("msg").innerText = "Login Success";
  } else {
    document.getElementById("msg").innerText = "Invalid Credentials";
  }
}
