import requests,json
Base_url="http://127.0.0.1:8000/"
End_point="api/"
def delte_resource(id):
    up_data={
        "id":id
    }
    resp=requests.put(Base_url+End_point,data=json.dumps(up_data))
    print(resp.status_code)
    print(resp.json())
delte_resource(1)
# def update_resource(id):
#     up_data={
#         "id":id,
#         "esal":15500,
#         "eaddr":'pune',
#     }
#     resp=requests.put(Base_url+End_point,data=json.dumps(up_data))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(1)
#  this for put the resource
# def create_resource()
#     new_data={
#         "eno":102,
#         "ename":'raj',
#         "esal":10000,
#         "eaddr":"pune"
#     }
#     resp=requests.post(Base_url+End_point,data=json.dumps(new_data))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()

#get the resoure
# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={"id":id}
#     resp=requests.get(Base_url+End_point,data=json.dumps(data))
#     data=resp.json()
#     print(resp.status_code)
#     print(resp.json())
# get_resource(3)
