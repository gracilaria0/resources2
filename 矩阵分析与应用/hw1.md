作业一
======

#### 1.1
**有线性方程组  
$`\left\{\begin{array}{}
    0.835x &+ 0.667y &= 0.168 \\
    0.333x &+ 0.266y &= 0.067 
\end{array}\right.`$，  
记矩阵$`\boldsymbol{A}$和$\left(\boldsymbol{A}|\boldsymbol{b}\right)`$为此线性方程组的系数矩阵和增广矩阵。分别使用5个和6个有效数字计算矩阵$`\boldsymbol{A}`$和$`\left(\boldsymbol{A}|\boldsymbol{b}\right)`$的秩，并判断方程组是否可解。**

##### ①在6位有效数字下：
显然$`\boldsymbol{A}`$和$`\left(\boldsymbol{A}|\boldsymbol{b}\right)`$的所有$`1`$阶子式全非零，  
$`\det\boldsymbol{A} = \det\left[\boldsymbol{A} | \boldsymbol{b}\right]_3 = 0.835\times 0.266 - 0.333\times 0.667 = 0.222110 - 0.222111 = -0.000001 \neq 0`$，  
所以$`\mathrm{rank}\left(\boldsymbol{A}\right) = 2, \mathrm{rank}\left(\boldsymbol{A}|\boldsymbol{b}\right) = 2`$。 
$`\boldsymbol{A}`$满秩，方程组可解且有唯一解。

##### ②在5位有效数字下：
显然$`\boldsymbol{A}`$和$`\left(\boldsymbol{A}|\boldsymbol{b}\right)`$的所有$`1`$阶子式全非零，  
$`\begin{array}{rl}
    \det\boldsymbol{A} = \det\left[\boldsymbol{A} | \boldsymbol{b}\right]_3 &= 0.835\times 0.266 - 0.333\times 0.667 = 0.22211 - 0.22211 = 0, \\
    \det\left[\boldsymbol{A} | \boldsymbol{b}\right]_2 &= 0.835\times 0.067 - 0.333\times 0.168 = 0.05594 - 0.05594 = 0, \\
    \det\left[\boldsymbol{A} | \boldsymbol{b}\right]_1 &= 0.667\times 0.067 - 0.266\times 0.168 = 0.04469 - 0.04469 = 0,
\end{array}`$  
所以$`\mathrm{rank}\left(\boldsymbol{A}\right) = 1, \mathrm{rank}\left(\boldsymbol{A}|\boldsymbol{b}\right) = 1`$，$`\boldsymbol{A}`$不满秩，方程组无解或有无穷解。  
对$`\boldsymbol{A}`$进行Gauss消元，有  
$`\begin{aligned}
    \boldsymbol{T}_{1,2}\left(-\frac{0.333}{0.835}\right)\left(\boldsymbol{A}|\boldsymbol{b}\right)
    &= \boldsymbol{T}_{1,2}\left(-0.39880\right)\left(\boldsymbol{A}|\boldsymbol{b}\right) \\
    &= \begin{pmatrix}
        0.835 & 0.667 & 0.168 \\
        0.333 - 0.33300 & 0.266 - 0.26600 & 0.067 - 0.066998
    \end{pmatrix} \\
    &= \begin{pmatrix}
        0.835 & 0.667 & 0.168 \\
        0 & 0 & 0.000002
    \end{pmatrix}
\end{aligned}`$
所以方程组无解。



#### 1.2
**$`\boldsymbol{A}`$为$`n\times n`$矩阵，分别计算$`\boldsymbol{A}\boldsymbol{e}_j, \boldsymbol{e}_i^\mathrm{T}\boldsymbol{A}\boldsymbol{e}_j`$，这里$`\boldsymbol{e}_i`$和$`\boldsymbol{e}_j`$分别是单位矩阵$`\boldsymbol{I}`$的第$`i`$列和第$`j`$列。**

