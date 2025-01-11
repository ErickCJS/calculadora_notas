document.getElementById('icono_ver').addEventListener('click', () =>{
    ver_nover();
})

function ver_nover(){
    let password = document.getElementById('password');
    let icon = document.getElementById('icono_ver');

    if(password.type == "password"){
        password.type = "text";
        icon.innerHTML = `
            <i class="bi bi-eye-slash-fill text-white"></i>
        `;
        icon.style.background = "#fe6d20";
        
    }else{
        password.type = "password";
        icon.innerHTML = `
        <i class="bi bi-eye-fill text-white"></i>`;
        icon.style.background = "#878787";
    
    }


}