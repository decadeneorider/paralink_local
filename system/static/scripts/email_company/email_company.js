$(function () {

//    1.初始化Table
    var oTable = new TableInit();
    oTable.Init();

});

var TableInit = function () {
    var oTableInit = new Object();
    //初始化Table
    oTableInit.Init = function () {
        $('#tb_group_company').bootstrapTable({
            url: '/group_company.json',         //请求后台的URL（*）
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
                field: 'company_name',
                title: '公司名称'
            },{
                field: 'company_department',
                title: '客户部门'
            },{
                field: 'company_linkman',
                title: '客户联系人 '
            },{
                field: 'company_email',
                title: '客户邮箱'
            },{
                field: 'company_saleman',
                title: '销售人员'
            },{
                field: 'business_develop',
                title: '业务拓展'
            },{
                field: 'project_manager',
                title: '项目经理'
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





$(document).ready(function () {
    $('#company_group').change(function () {
        var  company_group= $('#company_group option:selected');
        var company_group_id = company_group.val();

        $.ajax(
            {
                url: "/group_change_company.json",
                type: "post",
                beforeSend: function () {
                    return true;
                },
                data: {
                    "company_group_id": company_group_id
                },
                success: function (data) {
                    if (data.code === 200) {
                        $('#tb_group_company').bootstrapTable('load', data['msg']);
                    } else {
                        zlalert.alertInfo('网络错误');
                    }
                },
                error: function () {
                    zlalert.alertNetworkError();
                },
                complete: function () {
                }
            });
    })
});

function addGroupCompany() {
      $.ajax(
        {
            url: "/group_add_company.json",
            data: {
                "company_name": $('#company_name').val(),
                "company_group_id":$('#company_group option:selected').val(),
                "company_email":$("#company_email").val(),
                "company_department":$('#company_department').val(),
                "company_saleman":$('#saleman option:selected').val()
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

function deleteGroupCompany() {
    "use strict";

    cocoMessage.config({
        duration: 10000,
    });

    var rows = $('#tb_group_company').bootstrapTable('getSelections');
    if (rows) {
        var row = rows[0];
        var company_id;
        try{
            company_id = row.id;
        }
        catch(e)
        {
            company_id = 0;
        }
    }
    $.ajax(
        {
            url: "/group_del_company.json",
            data: {"id": company_id},
            type: "post",
            dataType: 'json',
            beforeSend: function () {
                $("#tip").html("<span style='color:blue'>正在处理...</span>");
                $("#btn_delete").attr({disabled: "disabled"});
                return true;
            },
            success: function (data) {
                if (data.code === 200) {
                    cocoMessage.info("删除成功！", 1000);
                    setTimeout(function () {
                        window.location.href = ('/email_company_edit');
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

function uploadFile() {
        var messagetxt = $("#message").val();
        var sql_message = messagetxt.replace(/\r\n/g, '<br/>').replace(/\n/g, '<br/>').replace(/\s/g, ' ');
        var formData = new FormData();
        var  fileObj = document.getElementById("FileUpload").files[0];
        var group_id = $('#group option:selected').val();
        var file_name = null;
        if (typeof (fileObj) == "undefined" || fileObj.size <= 0) {
            sendEmail(group_id,messagetxt,sql_message,file_name)
        }else{
            formData.append("file", fileObj); //加入文件对象
            $.ajax(
            {
                url: "/send_email_file",
                data: formData,
                type: "Post",
                dataType: "json",
                cache: false,//上传文件无需缓存
                processData: false,//用于对data参数进行序列化处理 这里必须false
                contentType: false, //必须
                success: function (result) {
                    file_name = result["file_name"];
                    sendEmail(group_id,messagetxt,sql_message,file_name)
                },

                error: function () {
                    alert('请求出错');
                },
                 complete: function () {
                    $("#submitButton").removeAttr("disabled");
                }

            });
        }

}


function sendEmail(company_group_id,messagetxt,sql_message,file_name) {
    var email_title =$("#email_title").val();
    $.ajax(
        {
            url: "/send_email.json",
            data: {
                "company_group_id": company_group_id,
                "message":messagetxt,
                "sql_message":sql_message ,
                "file_name": file_name,
                "email_title":email_title
            },
            type: "post",
            dataType: 'json',
             beforeSend: function () {
                $("#submitButton").attr({disabled: "disabled"});
            },
            success: function (data) {
                if (data.code === 200) {
                    zlalert.alertSuccessToast(data['msg']);
                } else {
                    zlalert.alertInfoToast(data['msg']);
                    $("#msg").val(data['tips']);
                }
            },
            error: function () {
                alert('请求出错');
            },
             complete: function () {
                $("#submitButton").removeAttr("disabled");
            }

         });
}
function motifyGroupName() {
    var  company_group= $('#company_group option:selected');
    var company_group_id = company_group.val();
    var group_name = $("#group_name").val();
    $.ajax(
        {
            url: "/motify_group_name.json",
            data: {
                "group_id": company_group_id,
                "group_name":group_name
            },
            type: "post",
            dataType: 'json',
             beforeSend: function () {
                $("#submitButton").attr({disabled: "disabled"});
            },
            success: function (data) {
                if (data.code === 200) {
                    zlalert.alertSuccessToast(data['msg']);
                    setTimeout(function () {
                        window.location.href = ('/email_company_edit');
                    }, 1500);
                } else {
                    zlalert.alertInfoToast(data['msg']);
                }
            },
            error: function () {
                alert('请求出错');
            },
             complete: function () {
                $("#submitButton").removeAttr("disabled");
            }

         });
}

