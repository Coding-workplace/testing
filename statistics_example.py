from statistics import (mean, fmean, median, median_low, median_high, median_grouped, mode, multimode, harmonic_mean, geometric_mean, pstdev, pvariance, stdev, variance, covariance, correlation, StatisticsError )

data = [1, 2, 3, 4, 5]
print(mean(data))   # 3
print(fmean(data))  # 3.0

a = [1, 2, 3, 4]
print(median(a))         # 2.5
print(median_low(a))     # 2
print(median_high(a))    # 3
print(median_grouped([1,2,2,3,4]))  # approximate using group interpolation


x = [1,2,2,3,3]
try:
    print(mode(x))
except StatisticsError as e:
    print("mode error:", e)     # ambiguous
print(multimode(x))            # [2, 3]

vals = [2.0, 3.0, 6.0]
print("Harmonic mean:",harmonic_mean(vals))  # 3 / (1/2 + 1/3 + 1/6) = 3.0
print("Geometric mean:", geometric_mean(vals)) # (2*3*6)^(1/3) ≈ 3.3019


data = [2,4,4,4,5,5,7,9]
print("population variance and stdev")
print(pvariance(data), pstdev(data))
print("sample variance and stdev")
print(variance(data), stdev(data))  # sample uses n-1


x = [1,2,3,4,5]
y = [5,4,3,2,1]
print("covariance")
print(covariance(x, y))   # negative covariance
print("correlation")
print(correlation(x, y))  # -1.0 for perfect inverse linear relation



