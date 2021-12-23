function ui_master_look() {
    $.ajax(
        {
            url: "/ui_web_master_look",
            data: {
                "environment": $('#environment').val(),
                "mobile": $('#mobile').val(),
                "pwd": $('#pwd').val(),
            },
            type: "post",
            beforeSend: function () {
                return true;
            },
            success: function (data) {
                if (data.code === 200) {
                    var user = data.msg;
                    $('#url').val(user.url);
                    $('#mobile').val(user.mobile);
                    $('#pwd').val(user.pwd);

                    $('#update_url').val(user.url);
                    $('#update_mobile').val(user.mobile);
                    $('#update_pwd').val(user.pwd);
                }
            },
            error: function () {
                zlalert.alertNetworkError();
            },
            complete: function () {
            }
        });
}

function ui_master_update() {
    $.ajax(
        {
            url: "/ui_web_master_update",
            data: {
                "environment": $('#environment').val(),
                "update_url": $('#update_url').val(),
                "update_mobile": $('#update_mobile').val(),
                "update_pwd": $('#update_pwd').val(),
            },
            type: "post",
            beforeSend: function () {
                $('#update_url').val('');
                $('#update_mobile').val('');
                $('#update_pwd').val('');
                $("#update_msg").html('');
                return true;
            },
            success: function (data) {
                $("#update_msg").html(data["msg"]);
                var dialog = $("#update-dialog");
                if (data.code === 200) {
                    setTimeout(function () {
                        dialog.modal("hide");
                    }, 3000);
                    ui_master_look();
                }
            },
            error: function () {
                zlalert.alertNetworkError();
            },
            complete: function () {
            }
        });
}

function output_data(json_data) {
    var _msg = json_data.msg;
    var res = '';
    for (var key in _msg) {
        var _msg_info = _msg[key];
        var s_res = '';
        for (var i = 0; i < _msg_info.length; i++) {
            s_res += (key + ': ' + JSON.stringify(_msg_info[i], 2));
        }
        res += (s_res + '\n');
    }
    return res;
}

function ui_master_page() {
    "use strict";

    cocoMessage.config({
        duration: 10000,
    });

    $.ajax(
        {
            url: "/ui_web_master_operate",
            data: {
                "environment": $('#environment').val(),
                "email_notice": $('#email_notice').val(),
                "mobile": $('#mobile').val(),
                "pwd": $('#pwd').val(),
            },
            type: "post",
            beforeSend: function () {
                $("#submitButton").attr({disabled: "disabled"});
                return true;
            },
            success: function (data) {
                var _msg = data.msg;
                $('#result').val(_msg);

            },
            error: function () {
                cocoMessage.warning(_msg, 0);
            },
            complete: function () {
                $("#submitButton").removeAttr("disabled");
            }
        });
}

function ui_master_add() {
    $.ajax(
        {
            url: "/ui_web_master_add",
            data: {
                "add_customer": $('#add_customer').val(),
                "add_url": $('#add_url').val(),
                "add_mobile": $('#add_mobile').val(),
                "add_pwd": $('#add_pwd').val(),
            },
            type: "post",
            beforeSend: function () {
                return true;
            },
            success: function (data) {
                var msg = data["msg"];
                if (data.code === 200) {
                    cocoMessage.success(msg, 3000);
                    setTimeout(function () {
                        window.location.reload();
                    }, 3500);
                }else {
                    cocoMessage.error(msg, 3000);
                }
            },
            error: function () {
                zlalert.alertNetworkError();
            },
            complete: function () {
            }
        });
}

function select_change(value) {
    ui_master_look();
}

