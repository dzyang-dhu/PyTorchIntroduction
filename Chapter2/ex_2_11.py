""" 为了能够现实下列代码的执行效果，请在安装PyTorch之后，在Python交互命令行界面，
    即在系统命令行下输入python这个命令回车后，在>>>提示符后执行下列代码
    （#号及其后面内容为注释，可以忽略）
"""

import torch

t1 = torch.rand(3, 4) # 产生一个3×4的张量
t1 # 打印张量的值
t1.sqrt() # 张量的平方根，张量内部方法
torch.sqrt(t1) # 张量的平方根，函数形式
t1 # 前两个操作不改变张量的值
t1.sqrt_() # 平方根原地操作
t1 # 原地操作，改变张量的值
torch.sum(t1) # 默认对所有的元素求和
torch.sum(t1, 0) # 对第0维的元素求和
torch.sum(t1, [0,1]) # 对第0、1维的元素求和
t1.mean() # 对所有元素求平均，也可以用torch.mean函数
t1.mean(0) # 对第0维的元素求平均
torch.mean(t1, [0,1]) # 对第0、1维元素求平均