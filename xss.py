import requests
 
# 从响应中检测payload是否有效
def check_reps(response,payload,type):
    index = response.find(payload)
    prefix = response[index-2:index-1]
    if type == 'Normal' and prefix != '=' and index >=0:
        return True
    elif type == 'Prop' and prefix == '=' and index >= 0:
        return True
 
    return False
 
 
# 实现xss扫描的主功能
def xss_scan(location):
    url = location.split('?')[0]
    param = location.split('?')[1].split('=')[0]  # 1代表第二部分
    with open('../dict/xss-payload.txt') as file:  # xss-payload.txt是字典文件需要自己去添加
        payload_list = file.readlines()
 
    for payload in payload_list:
        type = payload.strip().split(':',1)  #切分第一个：然后后面的直接删除
        payload = payload.strip().split(':', 1)[1]
        resp = requests.get(url=url,params={param:payload})
        if check_reps(resp.text,payload,type):
            print(f"此处存在xss漏洞：{payload}")
 
 
if __name__ == '__main__':
    xss_scan('http://192.168')
 
    # source = "hello woniu welcome woniu"
    # index = source.find('woniu')
    # print()