// Создание элементов страницы
var a = document.getElementById('inp1');
var b = document.getElementById('inp2');
var action = document.getElementById('action');
var dig = document.getElementById('digit');
// Создание элемента ответа
var answer = document.createElement('div');
answer.className = "answer";
// Допустимый ввод
var alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';

// Отправка запроса для вычисления на сервер
function send_to_server(a,b,action,dig){
    let req = {
        num1: a.value,
        num2: b.value,
        action: action.value,
        dig: dig.value
    };
    fetch(window.location+'/calculate', {
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
            show_rez_dec(data.rez_dec[0], data.rez_dec[1], data.rez_dec[2], action);
        })
    });
}
// Обработка некорректного ввода
function inp_err(inp){
    inp.style.border = "2px solid #E5BE01";
};
// Обработка корректного ввода
function inp_right(inp){
    inp.style.border = "1px solid #DBDBDB";
};
// Обработка ввода степени
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
// Обработка ввода числа
function inp_num(inp, dig){
    // console.log('[^('+alphabet.slice(0,dig.value)+')]');
    var re = new RegExp('(?!^-)(?!['+alphabet.slice(0,dig.value)+'])','gi');

    if(inp.value.length == 0 || inp.value.length > 50 || (inp.value.match(re).length - 1)){
        inp_err(inp);
        return 0;
    } 
    else {
        inp_right(inp);
        return 1;
    };
}
// Вывод ответа
function show_rez(a,b,dig,action,rez){
    answer.innerHTML = a.value+'<span>'+dig.value+'</span>'+' '+action.value+' '+b.value+'<span>'+dig.value+'</span>'
        +' = '+ rez+'<span>'+dig.value+'</span>';
    document.body.append(answer);
}

function show_rez_dec(a, b, rez, action, dig = 10){
    answer.innerHTML = a.value+'<span>'+dig.value+'</span>'+' '+action.value+' '+b.value+'<span>'+dig.value+'</span>'
        +' = '+ rez+'<span>'+dig.value+'</span>';
    document.body.append(answer);
}

document.getElementById('culcbut').onclick = function() {
    a.value = document.getElementById('inp1').value;
    b.value = document.getElementById('inp2').value;
    action.value = document.getElementById('action').value;
    dig.value = document.getElementById('digit').value;

    if(inp_dig(dig) + inp_num(a,dig) + inp_num(b,dig) == 3)
        send_to_server(a,b,action,dig);
};