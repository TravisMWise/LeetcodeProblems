from binary import Solution

def main():
    s = Solution()
    res = s.addBinary("11", "1")
    print(res)
    res = s.addBinary("11", "11")
    print(res)

if __name__ == '__main__':
    main()