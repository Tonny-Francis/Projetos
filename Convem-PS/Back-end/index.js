//Configuração Inicial
const express = require('express')

const server = express()
const port = process.env.PORT || 3000

server.use(express.json())

//Confuguração para evitar erro CORS
server.use((req, res, next) =>{
    res.header('Access-Control-Allow-Credentials', 'true')
    res.header('Access-Control-Allow-Origin', '*')
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept, Authorization')
    res.header('Access-Control-Max-Age', '86400')
    
    if(req.method === 'OPTIONS'){
        res.header('Access-Control-Allow-Methods', 'PUT, POST, PATCH, DELETE, GET')
    }
    next()
})

//Rotas
server.post('/answer', async (req, res) => {
    const { answer } = req.body

    if(!answer){
        res.status(422).json({answer: 'A resposta é obrigatória'})
        return
    }
    else if(answer === 'sim'){
        res.status(200).json({answer: 'Sucesso'})
        return
    }
    else{
        res.status(200).json({answer: 'Erro'})
        return
    }
})

server.listen(port)