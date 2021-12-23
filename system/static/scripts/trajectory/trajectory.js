// submit form
function get_trajectory() {
    $.ajax(
        {
            url: "/get_trajectory.json",
            data: {
                "url": $("#trajectory_url").val(),
                "mobile": $("#trajectory_mobile").val(),
                "pwd": $("#trajectory_pwd").val(),
                "code": $("#trajectory_code").val()
            },
            dataType: "json",
            type: "post",
            beforeSend: function () {
                $("#trajectory_url").attr({disabled: "disabled"});
                $("#trajectory_mobile").attr({disabled: "disabled"});
                $("#trajectory_pwd").attr({disabled: "disabled"});
                $("#trajectory_code").attr({disabled: "disabled"});
                $("#submitButton").attr({disabled: "disabled"});
            },
            success: function (data) {
                if (data['code'] === 200) {
                    zlalert.alertSuccessToast(data['msg']);
                    window.location.href = '/historical_records';
                } else {
                    zlalert.alertInfo(data['msg']);
                }
            },
            error: function () {
                zlalert.alertNetworkError();
            },
            complete: function () {
                $("#trajectory_url").removeAttr("disabled");
                $("#trajectory_mobile").removeAttr("disabled");
                $("#trajectory_pwd").removeAttr("disabled");
                $("#trajectory_code").removeAttr("disabled");
                $("#submitButton").removeAttr("disabled");
            }
        });
}
