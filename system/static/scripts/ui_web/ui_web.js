function ui_web_bottom(){
     $.ajax(
        {
            url: "/ui_web.json",
            data: {
                "test_case": $('#test_case option:selected').val(),
                "test_environment": $('#test_environment option:selected').val(),
            },
            dataType: "json",
            type: "post",
            success: function (data) {
                if (data['code'] === 200) {
                    window.location.href =( '/ui_web_test_trunk');
                } else {
                    zlalert.alertInfoToast(data['msg']);
                }
            },
            error: function () {
                zlalert.alertNetworkError();
            },

        });
}

