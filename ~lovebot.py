import ch
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as urlreq
from cleverbot import Cleverbot
from datetime import datetime, timedelta
from time import sleep
import json
import os
from selenium.webdriver.chrome.options import Options
import base64
from base64 import b64encode
import html
import pickle
from requests.auth import HTTPBasicAuth
from urllib.request import Request, urlopen
import re
from HTMLParser import HTMLParser
from xml.etree.ElementTree import XML
from pasteee import Paste
import random
from langdetect import detect_langs
from random_words import RandomWords
import traceback
from watson_developer_cloud import LanguageTranslatorV2
import codecs
import urllib
import requests
import time

print("Bot Started At ",time.ctime())
trigger = False
#file = open("monitor.txt","w")

def msg(args):
    return "<b>%s</b>" % (args)

def write(msg):
    #file = open("monitor.txt","wb")
    file.write('%s\n' % msg)
    #file.close()

#def rs_bot(room):
    #os.system("taskkill /im python.exe /f /t")
    #os.system("start \"C:\\Python34\\python.exe\" \"C:\\Users\\Devin\\Desktop\\chatbot\\lovebot.py")

def get_profiletext_info(args):
    pt = []
    for x in BeautifulSoup(requests.get("http://" + args + ".chatango.com/").text, "html.parser").findAll("span", {
        "class": "profile_text"}):
        pt.append(x.text.strip())
    return pt

def pastee(desc, text):
  try:  
    param = {'key':'your api key','description':desc,'language':'plain','paste':text,'format':'simple'}
    response = requests.post("https://paste.ee/api", data=param, verify=True)
    rawresp = str(response.content).replace("b'","").replace("'","").replace("/p/","/r/")
    return rawresp
  except Exception as e:
      return str(e)

def ghost(text):
    try:
            url = "https://ghostbin.com/paste/new"
            data = {'text':args, 'lang':'text'}
            response = requests.post(url, data=data, headers={"User-Agent":"Mozilla/5.0"})
            room.message(msg(response.url), True)
    except Exception as e:
        room.message(str(e))
        

def stab(text):
    try:
            url = "https://killr.io/create"
            data = {'code':args}
            response = requests.post(url, data=data, headers={"User-Agent":"Mozilla/5.0"}, verify=False)
            jok = json.loads(response.text)
            result = "https://killr.io/"+str(jok['slug'])+"/raw"
            return result
            #room.message(msg("https://killr.io/"+str(jok['slug'])+"/raw"), True)
    except Exception as e:
            return str(e)

def haste(text):
    try:
            url = "https://hastebin.com/documents"
            data = {'text':args}
            response = requests.post(url, data=args, headers={"User-Agent":"Mozilla/5.0"})
            jok = json.loads(response.text)
            result = "https://hastebin.com/"+str(jok['key'])
            return result
    except Exception as e:
            return str(e)
