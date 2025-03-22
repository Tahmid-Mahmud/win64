l=localStorage
l.setItem("tpass", "fm2020b");

function login(){
    user=document.getElementById("user").value
    pass=document.getElementById("pass").value
    fm=l.getItem("tpass");
    if (user=="TEACHER" && pass==fm){
        console.log("2")
    }
    else if (user=="CADET" && pass=="2120"){
        window.open("./profile.html")
    }else{
        console.log("00")
    }
}

function shide(thiis){
    pass=document.getElementById("pass");
    console.log(thiis.innerHTML)
    if (thiis.innerHTML=='show password') {
        thiis.innerHTML='hide password';
        pass.type='text';
    } else {
        thiis.innerHTML='show password';
        pass.type='password';
    }
}
