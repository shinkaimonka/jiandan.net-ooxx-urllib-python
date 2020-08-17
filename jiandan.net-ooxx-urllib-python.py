import urllib.request
import os
import base64
import easygui
import datetime

now_time = datetime.datetime.now().strftime("%Y%m%d")
print("当前日期是%s" %now_time)
mkdir_choise = 0


def base64plus(b64pstr):
    by64p = b64pstr.encode("utf-8")
    b64pstr =base64.b64encode(by64p) 
    b64pstr = str(b64pstr)[2:-1]
    return b64pstr


def get_url(now_page):
    page = int(now_page) - 1
    print(page)
    if page >= 1 :      
        base64_enplus = "%s - %s" %(now_time,page)
        base64_page = base64plus(base64_enplus)
        nextpage_url = "http://jiandan.net/ooxx/%s#comments" %base64_page
        #nextpage_url = "http://jiandan,net/ooxx/",base64plus(str(now_time)+"-"+str(page)),"#comments"
        return nextpage_url
    else:
        return "-1"

    
    
def open_url(url="http://jiandan.net/ooxx/"):
    req = urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0")
    response = urllib.request.urlopen(req)
    html = response.read()
    return html



def get_nowpage(url="http://jiandan.net/ooxx/"):
    html = open_url(url).decode("utf-8")
    finda = html.find("current-comment-page")
    findb = html.find("]",finda)
    print(finda)
    print(findb)
    find_nowpage =html[finda+23 : findb]
    return find_nowpage

    
def find_imgs(url="http://jiandan.net/ooxx/"):
    global global_url
    global_url = url
    print("find_imgs调用开始")
    html = open_url(url).decode("utf-8")
    img_addrs = [ ]
    
    imgs_urla = html.find("img src=")

    while imgs_urla != -1:
        
        print("调用while")
        print(imgs_urla)
        b = html.find("jpg",imgs_urla,imgs_urla+255)

        if b != -1:
            img_addrs.append(html[imgs_urla+11 : b+3])
            
            print(img_addrs)
            b = imgs_urla + 9
            imgs_urla = html.find("img src=",b)
        elif b == -1:
            imgs_urla = -1
            
        a = html.find("img src=" , b)
        print(a)
    return img_addrs
        

def save_imgs(img_addrs):
    global mkdir_choise
    if mkdir_choise == 0:      
        try:
            os.mkdir("OOXX")
        except:
            pass
        mkdir_choise += 1
        os.chdir("OOXX")
    print("save中")
    for each in img_addrs:
        
        print(each)
        print("for中")
        
        each3 = "http://" + each
        print(each3)
        print(each,"是each")
        jpgname1 = each.rfind("/") + 1
        jpgname2 = each.find(".jpg")
        
        print(jpgname1)
        print(jpgname2)

        jpgname = each[jpgname1 : jpgname2] + ".jpg"
        print(jpgname)
        with open(jpgname,"wb") as f:
            img = open_url(each3)
            #print(img)
            f.write(img)
 

        
stop_msg = False       
        
#if  __name__ == '__main__':
    #find_imgs = find_imgs()
    #save_imgs(find_imgs)

temp_url = ""



def command():
    img_addrs = find_imgs()
    save = save_imgs(img_addrs)
    while_of = True
    global stop_msg
    if stop_msg == True:
        #SystemExit()
        print(stop_msg)
        pass
        easygui.msgbox(msg='停止成功\n爬取的数据在/OOXX文件夹\n\nby shinkaimonka', title=' 停止成功', ok_button=' OK ', image=None, root=None)
    else:
        print(global_url)
        find_nowpage = get_nowpage(global_url)
    
    
 
        while True:
            
            nextpage_url = get_url(find_nowpage)
            print(nextpage_url)
            if stop_msg == True:
                print(stop_msg)
                easygui.msgbox(msg='停止成功\n爬取的数据在/OOXX文件夹\n\nby shinkaimonka', title=' 停止成功', ok_button=' OK ', image=None, root=None)
                break
            if nextpage_url == "-1":
              
                while_of = False
                break
            else:
                img_addrs = find_imgs(nextpage_url)

                finish = save_imgs(img_addrs)

                find_nowpage = get_nowpage(global_url)
    pass
import threading
import sys

def operation():
    choices = easygui.buttonbox(msg='运行中\n\n\n注:终止后请稍等片刻,将在本页图片下载完成后终止', title='jiandan.net/ooxx爬虫-运行中', choices=('stop','隐藏'), image=None)
    if choices == "stop":
       global stop_msg
       stop_msg = True
       pass



if __name__ == '__main__':
    choices = easygui.ccbox(msg='煎蛋网爬虫,202008测试可用,链接base64编码\nby shinkaimonka\n注:会在工作目录创建OOXX文件夹 ', title='http://jiandan.net/ooxx 爬虫 ', choices=(' 启动 ', ' 退出 '), image=None)
    print(choices)
    if choices == True:
        threads = [ ]
        t1 = threading.Thread(target = operation)
        t2 = threading.Thread(target = command)
        #t3 = threading.Thread(target = )

        t1.setDaemon(True)
        t1.daemon
        t1.start()
        t2.start()
    else:
        pass
                                    
                                    
                                                                              

            
