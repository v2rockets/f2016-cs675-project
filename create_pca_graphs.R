#!/usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)

in.file <- args[1]
print(in.file)
data <- read.table(in.file, sep = " ")

x.control <- data$V2[data$V1 == 0]
y.control <- data$V3[data$V1 == 0]

x.exp <- data$V2[data$V1 == 1]
y.exp <- data$V3[data$V1 == 1]

x.range <- c(min(data$V2), max(data$V2))
y.range <- c(min(data$V3), max(data$V3))

print(x.exp)
print(x.range)
print(y.range)

#plot.window(xlim = x.range, ylim = y.range)
cwd <- getwd()
print(cwd)
out.file <- paste0(cwd, "/", in.file, ".graph.png")
print(out.file)

png(filename = out.file)

plot(x.control, y.control, type = "p", col = "red",
        xlim = x.range, ylim = y.range,
        main = paste0(in.file, " PC"), xlab = "1st PC", ylab = "2nd PC")
points(x.exp, y.exp, type = "p", col = "green")
