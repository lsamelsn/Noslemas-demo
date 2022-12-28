import requests
import json

url = "https://api.crescolabs.com/carts/op/add-item"

payload = json.dumps({
  "inventory_id": 1186610,
  "quantity": 1,
  "usage_type": "recreational",
  "order_type": "pickup",
  "store_id": 632,
  "cart_id": 11625210
})
headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0',
		'Accept': 'application/json, text/plain, */*',
		'Accept-Language': 'en-US,en;q=0.5',
		'Accept-Encoding': 'gzip, deflate, br',
		'Content-Type': 'application/json',
		'x-api-key': 'hE1gQuwYcO54382jYNH0c9W0w4fEC3dJ8ljnwVau',
		'ordering_app_id': '9ha3c289-1260-4he2-nm62-4598bca34naa',
		'store_id': '632',
		'Authorization': 'eyJraWQiOiJTRFd6VGlZMjFQSVpkUDdMaVhzU3hEdUdyN3lFNkpYVCs0Um01UDQydlRBPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI5ZWM5MTcwOS04OTJiLTQwNGItOGNiOS04NzMxNmFhMTk3NDEiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tXC91cy13ZXN0LTJfSmpYd1lCUHBOIiwicGhvbmVfbnVtYmVyX3ZlcmlmaWVkIjpmYWxzZSwiY29nbml0bzp1c2VybmFtZSI6IjllYzkxNzA5LTg5MmItNDA0Yi04Y2I5LTg3MzE2YWExOTc0MSIsImdpdmVuX25hbWUiOiJMaW5jb2xuIiwiYXVkIjoiMzRhbjVlYmM3OHJrajZndWQxMjZnN21pY2kiLCJldmVudF9pZCI6ImZkMmQ2NTUwLTUxYzktNDA0Zi1iNGYwLTI2OTA2Y2Y3Y2Q0NyIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjcyMTkxNzUxLCJwaG9uZV9udW1iZXIiOiIrMTQ4MDM1MjI3MTgiLCJleHAiOjE2NzIxOTUzNTEsImlhdCI6MTY3MjE5MTc1MSwiZmFtaWx5X25hbWUiOiJTYW1lbHNvbiIsImVtYWlsIjoibGluY29sbi5zYW1lbHNvbkBnbWFpbC5jb20ifQ.PMMABBfXXKZOafOgE-ZpIzKRPhC7XYf_X0BwGQiXK-ZlNU80iN6BTEdcsO_QHNxGVmPCbi8kMsgCuEZs5HTmr5hjJsE4pHA3vv7wYIViZusDbF8Vp6-BgAFKpfvK8EE6Txyvwk4ar9PxGs7LNHnFLt-wWcnF7RfNHnEVxNvgklBL4FKZwjrB6i25zYug24P8tgfqIHh48Dm8b8N7r4kt8-9xus26nxblugiLMxh-hZCD4Ugqn7h_dBO1divocPj1qC325EtzHwTtjvmE2jeCHIBokUP-mxhgecZ_WDgy1ghT2-Oddfm5EDyWaqcPES20iik6O3Oij4OcXxn0mUrT1w',
		'Origin': 'https://www.sunnyside.shop',
		'DNT': '1',
		'Connection': 'keep-alive',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'cross-site',
		'TE': 'trailers'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
