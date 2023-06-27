import requests
from data.config import connection_str as conn


def add_order(data: dict, tid):

    message = ""
    order_list = []
    price = 0

    for i in data["order_data"]:
        # reauests data about good
        get_ = requests.get(conn+"goods/getbyid", params={'id_': int(i["id"])})
        get_ = get_.json()
        # Creating sample for adding order list
        order_list.append([get_["id_"], i["count"]])
        # Counting end price of order
        price += int(get_["value"])*int(i["count"])
        # creating order message
        message += f"Предмет {get_['name']} в кол-ве {i['count']}шт. общей стоимостью: {int(get_['value'])*int(i['count'])}\n"
    # creating main order profile
    ordr = requests.post(conn+"order/create", json={"tid": tid, "price": float(price), "status": 0, "description": ""})
    ordr = ordr.json()
    print(ordr)
    # Creating order list profiles
    for i in order_list:
        ordrlist = requests.post(conn+"orderlist/create", json={"good_id": i[0], "amount": i[1], "order_id": ordr["id_"]})
    
    message += f"\tОбщая сумма заказа: {price}"
    return message


def reg_new_acc(tid, phone="", nickname="", name="", address=""):
    usr = requests.post(conn+"user/create", json={"tid": int(tid), "phone": phone, "nickname": nickname, "name": name, "address": address, "permissions": 0})
    usr = usr.json()
    print(usr)




if __name__ == "__main__":
    pass
    # print(test())
