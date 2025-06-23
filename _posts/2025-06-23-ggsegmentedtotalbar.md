---
title: "Segmented Total Bar Chart in R with ```ggsegmentedtotalbar```"
tags: [r]
categories: [r]
author_profile: true   # true yaparsan kenar bar’da profil çıkar
layout: single          # Academic Pages varsayılanı
read_time: true
---

Kevin Flerlage, who is a data visualization specialist, suggested a great alternative to stacked bar plot on his blog. He called this new alternative “segmented total bar plot”. This R package ggsegmentedtotalbar implements this idea. The package is built on top of the ggplot2 package, which is a popular data visualisation package in R. The ggsegmentedtotalbar function creates a segmented total bar plot with custom annotations (boxes) added for each group. The height of each box is determined by the Total value associated with each group.

The core thing behind usage of ggsegmentedtotalbar is to create a data frame with the following columns:

group: A string representing the name of the grouping variable.
segment: A string representing the name of the segmenting variable.
value: A string representing the name of the value variable (used for the height of bars).
total: A string representing the name of the total variable (used for determining the box height for each group).
The good thing is that your data frame does not have to have the same column names. However, you need to specify the names of the columns in the data frame when calling the ggsegmentedtotalbar function correctly.

The function ggsegmentedtotalbar takes a data frame and the names of the columns as arguments. It creates a bar plot based on grouped data with annotations (boxes) added for each group. The height of each box is determined by the Total value associated with each group.

```
# Example data frame
df_ex <- data.frame(
  group = c("A", "A","A","B", "B","B","C","C","C","D","D","D"),
  segment = c("X","Y","Z", "X","Y","Z", "X","Y","Z","X","Y","Z"),
  value = c(10, 20, 30, 40,50,60, 70,80,90, 100, 110, 120),
  total = c(60,60,60, 150,150,150, 240,240,240, 360,360,360)
)
# Create the segmented total bar plot
p <- ggsegmentedtotalbar(df_ex, "group", "segment", "value", "total")
# Print the plot
print(p)
```

![image](https://github.com/user-attachments/assets/0e9c08c6-b404-4e39-9883-c3a82b283f58)


The function also provides three parameters that you can use to customize the plot:

alpha: A numeric value (between 0 and 1) controlling the transparency of the background boxes. Default is 0.3.
color: A string specifying the color of the background boxes. Default is “lightgrey”.
label: Logical. If TRUE, adds labels showing total values above the boxes and value labels on each segment. Default is FALSE.

```
# Create the segmented total bar plot with labels
p <- ggsegmentedtotalbar(df_ex, "group", "segment", "value", "total",
                         label = TRUE, label_size = 4, label_color = "black")
# Print the plot
print(p)
```

![image](https://github.com/user-attachments/assets/50b2b4bb-2d1c-438b-aaba-bdb16133fccb)

```
# Create the segmented total bar plot with labels and different total box. 
p <- ggsegmentedtotalbar(df_ex, "group", "segment", "value", "total",
                         label = TRUE, label_size = 4, label_color = "black",
                         alpha = 0.2, color = "steelblue")
# Print the plot
print(p)
```

![image](https://github.com/user-attachments/assets/c97ff6cc-ff64-4032-a247-2a40cf58b6b3)


Apart from these parameters, you can also customize your plot by utilizing ggplot2 related functions. Here is another example.

![image](https://github.com/user-attachments/assets/4dbc7064-4662-4a4b-9778-24ddbeb6ac5e)

