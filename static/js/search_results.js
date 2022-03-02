function getParameter(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    let regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

$(function () {
    let TMDB_key = "2ea03f51befa185a18aff32033bbf3f4"
    let img_url = "https://image.tmdb.org/t/p/original"
    let opt = getParameter("option")
    let kw = getParameter("keyword")
    if (opt == "Movie"){
        $("#category option:eq(0)").attr("selected", "selected");
    }else{
        $("#category option:eq(1)").attr("selected", "selected");
    }
    $("[name='keyword']").val(kw)

    if(opt == "Movie"){
        $.ajax({
            url : 'https://api.themoviedb.org/3/search/movie',
            data : {
                api_key : TMDB_key,
                language : 'ko-KR',
                query : kw
            },
            method : 'GET',
            timeout : 5000,
            dataType : 'json',
            success : function (result){
                $('#result_container').empty()
                let search_result = result['results']
                for(let i = 0; i<search_result.length; i++){
                    let title = search_result[i]['title']
                    let media_id = search_result[i]['id']
                    let release_date = search_result[i]["release_date"]
                    let img = img_url + search_result[i]["poster_path"]
                    if(search_result[i]["poster_path"] == null){
                        img = "/static/img/No-Image-Available.jpg"
                    }
                    let overview = search_result[i]["overview"]

                    let list_container = $('<div></div>').addClass("d-flex align-items-start align-items-center my-1 px-1 border border-secondary rounded")
                    list_container.on('mouseenter', e => {
                        list_container.addClass("border-dark border-3")
                    })
                    list_container.on('mouseleave', e => {
                        list_container.removeClass("border-dark border-3")
                    })
                    list_container.on('click', function (){
                        go_to_commu_board(title, media_id, "movie")
                    })
                    let poster_div = $('<div></div>').addClass("m-0 align-items-center poster-div")
                    let poster_img = $('<img />').addClass("align-self-center poster")
                    poster_img.attr('src', img).attr('alt', title+"포스터")
                    poster_div.append(poster_img)

                    let info_div = $('<div></div>').addClass("d-flex flex-column flex-fill align-items-start justify-content-start my-1 mx-3 overview-div")
                    let title_div = $('<div></div>').addClass("my-3 fs-4 font-weight-bold").text(title)
                    let date_div = $('<div></div>').addClass("my-1").text("개봉일 : "+release_date)
                    let overview_div = $('<div></div>').addClass("my-1 overview-box").text(overview)
                    info_div.append(title_div)
                    info_div.append(date_div)
                    info_div.append(overview_div)

                    list_container.append(poster_div)
                    list_container.append(info_div)

                    $("#result_container").append(list_container)
                }
            },
            error : function (){
                alert('정보를 불러오는데 실패했습니다.')
            }
        })
    }
    else{
        $.ajax({
            url : 'https://api.themoviedb.org/3/search/tv',
            data : {
                api_key : TMDB_key,
                language : 'ko-KR',
                query : kw
            },
            method : 'GET',
            timeout : 5000,
            dataType : 'json',
            success : function (result){
                $('#result_container').empty()
                let search_result = result['results']
                for(let i = 0; i<search_result.length; i++){
                    let title = search_result[i]['name']
                    let media_id = search_result[i]['id']
                    let first_air_date = search_result[i]["first_air_date"]
                    let img = img_url + search_result[i]["poster_path"]
                    if(search_result[i]["poster_path"] == null){
                        img = "/static/img/No-Image-Available.jpg"
                    }
                    let overview = search_result[i]["overview"]

                    let list_container = $('<div></div>').addClass("d-flex align-items-start align-items-center my-1 px-1 border border-secondary rounded")
                    list_container.on('mouseenter', e => {
                        list_container.addClass("border-dark border-3")
                    })
                    list_container.on('mouseleave', e => {
                        list_container.removeClass("border-dark border-3")
                    })
                    list_container.on('click', function (){
                        go_to_commu_board(title, media_id, "tv")
                    })
                    let poster_div = $('<div></div>').addClass("m-0 align-items-center poster-div")
                    let poster_img = $('<img />').addClass("align-self-center poster")
                    poster_img.attr('src', img).attr('alt', title+"포스터")
                    poster_div.append(poster_img)

                    let info_div = $('<div></div>').addClass("d-flex flex-column flex-fill align-items-start justify-content-start my-1 mx-3 overview-div")
                    let title_div = $('<div></div>').addClass("my-3 fs-4 font-weight-bold").text(title)
                    let date_div = $('<div></div>').addClass("my-1").text("방영일 : "+first_air_date)
                    let overview_div = $('<div></div>').addClass("my-1 overview-box").text(overview)
                    info_div.append(title_div)
                    info_div.append(date_div)
                    info_div.append(overview_div)

                    list_container.append(poster_div)
                    list_container.append(info_div)

                    $("#result_container").append(list_container)
                }

            },
            error : function (){
                alert('정보를 불러오는데 실패했습니다.')
            }
        })
    }
})

function go_to_commu_board(title, id, category){
    document.location.href = '/commu/'+id+'/list/?title='+title+"&category="+category
}