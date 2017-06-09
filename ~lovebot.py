import ch
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as urlreq
from cleverbot import Cleverbot
from bs4 import SoupStrainer
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
drigger = time.time()
ytinfotrigger = False
#file = open("monitor.txt","w")

def msg(args):
    return "<b>%s</b>" % (args)

def font(args):
    text = args
    hexs = ""
    clist = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    ignorehex = ['151C1F', '151C1F', '202020', '37212B', '151B20', '06241D', '800000', '4B0082']
    for i in range(6):
        hexs = hexs+random.choice(clist)
    if hexs in ignorehex:
        font(text)
    else:    
        return "<f x11"+hexs+"=\'1\'>"+args

def hexfont():
    hexs = ""
    clist = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    ignorehex = ['151C1F', '151C1F', '202020', '37212B', '151B20', '06241D', '800000', '4B0082']
    for i in range(6):
        hexs = hexs+random.choice(clist)
    if hexs in ignorehex:
        font(text)
    else:
        return hexs

def write(msg):
    #file = open("monitor.txt","wb")
    file.write('%s\n' % msg)
    #file.close()

def rs_bot(room):
    os.system("taskkill /im python.exe /f /t")
    os.system("start \"C:\\Python34\\python.exe\" \"C:\\Users\\Devin\\Desktop\\chatbot\\lovebot.py")

def ptext(args):
    text = []
    for x in BeautifulSoup(requests.get("http://" + args + ".chatango.com/").text, "html.parser").findAll("span", {
        "class": "profile_text"}):
        text.append(x.text.strip())
    return text

def pastee(desc, text):
  try:  
    param = {'key':'yourapi','description':desc,'language':'plain','paste':text,'format':'simple'}
    response = requests.post("https://paste.ee/api", data=param, verify=True)
    rawresp = str(response.content).replace("b'","").replace("'","").replace("/p/","/r/")
    return rawresp
  except Exception as e:
      return str(e)

def ghost(text):
    try:
            url = "https://ghostbin.com/paste/new"
            data = {'text':text, 'lang':'text'}
            response = requests.post(url, data=data, headers={"User-Agent":"Mozilla/5.0"})
            return str(response.url)
    except Exception as e:
        print(str(e))
        

def stab(text):
    try:
            url = "https://killr.io/create"
            data = {'code':text}
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
            data = {'text':text}
            response = requests.post(url, data=text, headers={"User-Agent":"Mozilla/5.0"})
            jok = json.loads(response.text)
            result = "https://hastebin.com/"+str(jok['key'])
            return result
    except Exception as e:
            return str(e)
