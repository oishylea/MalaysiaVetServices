library(tidyverse)

set.seed(123)
num_students <- 100
grades <- sample(c("A", "B", "C", "D", "F"), num_students, replace = TRUE, prob = c(0.2, 0.3, 0.3, 0.1, 0.1))

student_data <- data.frame(Grade = grades)

ggplot(student_data, aes(x = Grade)) +
  geom_bar() +
  scale_x_discrete(limits = c("A", "B", "C", "D", "F")) +
  labs(
    title = "Frequency of Student Grades",
    x = "Grade",
    y = "Count"
  ) +
  theme_minimal()

