import requests
import random
class PhonHu:

    def __init__(self):
        # 实例化会话对象
        # 保持登录用的
        self.sessionRequest = requests.session()

    # 获取登录cookie 调用后返回cookie
    def loging_get_cookie(self):
        login = 'http://pre.wms.ponhu.cn/index.php/User/login'  # 登录url
        header = {
            'Host': 'pre.wms.ponhu.cn',
            'Connection': 'keep-alive',
            'Content-Length': '65',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'http://pre.wms.ponhu.cn',
            'Referer': 'http://pre.wms.ponhu.cn/index.php/User/login',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9'
        }  # 登录用请求头
        # 登录需要用到的参数 包含账号密码
        data = {'sub': 1, 'username': 13810151896, 'password': 123456, 'hidden_Message': 0, 'code': ''}
        # 调用登录接口传对应data header 用res承接返回值
        res = self.sessionRequest.post(url=login, data=data, headers=header)
        PHPSESSID = res.cookies['PHPSESSID']
        username = res.cookies['username']
        # 由于直接从返回值里取出cookie使用,取出的格式下一个接口会不认可，所以需要将cookie内参数取出后再次拼接为字符串
        phonhu_cookie = 'PHPSESSID=' + PHPSESSID + ';username=' + username
        # 返回拼接后的cookie
        return phonhu_cookie

    # 调用后添加商品gotoware_type为入库方式默认为2代表买断3寄售在库10联营 num为创建的商品个数，默认为1个
    def add_goods(self, gotoware_type=2, num=1):
        add_goods_url = 'http://pre.wms.ponhu.cn/index.php/Releaseinter/submit_ruku'
        add_goods_header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Host': 'pre.wms.ponhu.cn',
            'Proxy-Connection': 'keep-alive',
            'Content-Length': '6573',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'Origin': 'http://pre.wms.ponhu.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
            'Referer': 'http://pre.wms.ponhu.cn/Releaseinter/index',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',

            'Cookie': self.loging_get_cookie()
            }  # 创建商品请求头

        print(add_goods_header)  # 打印请求头

        # for循环 num控制循环数量 默认为1
        for i in range(num):
            # 商品图片list
            image_list = [
                'https://img-ppcdn.ponhu.cn/Fi3YWKyaJJKv6tnr0FqKYSxj1xdf',
                'https://img-ppcdn.ponhu.cn/FuR_js4859rib_ZmU4AZ0kwj8MfU',
                'https://img-ppcdn.ponhu.cn/FijIXuvsgeFshY2l1NNaOyIMPmVP',
                'https://img-ppcdn.ponhu.cn/FsBkqjU70yxxZx7wLg36eRDydQGk',
                'https://res.ponhu.cn/XY20210818222021438.jpg',
                'https://res.ponhu.cn/XY20210818114928932.jpg',
                'https://img-ppcdn.ponhu.cn/FuEUsz43XCfrhF_CrndiMhVWFNjD',
                'https://img-ppcdn.ponhu.cn/FnitKCajkiVFNGpeuNd-7cFIg6rw',
                'https://img-ppcdn.ponhu.cn/FtEuXHRrRaNjmMdwQ69gaz7hvF2S',
                'https://img-ppcdn.ponhu.cn/Ft_WV4eV1xbVLSZwsz2X40R6Mtm4'
            ]
            # 利用random.choice(image_list)函数从商品图片列表内随机返回一个元素 使测试数据更有可观性
            goods_image = random.choice(image_list)
            goods_data = {
                'gotoware_type': gotoware_type,
                'cost_price': '',
                'cg_price': 150,
                'w_price': 400,
                'gh_price': 600,
                'pai_price': '',
                'buy_price': 850,
                'original_price': '',
                'temai_price': '',
                'warehouseid': 51,
                'stores': 90,
                'typesid': 1,
                'goods_location': '',
                'fuId': '',
                'goods_level': 1,
                'level': 'F',
                'gong_code': '',
                'is_contract': 0,
                'send_time': 2,
                'adimg': '(binary)',
                'jiamengshop': 0,
                'bz': 1,
                'supply_type': '',
                'ware_remarks': '',
                'method_type': '',
                'con_name': 1337,
                'con_name_writ': '',
                'purchase_first_channel': 5,
                'purchase_second_channel': 21,
                'appraiser': 68,
                'con_busman': 0,
                'newbusiness': 0,
                'con_price': '',
                'con_care': '',
                'con_yang': '',
                'pid': 41,
                'first_category_id': 1,
                'zid': 25,
                'movement': '',
                'goods_series_default': '未知系列',
                'movement_model': '',
                'uploadimages': goods_image,
                'u_name': '接口自动化创建商品',
                'goods_selling': '',
                'goods_beizhu': '',
                'cheng': 1,
                'fitgroup': 2,
                'goods_year': '',
                'goods_year_default': '未知年份',
                'bdcontacts': '',
                'hpcontacts': '',
                'hzcontacts': '',
                'bag_number': '',
                'bag_chang': '',
                'pei_chang': '',
                'shi_chang': '',
                'watch_code': '',
                'watch_wtrap_factory': 1,
                'watch_clasp_factory': 1,
                'card_date': '',
                'jing': '',
                'watch_diameter': '',
                'wanzhou': '',
                'depth': '',
                'yi_colour': ''
            }  # 创建商品请求参数

            goods_res = self.sessionRequest.post(url=add_goods_url, headers=add_goods_header, data=goods_data)
            print(goods_res.text)

if __name__ == '__main__':

    PhonHu().add_goods(gotoware_type=2, num=1)
