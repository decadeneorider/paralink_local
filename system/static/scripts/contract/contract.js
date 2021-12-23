$(function () {

//    1.初始化Table
    var oTable = new TableInit();
    oTable.Init();

});

// submit form
function updateForm() {
    $("#update_user_password").validate();
    $.ajax(
        {
            url: "/user_password.json",
            data: {"password": $("#password").val()},
            type: "post",
            beforeSend: function () {
                $("#tip").html("<span style='color:blue'>正在处理...</span>");
                return true;
            },
            success: function (data) {
                if (data.code === 200) {
                    zlalert.alertSuccessToast('修改成功！');
                    $("#tip").html("<span style='color:blueviolet'>恭喜，新增成功！</span>");
                    window.location.href = ('/');
                } else {
                    zlalert.alertInfoToast('失败，请重试: ' + data.msg);
                    $("#tip").html("<span style='color:red'>失败，请重试</span>");
                    window.location.href = ('/edit_user_password');
                }
            },
            error: function () {
                zlalert.alertNetworkError();
            },
            complete: function () {

            }
        });
}

function co_create() {
    var customer = $("#customer option:selected");
    var vender = $("#vender option:selected");
    var saleman = $("#saleman option:selected");
    var configure_text = $("#configure").val();
    var des1 = configure_text.replace(/\r\n/g, '<br/>').replace(/\n/g, '<br/>').replace(/\s/g, ' ');
    $.ajax(
        {
            url: "/contract_add.json",
            data: {

                "contract_id": $("#contract_id").val(),
                "customer": customer.text(),
                "vender": vender.text(),
                "saleman": saleman.text(),
                "configure": des1,
                "receipt_date": $("#receipt_date").val(),
                "order_date": $("#order_date").val(),
                "shipmemt_date": $("#shipmemt_date").val(),
                "arrival_date": $("#arrival_date").val(),
                "acceptment_date": $("#acceptment_date").val(),
                "due_date": $("#due_date").val(),
                "remind_need": $("#remind_need").val(),
                "remark": $("#remark").val()
            },
            dataType: "json",
            type: "post",
            success: function (data) {
                if (data.code === 200) {
                    zlalert.alertSuccessToast(data['msg']);
                    setTimeout(
                        function () {
                            window.location.href = '/contract_display';
                        },2000
                    );
                } else {
                    zlalert.alertInfoToast(data['msg']);
                }
            },
            error: function () {
                zlalert.alertNetworkError();
            },

        });
}

function co_modify() {
    var customer = $("#customer option:selected");
    var vender = $("#vender option:selected");
    var saleman = $("#saleman option:selected");
    var configure_text = $("#configure").val();
    var des1 = configure_text.replace(/\r\n/g, '<br/>').replace(/\n/g, '<br/>').replace(/\s/g, ' ');

    $.ajax(
        {
            url: "/contract_modify.json",
            data: {

                "contract_id": $("#contract_id").val(),
                "customer": customer.text(),
                "vender": vender.text(),
                "saleman": saleman.text(),
                "configure": des1,
                "receipt_date": $("#receipt_date").val(),
                "order_date": $("#order_date").val(),
                "shipmemt_date": $("#shipmemt_date").val(),
                "arrival_date": $("#arrival_date").val(),
                "acceptment_date": $("#acceptment_date").val(),
                "due_date": $("#due_date").val(),
                "remind_need": $("#remind_need").val(),
                "remark": $("#remark").val()
            },
            dataType: "json",
            type: "post",
            beforeSend: function () {
                $("#environment").attr({disabled: "disabled"});
                $("#mobile").attr({disabled: "disabled"});
                $("#orderNum").attr({disabled: "disabled"});
                $("#submitButton").attr({disabled: "disabled"});
            },
            success: function (data) {
                if (data.code === 200) {
                    zlalert.alertSuccessToast(data['msg']);
                    setTimeout(
                        function () {
                            window.location.href = '/contract_display';
                        },2000
                    );
                } else {
                    zlalert.alertInfoToast(data['msg']);
                }
            },
            error: function () {
                zlalert.alertNetworkError();
            },
            complete: function () {
                $("#environment").removeAttr("disabled");
                $("#mobile").removeAttr("disabled");
                $("#orderNum").removeAttr("disabled");
                $("#submitButton").removeAttr("disabled");
            }
        });
}


