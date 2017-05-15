var valueNum = 0;

document.addEventListener('DOMContentLoaded', ReadCookie, false);

document.addEventListener('click', play, false);
document.addEventListener('click', play2, false);
document.addEventListener('click', play3, false);

 function play(){
    choice = document.getElementById('rock');
    choice.addEventListener('click', final_result1, false);
}

function play2(){
    choice = document.getElementById('paper');
    choice.addEventListener('click', final_result2, false);
}

function play3(){
    choice = document.getElementById('scissors');
    choice.addEventListener('click', final_result3, false);
}
 
// This function is an edited version of the one found at  http://www.tutorialspoint.com/javascript/javascript_cookies.htm
 function ReadCookie(){
    var Welcome = document.cookie;
    cookiearray = Welcome.split(';'); 
    for(var i=0; i<cookiearray.length; i++){
        value = cookiearray[i].split('=')[1];
        valueNum = parseInt(value,10);
        if(valueNum < 5){
            document.getElementById('outcome').innerHTML = "Go Away!";
        }
    }
}

function final_result1(){ 
    var computer = Math.floor((Math.random() * 3) + 1);

        if(computer === 1 && valueNum > 4){
            document.getElementById('outcome').innerHTML = "It's a tie ";
        }if(computer === 2 && valueNum > 4){
            document.getElementById('outcome').innerHTML = "Rock LOSES to Paper";
        }if(computer === 3 && valueNum > 4){
            document.getElementById('outcome').innerHTML = "Rock BEATS Scissors";
        }
   
    event.preventDefault();
}

function final_result2(){
    var computer = Math.floor((Math.random() * 3) + 1);
    
        if(computer === 1 && valueNum > 4){
            document.getElementById('outcome').innerHTML = "Paper BEATS Rock";
        }else if(computer === 2 && valueNum > 4){
            document.getElementById('outcome').innerHTML = "Its a tie!";
        }else if(computer === 3 && valueNum > 4){
            document.getElementById('outcome').innerHTML = "Paper LOSES to Scissors";
        }
    
    event.preventDefault();
}

function final_result3(){
    var computer = Math.floor((Math.random() * 3) + 1);
   
        if(computer === 1 && valueNum > 4){
            document.getElementById('outcome').innerHTML = "Scissors LOSES to Rock";
        }else if(computer === 2 && valueNum > 4){
            document.getElementById('outcome').innerHTML = "Scissors BEATS Paper";
        }else if(computer === 3 && valueNum > 4){
            document.getElementById('outcome').innerHTML = "It's a tie!";
        }

   event.preventDefault();
}