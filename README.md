### 最简单的正则表达式工具
#### 功能描述
* 无需会正则表达式即可快速上手使用 
                 
#### pip安装
```shell
pip install re_helper
```

##### 1.提取所有图片地址
```
    from re_helper import ReHelper
    source_str = '<img src="http://www.sss.com/a.png" alt="111"/>\n' \
                 '<img src="/a.png" alt="111"/>'
    src_list = ReHelper.extract_all_image_src(source_str)
    print(src_list)
    src_list2 = ReHelper.extract_all_image_src(source_str, pre_url='http://www.sss.com')
    print(src_list2)
```

##### 2.删除文本中的所有<![CDATA标签
```
    source_html = """
        // <![CDATA[ if (!window.location.search) { const pathname = window.location.pathname.split('/'); window.location.href = `/${pathname[1]}/${pathname[2]}?page=1&sort=price_discount,desc`; } // ]]> ผู้นำแห่งผลิตภัณฑ์เครื่องไฟฟ้าชั้นนำจากเนเธอแลนด์ที่มุ่งเน้นการพัฒนาผลิตภัณฑ์ที่ช่วยทำให้ชีวิตประจำวันของผู้คนสะดวกสบายขึ้น ไม่ว่าจะเป็นผลิตภัณฑ์เครื่องไฟฟ้าในครัวเรือน ผลิตภัณฑ์ดูแลร่างกาย ผลิตภัณฑ์ดูแลแม่และเด็ก และอีกมากมาย ให้ชีวิตทุกวันของคุณมีความสุข และสะดวกสบายด้วยผลิตภัณฑ์เครื่องไฟฟ้า PHILIPS
        """
    print(ReHelper.delete_cdata_label(source_html))
```

##### 3.删除文本中的换行和tab占位符
```
    print(ReHelper.delete_tab_and_br('123   456 9000\n \t 33\r\t222제조일자/유효기간:판매자에게 문의\n\t\t\t\t\t'))
```

##### 4.删除文本中的所有html标签
```
    source_s = "云云小坊 隱形內衣BRA 超黏款上薄下厚布面隱形胸罩膚色) <font color=#FF00CC><b>*隱形胸罩屬衛生用品，使用過請勿退貨*</font><br> | 膚A"
    print(ReHelper.delete_html_tag(source_s))
```

##### 5.提取文本中的百分数
```
    print(ReHelper.extract_percent('asdqqq 87.9%'))
```
##### 6.根据正则提取字符串中第一个匹配的元素
```
    print(ReHelper.extract_one_by_pattern("<p>(.*?)</p>", "<p>111111111111</p>", exclude=['<p>', '</p>']))
```

##### 7.匹配<script type="application/json"></script>中的元素
```
    sss = """
    <script type="application/json">{"number":123456}</script>
    """
    print(ReHelper.parse_application_json_script_data(sss))
```
##### 8.匹配数值类型价格
```
    print(ReHelper.get_price('Price:$10.18 ($0.28 / Count)'))
```

