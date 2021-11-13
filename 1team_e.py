import random
import time
random.seed()


lname=["sib","porteghal","moz",
      "sag","gorbe","moosh",
      "kif","kafsh","kolah","lamp"
      ]
lq=[
    "0. guess :",
    "1. khordani hast ya na? ",
    "2. jandar ya bijan ?",
    "3. to jib ja mishe ya na?",
    "4. range on chie?",
    "5. poshidani hast ya na?",
    "6. mishe to khone estefade kard ya na?",
    "7. electiriki ya na ? ",
    "8. size chie?",
    "9. maze chie?",
    "10. vahshi ya ahli?",
    "11. zemestoni ya tabestoni?",
    "12. pestandar ya na?",
    "13. parande ya na?",
    "14. khazande ya na?",
    "15. gherde ya na?",
    "16. shekastani hast ya na?",
    "17. maye ya jamed?",
    "18. ghazash chie?",
    "19. tazeinie ya na?",
    "20. sedash chie?"
   ]
def lamp (input_user):
    ansewrs = [
    "na",
    "bijan" ,
    "ja momkene mishe",
    "anvae rang ha",
    "are",
    "bale",
    "are",
    "anvae size ha",
    "nadare!",
    "na",
    "hardo",
    "na",
    "na",
    "na",
    "momkene",
    "are",
    "jamed",
    "nadare",
    "momkene",
    "nadare"
    ]
    print (ansewrs[input_user-1])
def kolah (input_user):
    ansewrs = [
    "na",
    "bijan" ,
    "ja momkene mishe",
    "anvae rang ha",
    "are",
    "bale",
    "na",
    "anvae size ha",
    "nadare!",
    "na",
    "hardo",
    "na",
    "na",
    "na",
    "na",
    "na",
    "jamed",
    "nadare",
    "momkene",
    "nadare"
    ]
    print (ansewrs[input_user-1])
def kafsh (input_user):
    ansewrs = [
    "na",
    "bijan" ,
    "na",
    "anvae rang ha",
    "are",
    "bale",
    "na",
    "anvae size ha",
    "nadare!",
    "na",
    "hardo",
    "na",
    "na",
    "na",
    "na",
    "na",
    "jamed",
    "nadare",
    "momkene",
    "nadare"
    ]
    print (ansewrs[input_user-1])
def kif (input_user):
    ansewrs = [
    "na",
    "bijan" ,
    "ja momkene mishe",
    "anvae rang ha",
    "are",
    "bale",
    "na",
    "anvae size ha",
    "nadare!",
    "na",
    "hardo",
    "na",
    "na",
    "na",
    "na",
    "na",
    "jamed",
    "nadare",
    "momkene",
    "nadare"
    ]
    print (ansewrs[input_user-1])

def moz (input_user):
    ansewrs = [
    "khordani",
    "bijan" ,
    "ja mishe",
    "zard",
    "na",
    "bale",
    "na",
    "khochak",
    "shirin",
    "marbot nist",
    "nadare(bishtar tabeston)",
    "na",
    "na",
    "na",
    "na",
    "na",
    "jamed",
    "nadare",
    "mitone bashe",
    "nadare"
    ]
    print (ansewrs[input_user-1])
def moosh (input_user):
    ansewrs = [
    "na",
    "jandar" ,
    "ja momkene mishe",
    "anvae rang ha",
    "na",
    "bale",
    "na",
    "kochik",
    "nadare!",
    "hardo momkene",
    "nadare",
    "bale",
    "na",
    "na",
    "na",
    "na",
    "jamed",
    "hame chi",
    "momkene",
    "nadare"
    ]
    print (ansewrs[input_user-1])
def gorbe (input_user):
    ansewrs = [
    "na",
    "jandar" ,
    "ja momkene mishe",
    "anvae rang ha",
    "na",
    "bale",
    "na",
    "anvae size ha",
    "nadare!",
    "hardo momkene",
    "nadare",
    "bale",
    "na",
    "na",
    "na",
    "na",
    "jamed",
    "mahi",
    "momkene",
    "mio mio"
    ]
    print (ansewrs[input_user-1])
def sag (input_user):
    ansewrs = [
    "na",
    "jandar" ,
    "ja momkene mishe",
    "anvae rang ha",
    "na",
    "bale",
    "na",
    "anvae size ha",
    "nadare!",
    "hardo momkene",
    "nadare",
    "bale",
    "na",
    "na",
    "na",
    "na",
    "jamed",
    "ostekhon",
    "momkene",
    "vagh vagh"
    ]
    print (ansewrs[input_user-1])

def sib (input_user):
    ansewrs = [
    "khordani",
    "bijan" ,
    "ja mishe",
    "ghermez,sabz zard",
    "na",
    "bale",
    "na",
    "khochak",
    "torsh",
    "marbot nist",
    "nadare",
    "na",
    "na",
    "na",
    "gherd",
    "na",
    "jamed",
    "nadare",
    "mitone bashe",
    "nadare"
    ]
    print (ansewrs[input_user-1])

def porteghal (input_user):
    ansewrs = [
    "khordani",
    "bijan" ,
    "ja mishe",
    "narengi",
    "na",
    "bale",
    "na",
    "khochak",
    "torsh",
    "marbot nist",
    "nadare(bishtar zemeston)",
    "na",
    "na",
    "na",
    "gherd",
    "na",
    "jamed",
    "nadare",
    "mitone bashe",
    "nadare"
    ]
    print (ansewrs[input_user-1])

ans = random.choice(lname)
score = 100
win = False
dict_guess={}
count = 1
while (score>0):
    for i in range (21):
        print (lq[i])
    input_user = input("adad goziene mored nazar : ")
    if (input_user.isnumeric()):
        if (int(input_user) <=20 and int(input_user)>=0):
            input_user=int(input_user)
            if (input_user == 0):
                guess_ans=input("javab shoma ? : ").lower()
                dict_guess.update({count :guess_ans})
                count+=1
                if (guess_ans == ans ):
                    score+=20
                    print (" bordi!!!!!!!!!! \n" )
                    win = True
                    break
                else:
                    score-=10
                    print (" eshtebah bod \n",score ,'\n','chand sanie ta edame bazi')
                    time.sleep(5)
            else:
                if (ans == "sib"):
                    sib(input_user)
                if (ans == "porteghal"):
                    porteghal(input_user)
                if (ans == "moz"):
                    moz(input_user)
                if (ans == "sag"):
                    sag(input_user)
                if (ans == "gorbe"):
                    gorbe(input_user)
                if (ans == "moosh"):
                    moosh(input_user)
                if (ans == "lamp"):
                    lamp(input_user)
                if (ans == "kif"):
                    kif(input_user)
                if (ans == "kafsh"):
                    kafsh(input_user)
                if (ans == "kolah"):
                    kolah(input_user)
                score-=5
                print (score ,"\nchand sanie ta edame bazi","\n\n\n",)
                time.sleep(5)
        else:
            print()
            print(">>>>lotfan az bein adad mojod!!<<<<")
            print()
            time.sleep(5)
    else :
        print()
        print(">>>lotfan bein gozine hay mojod entekhab konid!!!<<<")
        print()
        time.sleep(5)
else:
    ("bakhti!!!!\n","0")

print()
print('--------recorded history----------')
print(dict_guess,'\n',ans ,'score is:','\n',score)



