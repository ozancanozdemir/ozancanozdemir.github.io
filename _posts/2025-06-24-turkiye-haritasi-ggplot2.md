---
title: "R’da ggplot2 paketi kullanarak Türkiye Haritası Çizdirmek"
tags: [r]
categories: [r]
author_profile: true   # true yaparsan kenar bar’da profil çıkar
layout: single          # Academic Pages varsayılanı
read_time: true
---

2018 yılında hazırlamış olduğum [**R’da ggplot2 ve maps Kutuphanelerini Kullanarak Harita Cizdirmek**](https://users.metu.edu.tr/ozancan/harita.html) adlı yazımda, R’da ggplot2 ve maps paketlerini kullanarak harita çizdirmeyi anlatmıştım. Yıllar içinde oldukça fazla bu yazıyla ilgili mailler aldım, ancak aldığım son mailler bu yazıda kullandığım kodların, kullandığım veri kaynağı olan **GADM** platformunun paylaştığı veri içeriğini değiştirmesi nedeniyle istenilen sonucu vermediğine dairdi, o nedenle yıllar sonra bu içeriği güncellemek istedim. Bu içerikte de yine **GADM** de bu sefer JSON olarak paylaşılan verileri kullanarak bir Türkiye haritası oluşturacağız ve bir örnek üzerinden gradyan (gradient) renklendirmeler yapacağız.

İlk olarak Türkiye'nin level-0 yani il düzeyindeki JSON formatındaki konumsal verilerine erişim sağlayacağız. Bu verileri bilgisayarınıza indirebileceğiniz gibi, direkt bağlantı üzerinden de erişim sağlayabilir ve lokal cihazınızda işleyebilirsiniz.

İlk olarak gerekli paketlerimizi yükleyelim. Bu eğiticide ggplot2, sf, stringr ve dplyr paketlerini kullanacağız.

```{r}
library(ggplot2) #veri görselleştirme için
library(sf) #konum verisini işlemek için
library(dplyr) #veri manipülasyonu için
library(stringr) #string işlemleri için
```

Şimdi veri setimizi indirelim.

```{r}
veriniz <- st_read("https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_TUR_1.json")
```

Bu veri seti içerisinde Türkiye'nin il düzeyindeki konum verileri bulunmaktadır. Bu veri setini inceleyelim.

```{r}
head(veriniz)
```

```
Simple feature collection with 6 features and 11 fields
Geometry type: MULTIPOLYGON
Dimension:     XY
Bounding box:  xmin: 29.6638 ymin: 36.5385 xmax: 44.4965 ymax: 41.0905
Geodetic CRS:  WGS 84
    GID_1 GID_0 COUNTRY   NAME_1      VARNAME_1 NL_NAME_1 TYPE_1 ENGTYPE_1 CC_1
1 TUR.1_1   TUR  Turkey    Adana         Seyhan        NA     Il  Province   NA
2 TUR.2_1   TUR  Turkey Adiyaman       Adıyaman        NA     Il  Province   NA
3 TUR.3_1   TUR  Turkey    Afyon Afyonkarahisar        NA     Il  Province   NA
4 TUR.4_1   TUR  Turkey     Agri  Ağri|Karaköse        NA     Il  Province   NA
5 TUR.5_1   TUR  Turkey  Aksaray             NA        NA     Il  Province   NA
6 TUR.6_1   TUR  Turkey   Amasya             NA        NA     Il  Province   NA
  HASC_1 ISO_1                       geometry
1  TR.AA TR-01 MULTIPOLYGON (((35.4143 36....
2  TR.AD TR-02 MULTIPOLYGON (((38.1033 37....
3  TR.AF    NA MULTIPOLYGON (((30.1946 37....
4  TR.AG TR-04 MULTIPOLYGON (((43.102 39.3...
5  TR.AK TR-68 MULTIPOLYGON (((33.2495 38....
6  TR.AM TR-05 MULTIPOLYGON (((35.3708 40....
```


Bu veri setinde bizim için önemli olan sütunlar `NAME_1` ve `geometry` sütunlarıdır. `NAME_1` sütunu il isimlerini, `geometry` sütunu ise il sınırlarını içermektedir.

Bu verinin bir avantajı görselleştirmeye hazır olmasıdır. Bu nedenle ggplot2 paketinden `geom_sf()` komutu ile bu veriyi görselleştirebiliriz.

```{r}
ggplot(data = veriniz) +geom_sf()
```

![image](https://github.com/user-attachments/assets/b21a43b5-6133-49e2-a5e8-17baf58962fa)


Bu kodu çalıştırdığınızda Türkiye haritasını göreceksiniz. Ancak bu harita üzerinde herhangi bir düzenleme (başlık, tema vs.) ve renklendirme yapmadık.

Şimdi bu haritayı renklendirelim. İlk olarak gradyan renklendirme yapalım. Bunun için ben, geçtiğimiz sene Aralık ayında yayınlamış olduğum `turkeyelections` paketindeki hazır verilerden kullanacağım.

İlk olarak gradyan renklendirme, yani sayısal değerlere göre belirli bir renk skalasında renk değişimi, uygulayacağım.

```{r}
secim_2023 <- turkeyelections::genel_secim_2023_il
secim_2023 |> head()
```

```
              Il Kayitli_Secmen_Sayisi Oy_Kullanan_Secmen_Sayisi
1          ADANA               1615326                   1414930
2       ADIYAMAN                399303                    327349
3 AFYONKARAHİSAR                536910                    484075
4           AĞRI                307114                    223699
5        AKSARAY                296566                    257662
6         AMASYA                256807                    236644
  Gecerli_Oy_Toplami MILLET HAK-PAR  TKP TKH SOL_PARTI GENCPARTI MEMLEKET   BBP
1            1378331   1411     873 1362 353      2290      4092    10733 12594
2             314939    515     387  428 114       900       334     1401  3119
3             471248    831     426  330 118       118         0     3716  5145
4             212257    125     285  281 137      1342       188     1557   605
5             250917    377     220  164  54       256       319     1727  5304
6             230956    159     247  135  62       136       224     1289  1914
  AK_Parti YENIDEN_REFAH    MHP YESIL_SOL_PARTI   TIP   AB ANAP  YP HKP
1   412978         24556 149861          133770 31347 1406    0   0 866
2   164067         15169  12754           38042     0    0    0 170 316
3   205859         14013  75657            1507  1020    0    0 134 364
4    51895          4186   4805          118684     0    0    0 356 199
5   108422          6465  52466            1477   628  394    0 108 197
6    90021          4133  38680             780   845    0  424  51 156
  MILLI_YOL VATAN_PARTISI GBP    CHP IYI_Parti  AP ZAFER_PARTISI
1         0          1804   0 392822    149935   0         29480
2         0           304 257  58397         0   0          1955
3         0           410 322  86842     59015   0         10604
4         0           242   0  22638      3466 463             0
5       158           271   0      0     63281   0          3379
6         0           152 151  68337     16590 742          3486
  SOSYALIST_GUC_BIRLIGI_ITTIFAKI CUMHUR_ITTIFAKI EMEK_VE_OZGURLUK_ITTIFAKI
1                             45            8594                       310
2                             21            1483                         0
3                             32            3230                        16
4                             20             588                         2
5                             29            2199                        13
6                              8            1550                         6
  MILLET_ITTIFAKI ATA_ITTIFAKI BAGIMSIZ_TOPLAM_OY MILLET_% HAK-PAR_% TKP_%
1            5823            8               1018     0.10      0.06  0.09
2               0            0              14806     0.16      0.12  0.13
3            1538            1                  0     0.17      0.09  0.07
4             133            3                 57     0.05      0.13  0.13
5               2            0               3007     0.15      0.08  0.06
6             647           31                  0     0.06      0.10  0.05
  TKH_% SOL_PARTI_% GENCPARTI_% MEMLEKET_% BBP_% AK_Parti_% YENIDEN_REFAH_%
1  0.02        0.16        0.29       0.77  0.91      29.96            1.78
2  0.03        0.28        0.10       0.44  0.99      52.09            4.81
3  0.02        0.02        0.00       0.78  1.09      43.68            2.97
4  0.06        0.63        0.08       0.73  0.28      24.44            1.97
5  0.02        0.10        0.12       0.68  2.11      43.21            2.57
6  0.02        0.05        0.09       0.55  0.82      38.97            1.78
  MHP_% YESIL_SOL_PARTI_% TIP_% AB_% ANAP_% YP_% HKP_% MILLI_YOL_%
1 10.87              9.70  2.27 0.10   0.00 0.00  0.06        0.00
2  4.04             12.07  0.00 0.00   0.00 0.05  0.10        0.00
3 16.05              0.31  0.21 0.00   0.00 0.02  0.07        0.00
4  2.26             55.91  0.00 0.00   0.00 0.16  0.09        0.00
5 20.90              0.58  0.25 0.15   0.00 0.04  0.07        0.06
6 16.74              0.33  0.36 0.00   0.18 0.02  0.06        0.00
  VATAN_PARTISI_% GBP_% CHP_% IYI_Parti_% AP_% ZAFER_PARTISI_%
1            0.13  0.00 28.49       10.87 0.00            2.13
2            0.09  0.08 18.54        0.00 0.00            0.62
3            0.08  0.06 18.42       12.52 0.00            2.25
4            0.11  0.00 10.66        1.63 0.21            0.00
5            0.10  0.00  0.00       25.21 0.00            1.34
6            0.06  0.06 29.58        7.18 0.32            1.50
  SOSYALIST_GUC_BIRLIGI_ITTIFAKI_% CUMHUR_ITTIFAKI_%
1                             0.00              0.62
2                             0.00              0.47
3                             0.00              0.68
4                             0.00              0.27
5                             0.01              0.87
6                             0.00              0.67
  EMEK_VE_OZGURLUK_ITTIFAKI_% MILLET_ITTIFAKI_% ATA_ITTIFAKI_%
1                        0.02              0.42           0.00
2                        0.00              0.00           0.00
3                        0.00              0.32           0.00
4                        0.00              0.06           0.00
5                        0.00              0.00           0.00
6                        0.00              0.28           0.01
  BAGIMSIZ_TOPLAM_OY_%
1                 0.07
2                 4.70
3                 0.00
4                 0.02
5                 1.19
6                 0.00

```


İndirdiğimiz veri setinde `Il` sütunu il isimlerini, % işareti ile beraber yer alan parti isimleri ise o partinin oy oranının illere göre yüzde olarak dağılımını içermektedir.

`dplyr` paketi içinde yer alan `glimpse()` komutu ile de verideki değişkenlerin sınıflarını da görebiliriz.

```{r}
secim_2023 |> glimpse()
```

```
Rows: 87
Columns: 64
$ Il                                 <chr> "ADANA", "ADIYAMAN", "AFYONKARAHİSA…
$ Kayitli_Secmen_Sayisi              <dbl> 1615326, 399303, 536910, 307114, 29…
$ Oy_Kullanan_Secmen_Sayisi          <dbl> 1414930, 327349, 484075, 223699, 25…
$ Gecerli_Oy_Toplami                 <dbl> 1378331, 314939, 471248, 212257, 25…
$ MILLET                             <dbl> 1411, 515, 831, 125, 377, 159, 1124…
$ `HAK-PAR`                          <dbl> 873, 387, 426, 285, 220, 247, 459, …
$ TKP                                <dbl> 1362, 428, 330, 281, 164, 135, 3561…
$ TKH                                <dbl> 353, 114, 118, 137, 54, 62, 552, 20…
$ SOL_PARTI                          <dbl> 2290, 900, 118, 1342, 256, 136, 142…
$ GENCPARTI                          <dbl> 4092, 334, 0, 188, 319, 224, 2023, …
$ MEMLEKET                           <dbl> 10733, 1401, 3716, 1557, 1727, 1289…
$ BBP                                <dbl> 12594, 3119, 5145, 605, 5304, 1914,…
$ AK_Parti                           <dbl> 412978, 164067, 205859, 51895, 1084…
$ YENIDEN_REFAH                      <dbl> 24556, 15169, 14013, 4186, 6465, 41…
$ MHP                                <dbl> 149861, 12754, 75657, 4805, 52466, …
$ YESIL_SOL_PARTI                    <dbl> 133770, 38042, 1507, 118684, 1477, …
$ TIP                                <dbl> 31347, 0, 1020, 0, 628, 845, 0, 130…
$ AB                                 <dbl> 1406, 0, 0, 0, 394, 0, 1111, 1109, …
$ ANAP                               <dbl> 0, 0, 0, 0, 0, 424, 1810, 1936, 177…
$ YP                                 <dbl> 0, 170, 134, 356, 108, 51, 0, 136, …
$ HKP                                <dbl> 866, 316, 364, 199, 197, 156, 494, …
$ MILLI_YOL                          <dbl> 0, 0, 0, 0, 158, 0, 623, 656, 635, …
$ VATAN_PARTISI                      <dbl> 1804, 304, 410, 242, 271, 152, 1292…
$ GBP                                <dbl> 0, 257, 322, 0, 0, 151, 778, 548, 6…
$ CHP                                <dbl> 392822, 58397, 86842, 22638, 0, 683…
$ IYI_Parti                          <dbl> 149935, 0, 59015, 3466, 63281, 1659…
$ AP                                 <dbl> 0, 0, 0, 463, 0, 742, 2525, 2820, 3…
$ ZAFER_PARTISI                      <dbl> 29480, 1955, 10604, 0, 3379, 3486, …
$ SOSYALIST_GUC_BIRLIGI_ITTIFAKI     <dbl> 45, 21, 32, 20, 29, 8, 73, 52, 37, …
$ CUMHUR_ITTIFAKI                    <dbl> 8594, 1483, 3230, 588, 2199, 1550, …
$ EMEK_VE_OZGURLUK_ITTIFAKI          <dbl> 310, 0, 16, 2, 13, 6, 37, 83, 109, …
$ MILLET_ITTIFAKI                    <dbl> 5823, 0, 1538, 133, 2, 647, 5201, 3…
$ ATA_ITTIFAKI                       <dbl> 8, 0, 1, 3, 0, 31, 167, 170, 202, 2…
$ BAGIMSIZ_TOPLAM_OY                 <dbl> 1018, 14806, 0, 57, 3007, 0, 562, 1…
$ `MILLET_%`                         <dbl> 0.10, 0.16, 0.17, 0.05, 0.15, 0.06,…
$ `HAK-PAR_%`                        <dbl> 0.06, 0.12, 0.09, 0.13, 0.08, 0.10,…
$ `TKP_%`                            <dbl> 0.09, 0.13, 0.07, 0.13, 0.06, 0.05,…
$ `TKH_%`                            <dbl> 0.02, 0.03, 0.02, 0.06, 0.02, 0.02,…
$ `SOL_PARTI_%`                      <dbl> 0.16, 0.28, 0.02, 0.63, 0.10, 0.05,…
$ `GENCPARTI_%`                      <dbl> 0.29, 0.10, 0.00, 0.08, 0.12, 0.09,…
$ `MEMLEKET_%`                       <dbl> 0.77, 0.44, 0.78, 0.73, 0.68, 0.55,…
$ `BBP_%`                            <dbl> 0.91, 0.99, 1.09, 0.28, 2.11, 0.82,…
$ `AK_Parti_%`                       <dbl> 29.96, 52.09, 43.68, 24.44, 43.21, …
$ `YENIDEN_REFAH_%`                  <dbl> 1.78, 4.81, 2.97, 1.97, 2.57, 1.78,…
$ `MHP_%`                            <dbl> 10.87, 4.04, 16.05, 2.26, 20.90, 16…
$ `YESIL_SOL_PARTI_%`                <dbl> 9.70, 12.07, 0.31, 55.91, 0.58, 0.3…
$ `TIP_%`                            <dbl> 2.27, 0.00, 0.21, 0.00, 0.25, 0.36,…
$ `AB_%`                             <dbl> 0.10, 0.00, 0.00, 0.00, 0.15, 0.00,…
$ `ANAP_%`                           <dbl> 0.00, 0.00, 0.00, 0.00, 0.00, 0.18,…
$ `YP_%`                             <dbl> 0.00, 0.05, 0.02, 0.16, 0.04, 0.02,…
$ `HKP_%`                            <dbl> 0.06, 0.10, 0.07, 0.09, 0.07, 0.06,…
$ `MILLI_YOL_%`                      <dbl> 0.00, 0.00, 0.00, 0.00, 0.06, 0.00,…
$ `VATAN_PARTISI_%`                  <dbl> 0.13, 0.09, 0.08, 0.11, 0.10, 0.06,…
$ `GBP_%`                            <dbl> 0.00, 0.08, 0.06, 0.00, 0.00, 0.06,…
$ `CHP_%`                            <dbl> 28.49, 18.54, 18.42, 10.66, 0.00, 2…
$ `IYI_Parti_%`                      <dbl> 10.87, 0.00, 12.52, 1.63, 25.21, 7.…
$ `AP_%`                             <dbl> 0.00, 0.00, 0.00, 0.21, 0.00, 0.32,…
$ `ZAFER_PARTISI_%`                  <dbl> 2.13, 0.62, 2.25, 0.00, 1.34, 1.50,…
$ `SOSYALIST_GUC_BIRLIGI_ITTIFAKI_%` <dbl> 0.00, 0.00, 0.00, 0.00, 0.01, 0.00,…
$ `CUMHUR_ITTIFAKI_%`                <dbl> 0.62, 0.47, 0.68, 0.27, 0.87, 0.67,…
$ `EMEK_VE_OZGURLUK_ITTIFAKI_%`      <dbl> 0.02, 0.00, 0.00, 0.00, 0.00, 0.00,…
$ `MILLET_ITTIFAKI_%`                <dbl> 0.42, 0.00, 0.32, 0.06, 0.00, 0.28,…
$ `ATA_ITTIFAKI_%`                   <dbl> 0.00, 0.00, 0.00, 0.00, 0.00, 0.01,…
$ `BAGIMSIZ_TOPLAM_OY_%`             <dbl> 0.07, 4.70, 0.00, 0.02, 1.19, 0.00,…

```

Bu eğiticide biz CHP'nin oy oranlarını harita renklendirme işlemi için kullanacağız, o yüzden bu veri setinden bir subset almamız gerekiyor.

```{r}
chp_data <- secim_2023 |> select(Il,`CHP_%`)
```

```{r}
chp_data
```

```
               Il CHP_%
1           ADANA 28.49
2        ADIYAMAN 18.54
3  AFYONKARAHİSAR 18.42
4            AĞRI 10.66
5         AKSARAY  0.00
6          AMASYA 29.58
7        ANKARA-1 41.86
8        ANKARA-2 20.38
9        ANKARA-3 27.75
10        ANTALYA 32.26
11        ARDAHAN 29.62
12         ARTVİN 29.74
13          AYDIN 35.50
14      BALIKESİR 31.33
15         BARTIN 31.65
16         BATMAN  7.91
17        BAYBURT  0.00
18        BİLECİK 26.54
19         BİNGÖL  5.15
20         BİTLİS  0.00
21           BOLU 21.61
22         BURDUR 31.02
23        BURSA-1 26.93
24        BURSA-2 21.07
25      ÇANAKKALE 35.27
26        ÇANKIRI  0.00
27          ÇORUM 30.98
28        DENİZLİ 31.82
29     DİYARBAKIR  7.63
30          DÜZCE 22.58
31         EDİRNE 39.35
32         ELAZIĞ 20.51
33       ERZİNCAN 36.31
34        ERZURUM  6.39
35      ESKİŞEHİR 34.05
36      GAZİANTEP 20.07
37        GİRESUN 20.33
38      GÜMÜŞHANE  0.00
39        HAKKARİ  6.66
40          HATAY 28.32
41          IĞDIR  5.91
42        ISPARTA 21.97
43     İSTANBUL-1 31.63
44     İSTANBUL-2 26.36
45     İSTANBUL-3 26.15
46        İZMİR-1 42.02
47        İZMİR-2 40.13
48  KAHRAMANMARAŞ 15.92
49        KARABÜK 21.69
50        KARAMAN 18.97
51           KARS 16.07
52      KASTAMONU 21.49
53        KAYSERİ 16.87
54      KIRIKKALE 26.46
55     KIRKLARELİ 45.60
56       KIRŞEHİR 29.12
57          KİLİS 19.93
58        KOCAELİ 23.72
59          KONYA 13.22
60        KÜTAHYA 16.42
61        MALATYA 21.38
62         MANİSA 29.26
63         MARDİN  6.55
64         MERSİN 30.83
65          MUĞLA 37.62
66            MUŞ  0.00
67       NEVŞEHİR 17.13
68          NİĞDE 23.95
69           ORDU 24.01
70       OSMANİYE 16.96
71           RİZE 21.36
72        SAKARYA 15.96
73         SAMSUN 19.40
74          SİİRT  7.15
75          SİNOP 25.43
76          SİVAS 15.97
77      ŞANLIURFA  7.46
78         ŞIRNAK  8.14
79       TEKİRDAĞ 36.26
80          TOKAT 20.37
81        TRABZON 17.68
82        TUNCELİ 32.12
83           UŞAK 28.93
84            VAN  8.20
85         YALOVA 28.62
86         YOZGAT  0.00
87      ZONGULDAK 32.02
```

Bu veri setini `veriniz` veri seti ile birleştirmeden önce yapmamız gereken bazı işlemler var. İlk olarak `chp_data` veri setinde yer alan `Il` sütunundaki il isimlerini `veriniz` veri setindeki `NAME_1` sütunundaki il isimleri ile aynı hale getirmemiz gerekiyor. Üstelik `chp_data` veri setinde bazı illerde seçim bölgeleri birden fazla olduğu için örneğin Ankara ve Istanbul gibi, bu illeri birleştirmemiz gerekiyor. Burada illerin ortalama değerlerini alarak bu boyut küçültme işlemini gerçekleştirdim. Daha sonra ise il isimlerini, `veriniz` doyasıyla birleştirirken uygun olması için kolon adı değişikliği ve harf boyutu değişiklikleriyle güncelledim.

```{r}
chp_data <- chp_data |>  mutate(
    NAME_1 = stringr::str_extract(Il, "^[A-Za-zÇĞÖŞÜİ]+") #sayısal değerleri çıkarttık 
  ) |>   group_by(NAME_1) %>%
  # Aynı şehirlerin ortalama CHP_%% değerini hesapla
  summarise(
    CHP_oy = mean(`CHP_%`, na.rm = TRUE),
    .groups = "drop"
  ) |>  mutate(
    NAME_1 = stringr::str_to_sentence(NAME_1)
  )
```

```{r}
chp_data
```

```
# A tibble: 81 × 2
   NAME_1         CHP_oy
   <chr>           <dbl>
 1 Adana            28.5
 2 Adiyaman         18.5
 3 Afyonkarahi̇sar   18.4
 4 Aksaray           0  
 5 Amasya           29.6
 6 Ankara           30.0
 7 Antalya          32.3
 8 Ardahan          29.6
 9 Artvi̇n           29.7
10 Aydin            35.5
# ℹ 71 more rows
```

Verimiz birleştirmeye hazır (mı?)

Henüz değil. Çünkü yaptığımız harf dönüşümü sonrasında **i** harfi ile ilgili bir sorun var. Bu sorunu çözmek için `str_replace_all()` fonksiyonunu kullanarak **i** harfini **i** harfine dönüştürmemiz gerekiyor.

```{r}
chp_data$NAME_1<-stringr::str_replace_all(chp_data$NAME_1,"i̇","i")
```

Bir sorunumuz daha var, iki veri setindeki il isimleri arasında uyuşmazlık gösterenler var? Örneğin `veriniz` dosyasında Zonguldak ili Zinguldak olarak kodlanmış durumda ya da Kırıkkale, Kinkkale olarak kodlanmış.

Aşağıdaki kod, bu uyuşmazlıkları çözmek için kullanılabilir.

```{r}
veriniz$NAME_1<-c("Adana", "Adiyaman", "Afyonkarahisar", "Ağri", "Aksaray", "Amasya",  "Ankara", "Antalya", "Ardahan", "Artvin", "Aydın", "Balıkesir", 
 "Bartın", "Batman", "Bayburt", "Bilecik", "Bingöl", "Bitlis",   "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Düzce", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Iğdır", "Isparta", "İstanbul", "İzmir",  "Kahramanmaraş", "Karabük", "Karaman", "Kars", "Kastamonu", "Kayseri", "Kilis","Kirikkale", "Kirklareli", "Kırşehir", "Kocaeli", "Konya",  "Kütahya", "Malatya", "Manisa", "Mardin", "Mersin", "Muğla",  "Muş", "Nevşehir", "Niğde", "Ordu", "Osmaniye", "Rize", "Sakarya",  "Samsun", "Şanlıurfa", "Siirt", "Sinop", "Şırnak", "Sivas",  "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Uşak", "Van", 
"Yalova", "Yozgat", "Zonguldak")
```

Evet, şimdi hazırız!

```{r}
veriniz_joined <- left_join(veriniz, chp_data, by = c("NAME_1" = "NAME_1"))
```

```{r}
veriniz_joined |> head()
```

```
Simple feature collection with 6 features and 12 fields
Geometry type: MULTIPOLYGON
Dimension:     XY
Bounding box:  xmin: 29.6638 ymin: 36.5385 xmax: 44.4965 ymax: 41.0905
Geodetic CRS:  WGS 84
    GID_1 GID_0 COUNTRY         NAME_1      VARNAME_1 NL_NAME_1 TYPE_1
1 TUR.1_1   TUR  Turkey          Adana         Seyhan        NA     Il
2 TUR.2_1   TUR  Turkey       Adiyaman       Adıyaman        NA     Il
3 TUR.3_1   TUR  Turkey Afyonkarahisar Afyonkarahisar        NA     Il
4 TUR.4_1   TUR  Turkey           Ağri  Ağri|Karaköse        NA     Il
5 TUR.5_1   TUR  Turkey        Aksaray             NA        NA     Il
6 TUR.6_1   TUR  Turkey         Amasya             NA        NA     Il
  ENGTYPE_1 CC_1 HASC_1 ISO_1 CHP_oy                       geometry
1  Province   NA  TR.AA TR-01  28.49 MULTIPOLYGON (((35.4143 36....
2  Province   NA  TR.AD TR-02  18.54 MULTIPOLYGON (((38.1033 37....
3  Province   NA  TR.AF    NA  18.42 MULTIPOLYGON (((30.1946 37....
4  Province   NA  TR.AG TR-04  10.66 MULTIPOLYGON (((43.102 39.3...
5  Province   NA  TR.AK TR-68   0.00 MULTIPOLYGON (((33.2495 38....
6  Province   NA  TR.AM TR-05  29.58 MULTIPOLYGON (((35.3708 40....
```

Şimdi haritamızı çizdirebiliriz. Bu koroplet haritada renk skalasında genellikle bilinenin aksine, yüksekten düşüğe geçişi mavi-turuncu renk skalasında gerçekleştireceğiz.

```{r}
ggplot(data = veriniz_joined) +geom_sf(aes(fill = CHP_oy))+
  scale_fill_gradient2(high = "steelblue", low = "darkorange",mid="white", midpoint = mean(veriniz_joined$CHP_oy,na.rm=T))+theme_void() +
  labs(title = "CHP'nin 2023 Seçim Sonuçları Oy Dağılımı", fill = "CHP Oy Oranı",caption = "Haritayı Hazırlayan: Ozancan Özdemir") + theme(plot.title = element_text(size = 15,face="bold"), plot.subtitle = element_text(size = 10,face="bold"), plot.caption = element_text(size = 10,face="bold"),legend.position = "top")
```

![image](https://github.com/user-attachments/assets/89e6b6c9-d719-441b-a79b-da1f6849fce2)


Bu komutta `ggplot2` paketinden `geom_sf()` fonksiyonu ile haritayı çizdik. `aes()` fonksiyonu ile renklendirme yapacağımız sütunu belirledik. `scale_fill_gradient2()` fonksiyonu ile renk skalasını belirledik. `theme_void()` fonksiyonu ile arka planı beyaz yaptık. `labs()` fonksiyonu ile başlık ve eksen isimlerini belirledik. `theme()` fonksiyonu ile başlık ve eksen isimlerinin boyutunu ve fontunu belirledik.

Sonuçta bu kodu çalıştırdığınızda Türkiye haritası üzerinde CHP'nin 2023 seçim sonuçlarına göre illere göre oy oranlarını göreceksiniz.

Umarım faydalı bir içerik olmuştur!

Bu dökümandaki kodlara [ilgili GitHub reposundan](https://github.com/ozancanozdemir/R-da-ggplot2-kullanarak-Turkiye-Haritas-Cizdirmek-Draw-Turkey-s-Map-in-R-with-ggplot2) ulaşabilirsiniz.

Soru ve görüşleriniz için ozancanozdemir\@gmail.com adresine e-mail yollayabilirsiniz.
