// var button = document.getElementsByTagName("button")[0];
// //button is an array
// button.addEventListener("click", function(){
//     console.log("CLICK!!!!");
// })

var button = document.getElementById("enter");
var input = document.getElementById("userInput");
var ul = document.querySelector("ul");

function inputLength(){
    return input.value.length;
}

function createListElement(){
    var li = document.createElement("li");
    li.appendChild(document.createTextNode(input.value));
    ul.appendChild(li);
    input.value = "";
}

function addListAfterClick(){
    if(inputLength() > 0){
        createListElement();
    }
}

function addListAfterKeypress(event){
    if(inputLength() > 0 && event.keyCode === 13){
        createListElement();
    }
}

//Callback Functions: When that line of javascript runs, we don't want
// the addListAfterClick function to run because we're adding the event
//listener now to wait for click or keypress
//We're passing a reference to the function without running it
button.addEventListener("click", addListAfterClick);

input.addEventListener("keypress", addListAfterKeypress);