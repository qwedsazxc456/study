def solution(n, times):
    f,l=0,min(times)*n
    while f != l:
        s=0
        m=(l+f)//2
        for i in times:
            s += m//i
        if s < n :
            f = m+1
        else:
            l = m
    answer = l
    return answer