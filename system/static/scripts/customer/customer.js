$(function () {

//    1.初始化Table
    var oTable = new TableInit();
    oTable.Init();

});

var TableInit = function () {
    var oTableInit = new Object();
    //初始化Table
    oTableInit.Init = function () {
        $('#tb_customer').bootstrapTable({
            url: '/customer.json',         //请求后台的URL（*）
               //请求方式（*）
            toolbar: '#toolbar',                //工具按钮用哪个容器
            striped: true,                      //是否显示行间隔色
            cache: false,                       //是否使用缓存，默认为true（*）
            pagination: true,                   //是否显示分页（*）1
            sortable: true,                     //是否启用排序
            sortOrder: "asc",                   //排序方式
            queryParams: oTableInit.queryParams,//传递参数（*）
            sidePagination: "server",           //分页方式：client客户端分页，server服务端分页（*）
            pageNumber: 1,                       //初始化加载第一页，默认第一页
            pageSize: 25,                       //每页的记录行数（*）
            pageList: [10, 25, 50, 100, 500],        //可供选择的每页的行数（*）
            search: false,                       //是否显示表格搜索，此搜索是客户端搜索，不会进服务端
            strictSearch: false,
            showColumns: false,                  //是否显示所有的列
            showRefresh: true,                  //是否显示刷新按钮
            minimumCountColumns: 2,             //最少允许的列数
            clickToSelect: true,                //是否启用点击选中行
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
                field: 'company_name',
                title: '客户名称'
            },{
                field: 'location',
                title: '地点'
            },{
                field: 'configure',
                title: '配置'
            },{
                field: 'test_subject',
                title: '客户测试项目'
            },{
                field: 'product_type',
                title: '产品类型'
            },{
                field: 'saleman',
                title: '销售'
            },{
                field: 'business_develop',
                title: '业务拓展'
            },{
                field: 'project_manager',
                title: '项目经理'
            },{
                field: 'chief_task',
                title: '主要任务'
            },{
                field: 'provide_js',
                title: '是否提供脚本'
            },{
                field: 'linkman_name',
                title: '客户联系人'
            },{
                field: 'department',
                title: '部门'
            },{
                field: 'position1',
                title: '职位'
            },{
                field: 'email',
                title: '邮箱'
            },{
                field: 'vender',
                title: '原厂'
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



function addCustomer() {

    $.ajax(
        {
            url: "/add_customer",
            data: {
                "company_name": $('#company_name').val(),
                "location": $('#location').val(),
                "configure":$('#configure').val(),
                "test_subject":$('#test_subject').val(),
                "product_type":$('#product_type').val(),
                "chief_task":$('#chief_task').val(),
                "saleman":$("#saleman option:selected").val(),
                "provide_js":$('#provide_js').val(),
                "linkman_name":$('#linkman_name').val(),
                "department":$('#department').val(),
                "position1":$('#position1').val(),
                "email":$('#email').val(),
                "vender":$("#vender option:selected").val(),
                "business_develop":$("#business_develop option:selected").val(),
                "project_manager":$("#project_manager option:selected").val()
            },
            type: "post",
            dataType: 'json',
            success: function (data) {
                if (data.code === 200) {
                    zlalert.alertSuccessToast(data['msg']);
                    setTimeout(function () {
                            window.location.href = '/customer';
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

function add_gruop() {
    var rows = $('#tb_customer').bootstrapTable('getSelections');
    if (rows) {
        var row = rows[0];
        var customer_id;
        try{
            customer_id = row.id;
        }
        catch(e)
        {
            customer_id = 0;
        }
    }
    $.ajax(

        {
            url: "/add_into_group",
            data: {
                "customer_id":customer_id,
                "group_id":$("#group_name option:selected").val()
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






function deleteCustomer() {
    "use strict";

    cocoMessage.config({
        duration: 10000,
    });

    var rows = $('#tb_customer').bootstrapTable('getSelections');
    if (rows) {
        var row = rows[0];
        var customer_id;
        try{
            customer_id = row.id;
        }
        catch(e)
        {
            customer_id = 0;
        }
    }
    $.ajax(
        {
            url: "/del_customer",
            data: {"id": customer_id},
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
                        window.location.href = ('/customer');
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



function searchCustomer() {

        $.ajax(
        {
            url: "/search_customer.json",
            data: {
               "company_name": $("#company_name").val(),
                "linkman_name": $("#linkman_name").val(),
                "email": $("#company_email").val()
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
                    $('#tb_customer').bootstrapTable('load', data['msg']);
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


function modifyCustomer() {
    var rows = $('#tb_customer').bootstrapTable('getSelections');
     var row = rows[0];
     var customer_id;
    if (rows.length != 0 ) {

        try{
            customer_id = row.id;
        }
        catch(e)
        {
            customer_id = 0;
        }
    }
     $.ajax(
        {
            url: "/customer_modify_display",
            data: {
                "customer_id":customer_id,
            },
            type: "post",
            dataType: 'json',
            success: function (data) {
                if (data.code == 200) {
                    window.location.href = ('/customer_motify');

                }else{
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
function saveCustomer() {

    $.ajax(
        {
            url: "/customer_motify.json",
            data: {
                "id":$('#id').val(),
                "company_name": $('#company_name').val(),
                "location": $('#location').val(),
                "configure":$('#configure').val(),
                "test_subject":$('#test_subject').val(),
                "product_type":$('#product_type').val(),
                "chief_task":$('#chief_task').val(),
                "saleman":$("#saleman option:selected").val(),
                "provide_js":$('#provide_js').val(),
                "linkman_name":$('#linkman_name').val(),
                "department":$('#department').val(),
                "position1":$('#position1').val(),
                "email":$('#email').val(),
                "vender":$("#vender option:selected").val(),
                "business_develop":$("#business_develop option:selected").val(),
                "project_manager":$("#project_manager option:selected").val()

            },
            type: "post",
            dataType: 'json',
            success: function (data) {
                if (data.code === 200) {
                    zlalert.alertSuccessToast(data['msg']);
                    setTimeout(function () {
                            window.location.href = '/customer';
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