import math

def main():
    n = int(input())
    A = list(map(float, input().split()))
    B = list(map(float, input().split()))

    dx = 0.0001
    N = int((2 * math.pi) / dx) + 1

    Y = [0.0] * N
    X = [i * dx for i in range(N)]

    for i in range(N):
        x = X[i]
        y = sum(math.sin(A[j] * x + B[j]) for j in range(n))
        Y[i] = y

    peaks = []
    peak_indices = []

    for i in range(1, N - 1):
        if Y[i] > Y[i - 1] and Y[i] > Y[i + 1]:
            peaks.append(X[i])
            peak_indices.append(i)

    if Y[0] > Y[1]:
        peaks.insert(0, X[0])
        peak_indices.insert(0, 0)
    if Y[N - 1] > Y[N - 2]:
        peaks.append(X[N - 1])
        peak_indices.append(N - 1)

    num_valleys = len(peaks) - 1
    if num_valleys <= 0:
        print(1)
        return

    max_width = 0.0
    valley_index = 1

    for i in range(num_valleys):
        width = peaks[i + 1] - peaks[i]
        if width > max_width:
            max_width = width
            valley_index = i + 1

    print(valley_index,end="")

if __name__ == "__main__":
    main()