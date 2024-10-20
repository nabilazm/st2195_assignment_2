

install.packages("rvest")

setwd('C:/Repository/Assignment 2')

library(rvest)

html <- read_html("https://en.wikipedia.org/wiki/Comma-separated_values#Example")

car_table <-  html %>% html_node('#mw-content-text > div.mw-content-ltr.mw-parser-output > table.wikitable') %>% html_table()

write.csv(car_table, "car_table.csv", row.names = FALSE)
