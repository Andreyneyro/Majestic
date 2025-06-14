import requests

url = "https://funpay.com/lots/offerSave"

payload = 'active=on&amount=1&auto_delivery=on&csrf_token=cjtl0mfx2roa5zl2&deleted=&fields%5Bdesc%5D%5Ben%5D=123&fields%5Bdesc%5D%5Bru%5D=123&fields%5Bimages%5D=&fields%5Bmethod%5D=%D0%9F%D0%BE%D0%B4%D0%B0%D1%80%D0%BA%D0%BE%D0%BC&fields%5Bpayment_msg%5D%5Ben%5D=123&fields%5Bpayment_msg%5D%5Bru%5D=28312&fields%5Bregion2%5D=&fields%5Bregion%5D=%D0%9A%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD&fields%5Bsummary%5D%5Ben%5D=28312&fields%5Bsummary%5D%5Bru%5D=28312&form_created_at=1749896693&location=&node_id=1042&offer_id=44436231&price=2233&secrets=123131s1ws1&server_id=10040'
headers = {
	'sec-ch-ua-platform': '"Windows"',
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0 (Edition std-2)',
	'Accept': 'application/json, text/javascript, */*; q=0.01',
	'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Opera GX";v="119"',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'sec-ch-ua-mobile': '?0',
	'Sec-Fetch-Site': 'same-origin',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Dest': 'empty',
	'host': 'funpay.com',
	'Cookie': 'PHPSESSID=HxpZNCkh-hrxNAZlqLymtaQCCGCETlFL; golden_key=d7aswvxw3615txo5f2vb9zm2x05jvrv2'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
