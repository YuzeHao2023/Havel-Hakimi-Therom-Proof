# Havel-Hakimi 定理证明与实现

本仓库包含两个互补的部分：

1. 一个 **Lean 4 形式化** 的 Havel–Hakimi 定理（见
   `src/HavelHakimi.lean`）。核心引理表明，对于一个
   非增序列，当且仅当对其执行一次 Havel–Hakimi 规约
   后得到的序列也满足 `hh_graphic`。
   这一结论是经典证明的组合核心。

2. 一个 **Python 实现** 的 Havel–Hakimi 算法，用于判断
   有限非负整数序列是否为简单无向图的度序列。代码
   位于 `havel_hakimi.py`，可直接从命令行运行。


## Lean 4 证明

Lean 形式化是在一个小型 mathlib 项目中进行的。要构建并
检查证明，你需要安装 Lean 工具链；在开发容器中使用
如下 `lake` 命令：

```sh
lake env         # 先在项目根目录下
lake build       # 编译库并检查证明
``` 

主要的定理是引理 `HavelHakimi.havel_hakimi`。


## Python 使用

该算法可以作为脚本调用，或作为模块导入::

```python
>>> from havel_hakimi import is_graphic
>>> is_graphic([3,3,2,2,2,1,1,1,1])
True
>>> is_graphic([4,4,3,1])
False
```

在命令行中：

```sh
$ python havel_hakimi.py 3 3 2 2 2 1 1 1 1
[3, 3, 2, 2, 2, 1, 1, 1, 1] -> True
```

你也可以运行附带的单元测试：

```sh
python -m unittest test_havel_hakimi.py
```

### 哥尼斯堡七桥示例

历史上的哥尼斯堡七桥问题可以用图的度数序列来表述。
四个陆地由七座桥相连，得到的度数序列为 `[5,3,3,3]`。
Havel–Hakimi 算法很快就表明该序列**不可图**——不存在
满足这样的度数的简单图。在原始问题中，这意味着没有
一条遍历每座桥一次的欧拉路径。

你可以运行示例脚本：

```sh
python examples/konigsberg.py
```

它会打印度数序列和测试结果。
