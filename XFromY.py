def min_string_factor(X, Y, S, R):
    n = len(X)
    m = len(Y)
    Y_rev = Y[::-1]

    # Initialize dp array
    INF = float('inf')
    dp = [INF] * (n + 1)
    dp[0] = 0  # No cost to form an empty string

    # Iterate through each character of X
    for i in range(1, n + 1):
        # Check substrings from Y
        for j in range(m):
            for k in range(j + 1, m + 1):  # Generate all substrings Y[j:k]
                if Y[j:k] == X[i - (k - j):i]:  # Match
                    dp[i] = min(dp[i], dp[i - (k - j)] + S)

        # Check substrings from reversed Y
        for j in range(m):
            for k in range(j + 1, m + 1):  # Generate all substrings Y_rev[j:k]
                if Y_rev[j:k] == X[i - (k - j):i]:  # Match
                    dp[i] = min(dp[i], dp[i - (k - j)] + R)

    result = dp[n]
    if result == INF:
        return "Impossible"
    else:
        return result

# Read inputs
X = input().strip()
Y = input().strip()
S, R = map(int, input().strip().split())

# Get the result and print without a newline at the end
print(min_string_factor(X, Y, S, R), end="")
