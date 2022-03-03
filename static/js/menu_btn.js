function board_modify() {
    let this_url = location.href.split('/')
    let media_info = this_url[4]
    let queryString = $("#post_id").text()
    document.location.href = '/commu/' + media_info + '/' + queryString + '/modify/'
}


function board_delete() {
    let result = confirm('정말 삭제할까요?')
    if (result) {
        let this_url = location.href.split('/')
        let media_info = this_url[4]
        let queryString = $('#post_id').text()

        document.location.href = '/commu/' + media_info + '/' + queryString + '/delete/'
    }
}

function make_comment() {
    let this_url = location.href.split('/')
    let media_info = this_url[4]
    let queryString = $('#post_id').text()
    $.ajax({
        async: true,
        url: '/commu/' + media_info + '/' + queryString + '/comment',
        type: 'GET',
        data: {
            c_board_id: $('#post_id').text(),
            comment_author: $('#now_login_id').val(),
            comment_content: $('#c_content').val()
        },
        dataType: 'json',
        timeout: 3000,
        success: function (result) {
            alert('성공')
         },
        error: function () {
            alert('/commu/' + media_info + '/' + queryString + '/comment')
            alert(" 오류 ")
        }
    })
}
