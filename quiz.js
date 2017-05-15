var xmlhttp;
var result;
var format;
var names;
var score = 0;
var answered = 0;

document.addEventListener('DOMContentLoaded', final_result, false);

function init(event) {
	var tag_value = event.srcElement.value;
	var id = event.srcElement.id;
	names = event.srcElement.className;
	format = tag_value.split(' ').join('+');
    format = document.getElementById(tag_value);
    format.addEventListener('click', get_result(), false);
    result = document.getElementById(format.name);   
}

function get_result() {
	var number = format.name;
	var tag_value = format.value.split(' ').join('+');
    var url = 'compare.py?'+ number +'='+tag_value;
    xmlhttp = new XMLHttpRequest();
    xmlhttp.addEventListener('readystatechange', response_handle, false);
    xmlhttp.open('GET', url, true);
    xmlhttp.send(null);
}

function response_handle() {
    if (xmlhttp.readyState === 4) {
        if (xmlhttp.status === 200) {
            result.innerHTML = xmlhttp.responseText;
        }if (xmlhttp.responseText.trim() == 'Correct') {
            score ++;
            answered ++;
            result.style.color = 'green';
            document.getElementsByName(names)[0].disabled = true;
            document.getElementsByName(names)[1].disabled = true;
            document.getElementsByName(names)[2].disabled = true;
        }else if (xmlhttp.responseText.trim() == 'Incorrect') { 
            result.style.color = 'red';
            answered ++;
			document.getElementsByName(names)[0].disabled = true;
            document.getElementsByName(names)[1].disabled = true;
            document.getElementsByName(names)[2].disabled = true;
        }
    }
}

function final_result(){
    final_result = document.getElementById('final_result');
    final_result.addEventListener('click', totalResult, false);
}

function totalResult(){
    var total_questions = document.getElementsByClassName('results').length
	var percent = (score/total_questions)*100;
    document.getElementById("finalResult").innerHTML = "You got " +score+ " / " +total_questions+ " questions correct";
    if(answered < total_questions){
        document.getElementById("finalResult").innerHTML = "Please Answer All Questions";
    }
    else if(percent >= 70){
        document.getElementById("finalResult").innerHTML = "<figure><img src='images/SuccessKid.jpg' />" + "<figcaption>You got "  +score+  " / " +total_questions+ " questions correct</figcaption><figure>";
    }
	else if(percent >= 50 && percent < 70){
        document.getElementById("finalResult").innerHTML = "<figure><img src='images/not_good.jpg' />" + "<figcaption>You got "  +score+  " / " +total_questions+ " questions correct</figcaption><figure>";
	}
	else if(percent < 50){
        document.getElementById("finalResult").innerHTML = "<figure><img src='images/failure.jpg' />" + "<figcaption>You only got "  +score+  " / " +total_questions+ " questions correct</figcaption><figure>";
	}
    event.preventDefault();
}
