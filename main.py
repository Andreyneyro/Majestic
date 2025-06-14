
Твоя задача создать универсалльный py скрипт который  будет выполнять пополнение товаров путем закупки у дригих 

база данных как должна выглядеть id, категория, лотбай, тволотбай, разделение - это уникальное значение по базе оно нужно при парсинге купленого товара 

1. 
начнем с того то что программа должна заходить в профиль https://funpay.com/users/15162792/ цифорки выведи в переменную 15162792 чтобы  было проще после чего наши лоты при парсинге лежат здесь 
<div class="offer">
                                    <div class="offer-list-title-container">
                                        <div class="offer-list-title">
                                            <h3><a href="https://funpay.com/lots/3267/">Оффлайн активации AI Limit</a></h3>
                                        </div>
                                                                                    <div class="offer-list-title-button">
                                                <a href="https://funpay.com/lots/3267/trade" class="btn btn-default btn-plus"><i class="fa fa-pen"></i></a>
                                            </div>
                                                                            </div>
                                    <div class="offer-tc-container">
                                        <!--noindex-->
<div class="tc table-hover table-clickable tc-short showcase-table tc-sortable" data-section-type="lot">
<div class="tc-header">
<div class="tc-desc">Описание</div>
<div class="tc-price sort" data-sort-field="tc-price" data-sort-type="num">Цена <i class="fa"></i></div>
</div>

<a href="https://funpay.com/lots/offer?id=44436204" class="tc-item">
<div class="tc-desc">
<div class="tc-desc-text">28312</div>
</div>
<div class="tc-price" data-s="33155.600815">
<div>33 156 <span class="unit">₽</span></div>
<div class="sc-offer-icons"><i class="auto-dlv-icon"></i></div>
</div>
</a>
</div>
<!--/noindex-->                                    </div>
                                </div>


это один из примеров в профиле очень много лотов может быть сколько угодно тебе надо от сюда вытащить из каждого лота эту ссылку https://funpay.com/lots/offer?id=44436204 именно id это id лота уникальное 
потом надо взять https://funpay.com/lots/3267/ 3267 это категория она тоже нужна все у нас в профиле очень много лотов по этому сначало собираем эти данные

2.
следуйщий этам теперь когда у нас есть все данные с лотов мы должны сверить их с базой данных тебе надо будет ее создать тк как сейчас ее нету в базе данных будет храниться все  с лотами связаное
первое это лот id 44436204 так же если лота нету в базе данных а он есть у нас тебе его надо добавить туд второне значение это его категория если этго лота не было так же заполняешь эти данные
первые  данны заполнили если не было лотов предположим обратное лоты заполнены но уже мы не увидели некоторые лоты тогда наша задача отправить get запрос с лотами котоыре мы не нашли https://funpay.com/lots/offerEdit?node=3267&offer=44436204 после чего 
?node=категория&offer=id  в коде <input type="hidden" name="csrf_token" value="hxqi0j4hmppeyh9v"> hxqi0j4hmppeyh9v это является токеном который нужен он может меняется но не часто по этому просто сохранить в переменную 
следуйщее если 

<textarea class="form-control textarea-lot-secrets" name="secrets" rows="7" placeholder="Товар 1
Товар 2
Товар 3
...">123131s1ws1</textarea>

здесь пусто тоесть тут пример проосто 123131s1ws1 но если нету не чего то данный лот запоминается вернемся по позже к этому 
если значение было то тогда мы отпровляем запрос ниже в payload active значение надо будет поменять на on auto_delivery=on так же csrf_token это то что мыполучили при гет отправке остольные данные надо будет спарситьв   конце с гет запроса  и подставить сюда

url = "https://funpay.com/lots/offerSave"

payload = 'active=on&amount=1&auto_delivery=on&csrf_token=hxqi0j4hmppeyh9v&deleted=&fields%5Bdesc%5D%5Ben%5D=123&fields%5Bdesc%5D%5Bru%5D=123&fields%5Bimages%5D=&fields%5Bmethod%5D=%D0%9F%D0%BE%D0%B4%D0%B0%D1%80%D0%BA%D0%BE%D0%BC&fields%5Bpayment_msg%5D%5Ben%5D=123&fields%5Bpayment_msg%5D%5Bru%5D=28312&fields%5Bregion2%5D=&fields%5Bregion%5D=%D0%9A%D0%B0%D0%B7%D0%B0%D1%85%D1%81%D1%82%D0%B0%D0%BD&fields%5Bsummary%5D%5Ben%5D=28312&fields%5Bsummary%5D%5Bru%5D=28312&form_created_at=1749893036&location=&node_id=1042&offer_id=44436231&price=2233&secrets=123131s1ws1&server_id=10040'
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
	'Cookie': 'golden_key=d7aswvxw3615txo5f2vb9zm2x05jvrv2'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)


