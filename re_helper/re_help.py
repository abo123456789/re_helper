#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 15:47
# @Author  : CC
# @File    : re_helper.py
import re
import urllib.parse


class ReHelper(object):

    @staticmethod
    def extract_all_image_src(str_source: str, pre_url: str = '') -> list:
        """
        extract all img src from str
        """
        images = []
        if str_source:
            images = re.findall(r'<img.*?src="(.*?)".*?/?>', str_source, flags=re.IGNORECASE)
            if len(images) == 0:
                images = re.findall(r'<img.*?src=\"(.*?)\".*?/?>', str_source, flags=re.IGNORECASE)
        if pre_url:
            return [urllib.parse.urljoin(pre_url, image) for image in images if image]
        else:
            return images

    @staticmethod
    def extract_videos_src(str_source: str) -> list:
        if str_source:
            return re.findall(r'<iframe.*?src="(.*?)".*?/?>', str_source, flags=re.IGNORECASE)
        return []

    @staticmethod
    def extract_one_by_pattern(pattern: str, str_source: str, exclude: list = None) -> [str, None]:
        """
        match one result from str
        """
        if str_source and pattern:
            match_group = re.search(pattern, str_source.strip(), flags=re.IGNORECASE)
            if match_group:
                if exclude:
                    rs = match_group.group()
                    if exclude:
                        for exists_str in exclude:
                            rs = rs.replace(exists_str, '')
                    return str.strip(rs)
                else:
                    return match_group.group()
        return None

    @staticmethod
    def extract_jsonp_result(str_source: str) -> [str, None]:
        # return ReHelper.extract_one_by_pattern(r'\((.*?)\);}', str_source, ['(', ');}'])
        source = ReHelper.extract_one_by_pattern(r'\((.*?)\);}catch', str_source)
        if source:
            return source.replace('(', '', 1).replace(');}catch', '')
        return None

    @staticmethod
    def extract_jsonp_result(str_source: str) -> [str, None]:
        source = ReHelper.extract_one_by_pattern(r'\((.*?)\);}catch', str_source)
        if source:
            return source.replace('(', '', 1).replace(');}catch', '')
        return None

    @staticmethod
    def extract_jsonp_method(str_source: str) -> [str, None]:
        return ReHelper.extract_one_by_pattern(r'try{(.*?)\(', str_source, ['try{', '('])

    @staticmethod
    def delete_cdata_label(str_source: str) -> [str, None]:
        if str_source:
            re_cdata = re.compile(r'(//<!\[CDATA\[[^>]*//\]\]>)|(// <!\[CDATA\[[^>]*// \]\]>)', re.I)
            return re_cdata.sub('', str_source)
        return None

    # @staticmethod
    # def delete_html_tag_and_content(str_source: str):
    #     if str_source:
    #         re_cdata = re.compile(r'<(\S*?) [^>]*>.*?</\1>|<.*?/>|<br>', re.I)
    #         return re_cdata.sub("", str_source, )
    #     return str_source

    @staticmethod
    def delete_html_tag(str_source: str):
        """
        删除文本中的html标签
        """
        if not str_source:
            return str_source
        re_cdata = re.compile(r'<[^>]+>', re.I)
        return re_cdata.sub("", str_source, )

    @staticmethod
    def delete_tab_and_br(str_source: str) -> [str, None]:
        if str_source:
            rt = re.compile(r'[\r\n\t<br>]', re.I).sub('', str_source)
            if rt:
                return ''.join(rt.split())
        return None

    @staticmethod
    def delete_br(str_source: str) -> [str, None]:
        if str_source:
            rt = re.compile(r'[\r\n\t]', re.I).sub('', str_source)
            if rt:
                return rt.replace("  ", "")
        return None

    @staticmethod
    def convert_array_2_str(array_str: list) -> [str, None]:
        """
        将数组元素转行字符串,并删除字符串中的空白和换行
        :param array_str: 字符串数组
        :return: str
        """
        if array_str:
            if isinstance(array_str, list):
                return ReHelper.delete_tab_and_br(''.join(array_str))
        return None

    @staticmethod
    def get_array_first(array_str: list) -> [str, None]:
        """
        获取数组中的第一个元素
        :param array_str:字符串数组
        :return:
        """
        if array_str:
            if isinstance(array_str, list):
                return array_str[0].strip()
        return None

    @staticmethod
    def get_price(price_str: str) -> [str, None]:
        # €|£|¥|$
        price_obj = re.search(r'\d+\.\d+|\d+', price_str)
        if price_obj:
            return price_obj.group()
        return ''

    @staticmethod
    def delete_comment_row(str_source: str) -> [str, None]:
        if str_source:
            re_cdata = re.compile(r'\/\/(.*)', re.I)
            return re_cdata.sub('', str_source)
        return None

    @staticmethod
    def extract_brackets_result(str_source: str) -> [str, None]:
        source = ReHelper.extract_one_by_pattern("\\(.*?\\)", str_source)
        if source:
            return source.replace('(', '', 1).replace(')', '')
        return None

    @staticmethod
    def extract_percent(str_source: str):
        source = ReHelper.extract_one_by_pattern(r"(\d+)%|(\d+\.\d+)%", str_source)
        return source

    @staticmethod
    def extract_bsr_ranks(bsr_str: str, split_str='in') -> list:
        if not bsr_str:
            return []
        bsr_str = bsr_str.strip()
        bsr_numbers = re.findall(fr'\d+,?\d*\s+{split_str}', bsr_str)
        bsr_types = re.split(fr'\d+,?\d*\s+{split_str}', bsr_str)
        bsr_types = [bsr_type.strip() for bsr_type in bsr_types if bsr_type and bsr_type.strip()]
        result = []
        for i in range(min(len(bsr_numbers), len(bsr_types))):
            bsr_number = bsr_numbers[i].replace(',', '').replace(split_str, '').strip()
            result.append((bsr_types[i], bsr_number))
        return result

    @staticmethod
    def extract_bsr_source_ranks(bsr_str: str, split_str='in') -> list:
        if not bsr_str:
            return []
        bsr_str = bsr_str.strip()
        bsr_str = bsr_str.replace('Classement des meilleures ventes d\'Amazon :', '')
        bsr_numbers = re.findall(fr'\d+,?\d*\s+{split_str}', bsr_str)
        bsr_types = re.split(fr'\d+,?\d*\s+{split_str}', bsr_str)
        bsr_types = [bsr_type.strip() for bsr_type in bsr_types if bsr_type and bsr_type.strip()]
        rs = [v + ' ' + d for v, d in zip(bsr_numbers, bsr_types)]
        return rs

    @staticmethod
    def get_first_number(s_str: str):
        if not s_str:
            return None
        res = re.search(r'\d+', s_str)
        if res:
            return res.group()
        return None

    @staticmethod
    def parse_application_ld_script_data(s_str: str):
        """
        解析<script type="application/ld+json"></script>类型数据
        <script type="application/ld+json" data-rh="true">123456</script>
        """
        return ReHelper.extract_one_by_pattern(r'application/ld[^>]*>[\s\S]*?</[^>]*script>',
                                               s_str,
                                               exclude=['</script>',
                                                        'application/ld+json">',
                                                        'application/ld+json" data-rh="true">'])

    @staticmethod
    def parse_application_json_script_data(s_str: str):
        """
        解析<script type="application/json"></script>类型数据
        <script type="application/json">{"number":123456}</script>
        """
        s_list = re.findall(r'application/json[^>]*>[\s\S]*?</[^>]*script>', s_str)
        return [s.strip("application/json\">").strip("</script>").strip()
                for s in s_list if s]

    @staticmethod
    def parse_email(s_str: str) -> list:
        if not s_str:
            return []
        return re.findall(r"[\w+]{1,20}@[\w+]{1,20}\.[\w+]{1,3}", s_str)

    @staticmethod
    def parse_chinese(s_str: str) -> [str, None]:
        if not s_str:
            return None
        o_results = re.findall(r"[\u4E00-\u9FA5]+", s_str)
        if o_results:
            return ''.join(o_results)
        return None


