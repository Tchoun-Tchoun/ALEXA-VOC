import os
import random
from os import system
import urllib
system("pip install --upgrade  amino.fix")
system("pip install gtts")
system("pip install requests")
import aminofix as amino
import time
from gtts import gTTS
import requests
from uuid import uuid4
client=amino.Client()
os.system("clear")
print("\t\033[1;32m Alexa  \033[1;36m Community Bot \n\n   Fixed By Rad \n \n")
email="beatytiemoko@gmail.com"
password="azertyuiop"

client.login(email=email,password=password)

cid="118423274"
cidy=118423274

adm=[]
self=client.socket
def generate_transaction_id(self):
        return str(uuid4())
transaction=generate_transaction_id(self)

admx=["http://aminoapps.com/p/4vomqsp"]

client.join_community(cid)
for i in admx:
	try:
		w=client.get_from_code(i).objectId
		adm.append(w)
	except:
		print("Invalid link")
subclient=amino.SubClient(comId=cid,profile=client.profile)
msg="""Follow GC rules
1.Do not spam
2.Respect Leaders, curators, Host and Cohosts
3.Don't spread hate
4.Be polite in chatrooms"""
print("Bot joined community")
subclient=amino.SubClient(comId=cid,profile=client.profile)
print("Joining All chatrooms")
subclient=amino.SubClient(comId=cid,profile=client.profile)
print("Alexa 1.0 Ready")
l=[]
lis = ["C'est certain",
    "Demandez à S.T.I.V",
    "Sans aucun doute",
    "Arrete avec tes questions stupide, s'ilteplait",
    "Je ne comprend pas votre question",
    "Je ne suis pas Google",
    "Bref, Tarak est notre Dieu",
    "Evidemment",
    "Oui",
    "Sans aucun doute",
    "Repose ta questions plus tard",
    "Je ne pense pas",
    "Je dors, plus tard",
    "Je ne peut pas pour le moment",
    "Attend je me concentre",
    "Non" ,"Probablement","100%", "Pas sur"]

@client.event("on_group_member_join")
def on_group_member_join(data):
	if data.comId==cidy:
		try:
			x=data.message.author.icon
			response=requests.get(f"{x}")
			file=open("sample.png","wb")
			file.write(response.content)
			file.close()
			img=open("sample.png","rb")
			subclient.send_message(chatId=data.message.chatId,message=f"""
[C]━━━━━━━━━━━━━━━
[c]Coucou <${data.message.author.nickname}$>
[C]━━━━━━━━━━━━━━━
Bienvenue dans le tchat de la communauté One Piece Rp, actuellement numero 1 du serveur Francais, nous te souhaitons un bon sejour parmis nous
[C]━━━━━━━━━━━━━━━""",embedId=data.message.author.userId,embedTitle=data.message.author.nickname,embedLink=f"ndc://x{cid}/user-profile/{data.message.author.userId}",embedImage=img,mentionUserIds=[data.message.author.userId])
			print(f"\nwelcomed {data.message.author.nickname} to gc ")
		except Exception as e:
			print(e)
				
@client.event("on_group_member_leave")
def on_group_member_leave(data):
	if data.comId==cidy:
		try:
			subclient.send_message(chatId=data.message.chatId,message="""[c]Que ton ame repose en paix...""")
			print(f"Someone left the gc")
		except Exception as e:
			print(e)

@client.event("on_text_message")
def on_text_message(data):
	if data.comId==cidy:
		ex=data.message.content
		cd=ex.split(' ')
		x=cd[0]
		c=cd[1:]
		adx=[]
		for w in cd:
			adx.append(w)
		print(adx)
		if ex:
			for i in adx:
				if len(i)<=50:
					if i[:23]=="http://aminoapps.com/p/" or i[:23]=="http://aminoapps.com/c/":
						fok=client.get_from_code(i)
						cidx=fok.path[1:fok.path.index("/")]
						if cidx!=cid:
							try:
								subclient.delete_message(chatId=data.message.chatId,messageId=data.message.messageId,asStaff=True)
								s=subclient.get_chat_thread(data.message.chatId).title
								subclient.start_chat(userId=adm,message=f"ndc://x{cid}/user/profile/{data.message.author.userId} was advertisng in {s}")
								
								subclient.send_message(chatId=data.message.chatId,message=f"<${data.message.author.nickname} don't advertise here")
								print("spotted advertiser")
							except Exception as e:
								print(e)
			if x.lower()=="/startvc" and c==[]:
				if x.lower() not in l:
					try:
						subclient.send_message(chatId=data.message.chatId,message="Starting VC in 5 seconds")
						time.sleep(5)
						client.start_vc(comId=cid,chatId=data.message.chatId,joinType=1)
						#subclient.send_message(chatId=data.message.chatId,message=f"Vc started")
						print(f"VC started")
					except Exception as e:
						print(e)
						try:
							subclient.send_message(chatId=data.message.chatId,message=f"[ic]Je n'ai pas assez de  pouvoir pour cela, <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
						except:
							pass
				else:
					try:
						subclient.send_message(chatId=data.message.chatId,message=f"Start command is locked <${data.message.author.nickname}$> !!",mentionUserIds=[data.message.author.userId])
					except:
						pass
			if x.lower()=="/endl" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="Ending VC in 5 seconds")
					time.sleep(5)
					client.end_vc(comId=cid,chatId=data.message.chatId,joinType=2)
				except Exception as e:
					print(e)
					subclient.send_message(chatId=data.message.chatId,message=f"[ic][ic]Je n'ai pas assez de  pouvoir pour cela, , <${data.message.author.nickname}$>",mentionUserIds=[data.message.author.userId])
			if x.lower()=="/chocolat" and c==[]:
				try:
					subclient.send_message(chatId=data.message.chatId,message="""
╔╦╦
╠╬╬╬╣
╠╬╬╬╣ I ♥
╠╬╬╬╣ Chocolat
╚╩╩╩╝""")
					print(f"Info requested by {data.message.author.nickname}")
				except Exception as e:
					print(e)
			
def socketRoot():
	j=0
	while True:
		if j>=300:
			print("Updating socket.......")
			client.close()
			client.start()
			print("Socket updated")
			j=0
		j=j+1
		time.sleep(1)
socketRoot()