function load_failed(){
    $('#ranking_container').text('데이터를 불러오지 못했습니다.')
}


//document ready
$(function() {
    let TMDB_key = "2ea03f51befa185a18aff32033bbf3f4"
    let img_url = "https://image.tmdb.org/t/p/original"

    /*
     *
     * week's top 5 movie
     *
     */
    $.ajax({
        url : "https://api.themoviedb.org/3/trending/movie/week",
        data : {
            api_key : TMDB_key
        },
        method : 'GET',
        timeout : 5000,
        dateType : 'json',
        success : function (result){
            // alert('STEP 1 성공')
            //영화 상위 5개의 id를 받아서 리스트에 저장
            let top5_movie = []
            let top5_movie_en_poster_path = []
            let top5_movie_title = []
            for(let i = 0; i<5; i++){
                top5_movie.push(
                    result['results'][i]['id']
                )

                top5_movie_en_poster_path.push(
                    result['results'][i]["poster_path"]
                )
                top5_movie_title.push(
                    result['results'][i]['title']
                )
            }

            //받은 5개의 영화id를 이용해서 한국어 포스터 이미지 찾기
            for(let i = 0; i<5; i++){
                $.ajax({
                url : "https://api.themoviedb.org/3/movie/"+top5_movie[i].toString()+"/images",
                data : {
                    api_key: TMDB_key,
                    include_image_language : "ko"
                },
                method: "GET",
                dateType: "json",
                success : function (result){
                    //alert("STEP 2 성공")
                    //찾은 영화포스터이미지, id 이용해서 html에 그리기
                    try{
                        let poster_path = result["posters"][0]["file_path"]
                        $('#mov_'+i).attr("src", img_url+poster_path)
                    }catch (e){
                        // console.error(i +"번째 작품의 한글 포스터가 없음.")
                        $('#mov_'+i).attr("src", img_url+top5_movie_en_poster_path[i])
                    }

                    let queryString = "?title="+top5_movie_title[i]
                    $('#mov_'+i).on("click", function (){
                        document.location.href = "commu/"+top5_movie[i]+"-movie/list"+queryString
                    })
                    $('#mov_'+i).on("mouseenter", function (){
                        $('#mov_'+i).addClass("focused")
                    })
                    $('#mov_'+i).on("mouseleave", function (){
                        $('#mov_'+i).removeClass("focused")
                    })

                },
                error : function (){
                    load_failed()
                }
                })
            }
        },
        error : function (){
            load_failed()
        }
  })


    /*
     *
     * week's top 5 tv program
     *
     */
    $.ajax({
        url : "https://api.themoviedb.org/3/trending/tv/week",
        data : {
            api_key : TMDB_key
        },
        method : 'GET',
        timeout : 5000,
        dateType : 'json',
        success : function (result){
            // alert('STEP 1 성공')
            //tv 상위 5개의 id를 받아서 리스트에 저장
            let top5_tv = []
            let top5_tv_en_poster_path = []
            let top5_tv_title = []
            for(let i = 0; i<5; i++){
                top5_tv.push(
                    result['results'][i]['id']
                )
                top5_tv_en_poster_path.push(
                    result['results'][i]["poster_path"]
                )
                top5_tv_title.push(
                    result['results'][i]['name']
                )
            }
            //받은 5개의 tv id를 이용해서 한국어 포스터 이미지 찾기

            for(let i = 0; i<5; i++){
                $.ajax({
                url : "https://api.themoviedb.org/3/tv/"+top5_tv[i].toString()+"/images",
                data : {
                    api_key: TMDB_key,
                    include_image_language : "ko"
                },
                method: "GET",
                dateType: "json",
                success : function (result){
                    //alert("STEP 2 성공")
                    //찾은 tv 포스터이미지, id 이용해서 html에 그리기
                    try{
                        let poster_path = result["posters"][0]["file_path"]
                        $('#tv_'+i).attr("src", img_url+poster_path)
                    }catch (e){
                        // console.error(i +"번째 작품의 한글 포스터가 없음.")
                        $('#tv_'+i).attr("src", img_url+top5_tv_en_poster_path[i])
                    }
                    let queryString = "?title="+top5_tv_title[i]
                    $('#tv_'+i).parent().on("click", function (){
                        document.location.href = "commu/"+top5_tv[i]+"-tv/list"+queryString
                    })
                    $('#tv_'+i).on("mouseenter", function (){
                        $('#tv_'+i).addClass("focused")
                    })
                    $('#tv_'+i).on("mouseleave", function (){
                        $('#tv_'+i).removeClass("focused")
                    })
                },
                error : function (){
                    load_failed()
                }
            })
        }
        },
        error : function (){
            load_failed()
        }
    })
})