library(tidyverse)
library(gganimate)
library(ggthemes)
library(ggtext)


h <- data_frame(t = seq(0, (2 * pi), by = 0.005), 
             x = 13 * sin(t)^3, 
             y = 13 * cos(t) - 
               5 * cos(2 * t) - 
               2 * cos(3 * t) - 
               1 * cos(4 * t),
             chunk = floor(x)) %>%select(-t) 



g <- ggplot(data = h,aes(x = x))+geom_line(aes(y=y),color = "maroon", size = 1.5)+
  mdthemes::as_md_theme(theme_fivethirtyeight())+theme(rect = element_rect(fill = "White",linetype = 0, colour = NA))+
  labs(title=paste0("<span style = 'color: #800000;'>**Happy Valentines Day**</span>"),caption = paste0("Plot by **Ozancan Ozdemir** | <span style = 'color: #800000;'>**@OzancanOzdemir**</span><br>"))

  
gif_g<-g+transition_reveal(x)
gif_g1=animate(gif_g)
anim_save("valentinesday.gif", animation=gif_g1)

