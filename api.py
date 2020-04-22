import requests
import json
import os
import time
from time import localtime, strftime
os.system('cls||clear')
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'



#def jprint(obj):
#     create a formatted string of the Python JSON object
#    text = json.dumps(obj, sort_keys=True, indent=4)
#    print(text)
#print(response.json())
response=requests.get("https://code.junookyo.xyz/api/ncov-moh/data.json")
data=response.json()['data']
t1=data['global']['cases']
t2=data['global']['deaths']
t3=data['global']['recovered']
v1=data['vietnam']['cases']
v2=data['vietnam']['deaths']
v3=data['vietnam']['recovered']
moc=268 #mốc người nhiễu

obj = time.localtime() 
t = time.asctime(obj) 
a=obj.tm_hour
if 18>a>=13:
    b=a-12
    c=('chiều')
elif a<=9:
    b=a
    c=('sáng')
elif a>=18:
    b=a-12
    c=('tối')
elif 9<a<=12:
    b=a
    c='trưa'

thu=obj.tm_wday
if thu==6:
    thu='Chủ Nhật'
elif thu==0:
    thu='Thứ Hai'
elif thu>=1:
    thu=(thu+2)
    thu=str('Thứ ')+str(thu)


print(color.BOLD+color.RED +'=================[Toàn cầu]================='+ color.END);
print('| Số người nhiễm:   ',t1,'              |');
print('| Số ca tử vong:    ',t2,'               |');
print('| Số người hồi phục:',t3,'               |');
print(color.BOLD+color.RED+'|================[Việt Nam]================|'+ color.END);
print('| Số người nhiễm:   ',v1,'                  |');
print('| Số ca tử vong:    ',v2,'                    |');
print('| Số người hồi phục:',v3,'                  |');
print(color.BOLD +'============================================'+ color.END);

if int(v1)>moc:
 print(color.BOLD + color.RED+ '\nCảnh báo!!!!!!!!' + color.END)
 print('Tăng', int(int(v1)-moc),'ca nhiễm tại Việt Nam (●^●)')
elif int(v1)==moc:
    print(color.BOLD+color.GREEN+'\nKhông có ca nhiễm mới.'+ color.END)
gio=strftime("%I:%M:%S", localtime())
print('\n[Cập nhập',c,thu,'lúc «',gio,'»]\n')
