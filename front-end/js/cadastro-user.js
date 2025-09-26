const url = 'http://127.0.0.1:5000/users'

async function cadastroUser(){

    let nome = document.getElementById('nome').value
    let email = document.getElementById('email').value
    let phone = document.getElementById('phone').value
    let senha = document.getElementById('senha').value

    let api = await fetch(url,{
        method:"POST",
        body:JSON.stringify(
            {
                "nome":nome,
                "email":email,
                "phone":phone,
                "senha":senha
            }
        ),
        headers:{
            'Content-Type':'application/json'
        }
    })

    if(api.ok){
        let resposta = await api.json();
        console.log(resposta)
        alert('Cadastro Realizado!')
        window.location.href = "login-user.html"
        return
    }

    let respostaErro =  await api.json();
    console.log(respostaErro)

}