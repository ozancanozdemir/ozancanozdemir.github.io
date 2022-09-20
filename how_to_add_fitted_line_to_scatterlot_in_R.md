How to Add a Fitted Line to a Scatter Plot in R?
================
Ozancan Ozdemir

In this tutorial, I will illustrate how to add a fitted line to a
scatter plot in R Programming language. The tutorial has two parts.

-   **Adding a fitted line to an R base scatter plot**

-   **Adding a fitted line to ggplot2 scatter plot**

Before starting the application part, I’ll briefly explain the concept
of the scatter plot and the fitted line, respectively.

A Scatter plot can help you identify the relationship between two
variables. It is a plot of one variable against another variable.

Among these two variables, one is the explanatory variable (independent
variable), and the other is the response variable. (dependent variable,
target variable). The decision of the explanatory and response variables
requires attention to have a scatter plot representing the true
relationship.

The most effective usage of the scatter plot is for investigating the
relationship between two numerical variables.

As stated above, the scatter plot is used to understand the relationship
between two variables. If these two variables are related (or
correlated), then we can also represent their relationship by a line on
the plot. A fitted line provides us to obtain the estimated regression
function between the explanatory variable and target variable.

After this brief introduction, let’s get started! We will use a very
famous dataset in this tutorial,`mtcars`.

``` r
head(mtcars)
```

    ##                    mpg cyl disp  hp drat    wt  qsec vs am gear carb
    ## Mazda RX4         21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
    ## Mazda RX4 Wag     21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
    ## Datsun 710        22.8   4  108  93 3.85 2.320 18.61  1  1    4    1
    ## Hornet 4 Drive    21.4   6  258 110 3.08 3.215 19.44  1  0    3    1
    ## Hornet Sportabout 18.7   8  360 175 3.15 3.440 17.02  0  0    3    2
    ## Valiant           18.1   6  225 105 2.76 3.460 20.22  1  0    3    1

## Adding a fitted line to an R base scatter plot

We will discover the underlying relationship between horsepower(hp) and
miles per gallon (mpg). To draw a scatter plot in base R, we use
plot()function. Here is how we are supposed to use it.

`plot(exploratory variable,response variable)`

``` r
plot(mtcars$hp,mtcars$mpg)
```

![](gt_files/figure-gfm/unnamed-chunk-2-1.png)<!-- -->

Now, we will manipulate the axis names and the title of the plot to have
a better view.

``` r
plot(mtcars$hp,mtcars$mpg,
     xlab  = "Horsepower",
     ylab = "Miles per Gallon",
     main = "The relationship between horsepower and miles per gallon")
```

![](gt_files/figure-gfm/unnamed-chunk-3-1.png)<!-- -->

As seen from the figure above, the two variables are related to each
other. When the horsepower increases, mpg decreases. Now, we can
represent this relationship by adding a fitted line to this scatter
plot. To do so, we will use abline() and lm() functions together.

`abline()` is used to add one or more lines to the current plot and lm()
is used to fit a linear model.

``` r
plot(mtcars$hp,mtcars$mpg,
     xlab  = "Horsepower",
     ylab = "Miles per Gallon",
     main = "The relationship between horsepower and miles per gallon")
abline(lm(mpg~hp,data = mtcars))
```

![](gt_files/figure-gfm/unnamed-chunk-4-1.png)<!-- -->

We can change the color and thickness of the line by using col and lwd
arguments, respectively.

``` r
plot(mtcars$hp,mtcars$mpg,
     xlab  = "Horsepower",
     ylab = "Miles per Gallon",
     main = "The relationship between horsepower and miles per gallon")
abline(lm(mpg~hp,data = mtcars),
       col = "red",
       lwd = 2)
```

![](gt_files/figure-gfm/unnamed-chunk-5-1.png)<!-- -->

In the example above, we add a straight fitted line to the scatter plot.
It is also possible to add a smoothed fitted line using lowess function.
We also use lines function instead of abline command.

``` r
plot(mtcars$hp,mtcars$mpg,
     xlab  = "Horsepower",
     ylab = "Miles per Gallon",
     main = "The relationship between horsepower and miles per gallon")
lines(lowess(x = mtcars$hp, y = mtcars$mpg),
       col = "red",
       lwd = 2)
```