##### 9.其它例子
```python
    from re_helper import ReHelper
    ReHelper.extract_bsr_ranks('19 in Mobile Phone Projectors 19 in Mobile 335,899 in aaaa')
    ReHelper.extract_bsr_source_ranks('   580 en Jardin (Voir les 100 premiers en Jardin)   2 en Amazon Launchpad Échappées sauvages'
                               '   4 en Thermomètres pour barbecue   '
                               '7 en Amazon Launchpad Perles rares    ', 'en')
    source_str = '<img SRC="http://www.sss.com/a.png" alt="111"/><img src="/a.png" alt="111"/>'

    for s_str in [source_str, None, 'aa', '', 'img']:
        result = ReHelper.extract_one_by_pattern("<img(.*?)/>", s_str, exclude=['img', 'alt'])
        print(result)
    print(ReHelper.extract_one_by_pattern('NCC認證碼：(.*?)\r\n', '\r\n■ NCC認證碼：CCAO18LP0070T0\r\n\r\n<B>【配件說明】',
                                          exclude=['NCC認證碼：']))
    
    print(ReHelper.extract_videos_src(
        "<center><iframe src=\"https://www.youtube.com/embed/JUhoGRh6yec\" frameborder=\"0\" width=\"1000\" height=\"580\"></iframe></center>"))

    video_str = """
    "<p><strong><span style=\"font-size: medium; font-family: 細明體;\"><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">※本型號特別備註：小米9手機背後鏡頭設計過高，本產品提供的防護措施為產品六面/八角/十二邊之防護檢測通過，可有效的保護手機螢幕面的安全，</span><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">且須維持產品的手感，故無法將厚度製作高過鏡頭，殼套孔位會低於鏡頭，如背面落地則有可能</span><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">無法保護背面鏡頭處，敬請知悉</span></span></strong><strong><span style=\"font-size: medium; font-family: 細明體;\"><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">※</span></span></strong></p> <p><span style=\"font-size: medium; font-family: 細明體; color: #000080;\">【特色說明】</span></p> <p><span style=\"font-size: medium; font-family: 細明體; color: #000080;\">★美國軍事級標準防摔測試：高度122cm，6面8角12邊，共26下，自由落體摔機測試合格通過！&#160;</span></p> <p><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">★材質通過歐盟標準-環保無毒檢測－家人小孩使用更放心！</span></p> <p><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">★四角加強氣墊、墊高設計，防撞力更徹底！</span></p> <p><span style=\"font-size: medium; font-family: 細明體; color: #000080;\">★超越一般殼套的五倍超強防撞擊力！</span></p> <p><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">★正摔！側摔！爆摔！通通不用怕！</span></p> <p><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">★真正的硬漢等級防撞防摔手機殼！&#160;</span></p> <p><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">點我看『爆摔測試影片』</span></p> <p><iframe style=\"background-image: url('img/iframe.gif');\" src=\"https://www.youtube.com/embed/wKxP6Y98Dhg?rel=0\" frameborder=\"0\" width=\"560\" height=\"315\"></iframe></p> <p><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">點我看</span><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">『</span><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">正妹摔機影片</span><span style=\"color: #000080; font-family: 細明體; font-size: medium;\">』</span><span style=\"color: #000080; font-family: 細明體; font-size: medium;\"><br /></span></p> <p><iframe style=\"background-image: url('img/iframe.gif');\" src=\"https://www.youtube.com/embed/-chYBP2eUmw?rel=0\" frameborder=\"0\" width=\"560\" height=\"315\"></iframe></p> <p style=\"font-family: verdana, arial, sans-serif;\"><span style=\"font-size: large; font-family: 細明體;\"><strong><span style=\"color: #ff0000;\">【軍事防摔規範小教室】</span></strong></span></p> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\"><span style=\"color: #ff0000; font-size: medium; font-family: 細明體;\"><strong>Q：</strong><span style=\"background-color: #ffff00;\"><strong>什麼是美國軍方米爾MIL-STD-810G防摔測試？</strong></span></span></div> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\">&#160;</div> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\"><span style=\"font-family: 細明體; font-size: medium;\"><span style=\"color: #ff0000;\">Ａ：</span><span style=\"color: #ff0000;\"><span style=\"white-space: pre-wrap;\">意思是指《空間及陸用設備環境試驗方法》，此標準後成為軍事和工業部門環境試驗方法的準則。</span></span></span></div> <p style=\"font-family: verdana, arial, sans-serif;\"><span style=\"color: #ff0000; font-family: 細明體; font-size: medium; white-space: pre-wrap;\">測試的項目包含溫度.濕度.速度.防摔.防彈...等所有軍事需面臨之環境測試。</span></p> <p style=\"font-family: verdana, arial, sans-serif;\"><span style=\"color: #ff0000; font-family: 細明體; font-size: medium; white-space: pre-wrap;\">而我們的軍功防摔手機殼，就是通過其中的：</span></p> <p style=\"font-family: verdana, arial, sans-serif;\"><span style=\"font-family: 細明體; font-size: medium;\"><span style=\"color: #ff0000; white-space: pre-wrap;\">「MIL-STD-810G防摔測試－</span><strong><span style=\"color: #ff0000;\">高度122cm，6面8角12邊，共26下，自由落體摔機測試合格通過</span></strong><span style=\"color: #ff0000; white-space: pre-wrap;\">」項目！</span></span></p> <p style=\"font-family: verdana, arial, sans-serif;\"><span style=\"color: #ff0000; font-family: 細明體; font-size: medium; white-space: pre-wrap;\">此標準目前也已被世界各國所認可，其不僅在軍品，同時也在工業產品中被廣泛所接受和採納。</span></p> <p style=\"font-family: verdana, arial, sans-serif;\"><span style=\"color: #ff0000; font-family: 細明體; font-size: medium; white-space: pre-wrap;\">也包含使用在手機配件中， 例如：犀牛盾、UGA手機殼等就是經過軍事級防摔測試的典型例子</span></p> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\">&#160;</div> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\"><span style=\"font-family: 細明體;\"><span style=\"font-size: large;\"><span style=\"color: #000088;\"></span><span style=\"font-size: medium;\"><span style=\"background-color: #ffff00; color: #ff0000;\"><strong>Q：什麼是「6面、8角、12邊」?</strong></span><span style=\"color: #000088;\">&#160;</span></span></span></span></div> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\"><span style=\"color: #ff0000; font-family: 細明體; font-size: medium; white-space: pre-wrap;\">6面：正面.背面.上下左右側面四邊</span></div> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\"><span style=\"font-size: medium; font-family: 細明體; color: #ff0000;\"><span style=\"white-space: pre-wrap;\">8角：前面四角，背面四角 </span></span></div> <div style=\"color: #3b3b3b; font-family: 新細明體; font-size: 16px;\"><span style=\"font-size: medium; font-family: 細明體; color: #ff0000;\"><span style=\"white-space: pre-wrap;\">12邊：側面三角度，共4邊，總共12邊角度</span></span></div>"
    """
    print(ReHelper.extract_videos_src(video_str))

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

    print(ReHelper.get_first_number('11222www2qq'))
    
    print(ReHelper.get_array_first(['1234 ', '5678']))
    
    print(ReHelper.parse_email('123 rew 123@qq.com 111ddddd as@yy.com qq.com'))

    print(ReHelper.parse_chinese('中123中国人chinese....!@'))
```



