// 切换select时，展示不同的模块数据
function mc_test(Names) {
    for (var i = 0; i < 10; i++) {    //  更改数字4可以改变选择的内容数量，在下拉总数值的基础上+1.比如：下拉菜单有5个值，则4变成6
        var temp_name = "model_x" + i;
        var NewsHot = "x" + i;    //  “X”是ID名称，比如：ID命名为“case1”，这里的“X”即为“case”
        if (Names === temp_name) {
            var news = document.getElementById(NewsHot);
            news.style.display = '';
        } else {
            var s_news = document.getElementById(NewsHot);
            s_news.style.display = 'none';
        }
    }
}

// 输出内容为json格式 反序列化以每行内容输出
function output_json_data(json_data, is_no_msg) {
    var _msg = '';
    if (is_no_msg === 'true') {
        _msg = json_data;
    } else {
        _msg = json_data['msg'];
    }
    var res = '';
    for (var key in _msg) {
        var _msg_info = _msg[key];
        var s_res = key + ': ' + _msg_info;
        res += (s_res + '\n');
    }
    return res;
}

// 获取当前请求url
function getRequestUrl() {
    var strFullPath = window.document.location.href;
    var strPath = window.document.location.pathname;
    var pos = strFullPath.indexOf(strPath);
    var prePath = strFullPath.substring(0, pos);
    var postPath = strPath.substring(0, strPath.substr(1).indexOf('/') + 1);
    return prePath + postPath;
}

// 输入框为空时增加css样式
function is_null_borderColor(ele) {
    var elem = "#" + ele;
    var value = $(elem);
    var elem_val = value.val();
    if (elem_val === '' || elem_val === undefined || elem_val === null) {
        value.css('borderColor', 'red');
    } else {
        value.css('borderColor', '');
    }
}

// 获取url中的参数
function getVariable(variable) {
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");
        if (pair[0] === variable) {
            return pair[1];
        }
    }
    return false;
}

// 往table追加数据
function addRow(tb, col1, col2) {
    var row = tb.insertRow(tb.FetchRowCount);
    row.insertCell(0).innerHTML = col1;
    row.insertCell(1).innerHTML = col2;
}