$`\begin{aligned}
    \boldsymbol{A}\boldsymbol{e}_j
    &= \begin{pmatrix}
        \boldsymbol{a}_1 & \boldsymbol{a}_2 & \cdots & \boldsymbol{a}_j & \cdots & \boldsymbol{a}_n
    \end{pmatrix}\begin{pmatrix}
        0\\0\\\vdots\\1\\\vdots\\0
    \end{pmatrix} \\
    &= 0\boldsymbol{a}_1 + 0\boldsymbol{a}_2 + \cdots + \boldsymbol{a}_j + \cdots + 0\boldsymbol{a}_n \\
    &= \boldsymbol{a}_j
\end{aligned}`$，  
即$`\boldsymbol{A}`$的第$`j`$列。  

$`\begin{aligned}
    \boldsymbol{e}_i^\mathrm{T}\boldsymbol{A}\boldsymbol{e}_j 
    &= \boldsymbol{e}_i^\mathrm{T}\boldsymbol{a}_j \\
    &= \begin{pmatrix}
        0 & 0 & \cdots & 1 & \cdots & 0
    \end{pmatrix}\begin{pmatrix}
        a_{1,j}\\a_{2,j}\\\vdots\\a_{i,j}\\\vdots\\a_{n,j}
    \end{pmatrix} \\
    &= 0a_{1,j} + 0a_{2,j} + \cdots + a_{i,j} + \cdots + 0a_{n,j} \\
    &= a_{i,j}
\end{aligned}`$，  
即$`\boldsymbol{A}`$第$`i`$行第$`j`$列的元素。  



#### 1.3
**证明：两个上（下）三角矩阵相乘仍为上（下）三角矩阵。**

由于在任意上三角矩阵$`\boldsymbol{U} = \left(u_{i,j}\right)`$中$`u_{i,j} = 0, \forall i>j`$，所以$`u_{i,j} = u_{i,j}\boldsymbol{1}_{\left[i\le j\right]}`$，$`\boldsymbol{U}=\left(u_{i,j}\boldsymbol{1}_{\left[i\le j\right]}\right)`$。  
任意两个上三角矩阵$`\boldsymbol{U} = \left(u_{i,k}\right) \in \mathbb{F}^{m\times n}, \boldsymbol{V} = \left(v_{k,j}\right) \in \mathbb{F}^{n\times p}`$，记$`\boldsymbol{A} = \left(a_{i,j}\right) = \boldsymbol{U}\boldsymbol{V} \in \mathbb{F}^{m\times p}`$，有  
$`\begin{aligned}
    \left|a_{i,j}\right|
    &= \left|\sum_{k=1}^n{u_{i,k}v_{k,j}}\right| \\
    &\le \sum_{k=1}^n{\left|u_{i,k}v_{k,j}\right|} \\
    &= \sum_{k=1}^n{\left|u_{i,k}\boldsymbol{1}_{\left[i\le k\right]}v_{k,j}\boldsymbol{1}_{\left[k\le j\right]}\right|} \\
    &= \sum_{k=1}^n{\left|u_{i,k}v_{k,j}\right|\boldsymbol{1}_{\left[i\le k\right]}\boldsymbol{1}_{\left[k\le j\right]}}
\end{aligned}`$。  
此处  
$`\begin{aligned}
    \boldsymbol{1}_{\left[i\le k\right]}\boldsymbol{1}_{\left[k\le j\right]}
    &= \boldsymbol{1}_{\left[i\le k\right]}\boldsymbol{1}_{\left[k\le j\right]}\boldsymbol{1}_{\left[i\le j\right]} \\
    &\le \boldsymbol{1}_{\left[i\le j\right]}
\end{aligned}`$，  
所以  
$`\begin{aligned}
    \left|a_{i,j}\right|
    &\le \sum_{k=1}^n{\left|u_{i,k}v_{k,j}\right|\boldsymbol{1}_{\left[i\le k\right]}\boldsymbol{1}_{\left[k\le j\right]}} \\
    &\le \sum_{k=1}^n{\left|u_{i,k}v_{k,j}\right|\boldsymbol{1}_{\left[i\le j\right]}} \\
    &= \boldsymbol{1}_{\left[i\le j\right]}\sum_{k=1}^n{\left|u_{i,k}v_{k,j}\right|}
\end{aligned}`$，  
此时$`\forall i>j, \left|a_{i,j}\right| \le \boldsymbol{1}_{\left[i\le j\right]}\sum_{k=1}^n{\left|u_{i,k}v_{k,j}\right|} = 0`$。即$`a_{i,j} = 0, \forall i>j`$，所以$`\boldsymbol{A}`$是上三角矩阵。  
下三角矩阵同理。