if __name__ == '__main__':
    pass
    ReHelper.extract_bsr_ranks('19 in Mobile Phone Projectors 19 in Mobile 335,899 in aaaa')
    print(ReHelper.extract_percent('asdqqq 87.9%'))
    source_str = '<img src="http://www.sss.com/a.png" alt="111"/>\n' \
                 '<img src="/a.png" alt="111"/>'
    src_list = ReHelper.extract_all_image_src(source_str)
    print(src_list)
    src_list2 = ReHelper.extract_all_image_src(source_str, pre_url='http://www.sss.com')
    print(src_list2)

    for s_str in [source_str, None, 'aa', '', 'img']:
        result = ReHelper.extract_one_by_pattern("<img(.*?)/>", s_str, exclude=['img', 'alt'])
        print(result)
    print(ReHelper.extract_one_by_pattern("<p>(.*?)</p>", "<p>111111111111</p>", exclude=['<p>', '</p>']))
    print(ReHelper.extract_one_by_pattern('NCC認證碼：(.*?)\r\n', '\r\n■ NCC認證碼：CCAO18LP0070T0\r\n\r\n<B>【配件說明】',
                                          exclude=['NCC認證碼：']))
    source_html = """
        // <![CDATA[ if (!window.location.search) { const pathname = window.location.pathname.split('/'); window.location.href = `/${pathname[1]}/${pathname[2]}?page=1&sort=price_discount,desc`; } // ]]> ผู้นำแห่งผลิตภัณฑ์เครื่องไฟฟ้าชั้นนำจากเนเธอแลนด์ที่มุ่งเน้นการพัฒนาผลิตภัณฑ์ที่ช่วยทำให้ชีวิตประจำวันของผู้คนสะดวกสบายขึ้น ไม่ว่าจะเป็นผลิตภัณฑ์เครื่องไฟฟ้าในครัวเรือน ผลิตภัณฑ์ดูแลร่างกาย ผลิตภัณฑ์ดูแลแม่และเด็ก และอีกมากมาย ให้ชีวิตทุกวันของคุณมีความสุข และสะดวกสบายด้วยผลิตภัณฑ์เครื่องไฟฟ้า PHILIPS
        """
    print(ReHelper.delete_cdata_label(source_html))

    print(ReHelper.extract_videos_src(
        "<center><iframe src=\"https://www.youtube.com/embed/JUhoGRh6yec\" frameborder=\"0\" width=\"1000\" height=\"580\"></iframe></center>"))

    video_str = """
    "<p><strong><span style=\"font-size: medium; font-family: 細明體;\"><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">※本型號特別備註：小米9手機背後鏡頭設計過高，本產品提供的防護措施為產品六面/八角/十二邊之防護檢測通過，可有效的保護手機螢幕面的安全，</span><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">且須維持產品的手感，故無法將厚度製作高過鏡頭，殼套孔位會低於鏡頭，如背面落地則有可能</span><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">無法保護背面鏡頭處，敬請知悉</span></span></strong><strong><span style=\"font-size: medium; font-family: 細明體;\"><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">※</span></span></strong></p> <p><span style=\"font-size: medium; font-family: 細明體; color: #000080;\">【特色說明】</span></p> <p><span style=\"font-size: medium; font-family: 細明體; color: #000080;\">★美國軍事級標準防摔測試：高度122cm，6面8角12邊，共26下，自由落體摔機測試合格通過！&#160;</span></p> <p><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">★材質通過歐盟標準-環保無毒檢測－家人小孩使用更放心！</span></p> <p><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">★四角加強氣墊、墊高設計，防撞力更徹底！</span></p> <p><span style=\"font-size: medium; font-family: 細明體; color: #000080;\">★超越一般殼套的五倍超強防撞擊力！</span></p> <p><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">★正摔！側摔！爆摔！通通不用怕！</span></p> <p><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">★真正的硬漢等級防撞防摔手機殼！&#160;</span></p> <p><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">點我看『爆摔測試影片』</span></p> <p><iframe style=\"background-image: url('img/iframe.gif');\" src=\"https://www.youtube.com/embed/wKxP6Y98Dhg?rel=0\" frameborder=\"0\" width=\"560\" height=\"315\"></iframe></p> <p><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">點我看</span><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">『</span><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">正妹摔機影片</span><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">』</span><span style=\"color: #000080; font-family: 細明體; font-size: medium;\"><br /></span></p> <p><iframe style=\"background-image: url('img/iframe.gif');\" src=\"https://www.youtube.com/embed/-chYBP2eUmw?rel=0\" frameborder=\"0\" width=\"560\" height=\"315\"></iframe></p> <p style=\"font-family: verdana, arial, sans-serif;\"><span style=\"font-size: large; font-family: 細明體;\"><strong><span style=\"color: #ff0000;\">【軍事防摔規範小教室】</span></strong></span></p> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\"><span style=\"color: #ff0000; font-size: medium; font-family: 細明體;\"><strong>Q：</strong><span style=\"background-color: #ffff00;\"><strong>什麼是美國軍方米爾MIL-STD-810G防摔測試？</strong></span></span></div> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\">&#160;</div> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\"><span style=\"font-family: 細明體; font-size: medium;\"><span style=\"color: #ff0000;\">Ａ：</span><span style=\"color: #ff0000;\"><span style=\"white-space: pre-wrap;\">意思是指《空間及陸用設備環境試驗方法》，此標準後成為軍事和工業部門環境試驗方法的準則。</span></span></span></div> <p style=\"font-family: verdana, arial, sans-serif;\"><span style=\"color: #ff0000; font-family: 細明體; font-size: medium; white-space: pre-wrap;\">測試的項目包含溫度.濕度.速度.防摔.防彈...等所有軍事需面臨之環境測試。</span></p> <p style=\"font-family: verdana, arial, sans-serif;\"><span style=\"color: #ff0000; font-family: 細明體; font-size: medium; white-space: pre-wrap;\">而我們的軍功防摔手機殼，就是通過其中的：</span></p> <p style=\"font-family: verdana, arial, sans-serif;\"><span style=\"font-family: 細明體; font-size: medium;\"><span style=\"color: #ff0000; white-space: pre-wrap;\">「MIL-STD-810G防摔測試－</span><strong><span style=\"color: #ff0000;\">高度122cm，6面8角12邊，共26下，自由落體摔機測試合格通過</span></strong><span style=\"color: #ff0000; white-space: pre-wrap;\">」項目！</span></span></p> <p style=\"font-family: verdana, arial, sans-serif;\"><span style=\"color: #ff0000; font-family: 細明體; font-size: medium; white-space: pre-wrap;\">此標準目前也已被世界各國所認可，其不僅在軍品，同時也在工業產品中被廣泛所接受和採納。</span></p> <p style=\"font-family: verdana, arial, sans-serif;\"><span style=\"color: #ff0000; font-family: 細明體; font-size: medium; white-space: pre-wrap;\">也包含使用在手機配件中， 例如：犀牛盾、UGA手機殼等就是經過軍事級防摔測試的典型例子</span></p> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\">&#160;</div> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\"><span style=\"font-family: 細明體;\"><span style=\"font-size: large;\"><span style=\"color: #000088;\"></span><span style=\"font-size: medium;\"><span style=\"background-color: #ffff00; color: #ff0000;\"><strong>Q：什麼是「6面、8角、12邊」?</strong></span><span style=\"color: #000088;\">&#160;</span></span></span></span></div> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\"><span style=\"color: #ff0000; font-family: 細明體; font-size: medium; white-space: pre-wrap;\">6面：正面.背面.上下左右側面四邊</span></div> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\"><span style=\"font-size: medium; font-family: 細明體; color: #ff0000;\"><span style=\"white-space: pre-wrap;\">8角：前面四角，背面四角 </span></span></div> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\"><span style=\"font-size: medium; font-family: 細明體; color: #ff0000;\"><span style=\"white-space: pre-wrap;\">12邊：側面三角度，共4邊，總共12邊角度</span></span></div>"
    """
    print(ReHelper.extract_videos_src(video_str))

    source_s = "云云小坊 隱形內衣BRA 超黏款上薄下厚布面隱形胸罩膚色) <font color=#FF00CC><b>*隱形胸罩屬衛生用品，使用過請勿退貨*</font><br> | 膚A"
    print(ReHelper.delete_html_tag(source_s))

    ss = 'try{jsonp_prod({"DECH2M-A9009R0X3-000":{"Seq":21933300,"Id":"DECH2M-A9009R0X3-000","Name":"\u3010\u7f8e\u6a02Medela\u3011\u5438\u4e73\u5668\u5c08\u7528\u514d\u624b\u6301\u80f8\u8863(\u5438\u4e73\u5668\u914d\u4ef6 \u81ea\u7531\u6a5f\/\u6f22\u5821\u6a5f\/\u667a\u6167\u578b\/\u91ab\u9662\u5c08\u7528\u578b\u96d9\u908a\u64e0\u4e73\u5c08\u7528)","Nick":"\u3010\u7f8e\u6a02Medela\u3011\u5438\u4e73\u5668\u5c08\u7528\u514d\u624b\u6301\u80f8\u8863(\u5438\u4e73\u5668\u914d\u4ef6 \u81ea\u7531\u6a5f\/\u6f22\u5821\u6a5f\/\u667a\u6167\u578b\/\u91ab\u9662\u5c08\u7528\u578b\u96d9\u908a\u64e0\u4e73\u5c08\u7528)","Store":"DECH2M","PreOrdDate":"","SpeOrdDate":"","Price":{"M":2400,"P":2400,"Prime":""},"Discount":0,"Pic":{"B":"\/items\/DECH2MA9009R0X3\/000001_1547950014.jpg","S":"\/items\/DECH2MA9009R0X3\/000002_1547950014.jpg"},"Weight":0.16,"ISBN":"","Qty":0,"Bonus":0,"isBig":0,"isSpec":1,"isCombine":0,"isDiy":0,"isRecyclable":0,"isCarrier":0,"isMedical":0,"isBigCart":1,"isSnapUp":0,"isDescAndIntroSync":0,"isFoodContents":0,"isHuge":0,"isEnergySubsidy":0,"isPrimeOnly":0,"isPreOrder24h":0,"isWarranty":0,"isLegalStore":1,"isFresh":0,"isBidding":0,"isSet":0,"Volume":{"Length":19,"Width":11,"Height":6},"isArrival24h":1,"isETicket":0,"ShipType":"Consign","isO2O":0}});}catch(e){if(window.console){console.log(e);}}'
    print(ReHelper.extract_jsonp_result(ss))

    st = 'try{jsonp_prod({"DECH2M-A9009R0X3-000":a;)}1222;)}catch{}'
    print(ReHelper.extract_jsonp_result(st))

    for ar in [['  123 456'], [], None, '123']:
        print(ReHelper.convert_array_2_str(ar))

    tt = [
        '\n            \n            Apply to cleansed face on day or night as needed to combat moisture depletion of normal to oily skin.\n            \n            \n\n\n\n\n\n\n\n            \n            \n        ']
    print(ReHelper.convert_array_2_str(tt))

    ss = """
    {
            // APP 여부(Y,N) : 앱일 경우 Y, 모웹은 N
            appYn: "N",
            // Header
            header: {
                type: "default"
            },
            isLogin : false
    }
        """
    print(ReHelper.delete_comment_row(ss))

    print(ReHelper.extract_brackets_result('000465(명품화장품 랑콤)'))

    print(ReHelper.delete_tab_and_br('123   456 9000\n \t 33\r\t222제조일자/유효기간:판매자에게 문의\n\t\t\t\t\t'))

    print(ReHelper.get_first_number('11222www2qq'))

    tt = '<script type="application/ld+json" data-rh="true">123456</script>'
    print(ReHelper.parse_application_ld_script_data(tt))

    print(ReHelper.get_array_first(['1234 ', '5678']))

    sss = """
    <script type="application/json">{"number":123456}</script>
    """
    print(ReHelper.parse_application_json_script_data(sss))

    print(ReHelper.parse_email('123 rew 123@qq.com 111ddddd as@yy.com qq.com'))

    print(ReHelper.parse_chinese('中123中国人chinese....!@'))

    print(ReHelper.get_price('Price:$10.18 ($0.28 / Count)'))
