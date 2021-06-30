const express = require('express') //express module 가져옴
const app = express() // 새로운 express app을 만듦 
const port = 5000

const mongoose = require('mongoose')
mongoose.connect('mongodb+srv://choyunhui:jyh980403@boilerplate.6dflk.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', {
    useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true, useFindAndModify: false
}).then(() => console.log('MongoDB Connected...'))
  .catch(err => console.log(err))

app.get('/', (req, res) => {
  res.send('Hello World!~~안녕하세요~')
}) //app이 루트 디렉토리에 오면 hello world 출력

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
}) // port 5000번에서 app 실행