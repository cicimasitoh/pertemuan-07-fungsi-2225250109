def jumlah_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(jumlah_n(10))
# Uji juga untuk n = 1, 5, 10, dan 100, lalu bandingkan dengan rumus n(n+1)/2[cite: 9]