def draw_stars(arr):
    star = "*"
    for number in range(len(arr)):
        if type(arr[number]) == str:
            print arr[number][0]*len(arr[number])
        else:
            print star*arr[number]

draw_stars([1,"elephant",5,"cat",3])