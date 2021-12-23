$(function () {
    $('.left_menu li').click(function () {
        $(this).addClass('cur').siblings().removeClass('cur');
        var index = $(this).index();
        if(index === 3){
            index = 2;
        }
        $('.right_menu .execution').eq(index).removeClass('hide').siblings().addClass('hide');
    });
    select_model();
    $("[data-toggle='popover']").popover();
});

function ui_web_bottom(){
     $.ajax(
        {
            url: "/ui_web.json",
            data: {
                "environment": $('#test_environment').val(),
                "case": $('#test_case').val(),
            },
            dataType: "json",
            type: "post",
            success: function (data) {
                // # 200 主干 201 全流程 202 线上冒烟
                if (data['code'] === 200) {
                    window.location.href =( '/ui_web_test_trunk');
                }else if (data['code'] === 201) {
                    window.location.href =( '/ui_web_all_case');
                }else if (data['code'] === 202) {
                    window.location.href =( '/ui_web_master');
                } else {
                    zlalert.alertInfoToast(data['msg']);
                }
            },
            error: function () {
                zlalert.alertNetworkError();
            },

        });
}

function select_model() {
    var mySelect= $("#mySelect").mySelect({
          mult:true,   //true为多选, false为单选
          option:[     //选项数据
              {label:"全部",value:"all"},
              {label:"需求",value:"needs"},
              {label:"交易",value:"transaction"},
              {label:"调度",value:"dispatch"},
              {label:"伙伴",value:"friends"},
              {label:"运输队",value:"transport_team"}
          ],
          onChange:function(res){//选择框值变化返回结果
              console.log(res);
          }
      });
    mySelect.setResult(["all"]);
}

function edit_cases() {
    $.ajax(
        {
            url: "/ui_web_test_trunk.json",
            data: {
                "model_num": $("#model").val(),
            },
            type: "post",
            beforeSend: function () {
                return true;
            },
            success: function (data) {
                if (data.code === 200) {
                    var data_comp = data["model_data"];
                    var data_str = JSON.stringify(data_comp, null, 2);
                    $('#model_data').val(data_str);
                } else {
                    zlalert.alertInfoToast('数据错误');
                }
            },
            error: function () {
                zlalert.alertNetworkError();
            },
            complete: function () {
            }
        });
}

function save_cases() {
    $.ajax(
        {
            url: "/ui_web_test_trunk_save.json",
            data: {
                "model_num": $("#model").val(),
                "model_data": $("#model_data").val()
            },
            type: "post",
            beforeSend: function () {
                return true;
            },
            success: function (data) {
                if (data.code === 200) {
                    zlalert.alertSuccessToast(data["msg"]);
                } else {
                    zlalert.alertInfoToast(data["msg"]);
                }
            },
            error: function () {
                zlalert.alertNetworkError();
            },
            complete: function () {
            }
        });
}

function implement_cases() {
    var select_values = $(".inputWrap ul li span").text();
    $.ajax(
        {
            url: "/ui_web_test_trunk_implement.json",
            data: {
                "trunk_case_mobile": $('#trunk_case_mobile').val(),
                "trunk_case_pwd": $('#trunk_case_pwd').val(),
                "model_list": select_values,
            },
            type: "post",
            beforeSend: function () {
                return true;
            },
            success: function (data) {
                if (data.code === 200) {
                    zlalert.alertSuccessToast(data['msg']);
                } else {
                    zlalert.alertInfoToast(data['msg']);
                }
            },
            error: function () {
                zlalert.alertNetworkError();
            },
            complete: function () {
            }
        });
}
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

function select_change(value) {
    ui_master_look();
}