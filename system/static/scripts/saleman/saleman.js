$(function () {

//    1.初始化Table
    var oTable = new TableInit();
    oTable.Init();

});

var TableInit = function () {
    var oTableInit = new Object();
    //初始化Table
    oTableInit.Init = function () {
        $('#tb_saleman').bootstrapTable({
            url: '/saleman.json',         //请求后台的URL（*）
            method: 'get',                      //请求方式（*）
            toolbar: '#toolbar',                //工具按钮用哪个容器
            striped: true,                      //是否显示行间隔色
            cache: false,                       //是否使用缓存，默认为true（*）
            pagination: false,                   //是否显示分页（*）1
            sortable: true,                     //是否启用排序
            sortOrder: "asc",                   //排序方式
            queryParams: oTableInit.queryParams,//传递参数（*）
            sidePagination: "server",           //分页方式：client客户端分页，server服务端分页（*）
            pageNumber: 1,                       //初始化加载第一页，默认第一页
            pageSize: 10,                       //每页的记录行数（*）
            pageList: [10, 25, 50, 100, 500],        //可供选择的每页的行数（*）
            search: false,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端
            strictSearch: false,
            showColumns: false,                  //是否显示所有的列
            showRefresh: true,                  //是否显示刷新按钮
            minimumCountColumns: 2,             //最少允许的列数
            clickToSelect: true,                //是否启用点击选中行
            height: 500,                        //行高，如果没有设置height属性，表格自动根据记录条数觉得表格高度
            uniqueId: "id",                     //每一行的唯一标识，一般为主键列
            showToggle: false,                    //是否显示详细视图和列表视图的切换按钮 2
            cardView: false,                    //是否显示详细视图
            detailView: false,                   //是否显示父子表
            singleSelect: true,                   //是否开启单选

            columns: [{
                checkbox: true
            }, {
                field: 'id',
                title: 'id',
                visible: false
            }, {
                field: 'saleman_name',
                title: '销售人员名称'
            },{
                field: 'saleman_email',
                title: '销售人员邮箱'
            }]
        });
    };
    //得到查询的参数
    oTableInit.queryParams = function (params) {
        var temp = {   //这里的键的名字和控制器的变量名必须一直，这边改动，控制器也需要改成一样的
            limit: params.limit,   //页面大小
            offset: params.offset //页码
//            keyword: $("#keyword").val()
        };
        return temp;
    };
    return oTableInit;
};



function addSaleman() {

    $.ajax(
        {
            url: "/add_saleman",
            data: {
                "saleman_name": $('#saleman_name').val(),
                "saleman_email": $('#saleman_email').val()
            },
            type: "post",
            dataType: 'json',
            success: function (data) {
                if (data.code === 200) {
                    zlalert.alertSuccessToast(data['msg']);
                    setTimeout(function () {
                        window.location.reload();
                    }, 1000);


                } else {
                    zlalert.alertInfoToast(data['msg']);
                }
            },
            error: function () {
                alert('请求出错');
            },

        });
}






function deleteSaleman() {
    "use strict";

    cocoMessage.config({
        duration: 10000,
    });

    var rows = $('#tb_saleman').bootstrapTable('getSelections');
    if (rows) {
        var row = rows[0];
        var saleman_id;
        try{
            saleman_id = row.id;
        }
        catch(e)
        {
            saleman_id = 0;
        }
    }
    $.ajax(
        {
            url: "/del_saleman",
            data: {"id": saleman_id},
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
                        window.location.href = ('/saleman');
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