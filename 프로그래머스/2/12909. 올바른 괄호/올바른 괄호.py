def solution(s):
    #패착 01. 이 if문을 for문밖에서 확인하려고 함
    if not s or s[0] == ')' or s[-1] == '(':
        return False

    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        #패착 02. if i == ')' and cnt >= 1:로 해버리면, 닫괄이 열괄보다 먼저 나오면 처리가 없음
        elif i == ')':
            if cnt >= 1:
                cnt -= 1
            else: #만약, ())같은 놈이 나온 경우:
                return False
                
    if cnt == 0:
        return True
    else:
        return False