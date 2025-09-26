const url = 'http://127.0.0.1:5000/login'

async function loginUsuario(){
    let tela = document.querySelector('body')
    tela.style.cssText = 'cursor: wait';

    let email = document.getElementById('email').value
    let senha = document.getElementById('senha').value

    let api = await fetch(url,{
        method: "POST",
        body:JSON.stringify(
            {
                "email": email,
                "senha": senha,
                "user_type_id": 1
            }            
        ),
        headers:{
            'Content-Type':'application/json'
        }
    })

    let resposta = await api.json();

    if(api.ok){
        console.log(resposta)
        alert('Login Efetuado!')
        localStorage.setItem('user', JSON.stringify(resposta));
        window.location.href = "../index.html";
        return
    }
    
    alert(resposta.data.errors)
    tela.style.cssText = 'cursor: default'
}