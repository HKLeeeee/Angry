function board_modify() {
    let queryString = $("#post_id").text()
    let media_id = $("#media_id").text()
    document.location.href = '/commu/' + media_id + '/' + queryString + '/modify/'
}

function like_post(id) {

}

function board_delete() {
    let result = confirm('정말 삭제할까요?')
    if (result) {
        let queryString = $('#post_id').text()
        let media_id = $("#media_id").text()
        document.location.href = '/commu/' + media_id + '/' + queryString + '/delete/'
    }
}


function creat_comment() {
    $.ajax({
        async: true,
        url: "",
        type: 'GET',
        data: {
            board_id: $('#11').text(),
            comment_content: $('#11').val()
        },
        dataType: 'json',
        timeout: 3000,
        success: function (result) {
            alert('성공')
        },
        error: function () {
            alert("어디서 오류 ")
        }


    })
}