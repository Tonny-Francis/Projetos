//Configuração Inicial
const express = require('express')
const server = express()
const port = process.env.PORT

server.use((req, res) =>{
    res.header("Access-Control-Allow-Origin", "*")
    res.header("Access-Control-Allow-Methods", "GET")
    res.header("Access-Control-Allow-Methods", "GET, OPTIONS")
    res.header("Access-Control-Allow-Headers", "Content-Type, Content-Length, Accept-Encoding")
})
//Rotas
server.get('/sim', async (req, res) =>{
    res.status(200).json({answer: 'sucesso'})
})

server.get('/nao', async (req, res) =>{
    res.status(200).json({answer: 'erro'})
})

server.listen(port)