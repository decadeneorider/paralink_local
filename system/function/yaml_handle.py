from ruamel import yaml


class ReadHandle:
    """yaml读文件"""

    def __init__(self, filepath):
        self.filepath = filepath

    # ReadHandle(FileDir.ui_master_dir).yaml_files_read()
    def yaml_files_read(self):
        with open(file=self.filepath, mode='r', encoding='utf-8') as f:
            r = yaml.safe_load_all(f)
            for i in r:
                return i


class WriteHandle:
    """yaml写数据"""

    def __init__(self, filepath):
        self.filepath = filepath

    def yaml_files_dump(self, key, is_second=None, _data=None, is_third=None, _data_2=None, is_fourth=None,
                        _data_3=None):
        with open(self.filepath, encoding="utf-8") as f:
            content = yaml.load(f, Loader=yaml.RoundTripLoader)
            # 根据key修改yml文件内容, 如: yaml_files_dump('update_data', is_second=True, _data='a')
            if is_second:
                content[_data] = key
                with open(self.filepath, 'w', encoding="utf-8") as nf:
                    yaml.dump(content, nf, Dumper=yaml.RoundTripDumper, allow_unicode=True)
            # 如: yaml_files_dump('123', _data='ui_master', is_third=True, _data_2='session')
            elif is_third:
                content[_data][_data_2] = key
                with open(self.filepath, 'w', encoding="utf-8") as nf:
                    yaml.dump(content, nf, Dumper=yaml.RoundTripDumper, allow_unicode=True)
            # 如: yaml_files_dump('update_data', is_fourth=True, _data='d', _data_2='e', _data_3='f')
            elif is_fourth:
                content[_data][_data_2][_data_3] = key
                with open(self.filepath, 'w', encoding="utf-8") as nf:
                    yaml.dump(content, nf, Dumper=yaml.RoundTripDumper, allow_unicode=True)
            # 覆盖文件
            else:
                with open(self.filepath, 'w', encoding="utf-8") as nf:
                    yaml.dump(key, nf, Dumper=yaml.RoundTripDumper, allow_unicode=True)