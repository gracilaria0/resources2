作业二
======

#### 2.1
**已知$`\boldsymbol{A} = \begin{pmatrix}
    2 & 0 & -1 \\
    -1 & 1 & 1 \\
    -1 & 0 & 1
\end{pmatrix}, \boldsymbol{A}^{-1} = \begin{pmatrix}
    1 & 0 & 1 \\
    0 & 1 & -1 \\
    1 & 0 & 2
\end{pmatrix}`$，试求矩阵$`\boldsymbol{B}, \boldsymbol{C}`$的逆矩阵。其中$`\boldsymbol{B} = \begin{pmatrix}
    2 & 0 & -1 \\
    -1 & 1 & 1 \\
    -1 & 2 & 1
\end{pmatrix}, \boldsymbol{C} = \begin{pmatrix}
    2 & 0 & -1 \\
    -1 & 1 & 1 \\
    -1 & 2 & 2
\end{pmatrix}`$。**

$`\boldsymbol{B} = \boldsymbol{A} + \begin{pmatrix}
    0 & 0 & 0 \\
    0 & 0 & 0 \\
    0 & 2 & 0
\end{pmatrix} = \boldsymbol{A} + 2\boldsymbol{e}_3\boldsymbol{e}_2^\mathrm{T}`$，
所以
$`\begin{aligned}
\boldsymbol{B}^{-1} &= \boldsymbol{A}^{-1} - 2\frac{\boldsymbol{A}^{-1}\boldsymbol{e}_3\boldsymbol{e}_2^\mathrm{T}\boldsymbol{A}^{-1}}{1 + 2\boldsymbol{e}_2^\mathrm{T}\boldsymbol{A}^{-1}\boldsymbol{e}_3} \\
&= \boldsymbol{A}^{-1} - 2\frac{\begin{pmatrix}
    1 \\ -1 \\ 2 
\end{pmatrix}\begin{pmatrix}
    0 & 1 & -1
\end{pmatrix}}{1 + 2\times \left(-1\right)} \\
&= \begin{pmatrix}
    1 & 0 & 1 \\
    0 & 1 & -1 \\
    1 & 0 & 2
\end{pmatrix} + 2\begin{pmatrix}
    0 & 1 & -1 \\
    0 & -1 & 1 \\
    0 & 2 & -2
\end{pmatrix} \\
&= \begin{pmatrix}
    1 & 2 & -1 \\
    0 & -1 & 1 \\
    1 & 4 & -2
\end{pmatrix}
\end{aligned}`$。

$`\boldsymbol{C} = \boldsymbol{B} + \begin{pmatrix}
    0 & 0 & 0 \\
    0 & 0 & 0 \\
    0 & 0 & 1
\end{pmatrix} = \boldsymbol{B} + \boldsymbol{e}_3\boldsymbol{e}_3^\mathrm{T}`$，
所以
$`\begin{aligned}
\boldsymbol{C}^{-1} &= \boldsymbol{B}^{-1} - \frac{\boldsymbol{B}^{-1}\boldsymbol{e}_3\boldsymbol{e}_3^\mathrm{T}\boldsymbol{B}^{-1}}{1 + \boldsymbol{e}_3^\mathrm{T}\boldsymbol{B}^{-1}\boldsymbol{e}_3} \\
&= \boldsymbol{B}^{-1} - \frac{\begin{pmatrix}
    -1 \\ 1 \\ -2 
\end{pmatrix}\begin{pmatrix}
    1 & 4 & -2
\end{pmatrix}}{1 + \left(-2\right)} \\
&= \begin{pmatrix}
    1 & 2 & -1 \\
    0 & -1 & 1 \\
    1 & 4 & -2
\end{pmatrix} + \begin{pmatrix}
    -1 & -4 & 2 \\
    1 & 4 & -2 \\
    -2 & -8 & 4
\end{pmatrix} \\
&= \begin{pmatrix}
    0 & -2 & 1 \\
    1 & 3 & -1 \\
    -1 & -4 & 2
\end{pmatrix}.
\end{aligned}`$



