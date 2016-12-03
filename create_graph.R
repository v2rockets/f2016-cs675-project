std.deviations <- read.table("std_dev.info", header = FALSE, sep = " ")

std.deviations.vect <- std.deviations$V2
names(std.deviations.vect) <- std.deviations$V1

mean.sd <- mean(std.deviations.vect)
var.sd <- var(std.deviations.vect)
sd.sd <- sd(std.deviations.vect)

print("Mean:")
print(mean.sd)
print("Variance:")
print(var.sd)
print("Standard deviation:")
print(sd.sd)

png("std_dev_hist.png")
hist(std.deviations.vect, breaks = 24)
