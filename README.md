## What is it?

元胞自动机（Cellular Automata） 是 20 世纪50 年代初由计算机之父冯·诺依曼（J.von Neumann） 为了模拟生命系统所具有的自复制功能而提出来的。此后，史蒂芬·沃尔夫勒姆（Stephen Wolfram） 对元胞自动机理论进行了深入的研究，例如，他对一维初等元胞机全部256 种规则所产生的模型进行了深入研究，并将元胞自动机分为平稳型、周期型、混沌型和复杂型4 种类型。元胞自动机采用离散的空间布局和离散的时间间隔，将元胞分成有限种状态，元胞个体状态的演变仅与其当前状态以及其某个局部邻域的状态有关。

## How to run?

- Need `Python3` and `pip3`
  - `pip install pygame` 
  - `python3 ./cellular_automata.py`

## Features

- 重构：使用更少的代码实现
- 每个单元的下一个状态，取决于相邻8个单元的状态
- 每 tick 只绘制变化了的单元
- 容器上下互联、左右互联
- Class 储存状态
- 空格暂停/恢复程序运行

## Rule

- 当前细胞为存活状态时，当周围的存活细胞低于2个时（不包含2个），该细胞变成死亡状态。（模拟生命数量稀少）
- 当前细胞为存活状态时，当周围有2个或3个存活细胞时，该细胞保持原样。
- 当前细胞为存活状态时，当周围有超过3个存活细胞时，该细胞变成死亡状态。（模拟生命数量过多）
- 当前细胞为死亡状态时，当周围有3个存活细胞时，该细胞变成存活状态。（模拟繁殖）

## How it works?

利用 pygame 库，将程序屏幕划分为 x * x 元胞自动机格大小，每格维护自己的状态，每 tick 按照原胞自动机的原理更新所有格的状态，并渲染出不同的颜色。

## How is the effect?

![](./元胞自动机.gif)