// submit form
function check_run_batch() {
    $.ajax(
        {
            url: "/task_run_batch.json",
            data: {
                "environment": $("#environment").val(),
                "job": $("#job").val(),
                "mobile": $("#job_mobile").val()
            },
            dataType: "json",
            type: "post",
            beforeSend: function () {
                $("#environment").attr({disabled: "disabled"});
                $("#job").attr({disabled: "disabled"});
                $("#job_mobile").attr({disabled: "disabled"});
                $("#submitButton").attr({disabled: "disabled"});
            },
            success: function (data) {
                if (data['code'] === 200) {
                    zlalert.alertInfoToast(data['msg']);
                } else {
                    zlalert.alertInfoToast(data['msg']);
                }
            },
            error: function () {
                zlalert.alertNetworkError();
            },
            complete: function () {
                $("#environment").removeAttr("disabled");
                $("#job").removeAttr("disabled");
                $("#job_mobile").removeAttr("disabled");
                $("#submitButton").removeAttr("disabled");
            }
        });
}