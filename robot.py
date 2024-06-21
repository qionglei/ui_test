import sys

import requests


class WeChat:
    def crowd_robot(self, message1,message2,message3):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=00da84d7-2c22-4cf0-98b2-65cfd514db07'

        # 发送普通文本
        # data = {
        #     "msgtype": "text",
        #     "text": {
        #         "content": f"{message}"
        #     }
        # }

        # 含有图片链接
        # data = {
        #     "msgtype": "news",
        #     "news": {
        #         "articles": [{
        #             "title": "中秋节礼品领取",
        #             "description": "今年中秋节公司有豪礼相送",
        #             "url": "www.qq.com",
        #             "picurl": "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
        #
        #         }]
        #     }
        # }

        # 有颜色的info
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": "<font color=\"warning\">%s</font> \n <font color=\"info\">%s</font> \n <font color=\"comment\">%s</font>" % (message1, message2,message3)
            }
        }

        response = requests.post(url=url, json=data)
        print(response.text)


# if __name__ == '__main__':
#     wx = WeChat()
#     # message = "测试通过python调用api\n hello world"
#
#     message1=str(sys.argv[0])
#     message2 = str(sys.argv[1])
#     message3 = str(sys.argv[1])
#
#     wx.crowd_robot(message1,message2,message3)
