//Configuração Inicial
const express = require('express')
const server = express()
const port = process.env.PORT

//Rotas
server.get('/sim', async (req, res) =>{
    res.status(200).json({answer: 'sucesso'})
})

server.get('/nao', async (req, res) =>{
    res.status(200).json({answer: 'erro'})
})

server.listen(port)