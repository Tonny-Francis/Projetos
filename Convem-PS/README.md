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
  a mesma támbem faz uso da função getAll() a qual faz uma requisição a API, que utiliza funções que podem ser encontradas em services.
</p>
<h3>Função button_click()</h3>
<p>Essa função é responsável por chamar a API quando o usuário der um click, mas antes mesmo de chamar a API é feita uma verificação dos dados digitados, coso seja digitado a palavra "sim" não importa a formatação (é utilizado o método toLowerCase) é passada a string "sim" que complementa o endpoint da API que retorna uma mensagem (sucesso) e qualquer palavra diferente de "sim" e passada a string "nao" para o endpoint e retorna (erro). Ainda existe uma verificação caso a mensagem da API difira da esperada, a qual retorna um erro "Erro Database"</p>
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
<h3>API</h3>
<p>Na parte da API temos endpoints que correspondem as repostas "sim" e "nao", a função a cima e que determina em qual endpoint vai fazer a requisição, os endpoints são:
  <ul>
    <li>https://633f2d4c0dbc3309f3c64f7d.mockapi.io/api/v1/sim</li>
    <li>https://633f2d4c0dbc3309f3c64f7d.mockapi.io/api/v1/nao</li>
  </ul>
  Como podem verificar a primeira tem uma resposta "sucesso" e a outra "erro"
</p>
<h2>Detalhes da Pasta Back-end</h2>
<p>Os arquivos encontrados nessa pasta referir-se a construção de uma API própria, mas recebi erro de cors ao obter a reposta da API é como estava sem tempo de dar continuidade optei por utilizar o MockAPI, esses arquivos não encontram-se em utilização no site Convem-PS mas ainda está hospeda. Os erros estão relacionados ao endereço de acesso, o serviço que atualmente hospeda essa API é o Heroku e seus endpoints são:
  <ul>
    <li>https://convemapi.herokuapp.com/sim</li>
    <li>https://convemapi.herokuapp.com/nao</li>
  </ul>
  </p>
