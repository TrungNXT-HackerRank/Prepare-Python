# import sys
output = []

if __name__ == '__main__':
    N = int(input())
    command_list = {
    "insert": lambda x: output.insert(x[0], x[1]),
    "print": lambda x: print(output),
    "remove": lambda x: output.remove(x[0]),
    "append": lambda x: output.append(x[0]),
    "sort": lambda x: output.sort(),
    "pop": lambda x: output.pop(),
    "reverse": lambda x: output.reverse()
    }
    for _ in range(N):
        string, *el = input().split()
        command_list[string](list(map(int, el)))







