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

##### [更多用法文档](https://github.com/abo123456789/re_helper) 




