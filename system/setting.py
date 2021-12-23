class ResCode:
    """返回状态码"""
    OK = 200
    NULL_ERROR = -1
    FORMAT_ERROR = -75
    LIMIT_ERROR = -120


class ResMsg:
    """返回信息"""
    OK = 'OK'
    STATUS_CHECKED = '校验成功'
    PARAMETER_ERROR = '参数错误'
    NULL_ERROR = '必填信息不能为空'
    MOBILE_NULL_ERROR = '手机号不能为空'
    MOBILE_FORMAT_ERROR = '手机号格式错误'