#### 2.2
**对于矩阵$`\boldsymbol{A} = \begin{pmatrix}
    1 & 4 & 5 \\
    4 & 18 & 26 \\
    3 & 16 & 30
\end{pmatrix}`$，**

##### (1) 求出它的LU分解形式；
$`\begin{aligned}
    \boldsymbol{A} &= \begin{pmatrix}
        1 & 4 & 5 \\
        4 & 18 & 26 \\
        3 & 16 & 30
    \end{pmatrix} \\
    \begin{pmatrix}
        1 & 0 & 0 \\
        -4 & 1 & 0 \\
        -3 & 0 & 1
    \end{pmatrix}\boldsymbol{A} &= \begin{pmatrix}
        1 & 4 & 5 \\
        0 & 2 & 6 \\
        0 & 4 & 15
    \end{pmatrix} \\
    \begin{pmatrix}
        1 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & -2 & 1
    \end{pmatrix}\begin{pmatrix}
        1 & 0 & 0 \\
        -4 & 1 & 0 \\
        -3 & 0 & 1
    \end{pmatrix}\boldsymbol{A} &= \begin{pmatrix}
        1 & 4 & 5 \\
        0 & 2 & 6 \\
        0 & 0 & 3
    \end{pmatrix},
\end{aligned}`$
右侧满足上三角，所以
$`\begin{aligned}
    \boldsymbol{L} &= \begin{pmatrix}
        1 & 0 & 0 \\
        -4 & 1 & 0 \\
        -3 & 0 & 1
    \end{pmatrix}^{-1}\begin{pmatrix}
        1 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & -2 & 1
    \end{pmatrix}^{-1} \\
    &= \begin{pmatrix}
        1 & 0 & 0 \\
        4 & 1 & 0 \\
        3 & 0 & 1
    \end{pmatrix}\begin{pmatrix}
        1 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & 2 & 1
    \end{pmatrix} \\
    &= \begin{pmatrix}
        1 & 0 & 0 \\
        4 & 1 & 0 \\
        3 & 2 & 1
    \end{pmatrix}.
\end{aligned}`$
$`\left\{\begin{aligned}
    \boldsymbol{U} &= \begin{pmatrix}
        1 & 4 & 5 \\
        0 & 2 & 6 \\
        0 & 0 & 3
    \end{pmatrix}, \\
    \boldsymbol{L} &= \begin{pmatrix}
        1 & 0 & 0 \\
        4 & 1 & 0 \\
        3 & 2 & 1
    \end{pmatrix}.
\end{aligned}\right.`$

