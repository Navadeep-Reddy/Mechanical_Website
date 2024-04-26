buttonEL = document.querySelector("#button-el");
userEl = document.querySelector("#user-el")
passEl = document.querySelector("#pass-el")

buttonEL.addEventListener("click", function(){
    console.log(userEl.value)
    console.log(passEl.value)
});