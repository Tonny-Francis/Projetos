<h1 align="Center">Convem PS</h1>
<p align="center">
<img src="https://img.shields.io/badge/STATUS-FINALIZADO-red"/>
</p>
<h2>Objetivo</h2>
<p>O intuito dessa aplicação é criar uma página web onde o usuário possa responder uma 
pergunta simples e dependendo da sua resposta realizar uma ação, utilizando o framework Angular e uma API.
</p>
<ul>
  Aplicações utilizadas no deploy e API
  <li>
    <a href="https://convem-ps.vercel.app/" target="_blank">Vercel</a>
  </li>
  <li>MockAPI</li>
</ul>
<h2>Estrutura do Site</h2>
<img src="https://github.com/Tonny-Francis/Projetos/blob/main/Convem-PS/Front-end/images/Hierarquia.png" width="500px">
<h2>Detalhes de Lógica</h2>
<p>
  Vale deixar um adendo, um pedaço da lógica que filtra a informação vinda do endpoint é feita no front-end na função do button_click(), 
  a mesma támbem faz uso da função getAll() a qual faz uma requisição a API.
</p>
<p>Função button_click()</p>
<code>
  <pre>
  button_click(){
    if(this.value.toLowerCase() == 'sim'){
      this.getData('sim')
      setTimeout(() => {
        for(let answer of this.interface){
          if(answer.answer == 'sucesso')
            this.openDialog()
          else
            alert('Erro Database')
        }
      }, 1000);
    }
    else{
      this.getData('nao')
      setTimeout(() => {
        for(let answer of this.interface){
          if(answer.answer == 'erro')
            alert('Erro')
          else
            alert('Erro Database')
        }
      }, 1000);
    }

  }
  </pre>
</code>