##### (2) 由LU分解求出$`\boldsymbol{A}^{-1}`$。
$`\boldsymbol{L}^{-1} = \begin{pmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & -2 & 1
\end{pmatrix}\begin{pmatrix}
    1 & 0 & 0 \\
    -4 & 1 & 0 \\
    -3 & 0 & 1
\end{pmatrix};`$
设$`\boldsymbol{U}\boldsymbol{X} = \boldsymbol{I}`$，
有  
$`\left\{\begin{aligned}
    x_{i,j} &= 0,\forall i>j \\
    x_{1,1} &= u_{1,1}^{-1} = 1 \\
    x_{2,2} &= u_{2,2}^{-1} = \frac{1}{2} \\
    x_{3,3} &= u_{3,3}^{-1} = \frac{1}{3} \\
    0 &= 2x_{2,3} + 6x_{3,3} \\
    0 &= 1x_{1,3} + 4x_{2,3} + 5x_{3,3} \\
    0 &= 1x_{1,2} + 4x_{2,2} + 5x_{3,2}
\end{aligned}\right.`$
解得$`\boldsymbol{U}^{-1} = \boldsymbol{X} = \begin{pmatrix}
    1 & -2 & \frac{7}{3} \\
    0 & \frac{1}{2} & -1 \\
    0 & 0 & \frac{1}{3}
\end{pmatrix}.`$
所以
$`\begin{aligned}
    \boldsymbol{A}^{-1} &= \boldsymbol{U}^{-1}\boldsymbol{L}^{-1} \\
    &= \begin{pmatrix}
        1 & -2 & \frac{7}{3} \\
        0 & \frac{1}{2} & -1 \\
        0 & 0 & \frac{1}{3}
    \end{pmatrix}\begin{pmatrix}
        1 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & -2 & 1
    \end{pmatrix}\begin{pmatrix}
        1 & 0 & 0 \\
        -4 & 1 & 0 \\
        -3 & 0 & 1
    \end{pmatrix} \\
    &= \begin{pmatrix}
        1 & -\frac{20}{3} & \frac{7}{3} \\
        0 & \frac{5}{2} & -1 \\
        0 & -\frac{2}{3} & \frac{1}{3}
    \end{pmatrix}\begin{pmatrix}
        1 & 0 & 0 \\
        -4 & 1 & 0 \\
        -3 & 0 & 1
    \end{pmatrix} \\
    &= \begin{pmatrix}
        1-7 + \frac{80}{3} & -\frac{20}{3} & \frac{7}{3} \\
        3 - 10 & \frac{5}{2} & -1 \\
        -1 + \frac{8}{3} & -\frac{2}{3} & \frac{1}{3}
    \end{pmatrix} \\
    &= \begin{pmatrix}
        \frac{62}{3} & -\frac{20}{3} & \frac{7}{3} \\
        -7 & \frac{5}{2} & -1 \\
        \frac{5}{3} & -\frac{2}{3} & \frac{1}{3}
    \end{pmatrix} = \frac{1}{6}\begin{pmatrix}
        124 & -40 & 14 \\
        -42 & 15 & -6 \\
        10 & -4 & 2
    \end{pmatrix}
\end{aligned}`$



#### 2.3
**矩阵$`\boldsymbol{A}`$和向量$`\boldsymbol{b}`$定义如下：
$`\boldsymbol{A} = \begin{pmatrix}
    1 & 2 & 4 & 17 \\
    3 & 6 & -12 & 3 \\
    2 & 3 & -3 & 2 \\
    0 & 2 & -2 & 6
\end{pmatrix}, \boldsymbol{b} = \begin{pmatrix}
    17 \\ 3 \\ 3 \\ 4
\end{pmatrix}`$，
使用部分主元法实现分解$`\boldsymbol{P}\boldsymbol{A} = \boldsymbol{L}\boldsymbol{U}`$，并求解方程组$`\boldsymbol{A}\boldsymbol{x} = \boldsymbol{b}`$。**

