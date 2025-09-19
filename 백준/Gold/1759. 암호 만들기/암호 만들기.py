import sys
input = lambda : sys.stdin.readline().rstrip()


def make_pswd(start, v_cnt, c_cnt, now_pswd) :
    if len(now_pswd) == L :
        if v_cnt >= 1 and c_cnt >= 2 :
            print(now_pswd)

        return
    for i in range(start, len(default_arr)) :
        if default_arr[i] in 'aeiou' :
            make_pswd(i + 1, v_cnt + 1, c_cnt, now_pswd + default_arr[i])
        else :
            make_pswd(i + 1, v_cnt, c_cnt + 1, now_pswd + default_arr[i])



L, C = map(int, input().split())
default_arr = sorted(list(input().split()))
make_pswd(0, 0, 0, '')