#### 1.4
**给出实现矩阵转置的算法。**

算法取决于存储矩阵的数据结构。此处给出算法伪代码。  
##### ①二维数组形式
二维数组形式的矩阵定义如下  

```pseudo
结构1 二维数组形式的矩阵
Structure Matrix2D
    rowCount: 行数
    colCount: 列数
    element[rowCount][colCount]: 矩阵的元素
end Structure
```

在此结构上实现转置算法需要依次变换其中元素  

```pseudo
算法1 二维数组形式矩阵转置
输入：待转置的Matrix2D m
输出：转置后的Matrix2D mT
Procedure transpose2D
    mT ← Matrix(
        rowCount ← m.colCount,
        colCount ← m.rowCount
    )
    For r ← 1 to mT.rowCount do
        For c ← 1 to mT.colCount do
            mT.element[r][c] ← m.element[c][r]
        end For
    end For
end Procedure
```

##### ②三元组列表形式
三元组列表形式的矩阵定义如下  

```pseudo
结构2 三元组列表形式的矩阵
Structure ThreeTuple
    row: 行号
    col: 列号
    val: 此位置的值
end Structure

Structure Matrix3T
    rowCount: 行数
    colCount: 列数
    eleCount: 矩阵中非零元素数量
    tupleLise[eleCount]: 三元组列表
end Structure
```

此结构中一般要求三元组列表按行号、列号的顺序排列。  
在此结构上实现转置算法只需要变换每个元素的行号和列号。但若要求重新将三元组变为有序，则可以设计一种更加快捷的算法：在变换位置前就为元素预留正确的位置。  

```pseudo
算法2 三元组列表形式矩阵转置
输入：待转置的Matrix3T m
输出：转置后的Matrix3T mT
Procedure transpose3T 
    position[m.colCount]
    For e ← 1 to m.eleCount do
        position[m.tupleList[e].col] ← position[m.tupleList[e].col] + 1
    end For
    For r ← 2 to m.colCount-1 do
        position[r] ← position[r] + position[r-1]
    end For
    For r ← 2 to m.colCount do
        position[r] ← position[r-1]
    end For
    position[1] ← 0

    mT ← Matrix(
        rowCount ← m.colCount,
        colCount ← m.rowCount,
        eleCount ← m.eleCount
    )
    For e ← 1 to m.eleCount do
        element ← m.tupleList[e]
        position[element.col] ← position[element.col] + 1
        mT.tupleList[position[element.col]] ← ThreeTuple(
            row ← element.col
            col ← element.row
            val ← element.val
        )
    end For
end Procedure
```

##### ③代码层面操作
无论选择哪种数据结构，若无过于复杂的运算需求，也可以选择不更改存储的矩阵元素数据，仅在代码层面实现“伪”转置操作。可以设计一个函数，在矩阵转置后返回对称位置的元素。以二维数组形式为例。  

```pseudo
算法3 代码层面矩阵转置时访问元素
输入：二维数组形式的矩阵m（包含表示是否被转置的状态变量isTransed）
输入：待访问的元素行号r和列号c
输出：m对应位置的元素e
Procedure getElement2D
    If m.isTransed then
        e ← m.element[c][r]
    Else then
        e ← m.element[r][c]
    end If
end Procedure
```