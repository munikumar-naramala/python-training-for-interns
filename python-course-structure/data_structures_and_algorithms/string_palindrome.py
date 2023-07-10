def is_palindrome(x):
    return x == x[::-1]


def min_partition(string, i, j):
    if i >= j or is_palindrome(string[i:j + 1]):
        return 0
    ans = float('inf')
    for k in range(i, j):
        count = (
                1 + min_partition(string, i, k)
                + min_partition(string, k + 1, j)
        )
        ans = min(ans, count)
    return ans


def main():
    string = "ababbbabbababa"
    print(
        min_partition(string, 0, len(string) - 1),
    )


if __name__ == "__main__":
    main()
