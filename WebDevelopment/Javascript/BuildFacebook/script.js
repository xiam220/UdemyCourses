var database = [
    {
        username: "melanie.xia",
        password: "supersecret"
    },
    {
        username: "sally",
        password: "123"
    },
    {
        username: "ingrid",
        password: "777"
    }
];

var newsFeed = [
    {
        username: "john.doe",
        timeline: "So tired from all that learning"
    },
    {
        username: "jane.doe",
        timeline: "Javascript is so cool!"
    },
    {
        username: "who.knows",
        timeline: "I don't anymore"
    }
];

function isUserValid(username, password){
    for(var i = 0; i < database.length; i++){
        if(database[i].username === username && database[i].password === password){
            return true;
        } 
    }
    return false;
}

function signIn(username, password){
    if(isUserValid(username, password)){
        console.log(newsFeed);
    } else{
        alert("Sorry, wrong username and password");
    }
}

var usernamePrompt = prompt("What's your username?");
var passwordPrompt = prompt("What's your password?");

signIn(usernamePrompt, passwordPrompt);
// function signIn(username, password){
//     if(username === database[0].username && password === database[0].password){
//         console.log(newsFeed);
//     } else {
//         alert("Sorry, wrong username and password");
//     }
// }