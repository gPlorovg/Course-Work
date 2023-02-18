// TODO: неработает ввод отрицательных чисел!!!

var a = document.getElementById('inp1');
var b = document.getElementById('inp2');
var action = document.getElementById('action');
var dig = document.getElementById('digit');

// var answer = document.createDocumentFragment('div');
// answer.className = "answer";
// answer.innerHTML = "answertext";
var answer = document.createElement('div');
answer.className = "answer";

var alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';


function send_to_server(a,b,action,dig){
    let req = {
        num1: a.value,
        num2: b.value,
        action: action.value,
        dig: dig.value
    };
    fetch('http://127.0.0.1:5000/calculate', {
        method: 'POST',
        headers: new Headers({
            'content-type': 'application/json;charset=utf-8'
        }),
        body: JSON.stringify(req)
    }).then(function (resp){
        if (resp.status != 200) {
            console.log("Response Error Status: " + resp.status);
            return ;
        }
        resp.json().then(function (data) {
            show_rez(a,b,dig,action,data.rez);
        })
    });
}

function inp_err(inp){
    inp.style.border = "2px solid #E5BE01";
};

function inp_right(inp){
    inp.style.border = "1px solid #DBDBDB";
};

function inp_dig(inp){
    if(Number(inp.value) < 2 || Number(inp.value) > 36 || isNaN(Number(inp.value))){
        inp_err(inp);
        return 0;
    }
    else{
        inp_right(inp);
        return 1;
    }
}

function inp_num(inp, dig){
    // console.log('[^('+alphabet.slice(0,dig.value)+')]');
    var re = new RegExp('[^('+alphabet.slice(0,dig.value)+')]','gi');
    if(inp.value.length == 0 || inp.value.match(re)){
        inp_err(inp);
        return 0;
    } 
    else {
        inp_right(inp);
        return 1;
    };
}

function show_rez(a,b,dig,action,rez){
    answer.innerHTML = a.value+'<span>'+dig.value+'</span>'+' '+action.value+' '+b.value+'<span>'+dig.value+'</span>'+' = '+ rez+'<span>'+dig.value+'</span>';
    document.body.append(answer);
}
document.getElementById('culcbut').onclick = function() {
    a.value = document.getElementById('inp1').value;
    b.value = document.getElementById('inp2').value;
    action.value = document.getElementById('action').value;
    dig.value = document.getElementById('digit').value;
    // inp_err(dig);

    

    if(inp_dig(dig) + inp_num(a,dig) + inp_num(b,dig) == 3)
        send_to_server(a,b,action,dig);
};