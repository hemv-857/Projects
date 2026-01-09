set.seed(52)

n <- 500
p_true <- 0.6
outcomes <- rbinom(n, 1, p_true)

# Forecaster behaviors
honest <- rep(p_true, n)
overconfident <- rep(0.9, n)
hedged <- rep(0.5, n)

brier <- function(y, p) {
  mean((p - y)^2)
}

log_score <- function(y, p) {
  p <- pmin(pmax(p, 1e-12), 1 - 1e-12)
  -mean(y * log(p) + (1 - y) * log(1 - p))
}

accuracy <- function(y, p) {
  mean((p >= 0.5) == y)
}

results <- data.frame(
  Model = c("Honest", "Overconfident", "Hedged"),
  Brier = c(
    brier(outcomes, honest),
    brier(outcomes, overconfident),
    brier(outcomes, hedged)
  ),
  LogScore = c(
    log_score(outcomes, honest),
    log_score(outcomes, overconfident),
    log_score(outcomes, hedged)
  ),
  Accuracy = c(
    accuracy(outcomes, honest),
    accuracy(outcomes, overconfident),
    accuracy(outcomes, hedged)
  )
)

print(results)