// function getParameter(name) {
//     name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
//     let regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
//         results = regex.exec(location.search);
//     return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
// }

function new_board() {
    let this_url = location.href.split('/')
    let media_info = this_url[4]
    if($('#now_login_id').text() == "AnonymousUser"){
        alert('로그인이 필요한 서비스 입니다.')
        document.location.href='/user/login/'
    }else{

        document.location.href = '/commu/' + media_info + '/create/'
    }

}


$(function () {
    let TMDB_key = "be76d11dead7090637c1dd4cc5e4aa4c"
    let img_url = "https://image.tmdb.org/t/p/original"
    let this_url = location.href.split('/')
    let media_info = this_url[4].split('-')
    let media_id = media_info[0]
    let category = media_info[1]

    if(category == 'movie'){
         $.ajax({
        async: true,
        url: "https://api.themoviedb.org/3/movie/" + media_id,
        data: {
            api_key: TMDB_key,
            language: "ko"
        },
        success: function (result) {
            if (result["success"] == false) {
                console.log(typeof result["success"])
                //tv ajax호출

            } else {
                let img = result["poster_path"]
                let title = result["title"]
                let date = result["release_date"]
                let rating = result["vote_average"]
                let overview = result["overview"]

                if (img != null) {
                    $('#poster_img').attr('src', img_url + img)
                }
                $('#media_title').text(title)
                $('#date').text('개봉일 : ' + date)
                $('#rating').text('평점 : ' + rating)
                $('#overview').text(overview)
            }
        },
        error: function () {
            alert('영화 정보를 불러오지 못했습니다.')
        }
    })
    }

    else {
        $.ajax({
        async: true,
        url: "https://api.themoviedb.org/3/tv/" + media_id,
        data: {
            api_key: TMDB_key,
            language: "ko"
        },
        success: function (result) {
            let img = result["poster_path"]
            let title = result["name"]
            let date = result["first_air_date"]
            let rating = result["vote_average"]
            let overview = result["overview"]

            if (img != null) {
                $('#poster_img').attr('src', img_url + img)
            }
            $('#media_title').text(title)
            $('#date').text('방영시작일 : ' + date)
            $('#rating').text('평점 : ' + rating)
            $('#overview').text(overview)
        },
        error: function () {
            alert('TV 정보를 불러오지 못했습니다.')
        }
    })
    }


})