![](gt_files/figure-gfm/unnamed-chunk-6-1.png)<!-- -->

The line representing the negative relationship between two variables of
interest is not straight due to the random variation.

So far, we have shown how to add a fitted line to a base scatter plot.
Now, let’s follow the same steps for ggplot2 scatter plot.

## Adding a fitted line to ggplot2 scatter plot

You have to install the ggplot2 package if you are interested in
creating a ggplot2 object. Then, load the package.

``` r
#install.packages(ggplot2) # install the ggplot2 package
library(ggplot2) #load the package
```

    ## Warning: package 'ggplot2' was built under R version 4.1.2

According to the ggplot2 idea, a plot can be split into 3 parts.

-   **plot = data + aesthetics + geometry**

-   **data** refers to a dataset you are working on.

-   **aesthetics** indicates x and y variable.

-   **geometry** indicates the type of the graphics. (scatter plot, bar
    chart, histogram, box plot, line plot, density plot etc.)

The geometry function for scatter plot in ggplot2 is geom_point().

``` r
ggplot(mtcars,aes(x = hp, y = mpg))+
  geom_point()
```

![](gt_files/figure-gfm/unnamed-chunk-8-1.png)<!-- -->

Now, we can change the axis names and add title to the plot.

``` r
ggplot(mtcars,aes(x = hp, y = mpg))+
  geom_point()+
  labs(x  = "Horsepower",
     y = "Miles per Gallon",
     title = "The relationship between horsepower and miles per gallon")
```

![](gt_files/figure-gfm/unnamed-chunk-9-1.png)<!-- -->

We can add the straight fitted line to the plot first. The geometric
function used for adding a fitted line is geom_smooth. Since we draw a
regression function line, we also use method = lm argument in the
function.

``` r
ggplot(mtcars,aes(x = hp, y = mpg))+
  geom_point()+
  labs(x  = "Horsepower",
     y = "Miles per Gallon",
     title = "The relationship between horsepower and miles per gallon")+
  geom_smooth(method = "lm")
```

    ## `geom_smooth()` using formula 'y ~ x'

![](gt_files/figure-gfm/unnamed-chunk-10-1.png)<!-- -->

The line on the figure above has a grey band. It is a confidence
interval, but we don’t want to have it. To remove it, we also use
se=FALSE argument.

``` r
ggplot(mtcars,aes(x = hp, y = mpg))+
  geom_point()+
  labs(x  = "Horsepower",
     y = "Miles per Gallon",
     title = "The relationship between horsepower and miles per gallon")+
  geom_smooth(method = "lm", se = FALSE)
```

    ## `geom_smooth()` using formula 'y ~ x'

![](gt_files/figure-gfm/unnamed-chunk-11-1.png)<!-- -->

We can change the color and thickness of the line by using col and size
arguments, respectively.

``` r
ggplot(mtcars,aes(x = hp, y = mpg))+
  geom_point()+
  labs(x  = "Horsepower",
     y = "Miles per Gallon",
     title = "The relationship between horsepower and miles per gallon")+
  geom_smooth(method = "lm", 
              se = FALSE,
              col = "red",
              size =2)
```

    ## `geom_smooth()` using formula 'y ~ x'

![](gt_files/figure-gfm/unnamed-chunk-12-1.png)<!-- -->

If we are interested in adding a smoothed fitted line rather than a
straight line, we just remove the method=lm argument from geom_smooth()
function.

``` r
ggplot(mtcars,aes(x = hp, y = mpg))+
  geom_point()+
  labs(x  = "Horsepower",
     y = "Miles per Gallon",
     title = "The relationship between horsepower and miles per gallon")+
  geom_smooth(se = FALSE,
              col = "red",
              size =2)
```

    ## `geom_smooth()` using method = 'loess' and formula 'y ~ x'

![](gt_files/figure-gfm/unnamed-chunk-13-1.png)<!-- -->

In summary, I illustrate how to add a fitted line to a scatter plot
(both base R and ggplot2 graph). For any questions and comments, you can
contact me via [e-mail.](mailto::ozancanozdemir@gmail.com)

[Back to main page.](https://ozancanozdemir.github.io/year-archive/)
