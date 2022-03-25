""" title：数据结构
 author：Archie"""



def BF (s , t):
    """BF 算法"""
    i = 0
    j = 0
    k = 0
    flag1 = -1
    while (i < len(s) and j < len(t)):
        # 匹配成功
        if (i - k == j) and (j == len(t) - 1) and (s[i] == t[j]):
            flag1 = k
            break
        # s和t相等就继续向后匹配
        if s[i] == t[j]:
            i = i + 1
            j = j + 1
        # 不相等从k的位置开始匹配
        else:
            k = k + 1
            i = k
            j = 0
            # 假如s中所剩字符小于t中所剩字符
            if (len(s) - i) < len(t):
                flag1 = -1
                break
    return flag1

    s = input('输入目标串s：')
    t = input('输入模式串t：')
    flag = BF(s, t)
    if flag != -1:
        print('t在s的位置：', flag)
    else:
        print(flag, '匹配失败')


class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self._head
        count = 0
        # 尾节点指向None，当未到达尾部时
        while cur is not None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print()
