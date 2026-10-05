N = 4

# Upper half
for i in range(1, N + 1):
    print("*" * (2 * i - 1))

# Lower half
for i in range(N, 0, -1):
    print("*" * (2 * i - 1))
