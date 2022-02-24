function new_board(){
    document.location.href='/commu/create/'
}
function board_modify(){
    let queryString =$("#post_id").text()
    document.location.href='/commu/'+queryString+'/modify/'
}
// function board_update(){
//     let queryString=$("#post_id").text()
//     document.location.href='/commu/'+queryString+'/update/'
// }
    let my_search ='관상'
    $.ajax({
        async:true,
        url:"https://api.themoviedb.org/3/search/movie?api_key=be76d11dead7090637c1dd4cc5e4aa4c&language=ko-KR&page=1&include_adult=false",
        data :{
            query:my_search
        },
        success:function (result){
            $('#movie_poster').empty()
            let posterTr=$('<tr></tr>')
            let posterTd=$('<td></td>')
            let poster=$('<img/>')
            posterTd.append(poster)
            let imgurl="https://www.themoviedb.org/t/p/original"+result['results'][0]['poster_path']
            poster.attr('src',imgurl)
            $(poster).css('height',350)
            $(poster).css('width',300)
            posterTr.append(posterTd)
            $('#movie_poster').append(posterTr)
            $('#titleoverview').empty()
            let hh=$('<h2></h2>').text(result['results'][0]['title'])
            let tr =$('<tr></tr>')
            let contentTd =$('<td></td>').text(result['results'][0]['overview'])
            tr.append(contentTd)
            $('#titleoverview').append(hh)
            $('#titleoverview').append(tr)
        },
        error:function (){
            alert('오류')
        }
    })