记序列$`\boldsymbol{p} = \begin{pmatrix}
    1 \\ 2 \\ 3 \\ 4
\end{pmatrix}`$，有
$`\begin{aligned}
    \left[\boldsymbol{A}|\boldsymbol{p}\right] &: \left[\begin{array}{cccc|c}
        1 & 2 & 4 & 17 & 1 \\
        3 & 6 & -12 & 3 & 2 \\
        2 & 3 & -3 & 2 & 3 \\
        0 & 2 & -2 & 6 & 4
    \end{array}\right] \\
    &\rightarrow\left[\begin{array}{cccc|c}
        3 & 6 & -12 & 3 & 2 \\
        1 & 2 & 4 & 17 & 1 \\
        2 & 3 & -3 & 2 & 3 \\
        0 & 2 & -2 & 6 & 4
    \end{array}\right] \\
    &\rightarrow\left[\begin{array}{cccc|c}
        3 & 6 & -12 & 3 & 2 \\
        \bold{\frac{1}{3}} & 0 & 8 & 16 & 1 \\
        \bold{\frac{2}{3}} & -1 & 5 & 0 & 3 \\
        \bold{0} & 2 & -2 & 6 & 4
    \end{array}\right] \\
    &\rightarrow\left[\begin{array}{cccc|c}
        3 & 6 & -12 & 3 & 2 \\
        \bold{0} & 2 & -2 & 6 & 4 \\
        \bold{\frac{1}{3}} & 0 & 8 & 16 & 1 \\
        \bold{\frac{2}{3}} & -1 & 5 & 0 & 3
    \end{array}\right] \\
    &\rightarrow\left[\begin{array}{cccc|c}
        3 & 6 & -12 & 3 & 2 \\
        \bold{0} & 2 & -2 & 6 & 4 \\
        \bold{\frac{1}{3}} & \bold{0} & 8 & 16 & 1 \\
        \bold{\frac{2}{3}} & \bold{-\frac{1}{2}} & 4 & 3 & 3
    \end{array}\right] \\
    &\rightarrow\left[\begin{array}{cccc|c}
        3 & 6 & -12 & 3 & 2 \\
        \bold{0} & 2 & -2 & 6 & 4 \\
        \bold{\frac{1}{3}} & \bold{0} & 8 & 16 & 1 \\
        \bold{\frac{2}{3}} & \bold{-\frac{1}{2}} & \bold{\frac{1}{2}} & -5 & 3
    \end{array}\right],
\end{aligned}`$
所以
$`\left\{\begin{aligned}
    \boldsymbol{L} &= \begin{pmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        \frac{1}{3} & 0 & 1 & 0 \\
        \frac{2}{3} & -\frac{1}{2} & \frac{1}{2} & 1
    \end{pmatrix}, \\
    \boldsymbol{U} &= \begin{pmatrix}
        3 & 6 & -12 & 3 \\
        0 & 2 & -2 & 6 \\
        0 & 0 & 8 & 16 \\
        0 & 0 & 0 & -5 
    \end{pmatrix}, \\
    \boldsymbol{P} &= \begin{pmatrix}
        0 & 1 & 0 & 0 \\
        0 & 0 & 0 & 1 \\
        1 & 0 & 0 & 0 \\
        0 & 0 & 1 & 0 
    \end{pmatrix}.
\end{aligned}\right.`$

得到$`\boldsymbol{P}\boldsymbol{A}\boldsymbol{x} = \boldsymbol{L}\boldsymbol{U}\boldsymbol{x} = \boldsymbol{P}\boldsymbol{b}`$，记$`\boldsymbol{U}\boldsymbol{x} = \boldsymbol{y}`$，有$`\boldsymbol{L}\boldsymbol{y} = \boldsymbol{P}\boldsymbol{b} = \begin{pmatrix}
    3 \\ 4 \\ 17 \\ 3
\end{pmatrix}`$。  
用两次回代，可以得到$`\boldsymbol{y} = \begin{pmatrix}
    3 \\ 4 \\ 16 \\ -5
\end{pmatrix}, \boldsymbol{x} = \begin{pmatrix}
    2 \\ -1 \\ 0 \\ 1
\end{pmatrix}`$。



#### 2.4
**当$`\xi`$取什么值的时候，矩阵$`\boldsymbol{A} = \begin{pmatrix}
    \xi & 2 & 0 \\
    1 & \xi & 1 \\
    0 & 1 & \xi
\end{pmatrix}`$不存在LU分解？**

$`\boldsymbol{A}`$的三个主子式
$`\begin{aligned}
    \boldsymbol{D}_1 &= \xi, \\
    \boldsymbol{D}_2 &= \xi^2 - 2, \\
    \boldsymbol{D}_3 &= \xi\left(\xi^2-1\right) - 2\xi = \xi\left(\xi^2 - 3\right).
\end{aligned}`$
所以当$`\xi \in \left\{0, \pm\sqrt{2}, \pm\sqrt{3}\right\}`$时，$`\boldsymbol{A}`$不存在LU分解。