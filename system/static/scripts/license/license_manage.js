$(function () {

//    1.初始化Table
    var oTable = new TableInit();
    oTable.Init();

});
var TableInit = function () {
    var oTableInit = new Object();
    //初始化Table
    oTableInit.Init = function () {
        $('#tb_license').bootstrapTable({
            url: '/license_manage.json',         //请求后台的URL（*）
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
            },{
                field: 'id',
                title: 'id',
                visible: false
            },{
                field: 'customer_name',
                title: '客户名'
            },{
                field: 'customer_department',
                title: '客户部门'
            },{
                field: 'customer_linkman',
                title: '联系人'
            },{
                field: 'kit_type',
                title: '套件类别'
            },
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


function uploadFile() {
        var formData = new FormData();
        var  fileObj = document.getElementById("FileUpload").files[0];
        var file_name = null;
        if (typeof (fileObj) == "undefined" || fileObj.size <= 0) {
        }else{
            formData.append("file", fileObj); //加入文件对象
            $.ajax(
            {
                url: "/upload_license_file",
                data: formData,
                type: "Post",
                dataType: "json",
                cache: false,//上传文件无需缓存
                processData: false,//用于对data参数进行序列化处理 这里必须false
                contentType: false, //必须
                success: function (data) {
                     var user = data.msg;
                     $('#url').val(user);
                },

                error: function () {
                    alert('请求出错');
                },


            });
        }

}


function create_license_manage() {
    
}