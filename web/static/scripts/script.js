$(document).on("submit", "form", function (e) {
    var oForm = $(this);
    var formId = oForm.attr("id");
    if (formId == "add_folder") {
        var post_url = '/submit_folder';
        $.ajax({
            type:'POST',
            url:post_url,
            data:{
              new_folder:$("#new_folder").val(),
            },
            success:function()
            {
                location.reload();
            }
        })
    }
    return false;
})

function submit_add() {
    var post_url = '/submit_add';
        $.ajax({
            type:'POST',
            url:post_url,
            data:{
              new_task:$("#new_task").val(),
              task_folder:$("#select_folder :selected").attr('id'),
            },
            success:function()
            {
                location.reload();
            }
        })
    return false;
}

function delete_task(id_task) {
    var post_url = '/submit_delete';
    $.ajax({
        type:'POST',
        url:post_url,
        data:{
            task_id:id_task,
        },
        success:function()
        {
            window.location.reload();
        }
    })
    return false;
}

function display_edit(id) {
    id = "#" + id;
    if ($(id).hasClass("hide")) {
        $(id).removeClass("hide");
    }
    else {
        $(id).addClass("hide");
    }
}

function edit_task(id_task){
    console.log(id_task);
    var post_url = '/submit_edit';
    var new_task = "#new_edit" + id_task;
    $.ajax({
        type:'POST',
        url:post_url,
        data:{
            task_id:id_task,
            new_task:$(new_task).val(),
        },
        success:function()
        {
            location.reload();
        }
    })
}

function show_folder(id_folder) {
    var folder = "#todo_" + id_folder;
    if ($(folder).hasClass("no_visible")) {
        $(folder).removeClass("no_visible");
    } else {
        $(folder).addClass("no_visible");
    }
}

function delete_folder(id_folder) {
    var post_url = '/delete_folder';
    $.ajax({
        type:'POST',
        url:post_url,
        data:{
            folder_id:id_folder,
        },
        success:function()
        {
            location.reload();
        }
    })
}