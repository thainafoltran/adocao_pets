const url = 'http://127.0.0.1:5000/pets'

async function cadastroPet(){

    let nome = document.getElementById('nome').value
    let especie = document.getElementById('especie').value
    let localizacao = document.getElementById('localizacao').value
    let idade = document.getElementById('idade').value

    let api = await fetch(url,{
        method:"POST",
        body:JSON.stringify(
            {
                "nome":nome,
                "especie":especie,
                "localizacao":localizacao,
                "idade":idade
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
        return
    }

    let respostaErro =  await api.json();
    console.log(respostaErro)

}