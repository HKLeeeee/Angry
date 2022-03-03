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
    //alert('/commu/' + media_info + '/' + queryString + '/comment')
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
            let tr = $('<tr></tr>').attr('id', 'comment_'+result['c_id'])
            let author_td = $('<td></td>').text(result['c_author'])
            tr.append(author_td)

            let content_td = $('<td></td>').text(result['c_content'])
            tr.append(content_td)

            let button_td = $('<td></td>')
            let button = $('<button></button>').addClass("btn btn-secondary btn-sm").text('Delete')
            button_td.on('click', function () {
                delete_comment(result['c_id'])
            })
            button_td.append(button)
            tr.append(button_td)

            $('#comment_container').prepend(tr)
        },
        error: function () {
            alert("댓글 등록에 실패했습니다.")
        }
    })
}

function delete_comment(comment_id) {
    let ask = confirm('이 댓글을 삭제할까요?')
    if (ask) {
        $.ajax({
        async: true,
        url: '/commu/commentDelete/',
        type: 'GET',
        data: {
            comment_id: comment_id
        },
        dataType: 'json',
        timeout: 3000,
        success: function (result) {
            $('#comment_' + result['c_id']).remove()
        },
        error: function () {
            alert('댓글 삭제 실패')
        }
    })
    }

}