i=0
ytdlink = False
#gametrigger = False
winner = False
botverse = False
class lovebot(ch.RoomManager, ch.Room):
  #try:  
    def onInit(self):
        self.enableBg()
        self.setNameColor("CC33CC")
        self.setFontColor("CC33CC")
        self.setFontFace("1")
        self.setFontSize(11)
        self.enableBg()

    def refreshusers(self, rooms):
     try:   
        users = []
        noofusers = []
        for rum in rooms:
            for user in self.getRoom(rum)._userlist:
                users.append(user)
            #room.message(font(msg("\r\r\r[Room Name] : "+args.title()))+"\r\r"+font(msg("[Room Message] : "+code.replace("\n","\r")))+font(msg("\r\r[Total users] : "+str(len(users)+1))), True)
            #self.setTimeout(2, self.leaveRoom, rum)
            noofusers.append(len(users))
            users.clear()
        return noofusers
     except Exception as e:
         print(str(e))
         pass

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
            #room.message(msg(user.name.title()+" is here @Devin997"), True)

    def onConnect(self,room):
        self.enableBg()
        print("Hello lovely peoples of "+room.name)
        #room.message(msg("Lovebotty is here !"), True)
    
    def find(self):    
        for x in rooms:
            if ("devin997" or "bungyoi" or "hackabot") in self.getRoom(str(x))._userlist:
                return str(x).lower()
        
    lurk = False
    stalkroom = '?'
    thisroom = '?'
    stalkuser = '?'
    lurkuser = False
    botverse = False
    gametrigger = False
    searchargue = '?'
    winner = False
    winnername = '?'
    def onMessage(self, room, user, message):
        global lurk
        global stalkroom
        global thisroom
        global trigger
        global i
        global drigger
        global ytinfotrigger
        global botverse
        global ytdlink
        global gametrigger
        global winner
        global searchargue
        global winnername
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
                if var[0] == "@lovebotty" or var[0] == "@Lovebotty":
                    key = "yourapi"
                    cs = '?'
                    if len(args)>0:
                        if i == 0:
                            url = "https://www.cleverbot.com/getreply?key="+key+"&input="+args
                            response = requests.get(url)
                            cs = json.loads(response.text)['cs']
                            i = i + 1
                            #room.message(msg("How are you ?"+" @"+user.name.title()),True)
                            if botverse:
                                room.message("@"+user.name.title()+msg(" How are you ?"),True)
                            else:
                                room.message(msg("How are you ?"+" @"+user.name.title()),True)
                        else:
                            url = "https://www.cleverbot.com/getreply?key="+key+"&input="+args+"&cs="+cs+"&callback=ProcessReply"
                            response = requests.get(url)
                            output = json.loads(response.text)["output"]
                            print(response.text)
                            #room.message(msg(output)+" @"+user.name.title(), True)
                            if botverse:
                                room.message("@"+user.name.title()+" "+msg(output), True)
                            else:
                                room.message(msg(output)+" @"+user.name.title(), True)
                    else:
                        #room.message("What do you need?"+" @<b>%s</b>" %(user.name.title()), True)
                        if botverse:
                            room.message("@"+user.name.title()+" What do you need?", True)
                        else:
                            room.message("What do you need?"+" @<b>%s</b>" %(user.name.title()), True)
            except Exception as e:
                print(str(e))
                self.pm.message(ch.User("devin997"), "[PM from "+room.name+" by "+user.name+"] : "+str(e))
                if var[0] == "@lovebotty":
                    key = "yourapi"
                    cs = '?'
                    if len(args)>0:
                        if i == 0:
                            url = "https://www.cleverbot.com/getreply?key="+key+"&input="+args
                            response = requests.get(url)
                            cs = json.loads(response.text)['cs']
                            i = i + 1
                            if botverse:
                                room.message(msg("@"+user.name.title()+msg(" How are you?")), True)
                            else:    
                                room.message(msg("How are you ?"+" @"+user.name.title()),True)  
                        else:
                            url = "https://www.cleverbot.com/getreply?key="+key+"&input="+args+"&cs="+cs+"&callback=ProcessReply"
                            response = requests.get(url)
                            output = json.loads(response.text)["output"]
                            print(response.text)
                            #room.message(msg(output)+" @"+user.name.title(), True)
                            if botverse:
                                room.message("@"+user.name.title()+" "+msg(output), True)
                            else:
                                room.message(msg(output)+" @"+user.name.title(), True)
                    else:
                        #room.message("What do you need?"+" @<b>%s</b>" %(user.name.title()), True)
                        if botverse:
                            room.message("@"+user.name.title()+" What do you need?", True)
                        else:
                            room.message("What do you need?"+" @<b>%s</b>" %(user.name.title()), True)
        except Exception as e:
            print(str(e))
            
        #Command say
        if cmd.lower() == "say" and prfx:
            if user.name.lower() in adminuser:
                room.message(font(msg(args)), True)
            else:
                room.message(font(msg(user.name.title()+" told me to say : "))+font(msg(args)), True)

        #Command botverse
        elif cmd.lower() == "botchat" and prfx and user.name.lower() in adminuser:
            botverse = True
            room.message(font(msg("Ready to chat with a bot")), True)

        #Command botverseOff
        elif cmd.lower() == "cbotchat" and prfx:
            botverse = False
            room.message(font(msg("Ok I'll shut up!")), True)

        #Command Urban Dictionary
        elif cmd.lower() == "ud" and prfx and len(args)>0:
            try:         
             thepage = urlreq.urlopen("http://www.urbandictionary.com/define.php?term="+args)
             parseonlydata = SoupStrainer("div",{"class":"meaning"}) 
             soup = BeautifulSoup(thepage,"html.parser",parse_only=parseonlydata)
             #p = soup.find("div",{"class","meaning"}).text
             room.message("\r\r"+font(msg("["+args+"] : "+str(soup.find("div",{"class","meaning"}).text).replace("\n","\r"))), True)
             #print("["+args+"] : "+str(p).replace("\n","\r"))
             return
            except:
             room.message(msg("Definition not found"), True)

        #Command checkonline USING IMAGE PROCESSING
        elif cmd.lower() == "co" and prfx:
            if len(args) == 0:
                room.message(fond(msg("<u>Syntax</u> : $co username")), True)
                return
            else:
                try:
                    page = urlreq.urlopen("http://"+args.lower()+".chatango.com")
                    content = page.read()
                    decoder = content.decode("UTF-8")
                    if "is not (yet) a registered Chatango name!" in decoder:
                      room.message(font(msg(args.title()+" is not Registered.")), True)
                      return
                    if "Legacy Flash version" in decoder:
                      room.message(font(msg(args.title()+" is a room.")), True)
                      return
                    var = "http://"+args.lower()+".chatango.com/i?17.jpg"
                    import Algorithmia
                    inputdata = {'url':var}
                    client = Algorithmia.client('yourapi')
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
                    if ("#559425" or "#97d24f" or "#b5e870" or "#78ab34") in hexs:
                        room.message(font(msg("<u>Username</u> : [ "+args.title()+" ]"))+"<f x11ffffff='1'> | "+font(msg("<u>Status</u> : "))+"<f x1118BB01=\'1\'>"+msg("[ Online ]"), True)
                    else:
                        room.message(font(msg("<u>Username</u> : [ "+args.title()+" ]"))+"<f x11ffffff='1'> | "+font(msg("<u>Status</u> : "))+"<f x11FF0033=\'1\'>"+msg("[ Offline ]"), True)
                except Exception as e:
                    print(str(e))
                    room.message(font(msg("Either User Dont Exist or I fucked Up !")), True)

        #Command random color size text
        elif cmd.lower() == "rtext" and prfx and len(args)>0:
         try:   
            text = args
            hexs = ""
            text = ""
            for letter in list(args):
                text = text + "<f x"+str(random.randint(9,22))+hexfont()+"=\""+str(random.randint(0,8))+"\">"+letter
            room.message(font(msg("<u>Weird Text</u> : "))+text, True)
            self.setTimeout(2, room.message, "Text code : "+text)
         except Exception as e:
             print(str(e))
        #Command gamesearch
        elif cmd.lower() == "gsearch" and prfx:
            if len(args) == 0:
                room.message(font(msg("<u>Syntax</u> : $gsearch gamename")), True)
                return
            else:
                try:
                    url = "http://games.gamepressure.com/search.asp"
                    data = {
                            'search':args
                        }
                    response = requests.post(url, data=data, verify=True)
                    soup = BeautifulSoup(response.text, "html.parser")
                    gamelink = soup.find("div", {"class":"box"}).find('a').get('href')
                    gamelink = "http://games.gamepressure.com"+gamelink
                    response = requests.get(gamelink)
                    soup = BeautifulSoup(response.text, "html.parser")
                    image = soup.find("div", {"class":"game-box-c game-box-c-eng"}).find('img').get('src')
                    title = soup.find("header").find("h1").text
                    score = soup.find("div", {"class":"score"}).text
                    developer = soup.find("div", {"class":"line-bot prod-wyd"}).findAll('a')
                    alist = []
                    for item in developer:
                        cleanr = re.compile('<.*?>')
                        cleantext = re.sub(cleanr, '', str(item))
                        alist.append(cleantext)
                    gdeveloper = alist[0]
                    genre = soup.find("div", {"class":"game-data-col"}).find('b').text
                    gamemode = soup.find("div", {"class":"game-data-extra"}).find('b').text
                    search = title.replace(" ","+")+"+trailer"
                    url = urlreq.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&MaxResults=1&key=yourapi" % "+".join(search))
                    udict = url.read().decode('utf-8')
                    data = json.loads(udict)
                    #print(str(data))
                    rest = []
                    for f in data["items"]:
                        rest.append(f)
                        d = rest[0]
                    trailerlink = "http://www.youtube.com/watch?v="+d["id"]["videoId"]
                    word_text = soup.findAll("div", {"class":"word-txt"})
                    cleanr = re.compile('<.*?>')
                    requirements = re.sub(cleanr, '', str(word_text[len(word_text)-1]))
                    if "Recommended:" in requirements:
                        requirements = requirements[20:]
                        room.message("\r\r\r"+font(msg(image))+font(msg("\r\r <u>Game Title</u> : "+title))+font(msg("\r<u>Game Score</u> : "+score))+font(msg("\r<u>Genre</u> : "+genre))+font(msg("\r<u>Game Mode</u> : "+gamemode))+font(msg("\r<u>Game Developer</u> : "+gdeveloper))+font(msg("\r<u>System Requirements</u> :-\r"+requirements.replace("\n", "")))+font(msg("\r<u>Game Trailer</u> : "+trailerlink)), True)
                    else:
                        requirements = requirements
                        rlink = stab("##"+title+" System Requirements :-\n\n\n"+requirements)
                        room.message("\r\r\r"+font(msg(image))+font(msg("\r\r <u>Game Title</u> : "+title))+font(msg("\r<u>Game Score</u> : "+score))+font(msg("\r<u>Genre</u> : "+genre))+font(msg("\r<u>Game Mode</u> : "+gamemode))+font(msg("\r<u>Game Developer</u> : "+gdeveloper))+font(msg("\r<u>System Requirements</u> : "+rlink))+font(msg("\r<u>Game Trailer</u> : "+trailerlink)), True)
                except Exception as e:
                    print(str(e))
                    room.message(font(msg("Game Not Found !")), True)

        #Command stop bot
        elif cmd.lower() == "bye" and prfx and user.name.lower() in adminuser:
            room.message(msg("Bye lovely peoples !"), True)
            self.setTimeout(1, self.leaveRoom, room.name)    

        #Command pm
        elif cmd.lower() == "pm" and prfx and user.name.lower() in adminuser:
          try:
            if len(args) == 0:
                room.message(msg("<u>Syntax</u> : $pm username message"), True)
            else:    
                var = args.split(maxsplit=1)
                self.pm.message(ch.User(var[0]), "[PM from "+room.name+" by "+user.name+"] : "+var[1])
                room.message(msg("PM Sent to "+var[0]), True)    
          except:
              room.message(msg("OOPS something went wrong!"), True)

        #Command yt
        elif cmd.lower() == "yt" and prfx and len(args)>0:
         try:
            args = urllib.parse.quote(args) 
            search = args.split()
            url = urlreq.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&MaxResults=1&key=yourapi" % "+".join(search))
            udict = url.read().decode('utf-8')
            #print(udict)
            data = json.loads(udict)
            #print(str(data))
            rest = []
            for f in data["items"]:
             rest.append(f)
            d = rest[0]
            link = "http://www.youtube.com/watch?v="+d["id"]["videoId"]
            videoid = d["id"]["videoId"]
            urla = urlreq.urlopen("https://www.googleapis.com/youtube/v3/videos?id=%s&key=yourapi&fields=items(id,snippet(channelId,title,categoryId),statistics)&part=snippet,statistics" % (videoid))
            udict = urla.read().decode('utf-8')
            data1 = json.loads(udict)
            #print(data1)
            try:
                views = data1["items"][0]["statistics"]["viewCount"]
                likes = data1["items"][0]["statistics"]["likeCount"]
                dislikes = data1["items"][0]["statistics"]["dislikeCount"]
            except:
                views = data1["items"][1]["statistics"]["viewCount"]
                likes = data1["items"][1]["statistics"]["likeCount"]
                dislikes = data1["items"][1]["statistics"]["dislikeCount"]
            title = d["snippet"]["title"]
            uploader = d["snippet"]["channelTitle"]
            description = d["snippet"]["description"]
            publishedat = d["snippet"]["publishedAt"]
            publishedat = publishedat.replace("T", " ")
            publishedat = publishedat.replace("Z", " ")
            #room.message(link)
            #room.message("<b>%s</b> \r<b>Title :</b> <b>%s</b>" % (link,title), True)
            room.message(font(msg(link))+font(msg("\rTitle : "+title))+font(msg("\r<u>Uploaded By </u>: "+uploader))+font(msg("\r <u>Description </u>: "+description))+font(msg("\r<u>Views</u> : "+views))+"<f x11ffffff='1'> | "+font(msg("  <u>Likes</u> : "+likes))+"<f x11ffffff='1'> | "+font(msg(" <u>Dislikes</u> : "+dislikes))+font(msg("\r <u>Published At </u>: "+publishedat)), True)
            return
         except Exception as e:
             print(str(e))
             room.message(font(msg("Video Not Found !")), True)

        #Command takeacc with request
        elif cmd.lower() == "takeacc" and prfx and len(args)>0:
            try:
                rw = RandomWords()
                email = rw.random_word()+"ayhtu45yhhn58hbnn@hotmail.com"
                print(email+"\n")
                usern = args
                if user.name.lower() == "devin997" or user.name.lower() == "bungyoi":
                    passn = "devin997"
                else:
                    passn = rw.random_word()
                url = "http://chatango.com/signupdir"
                data = {
                        "email":email,
                        "login":usern,
                        "password":passn,
                        "password_confirm":passn,
                        "storecookie":"on",
                        "signupsubmit":"Sign up",
                        "checkerrors":"yes"
                    }
                response = requests.post(url, data=data, headers={"User-Agent":"Mozilla/5.0"})
                if "Step 3: Fill in your profile so that people you chat with can see who you are" in response.text:
                    self.pm.message(ch.User(user.name), "Username : "+usern+"\nPassword : "+passn+" ")
                    room.message(font(msg("Account Creation Successful, login credentials are sent to you pm @"+user.name.title())), True)
                else:
                    room.message(font(msg("Account Creation Failed, Try Again!")), True)
            except:
                print(str(e))
        
        #Command takeacc
        #elif cmd.lower() == "takeacc" and prfx and len(args)>0 and user.name.lower() in adminuser: 
            #rw = RandomWords()  
            #email = rw.random_word()+"@hotmail.com"
            #usern = args
            #if user.name.lower() == "devin997" or user.name.lower() == "bungyoi":
                #passn = "devin997"
            #else:
                #passn = rw.random_word()
            #url = "http://chatango.com/signupdir"
            #driver = webdriver.PhantomJS()
            #driver = webdriver.Chrome()
            #try:
                #driver = webdriver.PhantomJS()
                #driver.get(url)
                #etbox = driver.find_element_by_name("email")
                #etbox.send_keys(email)
                #utbox = driver.find_element_by_name("login")
                #utbox.send_keys(usern)
                #ptbox = driver.find_element_by_name("password")
                #ptbox.send_keys(passn)
                #cptbox = driver.find_element_by_name("password_confirm")
                #cptbox.send_keys(passn)
                #submit = driver.find_element_by_name("signupsubmit")
                #submit.click()
                #driver.quit()
                #page = driver.find_element_by_xpath("//div[@id='errorbox']")
                #content = page.get_attribute('innerHTML')
                #con = content.strip()
                #print(con)
                #if con == "This screen name has been taken. Please choose another.":  
                    #room.message("This screen name has been taken. Please choose another.")
                    #driver.quit()    
            #except:
                #driver.quit()
                #room.message(msg("Success!..Account Details has been sent to your PM "+user.name.title()), True)
                #self.pm.message(ch.User(user.name), "Username : "+usern+"\nPassword : "+passn+" ")
                #print("Email : "+email)
                #print("Username : "+usern)
                #print("Password : "+passn)

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
            room.message("<b>Sent!</b>", True)
         except:
            room.message(font(msg("Wrong syntax , or room dont exist!")), True)
            
        #Command eval
        elif cmd.lower() == "eval" and prfx and user.name.lower() in accs and len(args)>0:
         try: 
            ret = eval(args)
            if ret == None:
              room.message(font(msg("True")), True)
              return
            room.message(str(ret))
         except:
             room.message("Error..")    

        #Command pingall
        elif cmd.lower() == "pingall" and prfx and user.name.lower() in adminuser:
            users = []
            for user in room._userlist:
              item = re.sub(r'(<User: |>)', '', str(user))
              users.append(font("@"+item.title()))
            room.message(' | '.join(users), True)    

        #Command nick
        elif cmd.lower() == "nick" and prfx:
            if len(args) == 0:
                room.message(font(msg("<u>Syntax</u> : $nick nickname")), True)
            else:
                try:
                    args = args.replace("\'", "\"")
                    file = open("nickdb.txt", "r+")
                    nicks = {}
                    found = False
                    for line in file:
                        if ":" in line:
                            key, value = line.split(":")
                            nicks[key] = value
                    for key in nicks.keys():
                        if key == user.name.lower():
                            found = True
                            del nicks[user.name.lower()]
                            nicks[user.name.lower()] = args
                    if found == False:
                        nicks[user.name.lower()] = args
                    name = nicks[user.name.lower()]
                    for key, value in nicks.items():
                        file.write('%s:%s\n' % (key, value))
                    file.close()
                    nicks.clear()
                    room.message(msg("@"+user.name.title()+" Your new nickname is : ")+name, True)
                except Exception as e:
                    print(str(e))
                    room.message(font(msg("Please Try Again.")), True)

        #Command seenick
        elif cmd.lower() == "seenick" and prfx:
          try:  
            if len(args) == 0:
                file = open("nickdb.txt", "r")
                nicks = {}
                found = False
                for line in file:
                    if ":" in line:
                        key, value = line.split(":")
                        value = value.replace("\n", "")
                        nicks[key] = value
                for key, value in nicks.items():
                    if key == user.name.lower():
                        found = True
                        room.message(msg("@"+user.name.title()+" Your nickname is : ")+value.replace("\n",""), True)
                        break
                if found == False:
                    room.message(font(msg("@"+user.name.title()+" You have not set your nickname.")), True)
                nicks.clear()    
                file.close()    
            else:
                file = open("nickdb.txt", "r")
                nicks = {}
                found = False
                for line in file:
                    if ":" in line:
                        key, value = line.split(":")
                        value = value.replace("\n", "")
                        nicks[key] = value
                for key, value in nicks.items():
                    if key == args.lower():
                        found = True
                        room.message(msg("@"+user.name.title()+" "+args.title()+" nickname is : ")+value, True)
                        break
                if found == False:
                    room.message(font(msg("@"+user.name.title()+" "+args.title()+" did not set any nickname.")), True)
                nicks.clear()
                file.close()    
          except Exception as e:
              print(str(e))
              
        #Command join
        elif cmd.lower() == "join" and prfx and len(args)>0 and user.name.lower() in adminuser:
            self.joinRoom(args)
            rooms.append(args.lower())
            room.message(font(msg("Joined to "+args)), True)

        #Command test
        #elif cmd.lower() == "test" and prfx and user.name.lower() in adminuser:
            #api_key = "yourapi"
            #client_id = "yourapi"
            #client_secret = "yourapi"
            #params = {
                    #'grant_type': 'client_credentials',
                    #'client_id': client_id,
                    #'client_secret': client_secret
                    #}
            #response = requests.post('https://bauth.blippar.com/token', data=params)
            #jok = json.loads(response.text)            
            #auth_token = jok["access_token"]
            #token_type = jok["token_type"]
            #try:
                #if (("http://" or "https://") and (".jpg" or ".png" or ".jpeg")) in args:
                    #file = open("slap.jpg", "wb")
                    #data = urllib.request.urlretrieve(args, file)
                    #print("done")
                    #params = {'input_image':args}
                    #headers = {}
                    #headers["Authorization"] = finaltoken
                    #response = requests.post('https://bapi.blippar.com/v1/imageLookup', data=params, headers=headers)
                    #print(response.text)
            #except Exception as e:
               # print(str(e))
                
        #Command start game
        elif cmd.lower() == "startgame" and prfx and user.name.lower() in adminuser:
            room.message(font(msg("Alright Game time you Bitches..")), True)
            self.setTimeout(3, room.message, font(msg("Find me an image that contains \"dog\". \r Use $submit imagelink ")), True)
            gametrigger = True
            searchargue = "dog"
            winner = False

        #Command submit game answer
        elif cmd.lower() == "submit" and prfx and gametrigger and winner == False:
            #Cloudsight API
            api_key = "yourapi"
            secret_key = "yourapi"
            try:
                import cloudsight
                auth = cloudsight.SimpleAuth(api_key)
                api = cloudsight.API(auth)
                if (("http://" or "https://") and (".jpg" or ".png" or "jpeg")) in args:
                    response = api.remote_image_request(args, {'image_request[locale]': 'en-US',})
                    #status = api.image_response(response['token'])
                    #while status['status'] != cloudsight.STATUS_COMPLETED:
                        #status = api.image_response(response['token'])
                        #print(response)
                    status = api.wait(response['token'], timeout=20)
                        #if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
                    print(status)
                    names = status["name"]
                    names = names.split()
                    print(str(names))
                    if searchargue in names:
                        winner = True
                        room.message(font(msg("Winner is : "))+"<f x11ffffff=\"1\"><b>%s</b>" % user.name.title(), True)
                        winnername = user.name
                        return
                    room.message(font(msg("Sorry Not the Correct Image.")), True)
                else:    
                    room.message(font(msg("Not a valid image")), True)    
            except Exception as e:
                print(str(e))
                    

        #Command leaveroom
        elif cmd.lower() == "leave" and prfx and len(args)>0 and user.name.lower() in adminuser:
            if args in rooms:
                self.setTimeout(2, self.leaveRoom, args)
                rooms.remove(args.lower())
                room.message(font(msg("Left "+args)), True)
            else:
                room.message(font(msg("I already left.")), True)

        #Command removeuser
        elif cmd.lower() == "removeuser" and prfx and user.name.lower() in adminuser and len(args)>0:
          if args.lower() in adminuser:
              adminuser.remove(args.lower())
              room.message(font(msg(args.title()+" has been removed from userlist.")), True)
          else:
              room.message(font(msg(args.title()+" is not in userlist." )), True)

        #Command displayuser
        elif cmd.lower() == "displaylist" and prfx and user.name.lower() in adminuser:
            room.message("<b>%s</b> : " % ("Users")+', '.join(adminuser), True)

        #Command addbotuser
        elif cmd.lower() == "addbotuser" and prfx and len(args)>0 and user.name.lower() in adminuser:
          if args.lower() not in adminuser:  
            adminuser.append(args)
            room.message(font(msg(args.title()+" has been added to userlist.")), True)
          else:
            room.message(font(msg(args.title()+" is already in userlist.")), True)

        #Command login
        elif cmd.lower() == "login" and len(args)>0 and args.lower() in accs and user.name.lower() in adminuser:
            room.message(font(msg("Changing Account.")), True)
            room.logout()
            if args.lower() == "devin997":
                self.setTimeout(2, room.login, args.lower(), "18sept1997")
                #room.login(args.lower(), "18sept1997")
                self.enableBg()
                self.setTimeout(4, room.message, font(msg("I am back")), True)
                return
            self.setTimeout(2, room.login, args.lower(), "dev18997")
            self.enableBg()
            self.setTimeout(4, room.message, font(msg("I am back")), True)
            
        #Command checkaccount
        elif cmd.lower() == "ca" and prfx and len(args)>0:
         try: 
            page = urlreq.urlopen("http://"+args.lower()+".chatango.com")
            content = page.read()
            decoder = content.decode("UTF-8")
            if "is not (yet) a registered Chatango name!" in decoder:
              room.message(font(msg(args.title()+" is not Registered.")), True)
            if "About "+args.capitalize()+":" in decoder:
              room.message(font(msg(args.title()+" is Registered.")), True)
            if "Legacy Flash version" in decoder:
              room.message(font(msg(args.title()+" is a room.")), True)
            if "is not a registered Chatango name!" in decoder:
              room.message(font(msg("Name contains banned words.")), True)
         except:
             room.message(font(msg("Check syntax or nontext.")), True)

        #Command cmds
        elif cmd.lower() == "cmds" and prfx:
            #room.message(msg("Commands :")+msg(','.join(cmds)), True)
            cmds.clear()
            thefile = open('cmd.txt', 'r')
            for e in thefile:
                cmds.append(font(msg(e.strip())))
            thefile.close()    
            room.message(font(msg("\r\r\r<u>Commands</u> :-"))+font(msg(" Use Prefix \'$\' \r\r commandname [syntax] \r\r"))+'<f x11ffffff=\'1\'> | '.join(cmds[:23]), True)
            #self.setTimeout(4, room.message, font(msg(' | '.join(cmds[28:]))), True)
            self.setTimeout(1, room.message, font(msg("\r\r\r"))+' <f x11ffffff=\'1\'> | '.join(cmds[23:]), True)
            #thefile.close()

        #Command translate
        elif cmd.lower() == "trans" and prfx and len(args)>0:
          try:
            args = urllib.parse.quote(args)  
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
            room.message(font(msg("Translated Text : "))+font(msg(jok['translationText'])), True)
          except:
              room.message(font(msg("Syntax error. "))+font(msg("\r Check the Language code from the link below. "))+font(msg("\r http://www.lingoes.net/en/translator/langcode.htm")), True)

        #Command software downloader
        elif cmd.lower() == "download" and prfx:
            if len(args) == 0:
                room.message(font(msg("<u>Syntax</u> : $download softwarename")), True)
                return
            else:
                try:
                    url = "http://www.filehorse.com/search?q="+args.replace(" ","+")
                    response = requests.get(url)
                    if ("200") in str(response):
                        soup = BeautifulSoup(response.text, "html.parser")
                        nexturl = soup.find("div", {"class":"cat_dl_btn"}).find('a').get('href')
                        response = requests.get(nexturl+"/download")
                        #print(response.text)
                        soup = BeautifulSoup(response.text, "html.parser")
                        dlinkv1 = soup.find("div", {"class":"download_info1"}).find('a').get('href')
                        shortener = "https://is.gd/create.php"
                        data = {
                            'url':dlinkv1
                        }
                        response = requests.post(shortener, data=data)
                        soup = BeautifulSoup(response.text, "html.parser")
                        dlink = soup.find("input", {"id":"short_url"}).get('value')
                        room.message(font(msg("Application Name : "+ args.title()))+font(msg("\r &nbsp &nbsp &nbsp &nbsp &nbsp &nbspDownload Link : "+dlink)), True)
                    else:
                        room.message(font(msg("Sorry, I couldn't find anything matching your search term")), True)
                except Exception as e:
                    print(str(e))
                    pass

        elif cmd.lower() == "connect" and prfx:
            if args:
              try:  
                  a = args.lower()
                  if len(a) == 1:
                      url = requests.get("http://st.chatango.com/groupinfo/"+a+"/"+a+"/"+a+"/gprofile.xml")
                  else:    
                      url = requests.get("http://st.chatango.com/groupinfo/"+a[0]+"/"+a[1]+"/"+a+"/gprofile.xml")
                  if url.status_code == 404:
                    room.message(user.name+", that's not a room.", True)
                  else:
                    if args.lower() in self.roomnames:
                      room.message(user.name+", I am already in that room.", True)
                    else:
                      self.joinRoom(args.lower())
                      room.message(user.name+", attempting to connect to <b>["+args.lower()+"]</b>", True)
              except:
                  room.message("not a valid argument")
            else:
              room.message(user.name+", usage: <f x10cc0000='courier new'><b>.connect [Room]</b>", True)


        #Command checkimage
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
                randresult.append(font(msg(images[pic_id])))
            room.message('\r\r'.join(randresult), True)
          except:
            room.message(font(msg("This command cant search gif images try $bgif !!")), True)
            
        #Command getimageadvance
        elif cmd.lower() == "geti" and prfx and len(args)>0:
          try:  
            args = str(args).replace(" ","%20")
            #QBIR
            ##https://www.bing.com/images/search?q=girl+sucking+penis&qs=n&form=QBILPG&pq=girl+sucking+penis&sc=0-0&sp=-1&sk=
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
                headers = {'Ocp-Apim-Subscription-Key': 'yourapi'}
                response = requests.get("https://api.cognitive.microsoft.com/bing/v5.0/images/search?q="+args+"&count=20"+"&safeSearch=Off", headers=headers)
                #print(response.text)
                jok = json.loads(response.text)
                for item in jok['value']:
                    images.append(str(item['thumbnailUrl']))
                for i in range(3):
                    result.append(font(msg(images[random.randint(0, random.randint(0,14))]))+".jpg")
                #room.message(str(len(images)))    
                room.message("\r\r\r".join(result), True)
                result.clear()                  
          except:
              room.message(font(msg("Image not found")),True)
                
        #Command bgif
        elif cmd.lower() == "bgif" and prfx and len(args)>0:
            args = args + " gif"
            args = args.replace(" ","%20")
            if ("gif") not in args:
                room.message(font(msg("Only gif Images!")), True)
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
                        link.append(font(msg(str(i))))
                if len(link) > 1:        
                    room.message("\r\r"+"\r\r\r".join(link[2:5]), True)
                else:
                    room.message(font(msg("Nu dirty gifs :@ !")), True)
                    
        #Command profilepic
        elif cmd.lower() == "pp" and prfx and len(args):
            site = "http://fp.chatango.com/profileimg/"+args[0]+"/"+args[1]+"/"+args+"/full.jpg"
            room.message(font(msg(args.title()+" :- "))+font(msg("\r\r"+site)), True)

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
            room.message(font(msg("Zodiac Compatibility Result : "))+font(msg(result))+font(msg("\r\r"+"To know more about stars compatibility visit :- "))+font(msg(pastes)), True)
          except:
              room.message(font(msg("Zodiac does not exist .")), True)    

        #Command userlist
        elif cmd.lower() == "luser" and prfx:
          try:
            if not args:
                users = []
                length = 0
                for user in room._userlist:
                    item = re.sub(r'(<User: |>)', '', str(user))
                    length = length + 1
                    users.append(font(msg(item)))
                if len(users) <= 27:    
                    room.message(font(msg("All Users ["+str(length)+"] : "))+' | '.join(users), True)
                else:
                    room.message(font(msg("All Users ["+str(length)+"] : "))+' | '.join(users[:27]), True)
                    time.sleep(1)
                    room.message(' | '.join(users[28:]))
            else:
                args = args.lower()
                users = []
                length = 0
                for item in self.getRoom(args)._userlist:
                    item = re.sub(r'(<User: |>)', '', str(item))
                    length = length + 1
                    users.append(font(msg(item)))
                if len(users) <= 27:
                    room.message(font(msg("All Users ["+str(length)+"] : "))+'<f x11ffffff="1"> | '.join(users), True)
                else:
                    room.message(font(msg("All Users ["+str(length)+"] : "))+' | '.join(users[:27]), True)
                    time.sleep(1)
                    room.message(' | '.join(users[28:]))
          except Exception as e:
              print(str(e))
              room.message(font(msg("I am not in "+args.title())), True)
        #Command rooms
        elif cmd.lower() == "lrooms" and prfx:
          try:  
            lrooms = []
            for item in rooms:
                lrooms.append(font(msg(item)))
            usrlist = self.refreshusers(rooms)
            data = font(msg("<u>Rooms</u> : "))
            j=0
            for i in lrooms:
                data = data + i + "[" + str(usrlist[j]) + "]" + "<f x11ffffff='1'> | "
                j = j + 1
            data = data.replace("\n","\r")    
            room.message(data, True)
          except Exception as e:
             print(str(e))
             pass

        #Command mal
        elif cmd.lower() == "mal" and prfx and len(args)>0:
          try:  
            response = requests.get("https://myanimelist.net/api/anime/search.xml?q="+args.replace(" ","_"), auth=HTTPBasicAuth('username', 'password*'), headers={'User-Agent':'Mozilla/5.0'})
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
            room.message(font(msg("\r\r\r"))+font(msg(title))+font(msg("\r<u>Title in English</u> : "))+font(msg(english))+"\r"+font(msg(image))+font(msg("\r<u>Status</u> : "))+font(msg(status))+"\r\r"+font(msg(synopsis)), True)
          except Exception as e:
              room.message(str(e))

        #Command createroom
        elif cmd.lower() == "croom" and prfx and len(args)>0 and user.name.lower() in adminuser:
            try:
                url1 = "http://chatango.com/creategrouplogin"
                data = {"lo": "username","uns": "0", "p": "password", "u": args, "d":args, "n":"test"}
                response = requests.post(url1, data=data, headers={"User-Agent":"Mozilla/5.0"})
                print(response.text)
                if "group_url="+args+"&islive=True&login=devinozaki" in response.text:
                    room.message(font(msg("Room Created Successfully, <u>Link</u> : http://"+args+".chatango.com")), True)
                    print("http://"+args+".chatango.com")
                else:
                    room.message(font(msg("Room cannot be created.")), True)
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
            room.message(font(msg("\r\r\r"+args.title()+" :-"))+"\r\r"+font(msg(image))+font(msg("\r\r"+'\r\r'.join(data[2:])))+font(msg("\r\rWatch this anime at :- \r\r"))+font(msg("\r".join(animesite))), True)
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
            room.message(font(msg("\r\r\r"))+font(msg(title))+font(msg("\r<u>Title in English</u> : "))+font(msg(english))+"\r"+font(msg(image))+font(msg("\r<u>Status</u> : "))+font(msg(status))+"\r\r"+font(msg(synopsis)), True)
           except Exception as e:
               room.message(str(e))
               
        #Command boobslap
        elif cmd.lower() == "boobslap" and prfx and len(args)>0:
            room.message(msg(user.name.title()+" boobslaps "+args.title()+" on his face and he falls on the ground like a bitch who had cowlike orgasm."), True)

        #Command sensationbot
        elif cmd.lower() == "stalk" and prfx and len(args)>0:
          try:  
            args = args.replace(" ","+")
            response = urlreq.urlopen("http://www.personalityforge.com/api/chat/?apiKey=(yourapi&chatbotID)&message="+args+"&externalID=DEVIN997-12345").read()
            print(response)
            udict = response.decode("UTF-8")
            jok = json.loads(udict)
            #room.message(msg("<u><u>Midnight Blue</u></u> : ")+msg(str(jok)), True)
            room.message(font(msg("<u><u>Midnight Blue</u></u> : "))+font(msg(str(jok['message']['message']))), True)
          except:
              room.message(font(msg("Devin....IP... @"+" @".join(accs))), True)
        #Command nyan
        elif message.body == "nyan":
            room.message(font(msg("nyandesuka *h*")), True)

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
                room.message(font(msg("\r\r\r[Room Name] : "+args.title()))+"\r\r"+font(msg("[Room Message] : "+code.replace("\n","\r")))+font(msg("\r\r[Total users] : "+str(len(users)+1))), True)
                self.setTimeout(2, self.leaveRoom, args)
                rooms.remove(args)
                users.clear()
            else:
                page = "http://ust.chatango.com/groupinfo/"+args[0]+"/"+args[1]+"/"+args+"/gprofile.xml"
                response = requests.get(page)
                print(response.status_code)
                print(type(response.status_code))
                if response.status_code == 404:
                    room.message(font(msg("Room Does Not Exist !")), True)
                    return
                self.joinRoom(args)
                rooms.append(args)
                room.message(font(msg("Joined Room : "))+font(msg(args))+font(msg("\rUse the cmd again to get room info.")), True)

        #Command soundcloud
        elif cmd.lower() == "sc" and prfx and len(args)>0:
         try:   
          try:  
            url = "https://soundcloud.com/search?q="+args.replace(" ", "%20")
            response = urlreq.urlopen(url).read()
            soup = BeautifulSoup(response, "html.parser")
            lists = soup.findAll("li")
            finallist = []
            for item in lists[4:]:
                soup = BeautifulSoup(str(item), "html.parser")
                title = soup.find('a').text
                link = soup.find('a').get('href')
                result = title +" -- "+"https://soundcloud.com"+link
                finallist.append(result)
            #soup = BeautifulSoup(''.join(lists[4:]))
            #title = soup.find('a').get('href')
            if len(finallist) == 0:
                room.message(msg("Search Result : 0 Found "), True)
                return
            link = random.choice(finallist)
            downloader = "https://www.klickaud.com/download.php?value="+link.split("--")[1]
            data = {
                    "csrfmiddlewaretoken": "lgv9CkYdSBz0crgeeTR9Tbbh9zs3N8Jm",
                    "mvideo-url":link.split("--")[1]
                }
            response = requests.get(downloader)
            soup = BeautifulSoup(response.text, "html.parser")
            dlink = soup.find("a", {"id":"no-link"}).get('href')
            shortener = "https://is.gd/create.php"
            data = {
                    'url':dlink
                }
            response = requests.post(shortener, data=data)
            soup = BeautifulSoup(response.text, "html.parser")
            dlink = soup.find("input", {"id":"short_url"}).get('value')
            room.message(font(msg("\r\r\r"+link))+font(msg("\r&nbsp &nbsp &nbsp &nbspDownload Link : "+dlink)), True)
          except Exception as e:
              print(str(e))
              room.message(font(msg("\r\r\r"+'\r'.join(finallist))), True)
         except Exception as e:
             print(str(e))
             room.message(font(msg("Something Wrong, Try Again")), True)
             
        #Command profile
        elif cmd.lower() == "profile" and prfx and len(args)>0:
         try:
          args = args.lower()
          user = ptext(args)
          if len(args) == 1:
              image = "http://fp.chatango.com/profileimg/" + args + "/" +args + "/" + args.lower() + "/full.jpg"
          else:
              image = "http://fp.chatango.com/profileimg/" + args[0] + "/" +args[1] + "/" + args.lower() + "/full.jpg"
          if "\x99" not in user[7]:  
              room.message(font(msg("User Profile Pic :-\r\r"))+font(msg(image))+font(msg("\r\r"+user[0]+" : "+user[1]))+font(msg("\rGender : "+user[3]))+font(msg("\r"+user[4]+" : "+user[5]))+font(msg("\r About :- \r\r"))+font(msg(user[7].replace("\n","\r"))), True)  
          else:
              paste = pastee(args.title()+"'s Profile Info", user[7])
              room.message(font(msg("User Profile Pic :-\r\r"))+font(msg(image))+font(msg("\r\r"+user[0]+" : "+user[1]))+font(msg("\rGender : "+user[3]))+font(msg("\r"+user[4]+" : "+user[5]))+font(msg("\r About :-"))+font(msg(paste)), True)
         except:
             room.message(font(msg("Profile Not Found!")), True)
             
        #Command profcode
        elif cmd.lower() == "profcode" and prfx and len(args)>0:
            response = requests.get("http://"+args+".chatango.com/getfullprofile")
            cleanr = re.compile('<.*?>')
            code = re.sub(cleanr, '', response.text)
            code = urllib.parse.unquote(code)
            code = code.replace("fp=","")
            paste = pastee("Full Profile : "+args, code)
            room.message(font(msg(args.title()+"'s profile code : "))+font(msg(paste)), True)

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
             
        #Command boot
        elif cmd.lower() == "boot" and prfx and len(args):
          try:  
            if args.lower() == "bitch":
                os.system("start \"C:\\Python34\\python.exe\" \"C:\\Users\\Devin\\Desktop\\chatbot\\bot.py")
            if args.lower() == "sextbot":
                os.system("start \"C:\\Python34\\python.exe\" \"C:\\Users\\Devin\\Desktop\\chatbot\\sextbot.py")    
          except:
              room.message(msg("Bot "+args.title()+" doesnt exist!"), True)
    
        #Command moy
        elif cmd.lower() == "mov" and prfx and len(args)>0 and user.name.lower() in adminuser:
            var = args.split(maxsplit=1)
            search = var[1].split()
            url = urlreq.urlopen("https://www.googleapis.com/youtube/v3/search?q=%s&part=snippet&MaxResults=1&key=yourapi" % "+".join(search))
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
          try:  
            var = args.replace(" ","+")
            response = requests.get("https://www.bing.com/search?q=%s&qs=n&form=QBLH&sp=-1&pq=%s" % (var,var), headers={"user-Agent":"Mozilla/5.0"}, verify=True)
            soup = BeautifulSoup(response.text, "html.parser")
            a = []
            for ref in soup.findAll('a'):
                if ("http://" or "https://") in str(ref.get('href')):
                    if ("go.microsoft" or "choice.microsoft.com" or "advertise.bingads.microsoft.com") in str(ref.get('href')):
                        continue
                    else:
                        a.append(str(ref.get('href')))
            room.message(font(msg("\r\r\rSearch query : <u>"+args+"</u> \r\rSearch Results :- \r\r\r"))+font(msg('\r'.join(a[:(len(a)-3)]))), True)    
          except Exception as e:
              print(str(e))
        #Command room/user ss
        elif cmd.lower() == "russ" and prfx and len(args)>0 and user.name.lower() in adminuser:
            chop = webdriver.ChromeOptions()
            chop.add_extension('adblock.crx')
            driver = webdriver.Chrome(chrome_options = chop)
            driver.get("http://"+args.lower()+".chatango.com")
            sleep(10)
            driver.save_screenshot('roompic.jpg')
            driver.quit()
            client_id = 'fbacb345ce77234'
            headers = {"Authorization": "Client-ID your client ID"}
            api_key = 'yourapi'
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

        #Command creep
        elif cmd.lower() == "creep" and prfx and len(args)>0:
            try:
                var = args.split(maxsplit=1)
                lurkuser = True
                stalkuser = var[0].lower()
                thisroom = var[1].lower()
                room.message(msg("Creep Mode Activated. Target : "+stalkuser.title()) ,True)
            except Exception as e:
                print(str(e))

        #Command creepoff
        elif cmd.lower() == "creepoff" and prfx:
            try:
                lurkuser = False
                room.message(msg("Creep Mode Deactivated!"), True)
            except:
                print(str(e))
            
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
                room.message(font(msg("\r\r\r"+user.name.title()))+font(msg(" Rolling Dice : -"))+"<f x11ffffff=\'1\'>"+msg("\r\r\rRolled Dice :")+'<f x11ffffff=\'1\'><b>\rRolled Dice : </b>'.join(dice)+font(msg("\r\rTotal : "))+str(total), True)    
            dice.clear()
            
        #Command rhyming word
        elif cmd.lower() == "rhyme" and prfx and user.name.lower() == "rebellus":
            if len(args) == 0:
                room.message(font(msg("<u>Syntax</u> : "+"$rhyme word")))
            else:
                try:
                    url = "http://www.rhymer.com/RhymingDictionary/"+args+".html"
                    response = requests.get(url)
                    print(response.text)
                except:
                    room.message(font(msg("Word Not Found!")))

        #Command ytinfotrigger
        elif cmd.lower() == "cytinfo" and prfx and ytinfotrigger:
            ytinfotrigger = False
            room.message(font(msg("Turning Off Youtube Link Info!")), True)

        #Command ytinfotrigger
        elif cmd.lower() == "cytinfo" and prfx and ytinfotrigger == False:
            ytinfotrigger = True
            room.message(font(msg("Turning On Youtube Link Info!")), True)    

        #Command ytdlink
        elif cmd.lower() == "ytdlink" and prfx:
            ytdlink = not ytdlink
            if ytdlink:
                room.message(font(msg("Alright I'll provide Download Link with youtube info.")), True)
            else:
                room.message(font(msg("Ok, I wont provide Download Link anymoar.")), True)

        #Command ytinfo
        elif "https://www.youtube.com/watch?v=" in message.body and ytinfotrigger:
          try:  
            url = message.body
            response = requests.get(url, headers={"User-Agent":"Mozilla/5.0"}, verify=True)
            #test = ghost((response.text).encode("utf-8"))
            #print(test)
            soup = BeautifulSoup(response.text,"html.parser")
            title = soup.find("meta",{"property":"og:title"}).get('content')
            desc = soup.find("meta",{"property":"og:description"}).get('content')
            views = soup.find("div", {"class":"watch-view-count"}).text
            views = views.replace("views","")
            if ytdlink:
                url = "http://keepvid.com/?url="+url
                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")
                dlinks = []
                for item in soup.find("table", {"class":"result-table"}).findAll('a'):
                    href = item.get('href')
                    if ("https://" or "http://") in href:
                        dlinks.append(href)       
                linktopost = dlinks[1]
                shortener = "https://is.gd/create.php"
                data = {
                        'url':linktopost
                    }
                response = requests.post(shortener, data=data)
                soup = BeautifulSoup(response.text, "html.parser")
                dlink = soup.find("input", {"id":"short_url"}).get('value')
                #image = soup.find("meta",{"property":"og:image"}).get('content')
                room.message(font(msg("<u>Video Title</u> : "))+font(msg(title))+font(msg("\r&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp<u>Description</u> : "+desc))+font(msg("\r&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp<u>Views</u> : "+views))+font(msg("\r&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbspDownload Link : "+dlink)), True)
            else:
                room.message(font(msg("<u>Video Title</u> : "))+font(msg(title)+font(msg("\r&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp<u>Description</u> : "+desc))+font(msg("\r&nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp<u>Views</u> : "+views))), True)
          except Exception as e:
              print(str(e))
              room.message(font(msg("Video Title : "+title)), True)
        #timu = time.ctime()
        #Command pet
        #elif timu >= time.ctime():
        
        #Command test
        elif cmd.lower() == "slap" and prfx and len(args)>0:
            var = args.split(maxsplit=1)
            site = "https://api.imgflip.com/caption_image"
            params = {'template_id':438680, 'username':'Devinozaki', 'password':'dev18997', 'text0':user.name.title()+" slaps "+var[0], 'text1':var[1]}
            response = requests.post(site, data=params, headers={"User-Agent":"Mozilla/5.0"}, verify=True)
            jok = json.loads(response.text.replace("\\", ""))
            print(response.text.replace("\\", ""))
            room.message(font(msg(str(jok['data']['url']))), True)

        #Command time
        elif message.body == "what time is it":
            room.message(msg("\r\r\rHere are the ways to know the current time \r 1.) Stand up slap your ass and go watch the wallclock or something. \r 2.) Kill yourself and note your time of death"), True)

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
                room.message(font(msg(cl[0]+"% "+chance)), True)    
            else:
                room.message(font(msg("@"+user.name.title()+" You need to give two names !")), True)

        #Command
        #elif cmd.lower() == "stealacc" and prfx and len(args)>0 and user.name.lower() == "devin997":
            #sleep(10)
            #room.message(msg("Success!..Account Details has been sent to your PM Devin997"), True)

        #Command logout
        elif cmd.lower() == "logout" and prfx and len(args)>0:
            self.getRoom(args).logout()
            room.message(font(msg("Steal Mode Activated !")), True)

        #Command ghost
        elif cmd.lower() == "ghost" and prfx and len(args)>0:
            url = "https://ghostbin.com/paste/new"
            data = {'text':args, 'lang':'text'}
            response = requests.post(url, data=data, headers={"User-Agent":"Mozilla/5.0"})
            room.message(font(msg(response.url)), True)

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
                room.message(font(msg("Searching %s on %s : %s" % (query, web, url))), True)
            except Exception as e:
                print(str(e))
                
        #Command extractcolors
        elif cmd.lower() == "extcolor" and prfx and len(args)>0:
            try:
                if (("http://" or "https://") and (".jpg" or ".png" or ".jpg" or ".jpeg")) not in args:
                    return
                key = "yourapi"
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
            room.message(font(msg("Autotranslate OFF !!")), True)
          except Exception as e:
              print(str(e))

        #Command AutoTranslateON
        elif cmd.lower() == "transon" and prfx:
          try:  
            trigger = True;
            room.message(font(msg("Autotranslate ON !!")), True)
          except Exception as e:
              print(str(e))

        #Command bgimg
        elif cmd.lower() == "bgimg" and prfx and len(args)>0:
            try:
                image = "http://"+args+".chatango.com/profileimg/"+args[0]+"/"+args[1]+"/"+args+"/msgbg.jpg"
                room.message(font(msg(args.title()+"\'s"))+font(msg(" Background Image :- \r\r"+image)), True)
            except:
                room.message(font(msg("Bg Image Not Found!")), True)
                       
        #Command searchmovie
        elif cmd.lower() == "smovie" and prfx and len(args)>0:
            try:
                key = "yourapi"
                url = "https://api.themoviedb.org/3/search/movie?api_key=%s&query=%s" % (key, args.replace(" ","+"))
                response = requests.get(url)
                jok = json.loads(response.text)
                image = "https://image.tmdb.org/t/p/w640"+jok["results"][0]["poster_path"]
                title = jok["results"][0]["title"]
                release_date = jok["results"][0]["release_date"]
                overview = jok["results"][0]["overview"]
                room.message(font(msg("\r\r\r"))+font(msg(image))+font(msg("\r\r<u>Title</u> :"))+font(msg(title))+font(msg("\r\r<u>Release Date</u> : "))+font(msg(release_date))+font(msg("\r\r<u>OverView</u> :"))+font(msg(overview)), True)
            except:
                room.message(font(msg("Movie Not Found!")), True)
        
        #Command quote
        elif cmd.lower() == "quote" and len(args)>0 and prfx:
            try:
                quotefile = open("quote.txt", "a")
                quote = args + " - By "+ user.name.title()
                quotefile.write(quote+"\n")
                quotefile.close()
                room.message(font(msg("Your quote has been saved "))+font(msg(user.name.title())), True)
            except Exception as e:
                room.message(msg(str(e)), True)

        #Command rquote
        elif cmd.lower() == "rquote" and prfx:
            file = open("quote.txt","r")
            quote = []
            for line in file:
                quote.append(line)
            if len(quote) == 0:
                room.message(msg("Quote Db is empty."), True)
                return
            file.close()
            room.message(font(msg(random.choice(quote).replace("\n","\r"))), True)    
            
        #Command colorext
        elif cmd.lower() == "colorext" and prfx:
            try:
                if len(args) == 0:
                    room.message(msg("<u>Syntax</u> : $colorext imagelink numberofcolors"), True)
                    return
                else:
                    if len(args.split(maxsplit=1)) == 2:
                        var = args.split(maxsplit=1)
                        import Algorithmia
                        if (("http://" or "https://") and (".jpg" or ".png" or "gif" or ".jpeg")) in args:
                            inputdata = {'url':var[0]}
                            client = Algorithmia.client('yourapi')
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
                                if len(hexs) == int(var[1]):
                                    break
                            data = ""
                            for item in hexs:
                                data = data + "\r<f x11"+item[1:]+"=\'1\'>"+"<b>"+item+"</b>"
                                #"\r".join(hexs)
                            #print(data)
                            #test = "<f x113a6c63=\'Comic\'>#3a6c63"
                            #room.message(test, True)
                            room.message("\r\r\r"+var[0]+msg("\r\r\rColors In the Image :-\r")+data, True)
                        else:                    
                            room.message(font(msg("Not a valid image")), True)
                    else:
                        room.message(font(msg("Imagelink or No of Colors is missing. \r <u>Syntax</u> : $colorext imagelink numberofcolors")), True)
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
            args = urllib.parse.quote(message.body)
            language_translator = LanguageTranslatorV2(
            username='yourapi',
            password='yourpassword')
            response = json.dumps(language_translator.identify(args.encode("utf-8")));
            lsymbol = json.loads(response)
            lsymbol = str(lsymbol["languages"][0]["language"])
            print(lsymbol)
            if lsymbol == "en":
                return
            url = "https://translate.yandex.net/api/v1.5/tr.json/translate?key=yourkey"
            payload = {
                'key':'your key',
                'text':message.body,
                'lang':lsymbol+"-"+"en",
                'format':'plain'
                }
            response = requests.post(url, data=payload)
            result = json.loads(response.text)
            room.message(font(msg("\r\r\r"+user.name.title()+" : "))+font(msg(message.body))+font(msg("\r <u>Translated text</u> \r"))+font(msg(user.name.title()+" : "))+font(msg(result["text"][0])), True)
          except Exception as e:
              print(str(e))
        
  #except Exception as e:
      #print(str(e))
      
rooms = ["prettylitty", "mabottesting","madebugroom"]
username = "accusername"
selecteduser = ["stupidaf","mouns12","devin997", "devinozaki"]
accs = ['devinozaki', 'devin997','bungyoi','ec5tacy','mih4el','lovebotty','r1kam1ka']
adminuser = ["devinozaki","devin997","orangue","bungyoi","mouns12"]
cmds = []
temprooms = []
password = "password"
#try:
lovebot.easy_start(rooms, username, password)
#except Exception as e:
    #print(str(e))
    #os.system("start C:\\Users\\Devin\\Desktop\\chatbot\\silentrunner.vbs")
    #exit()
