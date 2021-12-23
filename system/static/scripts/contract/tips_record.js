$(function () {

//    1.初始化Table
    var oTable = new TableInit();
    oTable.Init();

});
var TableInit = function () {
    var oTableInit = new Object();
    //初始化Table
    oTableInit.Init = function () {
        $('#tb_tips_contract').bootstrapTable({
            url: '/tips_record_display.json',         //请求后台的URL（*）
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
            },{
                field: 'saleman',
                title: '销售人员'
            }
            ,  {
                field: 'due_date',
                title: '维保到期日'
            },{
                field: 'tips_number',
                title: '邮件提醒次数'
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