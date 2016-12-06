#!/usr/bin/env Rscript

gini.vect <- c()

for (i in 0:4) {
    filename <- paste0(i, ".train.gini")
    data <- read.table(filename, header = TRUE, sep = '\t')
    for (j in 1:length(data$COL)) {
        if (data$FIRST_SPLIT[j] >= data$SECOND_SPLIT[j]) {
            gini.vect <- append(gini.vect, data$FIRST_SPLIT[j])
        } else {
            gini.vect <- append(gini.vect, data$SECOND_SPLIT[j])
        }
    }
    png(filename = paste0(i, ".gini.histogram.png"), width = 600, height = 480, units = "px")
    hist(gini.vect)
}
