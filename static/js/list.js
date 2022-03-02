function new_board(media_id) {
    document.location.href = '/commu/' + media_id + '/create/'
}

function getParameter(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    let regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

$(function () {
    let category = getParameter("category")
    let TMDB_key = "be76d11dead7090637c1dd4cc5e4aa4c"
    let img_url = "https://image.tmdb.org/t/p/original"

    let this_url = location.href.split('/')
    let media_id = this_url[4]

    $.ajax({
        async: true,
        url: "https://api.themoviedb.org/3/"+category+"/"+media_id,
        data : {
            api_key : TMDB_key,
            language : "ko"
        },
        success: function (result) {
            console.log(location.href)
            let img = result["poster_path"]
            let title = ""
            let date = ""
            if(category == "movie"){
                title = result["title"]
                date= result["release_date"]
            }else {
                title = result["name"]
                date = result["first_air_date"]
            }

            let rating= result["vote_average"]
            let overview=result["overview"]

            if (img != null){
                $('#poster_img').attr('src', img_url+img)
            }
            $('#media_title').text(title)
            if(category=='movie'){
                $('#date').text('개봉일 : '+date)
            }else{
                $('#date').text('방영시작일 : '+date)
            }
            $('#rating').text('평점 : '+rating)
            $('#overview').text(overview)
        },
        error: function () {
            alert('정보를 불러오지 못했습니다.')
        }
    })

})