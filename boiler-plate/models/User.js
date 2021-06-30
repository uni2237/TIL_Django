const mongoose = require('mongoose');

const userSchema = mongoose.Schema({
    name:{
        type:String,
        maxlength:50
        
    },
    email:{
        type:String,
        trin: true, // 중간에 공백있으면 없애줌
        unique: 1
    },
    password:{
        type:String,
        maxlength:5
    },
    lastname:{
        type:String,
        maxlength:50
    },
    role:{
        type: Number,
        default: 0
    },
    image: String, // 이렇게 그냥 한줄이면 {} 안써도 됨 
    token:{
        type:String
    },
    tokenExp:{ // token 사용가능한 유효기간
        type:Number
    }
})

const User = mongoose.model('User',userSchema)

module.exports={ User }//모델을 다른 파일에서도 쓸수 있도록 User를 export 해줌 