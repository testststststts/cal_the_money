#APY，一年的投資報酬率 APY 20% -> APM (20/12)%

#有個人每天會固定投資money塊錢，並且每個月都會有固定利息。
#請計算最後會獲得多少錢
#共有三輸入
# 1. 一個月要投資多少錢
# 2. 每個月的利息為多少%
# 3. 要投資幾個月
# 4.

import xml.etree.ElementTree as ET
#匯入xml函式庫 並且命名為 ET
def xml_to_dict(element): #把xml轉換為dictionary的函式
    result = {}
    for child in element:
        if len(child) == 0:
            result[child.tag] = child.text
        else:
            result[child.tag] = xml_to_dict(child)
    return result
tree = ET.parse("setting.xml") #讀取設定檔
root = tree.getroot() #獲取裡面的資料
data = xml_to_dict(root) #把資料轉化為dictionary處理
money = int(data["money"]) #輸入，一個月要投資多少錢
interest = int(data["interest"]) #輸入，每個月的利息為多少%
month = int(data["month"]) #輸入，要投資幾個月
#注意，輸入的東西一律要變成整數
total = 0 #儲存總額用
for i in range(month): #迴圈，表示要投資幾個月
    total = total + money #總額加上新投資的金額
    total = total * (1 + interest/100) #計算月利

result = open("result.txt","w",encoding="utf-8") #建立儲存最終數據的檔案
result.write("你最後剩下的錢為:"+str(int(total))) #寫入數據
result.close() #關閉檔案
print(int(total)) #輸出總金額