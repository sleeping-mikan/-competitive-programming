list_ = [["b","b","b","b","b","b","b","b","b","b","b","b","b","b","b"],
        ["b","w","w","w","w","w","w","w","w","w","w","w","w","w","b"],
        ["b","w","b","b","b","b","b","b","b","b","b","b","b","w","b"],
        ["b","w","b","w","w","w","w","w","w","w","w","w","b","w","b"],
        ["b","w","b","w","b","b","b","b","b","b","b","w","b","w","b"],
        ["b","w","b","w","b","w","w","w","w","w","b","w","b","w","b"],
        ["b","w","b","w","b","w","b","b","b","w","b","w","b","w","b"],
        ["b","w","b","w","b","w","b","w","b","w","b","w","b","w","b"],
        ["b","w","b","w","b","w","b","b","b","w","b","w","b","w","b"],
        ["b","w","b","w","b","w","w","w","w","w","b","w","b","w","b"],
        ["b","w","b","w","b","b","b","b","b","b","b","w","b","w","b"],
        ["b","w","b","w","w","w","w","w","w","w","w","w","b","w","b"],
        ["b","w","b","b","b","b","b","b","b","b","b","b","b","w","b"],
        ["b","w","w","w","w","w","w","w","w","w","w","w","w","w","b"],
        ["b","b","b","b","b","b","b","b","b","b","b","b","b","b","b"],]

R , C = map(int,input().split())


if list_[R - 1][C - 1] == "w":
    print("white")
else:
    print("black")