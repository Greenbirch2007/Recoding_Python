# 1.3 保存最后N个元素


# 我们希望在迭代或其他形式的处理过程中对最后几项记录做一个有限的历史记录统计



# 解决方案
# 保存有限额历史记录算是collections.deque的完美应用场景： 如下代码，对一系列文本行做简单的
#文本匹配操作，当发现有匹配时就输出当前的匹配行以及最后检查过的N行文本


from collections import deque

def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)


# Example use on a file

# if __name__ == '__main__':
#     with open('somefile.txt') as f:
#         for line,prevlines in search(f,'python',5):
#             for pline in prevlines:
#                 print(pline,end="")
#             print(line,end='')
#             print('-'*88)
#

# 讨论

#当编写搜索某项记录的代码时，通常会用到含有yield关键字的生成器函数。这将处理搜索过程
#的代码和使用搜索结果的代码成功解耦开来

#deque(maxlen=N)创建了一个固定长度的队列。当有新记录加入而队列已满时会自动移除最老的那条记录(往前推，先进先出)


# q= deque(maxlen=3)
# q.append(1)
# q.append(3)
# q.append(2)
# print(q)
# print('+'*88)
# q.append(6)
# print(q)
# q.append(8)
# print('+'*88)
# print(q)

#尽管可以在列表上手动完成这样的操作（append,del）,但队列这种解决方案要优雅多，运行速度也快得多

# 更普遍的是，当需要一个简单的队列结构时，deque是很有用的。如果不指定队列的大小，
# 也就得到一个无界限的队列，可以在两端执行添加和弹出操作  如：
# append默认从右侧加入，appendleft从左侧加入
# pop 默认从右侧删除， popleft从左侧删除
q = deque()
q.append(1)
q.append(3)
q.append(2)
print(q)
print('+'*88)
q.appendleft(6)
print(q)
print('+'*88)
q.append(8)
print(q)
print('+'*88)
q.pop()
print(q)
print('+'*88)
q.popleft()
print(q)
print('+'*88)

#从队列两端添加或弹出元素的复杂度都是O(1).这个和列表不同，当从列表的头部插入
#或移除元素时，列表的复杂度为O（N）