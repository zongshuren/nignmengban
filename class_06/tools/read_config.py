import configparser

# section option value
# cf = configparser.ConfigParser()
# cf.read('case.config', encoding='utf-8')
# res_1 = cf.get('MODE', 'mode')
# res_2 = cf['MODE']['mode']
# print(res_1, res_2)
# print(cf.sections())
# print(cf.items('PYTHON11'))
class ReadConfig:
    def read_config(self, file_name, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding='utf-8')
        return cf.get(section, option)

if __name__ == '__main__':
    res = ReadConfig().read_config('case.config', 'MODE', 'mode')
    print(res)