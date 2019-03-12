import  requests
def query():
    response=requests.get("https://kyfw.12306.cn/otn/leftTicket/queryX?leftTicketDTO.train_date=2019-03-12&leftTicketDTO.from_station=SHH&leftTicketDTO.to_station=NJH&purpose_codes=ADULT")
    #print(response.text)
    return response.json()['data']["result"]
for i in query():
    temp_list=i.split("|")
    if temp_list[23]!="无" and temp_list[23]!="":
        print(temp_list[3],temp_list[23])
    else:
        print(temp_list[3],"没票")