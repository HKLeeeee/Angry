function k_login(email) {
    if (email == undefined) {
        Kakao.API.request({
            url: "/v1/user/unlink",
            success: function () {
                location.href = "/user/login/";
            },

            fail: function () {
                alert("오류");
            }
        });
        alert("카카오 이메일 가입 후 이메일 제공에 동의해야 사용 가능합니다")
    } else {
        ee = email;
        $.ajax({
            async: true,
            url: "/user/kakaologin/",
            type: "GET",
            data: {
                e: ee
            },
            dataType: 'json',
            timeout: 3000,
            success: function (result) {
                if (result['result'] == "success") {
                    location.href = "/"
                } else {
                    Kakao.API.request({
                        url: "/v1/user/unlink",
                        success: function () {
                            alert("회원정보를 입력해주세요!\n(이메일 " +`${email}`+
                                "로 가입해주세요!)");
                            location.href = "/user/signup/";
                        },

                        fail: function () {
                            alert("오류");
                        }
                    });
                }

            },
            error: function () {
                alert("error")
            }
        })
    }

}