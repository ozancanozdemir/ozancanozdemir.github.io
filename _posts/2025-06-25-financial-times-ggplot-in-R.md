---
title: "How to make a Financial Times Plot with ggplot2 in R?"
tags: [r]
categories: [r]
author_profile: true
layout: single
read_time: true
---

Hello folks!

In this tutorial, I will illustrate how to draw a Financial Times plot with ggplot2 in R step by step. We know ggthemes package includes a theme related to Financial Times, but the theme is depreciated now.

My reference graph for this tutorial is given below.

![image](https://github.com/user-attachments/assets/6368f95e-cd64-4670-bba8-8e09ad869f8b)

In order to draw a plot having a similar pattern with above one, I will use only ggplot2 and ggpubr packages. Texts are from windows family. I do not import any extra fonts.

Let’s get started.

I will draw an inflation rate of Turkey. You can access the data from [here.](https://www.tcmb.gov.tr/wps/wcm/connect/TR/TCMB+TR/Main+Menu/Istatistikler/Enflasyon+Verileri/Tuketici+Fiyatlari)

Let’s read data at first.

```{r}
inflation<-readxl::read_xlsx("inflation_rate.xlsx")
head(inflation)
```

```{r}
# A tibble: 6 x 2
  Date                 Rate
  <dttm>              <dbl>
1 2005-01-01 00:00:00  9.24
2 2005-02-01 00:00:00  8.69
3 2005-03-01 00:00:00  7.94
4 2005-04-01 00:00:00  8.18
5 2005-05-01 00:00:00  8.7 
6 2005-06-01 00:00:00  8.95
```

Then, draw a line plot using ```geom_line``` geometric function.

```{r}
library(ggplot2)
ggplot(inflation,aes(x = Date,
                     y = Rate))+
  geom_line()
```

![image](https://github.com/user-attachments/assets/450818b4-6fff-4949-82f6-829100e044ce)

Now, we will start to manipulate the appearance of the plot by adding title and caption.

```{r}
ggplot(inflation,aes(x = Date,
                     y = Rate))+
  geom_line()+
  labs(title = "-
       
The Inflation rate in Turkey is at the peak of the last 17 years !",
       subtitle = "Starting from January 05.",
       caption = "FINANCIAL TIMES")
```

![image](https://github.com/user-attachments/assets/a4ff615e-022a-44f9-a206-801b388118d6)

Then, change the background color, change the color and tickness of the line and remove the vertical grid lines. We will use theme function in ggplot2 and ```col``` and ```size```arguments in ```geom_line``` function.

```{r}
ggplot(inflation,aes(x = Date,
                     y = Rate))+
  geom_line(col = "#f20656", size = 1.2)+
  labs(title = "-
       
The Inflation rate in Turkey is at the peak of the last 17 years !",
       subtitle = "Starting from January 05.",
       caption = "FINANCIAL TIMES")+
 theme(rect = element_rect(fill = "#262a33"),
        panel.background = element_rect(fill = "#262a33"),
        panel.grid.minor.x = element_blank(),
        panel.grid.major.x = element_blank(),
        panel.grid = element_line(color = "#92959e"),
        axis.title = element_blank())
```

![image](https://github.com/user-attachments/assets/336e36a7-707f-48a3-b091-66b66243a0d6)

After that, we will manipulate the texts on the plot. In other words, we will change the color and family of the texts. We will add the necessary arguments in ```theme``` function.

```{r}
ggplot(inflation,aes(x = Date,
                     y = Rate))+
  geom_line(col = "#f20656", size = 1.2)+
  labs(title = "-
       
The Inflation rate in Turkey is at the peak of the last 17 years !",
       subtitle = "Starting from January 05.",
       caption = "FINANCIAL TIMES")+
 theme(rect = element_rect(fill = "#262a33"),
        panel.background = element_rect(fill = "#262a33"),
        panel.grid.minor.x = element_blank(),
        panel.grid.major.x = element_blank(),
        panel.grid = element_line(color = "#92959e"),
        axis.title = element_blank(),
        plot.title = element_text(family ="Tw Cen MT", color = "white",size = 18),
       plot.subtitle = element_text(family ="Tw Cen MT", color = "#92959e"),
        plot.caption = element_text(family = "Times New Roman",face = "bold",color ="#92959e"),
       axis.text = element_text(size = 10, color ="#92959e", family = "Tw Cen MT"))
```

![image](https://github.com/user-attachments/assets/daba907d-19ee-4695-bb09-59b910016496)

Next, we’ll put the y-axis values to the right of the graph. Also, we will paste % sign next to the values by using ```scale_y_continuous``` function.

![image](https://github.com/user-attachments/assets/4eecdc33-f81f-4f91-b6b6-06487cfb95a7)


Lastly, we will add the second caption on the lower left corner of the plot, which may be the hardest part of this process. For this purpose, we will use annotate_custom function. We know that the input of this function is grob object. Thus, we will consider ```ggpubr``` package to produce a grob text object. Then, we will clip off using ```coord_cartesian```.

```{r}
caption2<-ggpubr::text_grob("Source: CBRT", family = "Tw Cen MT",face = "bold", color = "#92959e", size =10)

ggplot(inflation,aes(x = Date,
                     y = Rate))+
  geom_line(col = "#f20656", size = 1.2)+
  labs(title = "-
       
The Inflation rate in Turkey is at the peak of the last 17 years !",
       subtitle = "Starting from January 05.",
       caption = "FINANCIAL TIMES")+
 theme(rect = element_rect(fill = "#262a33"),
        panel.background = element_rect(fill = "#262a33"),
        panel.grid.minor.x = element_blank(),
        panel.grid.major.x = element_blank(),
        panel.grid = element_line(color = "#92959e"),
        axis.title = element_blank(),
        plot.title = element_text(family ="Tw Cen MT", color = "white",size = 18),
       plot.subtitle = element_text(family ="Tw Cen MT", color = "#92959e"),
        plot.caption = element_text(family = "Times New Roman",face = "bold",color ="#92959e"),
       axis.text = element_text(size = 10, color ="#92959e", family = "Tw Cen MT"))+
  scale_y_continuous(labels = function(x) paste0(x, "%"),position = "right")+
  annotation_custom(caption2,xmin=inflation$Date[10],xmax=inflation$Date[10],ymin=-6,ymax=-6)+
  coord_cartesian(clip = "off")
```

That’s it! If you wish to use this theme as a ggplot object, you can contact me via [e-mail](mailto::ozancanozdemir@gmail.com). 
