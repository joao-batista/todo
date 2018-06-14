function search() {
    post('task_search/')
}

function task_new() {
    post('task_new_ajax/')
}

function task_done(id) {
    post('task_done_ajax/', id)
}

function task_undo(id) {
    post('task_undo_ajax/', id)
}

function task_delete(id) {
    post('task_delete_ajax/', id)
}

function post(url, id) {
    var description = $('#description').val();
    var id = id || 0;

    $.ajax({
        headers     : { "X-CSRFToken": csrftoken },
        type        : 'POST', 
        url         : url,
        data        : { 'description' : description, 'id': id },
        dataType    : 'json',
        success     : function(results) {
            listar(results)
        }
    });
}

function listar(results) {
    var lista = "";
    var botoes = "";

    $.each(results, function(index, task) {

        var btn_done   = "<button class='btn btn-success' onclick='task_done(" + task.id + ")'><i class='fa fa-check'></i></button> "
        var btn_update = "<a class='btn btn-primary' href='task_update/" + task.id + "'><i class='fa fa-pencil'></i></a> "
        var btn_undo   = "<button class='btn btn-warning' onclick='task_undo("+ task.id + ")'><i class='fa fa-undo'></i></button> "
        var btn_delete = "<button class='btn btn-danger'  onclick='task_delete(" + task.id + ")'><i class='fa fa-trash-o'></i></button> "

        if(!task.done){
            botoes = btn_done.concat(btn_update)
        } else{
            botoes = btn_undo.concat(btn_delete)
        }

        lista += "<tr><td>" + task.description + "</td><td>" + botoes + "</td></tr>"
        
    });
    $('.table tbody').html(lista)

}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');