i=0                                                 
class lovebot(ch.RoomManager, ch.Room):
  try:  
    def onInit(self):
        self.setNameColor("CC33CC")
        self.setFontColor("B48AC1")
        self.setFontFace("1")
        self.setFontSize(11)
        self.enableBg()

    def updatecmd(self,string):
        cmds.clear()
        thefile = open('cmd.txt', 'r')
        for e in thefile:
            cmds.append(e.strip())
        thefile.flush()    
        thefile.close()
        thefile = open('cmd.txt', 'w')
        cmds.append(string)
        #thefile.truncate()
        for item in cmds:
            thefile.write("%s\n" % item)
        thefile.close()    

    #def onJoin(self, room, user):
        #if user.name.lower() in selecteduser:
            #room.message(msg(user.name.title()+" is here @(Username)"), True)

    def onConnect(self,room):
        self.enableBg()
        print("Hello lovely peoples of "+room.name)
        #room.message(msg("Lovebotty is here !"), True)
    
    def find(self):    
        for x in rooms:
            if ("(Username)" or "bungyoi" or "hackabot") in self.getRoom(str(x))._userlist:
                return str(x).lower()
        
    lurk = False
    stalkroom = '?'
    thisroom = '?'
    stalkuser = '?'
    lurkuser = False
    def onMessage(self, room, user, message):
        global lurk
        global stalkroom
        global thisroom
        global trigger
        global i
        try:    
         print(codecs.unicode_escape_decode("[{0}] {1}: {2}".format(room.name, user.name.title(), message.body)))
         if user.name.lower() != "lovebotty" and room.name.lower() == stalkroom and lurk == True:  
            self.getRoom(thisroom).message(msg("{"+room.name.title()+"} : "+"["+user.name.title()+"] : "+message.body), True)
             
         #write(user.name.title()+" : "+message.body)
        except Exception as e:
             #room.message(str(e))   
             #print("Purroblem I died #RIP")
             pass           
        try:
            cmd, args = message.body.split(" ",1)
        except:
            cmd, args = message.body, ""

        try:
            if cmd[0] == "$":
              prfx = True
              cmd = cmd[1:]
            else:
              prfx = False
        except:
            print("I died again")
        #if user.name.lower() != "lovebotty":
            #self.getRoom("mabottesting").message(user.name+" : "+message.ip)    
        com = message.body
        var = com.split(maxsplit=1)
        #Command talk
        try:
            try:
                if var[0] == "@username":
                    key = "Your Api Key"
                    cs = '?'
                    if len(args)>0:
                        if i == 0:
                            url = "https://www.cleverbot.com/getreply?key="+key+"&input="+args
                            response = requests.get(url)
                            cs = json.loads(response.text)['cs']
                            i = i + 1
                            room.message(msg("How are you ?"+" @"+user.name.title()),True)  
                        else:
                            url = "https://www.cleverbot.com/getreply?key="+key+"&input="+args+"&cs="+cs+"&callback=ProcessReply"
                            response = requests.get(url)
                            output = json.loads(response.text)["output"]
                            print(response.text)
                            room.message(msg(output)+" @"+user.name.title(), True)  
                    else:
                        room.message("What do you need?"+" @<b>%s</b>" %(user.name.title()), True)
            except Exception as e:
                print(str(e))
                self.pm.message(ch.User("(Username)"), "[PM from "+room.name+" by "+user.name+"] : "+str(e))
                if var[0] == "@username":
                    key = "Your Api Key"
                    cs = '?'
                    if len(args)>0:
                        if i == 0:
                            url = "https://www.cleverbot.com/getreply?key="+key+"&input="+args
                            response = requests.get(url)
                            cs = json.loads(response.text)['cs']
                            i = i + 1
                            room.message(msg("How are you ?"+" @"+user.name.title()),True)  
                        else:
                            url = "https://www.cleverbot.com/getreply?key="+key+"&input="+args+"&cs="+cs+"&callback=ProcessReply"
                            response = requests.get(url)
                            output = json.loads(response.text)["output"]
                            print(response.text)
                            room.message(msg(output)+" @"+user.name.title(), True)  
                    else:
                        room.message("What do you need?"+" @<b>%s</b>" %(user.name.title()), True)
        except Exception as e:
            print(str(e))
            
        #Command say
        if cmd.lower() == "say" and prfx:
            if user.name.lower() in adminuser:
                room.message(msg(args), True)
            else:
                room.message(msg(user.name.title()+" told me to say : "+args), True)

        #Command stop bot
        elif cmd.lower() == "bye" and prfx and user.name.lower() in adminuser:
            room.message(msg("Bye lovely peoples !"), True)
            self.setTimeout(1, self.leaveRoom, room.name)    

        #Command pm
        elif cmd.lower() == "pm" and prfx and len(args)>0 and user.name.lower() in adminuser:
          try:  
            var = args.split(maxsplit=1)
            self.pm.message(ch.User(var[0]), "[PM from "+room.name+" by "+user.name+"] : "+var[1])
            room.message(msg("PM Sent to "+var[0]), True)    
          except:
              room.message(msg("OOPS something went wrong!"), True)

        #Command yt
        elif cmd.lower() == "yt" and prfx and len(args)>0:
         try: 
            search = args.split()
            url = urlreq.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&MaxResults=1&key=(YOur APi Key)" % "+".join(search))
            udict = url.read().decode('utf-8')
            data = json.loads(udict)
            #print(str(data))
            rest = []
            for f in data["items"]:
             rest.append(f)
            d = rest[0]
            link = "http://www.youtube.com/watch?v="+d["id"]["videoId"]
            videoid = d["id"]["videoId"]
            title = d["snippet"]["title"]
            uploader = d["snippet"]["channelTitle"]
            #room.message(link)
            room.message("<b>%s</b> \r<b>Title :</b> <b>%s</b>" % (link,title), True)
            return
         except:
            room.message(msg("Video Not Found !"), True)

        #Command takeacc
        elif cmd.lower() == "takeacc" and prfx and len(args)>0 and user.name.lower() in adminuser: 
            rw = RandomWords()  
            email = rw.random_word()+"@hotmail.com"
            usern = args
            if user.name.lower() == "(Username)" or user.name.lower() == "(Username)":
                passn = "(Password)"
            else:
                passn = rw.random_word()
            url = "http://chatango.com/signupdir"
            driver = webdriver.PhantomJS()
            #driver = webdriver.Chrome()
            try:
                #driver = webdriver.PhantomJS()
                driver.get(url)
                etbox = driver.find_element_by_name("email")
                etbox.send_keys(email)
                utbox = driver.find_element_by_name("login")
                utbox.send_keys(usern)
                ptbox = driver.find_element_by_name("password")
                ptbox.send_keys(passn)
                cptbox = driver.find_element_by_name("password_confirm")
                cptbox.send_keys(passn)
                submit = driver.find_element_by_name("signupsubmit")
                submit.click()
                #driver.quit()
                page = driver.find_element_by_xpath("//div[@id='errorbox']")
                content = page.get_attribute('innerHTML')
                con = content.strip()
                print(con)
                if con == "This screen name has been taken. Please choose another.":  
                    room.message("This screen name has been taken. Please choose another.")
                    driver.quit()    
            except:
                driver.quit()
                room.message(msg("Success!..Account Details has been sent to your PM "+user.name.title()), True)
                self.pm.message(ch.User(user.name), "Username : "+usern+"\nPassword : "+passn+" ")
                print("Email : "+email)
                print("Username : "+usern)
                print("Password : "+passn)

        #Command find
        elif cmd.lower() == "find" and prfx and len(args):
            args = args.lower()
            if not ch.User(args).roomnames:
              room.message(msg("User "+args+" cannot be found."), True)
            else:
              room.message("<b>%s</b> can be found in : <b>%s</b>" % (args.capitalize(), ", ".join(ch.User(args).roomnames).title()),True)

        #Command announce
        elif cmd.lower() == "announce" and prfx and len(args)>0 and user.name.lower() in adminuser:
         try: 
            params = args.split(maxsplit=1)
            self.getRoom(params[0]).message(msg(params[1]), True)
            room.message("<b>Sent !</b>", True)
         except:
            room.message(msg("Wrong syntax , or room dont exist!"), True)
            
        #Command eval
        elif cmd.lower() == "eval" and prfx and user.name.lower() in accs and len(args)>0:
         try: 
            ret = eval(args)
            if ret == None:
              room.message("True")
              return
            room.message(str(ret))
         except:
             room.message("Error..")    

        #Command pingall
        elif cmd.lower() == "pingall" and prfx and user.name.lower() in adminuser:
            users = []
            for user in room._userlist:
              item = re.sub(r'(<User: |>)', '', str(user))
              users.append("@"+item)
            room.message(', '.join(users))    

        #Command join
        elif cmd.lower() == "join" and prfx and len(args)>0 and user.name.lower() in adminuser:
            self.joinRoom(args)
            rooms.append(args.lower())
            room.message(msg("Joined to "+args), True)

        #Command leaveroom
        elif cmd.lower() == "leave" and prfx and len(args)>0 and user.name.lower() in adminuser:
            self.setTimeout(2, self.leaveRoom, args)
            rooms.remove(args.lower())
            room.message(msg("Left "+args), True)

        #Command removeuser
        elif cmd.lower() == "removeuser" and prfx and user.name.lower() in adminuser and len(args)>0:
          if args.lower() in adminuser:
              adminuser.remove(args.lower())
              room.message(msg(args.title()+" has been removed from userlist."), True)
          else:
              room.message(msg(args.title()+" is not in userlist." ), True)

        #Command displayuser
        elif cmd.lower() == "displaylist" and prfx and user.name.lower() in adminuser:
            room.message("<b>%s</b> : " % ("Users")+', '.join(adminuser), True)

        #Command addbotuser
        elif cmd.lower() == "addbotuser" and prfx and len(args)>0 and user.name.lower() in adminuser:
          if args.lower() not in adminuser:  
            adminuser.append(args)
            room.message(msg(args.title()+" has been added to userlist."), True)
          else:
            room.message(msg(args.title()+" is already in userlist."), True)

        #Command login
        elif cmd.lower() == "login" and len(args)>0 and args.lower() in accs and user.name.lower() in adminuser:
            room.message(msg("Changing Account."), True)
            room.logout()
            if args.lower() == "(Username)":
                self.setTimeout(2, room.login, args.lower(), "18sept1997")
                self.setTimeout(4, room.message, msg("I am back"), True)
                return
            self.setTimeout(2, room.login, args.lower(), "dev18997")
            self.enableBg()
            self.setTimeout(4, room.message, msg("I am back"), True)
            
        #Command checkaccount
        elif cmd.lower() == "ca" and prfx and len(args)>0:
         try: 
            page = urlreq.urlopen("http://"+args.lower()+".chatango.com")
            content = page.read()
            decoder = content.decode("UTF-8")
            if "is not (yet) a registered Chatango name!" in decoder:
              room.message(msg(args.title()+" is not Registered."), True)
            if "About "+args.capitalize()+":" in decoder:
              room.message(msg(args.title()+" is Registered."), True)
            if "Legacy Flash version" in decoder:
              room.message(msg(args.title()+" is a room."), True)
            if "is not a registered Chatango name!" in decoder:
              room.message(msg("The given name contains banned word(s)."), True)
         except:
             room.message(msg("Check syntax or nontext."), True)

        #Command cmds
        elif cmd.lower() == "cmds" and prfx:
            #room.message(msg("Commands :")+msg(','.join(cmds)), True)
            cmds.clear()
            thefile = open('cmd.txt', 'r')
            for e in thefile:
                cmds.append(e.strip())
            room.message(msg("<u>Commands</u> : "+',  '.join(cmds)), True)
            thefile.close()

        #Command translate
        elif cmd.lower() == "trans" and prfx and len(args)>0:
          try: 
            var = args.split(maxsplit=2)
            url = "http://www.transltr.org/api/translate?text=%s&to=%s&from=%s"
            #eurl = url.encode("UTF-8")    
            response = requests.get("http://www.transltr.org/api/translate?text="+var[2]+"&to="+var[1]+"&from="+var[0])
            cleanr = re.compile('<.*?>')
            cleantext = re.sub(cleanr, '', response.text)
            jok = json.loads(cleantext)
            clean = re.compile('{"| |"|}')
            cln = re.sub(clean, '', cleantext)
            print(jok['translationText'])
            room.message(msg("Translated Text : "+jok['translationText']), True)
          except:
              room.message(msg("Syntax error. \r Check the Language code from the link below. \r http://www.lingoes.net/en/translator/langcode.htm"), True)

        #Command bing image 
        elif cmd.lower() == "gi" and prfx and len(args)>0:
          try:  
            args = str(args).replace(" ","%20")
            website = urlreq.urlopen("http://www.bing.com/images/search?q="+args+"&qs=n&form=QBIR&pq="+args+"&sc=0-0&sp=-1&sk=").read()
            soup = BeautifulSoup(website,"html.parser")
            images = []
            randresult = []
            for a in soup.findAll('a'):
                if (("http://" or "https://") and (".jpg" or ".png" or ".gif")) in a.get('href'):
                    images.append(a.get('href'))
                else:
                    continue
            for i in range(3):    
                pic_id = random.randint(0, len(images)-2)
                randresult.append(images[pic_id])
            room.message(msg('\r\r'.join(randresult)), True)
          except:
            room.message(msg("This command cant search gif images try $bgif !!"), True)
            
        #Command getimageadvance
        elif cmd.lower() == "geti" and prfx and len(args)>0:
          try:  
            args = str(args).replace(" ","%20")
            #QBIR
            website = urlreq.urlopen("http://www.bing.com/images/search?q="+args+"&qs=n&form=QBIR&pq="+args+"&sc=0-0&sp=-1&sk=").read()
            soup = BeautifulSoup(website,"html.parser")
            images = []
            link = []
            for img in soup.findAll('img'):
                images.append(img.get('src'))
            for i in images[2:]:
                if (".jpg" or ".png" or ".gif") in str(i):
                    link.append(i)
                else:
                    link.append(str(i).replace("=1.1", "=1.1.jpg"))
            if len(link) > 1:        
                room.message("\r\r\r"+"\r".join(link[0:3]))
            else:
                import extraction
                images = []
                result = []
                headers = {'Ocp-Apim-Subscription-Key': 'Your APi key'}
                response = requests.get("https://api.cognitive.microsoft.com/bing/v5.0/images/search?q="+args+"&count=20"+"&safeSearch=Off", headers=headers)
                #print(response.text)
                jok = json.loads(response.text)
                for item in jok['value']:
                    images.append(str(item['thumbnailUrl']))
                for i in range(3):
                    result.append(images[random.randint(0, random.randint(0,14))]+".jpg")
                #room.message(str(len(images)))    
                room.message(msg("\r\r\r".join(result)), True)
                result.clear()                  
          except:
              room.message(msg("Image not found"),True)
                
        #Command bgif
        elif cmd.lower() == "bgif" and prfx and len(args)>0:
            args = args.replace(" ","%20")
            if ("gif") not in args:
                room.message(msg("Only gif Images!"), True)
                return
            else:
                website = urlreq.urlopen("https://www.bing.com/images/search?q="+args+"&qs=n&form=QBILPG&pq="+args+"&Auth=Off").read()
                soup = BeautifulSoup(website,"html.parser")
                images = []
                link = []
                for img in soup.findAll('a'):
                    images.append(img.get('href'))
                for i in images:
                    if (("http://" or "https://") and (".gif")) in str(i):
                        link.append(str(i))
                if len(link) > 1:        
                    room.message("\r\r"+msg("\r\r\r".join(link[2:5])), True)
                else:
                    room.message(msg("Nu dirty gifs :@ !"), True)
                    
        #Command profilepic
        elif cmd.lower() == "pp" and prfx and len(args):
            site = "http://fp.chatango.com/profileimg/"+args[0]+"/"+args[1]+"/"+args+"/full.jpg"
            room.message(msg(args.title()+" :- ")+"\r\r"+site, True)

        #Command zodiac comptibility
        elif cmd.lower() == "zc" and prfx and len(args)>0:
          try:  
            var = args.split(maxsplit=1)
            moredata = []
            website = urlreq.urlopen("http://www.astrology-zodiac-signs.com/compatibility/"+var[0]+"-"+var[1]+"/").read()
            soup = BeautifulSoup(website,"html.parser")
            result = str(soup.find("div",{"class":"w-col w-col-6 w-clearfix"}).find('h3').text).replace("\n","")
            for data in soup.find("div",{"class":"headline-div-block"}).findAll('p'):
                #moredata.append(str(data))
                cleanr = re.compile('<.*?>')
                cleantext = re.sub(cleanr, '', str(data))
                moredata.append(cleantext)
            pastes = pastee(args, str("\n".join(moredata)))#.replace(",","\n"))
            print(pastes)
            room.message(msg("Zodiac Compatibility Result : "+result+"\r\r"+"To know more about stars compatibility visit :- "+pastes), True)
          except:
              room.message(msg("Zodiac does not exist ."), True)    

        #Command userlist
        elif cmd.lower() == "luser" and prfx:
            users = []
            for user in room._userlist:
                item = re.sub(r'(<User: |>)', '', str(user))
                users.append(item)
            room.message(msg("All Users : "+','.join(users)), True)    

        #Command mal
        elif cmd.lower() == "mal" and prfx and len(args)>0:
          try:  
            response = requests.get("https://myanimelist.net/api/anime/search.xml?q="+args.replace(" ","_"), auth=HTTPBasicAuth('username', 'password'), headers={'User-Agent':'Mozilla/5.0'})
            print(response.text)
            cleanr = re.compile('&lt.*?&gt')
            soup = BeautifulSoup(response.text,"lxml")
            image = soup.find('image').text
            title = soup.find('title').text
            english = soup.find('english').text
            synopsis = soup.find('synopsis').text.replace("\n","\r")
            #synopsis = re.sub(cleanr, '', synopsis)
            synopsis = synopsis.replace("<br />", "")
            synopsis = synopsis.replace("[i]","<u><i>")
            synopsis = synopsis.replace("[/i]","</i></u>")
            #room.message(synopsis)
            status = soup.find('status').text
            room.message(msg("\r\r\r"+title+"\r<u>Title in English</u> : "+english+"\r"+image+"\r<u>Status</u> : "+status+"\r\r"+synopsis), True)
          except Exception as e:
              room.message(str(e))
              
        #Command searchanime
        elif cmd.lower() == "sanime" and prfx and len(args)>0:
          try:
            url = "http://www1.gogoanime.tv/category/"+args.replace(" ","-")
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            cleanr = re.compile('<.*?>')
            webpage = urlopen(req).read()
            soup = BeautifulSoup(webpage, "html.parser")
            animesite = ["http://www1.gogoanime.tv/category/"+args.replace(" ","-"), "http://kissanime.ru/Anime/"+args.replace(" ","-"), "http://animehaven.to/"+args.replace(" ","-")]
            data = []
            #data = soup.find("div",{"class":"anime_info_body_bg"}).findAll('p')
            for dat in  soup.find("div",{"class":"anime_info_body_bg"}).findAll('p'):
                dat = re.sub(cleanr, '', str(dat).replace("\n","\r"))
                data.append(dat)
            image = soup.find("div",{"class":"anime_info_body_bg"}).find('img').get('src')    
            room.message(msg("\r\r\r"+args.title()+" :-")+"\r\r"+image+msg("\r\r"+'\r\r'.join(data[2:])+"\r\rWatch this anime at :- \r\r"+"\r".join(animesite)), True)
          except Exception as e:
           try:   
            #room.message(msg(str(e)), True)
            response = requests.get("https://myanimelist.net/api/anime/search.xml?q="+args.replace(" ","+"), auth=HTTPBasicAuth('username', 'password'), headers={'User-Agent':'Mozilla/5.0'})
            print(response.text)
            soup = BeautifulSoup(response.text,"lxml")
            image = soup.find('image').text
            title = soup.find('title').text
            english = soup.find('english').text
            synopsis = soup.find('synopsis').text
            synopsis = soup.find('synopsis').text.replace("\n","\r")
            synopsis = synopsis.replace("<br />", "")
            synopsis = synopsis.replace("[Written by MAL Rewrite]","")
            status = soup.find('status').text
            room.message(msg("\r\r\r"+title+"\r<u>Title in English</u> : "+english+"\r"+image+"\r<u>Status</u> : "+status+"\r\r"+synopsis), True)
           except Exception as e:
               room.message(str(e))
               
        #Command roominfo
        elif cmd.lower() == "roominfo" and prfx and len(args)>0:
            if args in rooms:
                page = "http://ust.chatango.com/groupinfo/"+args[0]+"/"+args[1]+"/"+args+"/gprofile.xml"
                users = []
                cleanr = re.compile('<.*?>')
                response = requests.get(page)
                code = re.sub(cleanr, '', response.text)
                code = urllib.parse.unquote(code)
                for user in self.getRoom(args)._userlist:
                    users.append(user)
                room.message(msg("\r\r\r[Room Name] : "+args.title()+"\r\r"+"[Room Message] : "+code.replace("\n","\r")+"\r\r[Total users] : "+str(len(users)+1)), True)
                self.setTimeout(2, self.leaveRoom, args)
                rooms.remove(args)
                users.clear()
            else:
                self.joinRoom(args)
                rooms.append(args)
                room.message(msg("Joined Room : "+args+"\rUse the cmd again to get room info."), True)
        #Command profile
        elif cmd.lower() == "profile" and prfx and len(args)>0:
         try:
          args = args.lower()
          user = get_profiletext_info(args)
          image = "http://fp.chatango.com/profileimg/" + args[0] + "/" +args[1] + "/" + args.lower() + "/full.jpg"
          if "\x99" not in user[7]:  
              room.message(msg("User Profile Pic :-\r\r")+image+msg("\r\r"+user[0]+" : "+user[1]+"\rGender : "+user[3]+"\r"+user[4]+" : "+user[5]+"\r About :- \r\r"+user[7].replace("\n","\r")), True)  
          else:
              paste = pastee(args.title()+"'s Profile Info", user[7])
              room.message(msg("User Profile Pic :-\r\r")+image+msg("\r\r"+user[0]+" : "+user[1]+"\rGender : "+user[3]+"\r"+user[4]+" : "+user[5]+"\r About :-"+paste), True)
         except:
             room.message(msg("Profile Not Found!"), True)
             
        #Command profcode
        elif cmd.lower() == "profcode" and prfx and len(args)>0:
            response = requests.get("http://"+args+".chatango.com/getfullprofile")
            cleanr = re.compile('<.*?>')
            code = re.sub(cleanr, '', response.text)
            code = urllib.parse.unquote(code)
            code = code.replace("fp=","")
            paste = pastee("Full Profile : "+args, code)
            room.message(msg(args.title()+"'s profile code : "+paste), True)

        #Command bgimage
        elif cmd.lower() == "gai" and prfx and len(args)>0:
            try:
                site = "http://"+args+".chatango.com/getfullprofile"
                website = urlreq.urlopen(site).read()
                cleanr = re.compile('<.*?>')
                code = re.sub(cleanr, '', str(website))
                code = urllib.parse.unquote(code)
                soup = BeautifulSoup(code, "html.parser")
                imgset = []
                image = soup.findAll('img')
                bimage = soup.find(attrs={"background-image":""})
                for im in image:
                    imgset.append(im.get('src'))
                #image = image.get('src')
                if len(imageset)>0:                    
                    room.message(msg("Images : "+'\r'.join(imgset)), True)
                else:
                    room.message(msg("No Image Found!"))
            except Exception as e:
                room.message(str(e))
  
        #Command checkpokemon
        elif cmd.lower() == "cpoke" and prfx:
            if len(args) == 0:
                f = open("pokedb.txt","r")
                pokemon = {}
                for line in f:
                    if ':' in line:
                        key, value = line.split(":")
                        pokemon[key] = value
                    else:
                        pass
                f.close()
                if user.name.lower() in pokemon.keys():
                    room.message(msg("@"+user.name.lower()+" you have captured pokemon : "+pokemon[user.name.lower()].replace("\n","")), True)
                else:
                    room.message(msg("@"+user.name.title()+" you haven't captured any pokemmon yet."), True)
                pokemon.clear()
            else:    
                f = open("pokedb.txt","r")
                pokemon = {}
                for line in f:
                    if ':' in line:
                        key, value = line.split(":")
                        pokemon[key] = value
                    else:
                        pass
                f.close()
                if args.lower() in pokemon.keys():
                    room.message(msg(args.title()+" captured pokemon : "+pokemon[args.lower()].replace("\n","")), True)
                else:
                    room.message(msg("This user's pokeball is empty af !"), True)
                    
        #Command poke
        elif cmd.lower() == "poke" and prfx:
          try:  
            f = open("pokedb.txt","r")
            pokemon = {}
            for line in f:
                if ':' in line:
                    key, value = line.split(":")
                    pokemon[key] = value
                else:
                    pass
            f.close()
            if user.name.lower() in pokemon.keys():
                room.message(msg("@"+user.name.lower()+" you have captured pokemon : "+pokemon[user.name.lower()].replace("\n","")), True)
            else:
                room.message(msg("@"+user.name.title()+" your pokeball is empty."), True)
            pokemon.clear()
          except Exception as e:
              room.message(str(e))
              
        #Command removepokemon
        elif cmd.lower() == "rp" and prfx and len(args)>0:
          try:  
            f = open("pokedb.txt","r")
            remove = {}
            for line in f:
                if ':' in line:
                    key, value = line.split(":")
                    remove[key] = value
                else:
                    pass
            f.close()
            if remove[user.name.lower()] == args.lower()+"\n":
                f = open("pokedb.txt","w")
                for key, value in remove.items():
                    if key == user.name.lower() and value == args.lower()+"\n":
                        pass
                    else:
                        f.write("%s:%s\n" % (key, value))
                f.close()
                room.message(msg("@"+user.name.title()+" released pokemon @"+args.title()+", pokeball is empty now."), True)
                remove.clear()
            else:
                room.message(msg("@"+user.name.title()+" you dont have this pokemon....yadumbfuck!"), True)
          except Exception as e:
              room.message(str(e))
              
        #Command pokeball
        elif cmd.lower() == "pb" and prfx and len(args)>0:
         if random.randint(0, 10) > 5:
          try:
            if user.name.lower() == args.lower():
                room.message(msg("@"+user.name.title()+" Yeah YEAH .. just fucking open the pokeball and lock yourself in that .. <u>YADUMBFUCK</u> !! :@ "), True)
                return
            claims = {}  
            file = open("pokedb.txt", "r")
            for line in file:
                if ':' in line:
                    key, value = line.split(":")
                    claims[key] = value
                else:
                    pass   
            #file.flush()    
            file.close()
            master = '?'
            for key, value in claims.items():
                if value == user.name.lower()+"\n":
                    master = key
                    break
            if user.name.lower()+"\n" in claims.values() and args.lower() == master:
                room.message(msg("@"+user.name.title()+" You cannot claim your MASTER"), True)
                return
            if args.lower()+"\n" in claims.values():
                #room.message(msg("@"+user.name+" you cannot use pokeball again, you have to empty pokeball before."), True)
                room.message(msg("@"+user.name+" this pokemon is already captured."), True)
            else:
                if user.name.lower() in claims.keys():
                    room.message(msg("@"+user.name+" you cannot use pokeball again, you have to empty your pokeball before."), True)
                else:
                    claims[user.name.lower()] = args
                    f = open("pokedb.txt", "w")
                    for key, value in claims.items():
                        f.write('%s:%s\n' % (key, value))
                    f.close()
                    #room.message(str(claims))
                    claims.clear()
                    room.message(msg("@"+user.name.title()+" throws a pokeball and catches @"+args.title()), True)
          except Exception as e:
              room.message(str(e))
         else:
             mocklist = ["but fails completely and hits head on the wall.","but pokemon punches him and runs away..", "but accidently captures him/her self."]
             mockdata = random.randint(0,2)
             room.message(msg("@"+user.name.title()+" tries to catch pokemon @"+args.title()+" "+mocklist[mockdata]), True)
    
        #Command search video and send to another room
        elif cmd.lower() == "mov" and prfx and len(args)>0 and user.name.lower() in adminuser:
            var = args.split(maxsplit=1)
            search = var[1].split()
            url = urlreq.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&MaxResults=1&key=(Your APi Key)" % "+".join(search))
            udict = url.read().decode('utf-8')
            data = json.loads(udict)
            rest = []
            for f in data["items"]:
             rest.append(f)
            d = rest[0]
            link = "http://www.youtube.com/watch?v="+d["id"]["videoId"]
            videoid = d["id"]["videoId"]
            title = d["snippet"]["title"]
            uploader = d["snippet"]["channelTitle"]
            room.message(msg("Sent to :"+var[0]), True)
            self.getRoom(var[0]).message("<b>%s</b> \r<b>Title :</b> <b>%s</b>" % (link,title), True)
            return
    
        #Command bing
        elif cmd.lower() == "search" and prfx and len(args)>0:
            var = args.replace(" ","+")
            response = requests.get("https://www.bing.com/search?q=%s&qs=n&form=QBLH&sp=-1&pq=%s" % (var,var), headers={"user-Agent":"Mozilla/5.0"}, verify=True)
            soup = BeautifulSoup(response.text, "html.parser")
            a = []
            for ref in soup.findAll('a'):
                if ("http://" or "https://") in str(ref.get('href')):
                    if "go.microsoft" in str(ref.get('href')):
                        continue
                    else:
                        a.append(str(ref.get('href')))
            room.message(msg("\r\r\rSearch query : <u>"+args+"</u> \r\rSearch Results :- \r\r\r")+msg('\r'.join(a)), True)    
        
        #Command room/user ss
        elif cmd.lower() == "russ" and prfx and len(args)>0 and user.name.lower() in adminuser:
            chop = webdriver.ChromeOptions()
            chop.add_extension('adblock.crx')
            driver = webdriver.Chrome(chrome_options = chop)
            driver.get("http://"+args.lower()+".chatango.com")
            sleep(10)
            driver.save_screenshot('roompic.jpg')
            driver.quit()
            client_id = 'Your CLient ID'
            headers = {"Authorization": "Client-ID Your Client ID"}
            api_key = 'YOur Api Key'
            url = "https://api.imgur.com/3/upload.json"
            payload = {'key':api_key, 'image':b64encode(open('roompic.jpg',"rb").read()), 'type':'base64', 'name':'roompic.jpg', 'title':'Picture'}
            response = requests.post(url, headers=headers, data=payload)
            jok = json.loads(response.text)
            #room.message(str(jok))
            room.message(str(jok['data']['link']))
            file = open("deletehash.txt","a")
            file.write("%s\n" % str(jok['data']['deletehash']))
            
        #Command lurk
        elif cmd.lower() == "lurk" and prfx and len(args)>0 and user.name.lower() in adminuser:
          try:
            var = args.split(maxsplit=1)
            lurk = True
            stalkroom = var[0].lower()
            thisroom = var[1].lower()
            room.message(msg("Lurking on Room : "+var[0].title()), True)
          except:
            room.message(msg("Syntax Error !"))
            
        #Command lurkoff
        elif cmd.lower() == "lurkoff" and prfx and user.name.lower() in adminuser:
            lurk = False
            room.message(msg("Stopped Lurking"), True)

        #Command dice
        elif cmd.lower() == "dice" and prfx:
            dice = []
            if args == 1 or len(args) == 0:
                dice.append(str(random.randint(1,6)))
                room.message(msg("Rolled Dice : "+''.join(dice)), True)
            elif args == 0 or int(args) > int(6):
                room.message(msg("Error!"), True)
            elif args != 0 or len(args)>0:
                for x in range(int(args)):
                    dice.append(str(random.randint(1,6)))
                    total = 0
                    for cal in dice:
                        total = total + int(cal)
                room.message(msg("\r\r\r"+user.name.title()+" Rolling Dice : -"+"\r\r\rRolled Dice :"+'\rRolled Dice : '.join(dice)+"\r\rTotal : "+str(total)), True)    
            dice.clear()
            
        #Command ytinfo
        elif "https://www.youtube.com/watch?v=" in message.body:
            url = message.body
            response = requests.get(url, headers={"User-Agent":"Mozilla/5.0"}, verify=True)
            soup = BeautifulSoup(response.text,"html.parser")
            title = soup.find("meta",{"property":"og:title"}).get('content')
            #image = soup.find("meta",{"property":"og:image"}).get('content')
            #desc = soup.find("meta",{"name":"description"}).get('content')
            room.message(msg("Video Title : "+title), True)

        #timu = time.ctime()
        #Command pet
        #elif timu >= time.ctime():
        
        #Command test
        elif cmd.lower() == "slap" and prfx and len(args)>0:
            var = args.split(maxsplit=1)
            site = "https://api.imgflip.com/caption_image"
            params = {'template_id':438680, 'username':'username', 'password':'password', 'text0':user.name.title()+" slaps "+var[0], 'text1':var[1]}
            response = requests.post(site, data=params, headers={"User-Agent":"Mozilla/5.0"}, verify=True)
            jok = json.loads(response.text.replace("\\", ""))
            print(response.text.replace("\\", ""))
            room.message(msg(str(jok['data']['url'])), True)

        #Command lovemeter
        elif cmd.lower() == "lm" and prfx and len(args)>0: 
            var = args.split(maxsplit=1)
            if len(var) == 2:
                response = requests.get("http://www.lovecalculator.co.nz/includes/data.php?firstname=%s&secondname=%s" % (var[0], var[1]))
                cleanr = re.compile('<.*?>')
                cleantext = re.sub(cleanr, '', response.text)
                cl = cleantext.split("%",1)
                other = cl[1].split(maxsplit=1)
                ot = other[0].split("%",1)
                if int(ot[0]) > 60:
                    chance = "@"+var[0].title()+" *h* @"+var[1].title()+" ;) ."
                else:
                    chance = "@"+var[0].title()+" *hb* @"+var[1].title()+" ;( ."
                room.message(msg(cl[0]+"% "+chance), True)    
            else:
                room.message(msg("@"+user.name.title()+" You need to give two names !"), True)

        #Command
        #elif cmd.lower() == "stealacc" and prfx and len(args)>0 and user.name.lower() == "(Username)":
            #sleep(10)
            #room.message(msg("Success!..Account Details has been sent to your PM (Username)"), True)

        #Command logout
        elif cmd.lower() == "logout" and prfx and len(args)>0:
            self.getRoom(args).logout()
            room.message(msg("Stealth Mode Activated !"), True)

        #Command ghost
        elif cmd.lower() == "ghost" and prfx and len(args)>0:
            url = "https://ghostbin.com/paste/new"
            data = {'text':args, 'lang':'text'}
            response = requests.post(url, data=data, headers={"User-Agent":"Mozilla/5.0"})
            room.message(msg(response.url), True)

        #Command openanysite
        elif cmd.lower() == "open" and prfx and len(args)>0:
            try:
                var = args.split(maxsplit=1)
                web = var[0]
                query = var[1]
                url = "http://api.duckduckgo.com/?q="+"!"+web+"+"+query+"&format=json&pretty=1&no_redirect=1"
                response = requests.get(url)
                jok = json.loads(response.text)
                url = jok["Redirect"]
                room.message(msg("Searching %s on %s : %s" % (query, web, url)), True)
            except Exception as e:
                print(str(e))
                
        #Command extractcolors from image
        elif cmd.lower() == "extcolor" and prfx and len(args)>0:
            try:
                if (("http://" or "https://") and (".jpg" or ".png" or ".jpg" or ".jpeg")) not in args:
                    return
                key = "Your APi key"
                url = "https://impalette.com/api/scan"
                params = {
                        'apiKey':key,
                        'link':args,
                    }
                response = requests.get(url, data=params)
                print(response.text)
            except Exception as e:
                print(str(e))
                
        #Command AutoTranslateOFF
        elif cmd.lower() == "transoff" and prfx:
          try:  
            trigger = False;
            room.message(msg("Autotranslate OFF !!"), True)
          except Exception as e:
              print(str(e))

        #Command AutoTranslateON
        elif cmd.lower() == "transon" and prfx:
          try:  
            trigger = True;
            room.message(msg("Autotranslate ON !!"), True)
          except Exception as e:
              print(str(e))

        #Command colorext
        elif cmd.lower() == "colorext" and prfx and len(args)>0:
            try:
                import Algorithmia
                if (("http://" or "https://") and (".jpg" or ".png" or "gif" or ".jpeg")) in args:
                    inputdata = {'url':args}
                    client = Algorithmia.client('Your Api Key')
                    algo = client.algo('vagrant/ColorSchemeExtraction/0.2.0')
                    output = algo.pipe(inputdata)
                    output = str(output).split("=")
                    output = output[1].replace(",metadata", "")
                    print(output)
                    colors = json.loads(output.replace("\'","\""))
                    #print(colors["colors"])
                    hexs = []
                    for value in colors["colors"]:
                        hexs.append(value["hex"])
                    room.message("\r\r\r"+args+"\r\r\r"+msg("\r".join(hexs)), True)
                else:                    
                    room.message(msg("Not a valid image"), True)
            except Exception as e:
                print(str(e))               
        
        #Command autotranslate
        elif trigger:    
          try:
            if user.name.lower() == "lovebotty":
                return
            if message.body[0] == "$" or message.body[0] == "!" or message.body[0] == "_" or message.body[0] == "~" or message.body[0] == "?" or message.body[0] == "^" or message.body[0] == "#" or message.body[0] == "." or message.body[0] == "-" or message.body[0] == "|" or message.body[0] == "/" or message.body[0] == "@" or message.body[0] == "%" or message.body[0] == "*" or message.body[0] == "&" or message.body[0] == "+" or message.body[0] == "=" or message.body[0] == ":" or message.body[0] == ";":
                return
            if len(message.body)<=10:
                return
            language_translator = LanguageTranslatorV2(
            username='your username',
            password='your password')
            response = json.dumps(language_translator.identify(message.body.encode("utf-8")));
            lsymbol = json.loads(response)
            lsymbol = str(lsymbol["languages"][0]["language"])
            if lsymbol == "en":
                return
            url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20170504T090047Z.d5ab4744f0fdc7ed.14857d8c1ba3f11ade80b91b4b07a299ee263b3b"
            payload = {
                'key':'Your Api Key',
                'text':message.body,
                'lang':lsymbol+"-"+"en",
                'format':'plain'
                }
            response = requests.post(url, data=payload)
            result = json.loads(response.text)
            room.message(msg("\r\r\r"+user.name.title()+" : "+message.body+"\r <u>Translated text</u> \r"+user.name.title()+" : "+result["text"][0]), True)
          except Exception as e:
              print(str(e))
        
  except Exception as e:
      print(str(e))
      
rooms = [] // add roomnames
username = "your bot name"
adminuser = [] # add admin users
cmds = []
temprooms = []
password = "your bot password"
try:
    lovebot.easy_start(rooms, username, password)
except Exception as e:
    print(str(e))
    os.system("start C:\\Users\\(USER)\\Desktop\\chatbot\\silentrunner.vbs") # Edit this filepath 
    exit()
