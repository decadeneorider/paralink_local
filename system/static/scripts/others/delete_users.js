function deleteUser() {
    "use strict";

    cocoMessage.config({
        duration: 10000,
    });

    var rows = $('#tb_users').bootstrapTable('getSelections');
    if (rows) {
        var row = rows[0];
        var user_id;
        try{
            user_id = row.id;
        }
        catch(e)
        {
            user_id = 0;
        }
    }
    $.ajax(
        {
            url: "/delete_user.json",
            data: {"id": user_id},
            type: "post",
            dataType: 'json',
            beforeSend: function () {
                $("#tip").html("<span style='color:blue'>正在处理...</span>");
                $("#btn_delete").attr({disabled: "disabled"});
                return true;
            },
            success: function (data) {
                if (data.code === 200) {
                    cocoMessage.info("修改成功！", 1000);
                    setTimeout(function () {
                        window.location.href = ('/users');
                    }, 1500);
                } else {
                   cocoMessage.error(data['msg'], 1000);
                }
            },
            error: function () {
                alert('请求出错');
            },
            complete: function () {
                $("#btn_delete").removeAttr("disabled");
            }
        });
}