var TableInit = function () {
    var oTableInit = new Object();
    //初始化Table
    oTableInit.Init = function () {
        $('#tb_contract').bootstrapTable({
            url: '/contract.json',         //请求后台的URL（*）
            toolbar: '#toolbar',                //工具按钮用哪个容器
            striped: true,                      //是否显示行间隔色
            cache: false,                       //是否使用缓存，默认为true（*）
            pagination: true,                   //是否显示分页（*）1
            sortable: true,                     //是否启用排序
            sortOrder: "asc",                   //排序方式
            queryParams: oTableInit.queryParams,//传递参数（*）
            sidePagination: "server",           //分页方式：client客户端分页，server服务端分页（*）
            pageNumber: 1,                       //初始化加载第一页，默认第一页
            pageSize: 50,                       //每页的记录行数（*）
            pageList: [10,20, 50, 100],        //可供选择的每页的行数（*）
            search: false,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端
            strictSearch: false,
            showColumns: false,                  //是否显示所有的列
            showRefresh: true,                  //是否显示刷新按钮
            minimumCountColumns: 2,             //最少允许的列数
            clickToSelect: true,                //是否启用点击选中行

            uniqueId: "contract_id",                     //每一行的唯一标识，一般为主键列
            showToggle: false,                    //是否显示详细视图和列表视图的切换按钮 2
            cardView: false,                    //是否显示详细视图
            detailView: false,                   //是否显示父子表
            singleSelect: true,                   //是否开启单选
            columns: [{
                checkbox: true
            }, {
                field: 'contract_id',
                title: '合同编号',
            }, {
                field: 'customer',
                title: '客户名'
            }, {
                field: 'vender',
                title: '原厂'
            }, {
                field: 'saleman',
                title: '销售人员'
            }
            , {
                field: 'receipt_date',
                title: '接单日期'
            }
            , {
                field: 'order_date',
                title: '下单日期'
            }
            , {
                field: 'shipmemt_date',
                title: '原厂发货日期'
            }
            , {
                field: 'arrival_date',
                title: '货到客户日期'
            }
            , {
                field: 'acceptment_date',
                title: '验收日期'
            }, {
                field: 'due_date',
                title: '维保到期日'
            }, {
                field: 'remind_need',
                title: '是否到期提醒'
            }, {
                field: 'remark',
                title: '详情',
                 formatter:function(value,row,index){
                    return '<a href="/contract_detail?contract_id='+row.contract_id+'">查看</a>'
                }
            }
            ]
        });
    };
    //得到查询的参数
    oTableInit.queryParams = function (params) {
        var temp = {   //这里的键的名字和控制器的变量名必须一直，这边改动，控制器也需要改成一样的
            limit: params.limit,   //页面大小
            offset: params.offset //页码
        };
        return temp;
    };
    return oTableInit;
};

function deleteContract() {
    "use strict";

    cocoMessage.config({
        duration: 10000,
    });

    var rows = $('#tb_contract').bootstrapTable('getSelections');
    console.log(rows.length);
     var row = rows[0];
     var contract_id;
    if (rows.length != 0 ) {

        try{
            contract_id = row.contract_id;
        }
        catch(e)
        {
            contract_id = 0;
        }
    }
    if(contract_id ==null||contract_id == 0){
        zlalert.alertInfoToast("请选择删除")
    }else{
        $.ajax(
        {
            url: "/contract_del.json",
            data: {"contract_id": contract_id},
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
                        window.location.href = ('/contract_display');
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

}
function searchContract() {

        $.ajax(
        {
            url: "/contract_search1.json",
            data: {
                "contract_id": $("#contract_id").val(),
                "customer": $("#customer").val(),
                "vender": $("#vender").val(),
                "saleman": $("#saleman").val(),
                "configure": $("#configure").val(),
                "due_date_first": $("#due_date_first").val(),
                "due_date_second": $("#due_date_second").val()
            },
            type: "post",
            dataType: 'json',
            beforeSend: function () {
                $("#tip").html("<span style='color:blue'>正在处理...</span>");
                $("#btn_delete").attr({disabled: "disabled"});
                return true;
            },
            success: function (data) {
                if (data.code == 200) {
                    $('#tb_contract').bootstrapTable('load', data['msg']);
                } else {
                   cocoMessage.error("请输入搜索项", 1000);
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

function modifyContract() {
    var rows = $('#tb_contract').bootstrapTable('getSelections');
    console.log(rows.length);
     var row = rows[0];
     var contract_id;
    if (rows.length != 0 ) {

        try{
            contract_id = row.contract_id;
        }
        catch(e)
        {
            contract_id = 0;
        }
    }
     $.ajax(
        {
            url: "/contract_modify_display",
            data: {
                "contract_id":contract_id,
            },
            type: "post",
            dataType: 'json',
            success: function (data) {
                if (data.code == 200) {
                    window.location.href = ('/contract_modify');

                }else{
                    console.log(12123132123123)
                    zlalert.alertInfoToast( data.msg)
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