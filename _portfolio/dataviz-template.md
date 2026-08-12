---
title: "Örnek Görselleştirme Başlığı (Example Visualization Title)"
category: dataviz-template
image: "/images/500x300.png"
meta: "Dashboard / Statik grafik / Interaktif uygulama (opsiyonel kısa etiket)"
description_tr: "Buraya çalışmanın Türkçe kısa açıklamasını yazın."
description_en: "Write a short English description of the work here."
link: "https://example.com"
link_label: "Open"
---

BU DOSYA BİR TASLAKTIR / THIS FILE IS A TEMPLATE.
Bu dosya "Data Visualization Portfolio" sekmesinde GÖRÜNMEZ çünkü yukarıdaki
"category" alanı "dataviz-template" olarak ayarlı. Bir çalışmanın gerçekten
sitede görünmesi için aşağıdaki adımları izleyin.

Yeni bir görselleştirme eklemek için:

1. Bu dosyayı bu klasör (_portfolio) içinde KOPYALAYIN ve yeni bir isim verin.
Örnek: dataviz-1.md, dataviz-2.md, dataviz-secim-2028.md ...

2. Yeni dosyanın en üstündeki front matter alanlarını doldurun:
- title: Çalışmanın başlığı (kart üzerinde görünür).
- category: BUNU "dataviz" OLARAK DEĞİŞTİRİN (bu satır değişmezse kart görünmez).
- image: Görselin adresi. Bir URL (https://...) ya da /images/ klasörüne
yüklediğiniz bir dosyanın yolu olabilir (örn: /images/benim-grafigim.png).
Görseller otomatik olarak standart bir kutuya (180px yükseklik) sığdırılıp
kırpılır, bu yüzden farklı boyutlardaki görseller için ekstra bir işlem
yapmanıza gerek yoktur.
- meta: Kart üzerinde başlığın altında görünen kısa etiket (opsiyonel).
Örn: "Interactive dashboard", "Static chart", "Shiny app".
- description_tr / description_en: Kısa açıklamalar (istediğiniz dilde
sadece birini de doldurabilirsiniz, diğerini silebilirsiniz).
- link / link_label: Çalışmanın canlı adresi ve buton yazısı (opsiyonel,
yoksa bu ikisini de silebilirsiniz).

3. Aynı klasörde bu şekilde istediğiniz kadar dosya oluşturarak
"Data Visualization Portfolio" sekmesine yeni kartlar ekleyebilirsiniz.

4. Bu taslak dosyayı (dataviz-template.md) silmeden bırakabilirsiniz;
"category" alanı "dataviz" olmadığı için sitede görünmeye devam etmez.
