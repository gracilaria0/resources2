作业四
======

#### 4.1
**设$`\boldsymbol{A}, \boldsymbol{X} \in \mathbb{R}^{n\times n}`$，试说明下面哪些是线性变换。**

##### (1) $`\mathcal{T}\left(\boldsymbol{X}\right) = \boldsymbol{AX} - \boldsymbol{XA}`$；
$`\begin{aligned}
    \mathcal{T}\left(\alpha\boldsymbol{X}_1 + \beta\boldsymbol{X}_2\right) &= \alpha\boldsymbol{A}\boldsymbol{X}_1 + \beta\boldsymbol{A}\boldsymbol{X}_2 - \alpha\boldsymbol{X}_1\boldsymbol{A} - \beta\boldsymbol{X}_2\boldsymbol{A} \\
    &= \alpha\mathcal{T}\left(\boldsymbol{X}_1\right) + \beta\mathcal{T}\left(\boldsymbol{X}_2\right)
\end{aligned}`$  
是线性变换。

##### (2) $`\mathcal{T}\left(\boldsymbol{A}\right) = \boldsymbol{A}^\mathrm{T}`$；
$`\begin{aligned}
    \mathcal{T}\left(\alpha\boldsymbol{A}_1 + \beta\boldsymbol{A}_2\right) &= \left(\alpha\boldsymbol{A}_1 + \beta\boldsymbol{A}_2\right)^\mathrm{T} \\
    &= \left(\alpha\boldsymbol{A}_1\right)^\mathrm{T} + \left(\beta\boldsymbol{A}_2\right)^\mathrm{T} \\
    &= \alpha\mathcal{T}\left(\boldsymbol{A}_1\right) + \beta\mathcal{T}\left(\boldsymbol{A}_2\right)
\end{aligned}`$  
是线性变换。

##### (3) $`\mathcal{T}\left(\boldsymbol{X}\right) = \frac{\boldsymbol{X} + \boldsymbol{X}^\mathrm{T}}{2}`$；
若$`\mathcal{T}_1\left(\boldsymbol{X}\right),\mathcal{T}_2\left(\boldsymbol{X}\right)`$都是线性变换，$`\mathcal{T}\left(\boldsymbol{X}\right) = \lambda\mathcal{T}_1\left(\boldsymbol{X}\right) + \mu\mathcal{T}_2\left(\boldsymbol{X}\right)`$满足    
$`\begin{aligned}
    \mathcal{T}\left(\alpha\boldsymbol{X}_1 + \beta\boldsymbol{X}_2\right) &= \lambda\mathcal{T}_1\left(\alpha\boldsymbol{X}_1 + \beta\boldsymbol{X}_2\right) + \mu\mathcal{T}_2\left(\alpha\boldsymbol{X}_1 + \beta\boldsymbol{X}_2\right) \\
     &= \lambda\left(\alpha\mathcal{T}_1\left(\boldsymbol{X}_1\right) + \beta\mathcal{T}_1\left(\boldsymbol{X}_2\right)\right) + \mu\left(\alpha\mathcal{T}_2\left(\boldsymbol{X}_1\right) + \beta\mathcal{T}_2\left(\boldsymbol{X}_2\right)\right) \\
     &= \alpha\left(\lambda\mathcal{T}_1\left(\boldsymbol{X}_1\right) + \mu\mathcal{T}_2\left(\boldsymbol{X}_1\right)\right) + \beta\left(\lambda\mathcal{T}_1\left(\boldsymbol{X}_2\right) + \mu\mathcal{T}_2\left(\boldsymbol{X}_2\right)\right) \\
     &= \alpha\mathcal{T}\left(\boldsymbol{X}_1\right) + \beta\mathcal{T}\left(\boldsymbol{X}_2\right)
\end{aligned}`$  
是线性变换，即两线性变换的线性组合仍然是线性变换。  
此处$`\mathcal{T}_1\left(\boldsymbol{X}\right) = \boldsymbol{X},\mathcal{T}_2\left(\boldsymbol{X}\right) = \boldsymbol{X}^\mathrm{T}`$均为线性变换，所以$`T\left(\boldsymbol{X}\right) = \frac{1}{2}T_1\left(\boldsymbol{X}\right) + \frac{1}{2}T_2\left(\boldsymbol{X}\right)`$也是线性变换。

##### (4) $`\mathcal{T}\left(\boldsymbol{x}\right) = \boldsymbol{Ax} + \boldsymbol{b}, \boldsymbol{x},\boldsymbol{b} \in \mathbb{R}^{n\times 1}, \boldsymbol{b}\ne \boldsymbol{0}`$。
$`\begin{aligned}
    \mathcal{T}\left(\alpha\boldsymbol{x}_1 + \beta\boldsymbol{x}_2\right) &= \boldsymbol{A}\left(\alpha\boldsymbol{x}_1 + \beta\boldsymbol{x}_2\right) + \boldsymbol{b} \\
     &= \alpha\boldsymbol{A}\boldsymbol{x}_1 + \boldsymbol{b} + \beta\boldsymbol{A}\boldsymbol{x}_2 + \boldsymbol{b} - \boldsymbol{b} \\
     &= \alpha\mathcal{T}\left(\boldsymbol{x}_1\right) + \beta\mathcal{T}\left(\boldsymbol{x}_2\right) - \boldsymbol{b}
\end{aligned}`$  
$`\boldsymbol{b} \ne 0`$，$`T`$不是线性变换。



#### 4.2
**设$`\boldsymbol{A} \in \mathbb{R}^{n\times n}`$，$`T`$是$`\mathbb{R}^{n\times 1}`$的一个线性算子，定义为$`\mathcal{T}\left(\boldsymbol{x}\right) = \boldsymbol{Ax}`$。记$`S`$为标准基，试说明$`\left[\mathcal{T}\right]_S = \boldsymbol{A}`$。**

对任意一个向量$`\boldsymbol{v} = \left(v_1, v_2, \cdots, v_n\right)`$，因为$`\boldsymbol{v} = v_1\boldsymbol{e}_1 + v_2\boldsymbol{e}_2 + \cdots + v_n\boldsymbol{e}_n`$，所以其在标准正交基下的坐标$`\left[\boldsymbol{v}\right]_S = \boldsymbol{v}`$。
$`\begin{aligned}
    \left[\mathcal{T}\right]_S &= \begin{pmatrix}
        \left[\mathcal{T}\boldsymbol{e}_1\right]_S & \left[\mathcal{T}\boldsymbol{e}_2\right]_S & \cdots & \left[\mathcal{T}\boldsymbol{e}_n\right]_S
    \end{pmatrix} \\
    &= \begin{pmatrix}
        \left[\boldsymbol{A}\boldsymbol{e}_1\right]_S & \left[\boldsymbol{A}\boldsymbol{e}_2\right]_S & \cdots & \left[\boldsymbol{A}\boldsymbol{e}_n\right]_S
    \end{pmatrix} \\
    &= \begin{pmatrix}
        \boldsymbol{A}\boldsymbol{e}_1 & \boldsymbol{A}\boldsymbol{e}_2 & \cdots & \boldsymbol{A}\boldsymbol{e}_n
    \end{pmatrix}
\end{aligned}`$  
其中$`\boldsymbol{A}\boldsymbol{e}_i`$是$`\boldsymbol{A}`$的第$`i`$列，上式即$`\boldsymbol{A}`$的各列按顺序排列在一起，最终仍然会组成$`\boldsymbol{A}`$。



#### 4.3
**对于向量空间$`\mathbb{R}^3`$，  
$`\begin{aligned}
    B &= \left\{\boldsymbol{u}_1 = \begin{pmatrix}
        1 \\ 0 \\ 0
    \end{pmatrix}, \boldsymbol{u}_2 = \begin{pmatrix}
        1 \\ 1 \\ 0
    \end{pmatrix}, \boldsymbol{u}_3 = \begin{pmatrix}
        1 \\ 1 \\ 1
    \end{pmatrix}\right\}, \\
    B' &= \left\{\boldsymbol{v}_1 = \begin{pmatrix}
        -1 \\ 0 \\ 0
    \end{pmatrix}, \boldsymbol{v}_2 = \begin{pmatrix}
        0 \\ 1 \\ 0
    \end{pmatrix}, \boldsymbol{v}_3 = \begin{pmatrix}
        0 \\ 1 \\ -1
    \end{pmatrix}\right\}
\end{aligned}`$  
为该空间的两组基。**

##### (1) 对于恒等算子$`\boldsymbol{I}`$，分别计算$`\left[\boldsymbol{I}\right]_B, \left[\boldsymbol{I}\right]_{B'}, \left[\boldsymbol{I}\right]_{BB'}`$；
$`\begin{aligned}
    \left[\boldsymbol{I}\right]_B &= \begin{pmatrix}
        \left[\boldsymbol{I}\boldsymbol{u}_1\right]_B & \left[\boldsymbol{I}\boldsymbol{u}_2\right]_B & \left[\boldsymbol{I}\boldsymbol{u}_3\right]_B
    \end{pmatrix} \\
    &= \begin{pmatrix}
        \left[\boldsymbol{u}_1\right]_B & \left[\boldsymbol{u}_2\right]_B & \left[\boldsymbol{u}_3\right]_B
    \end{pmatrix} \\
    &= \begin{pmatrix}
        1 & 0 & 0 \\
        0 & 1 & 0 \\
        0 & 0 & 1
    \end{pmatrix}.
\end{aligned}`$  
同理$`\left[\boldsymbol{I}\right]_{B'} = \begin{pmatrix}
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1
\end{pmatrix}`$。  
$`\begin{aligned}
    \left[\boldsymbol{I}\right]_{BB'} &= \begin{pmatrix}
        \left[\boldsymbol{I}\boldsymbol{u}_1\right]_{B'} & \left[\boldsymbol{I}\boldsymbol{u}_2\right]_{B'} & \left[\boldsymbol{I}\boldsymbol{u}_3\right]_{B'}
    \end{pmatrix} \\
    &= \begin{pmatrix}
        \left[\boldsymbol{u}_1\right]_{B'} & \left[\boldsymbol{u}_2\right]_{B'} & \left[\boldsymbol{u}_3\right]_{B'}
    \end{pmatrix},
\end{aligned}`$  
因为  
$`\begin{aligned}
    \boldsymbol{e}_1 &= -\boldsymbol{v}_1, \\
    \boldsymbol{e}_2 &= \boldsymbol{v}_2, \\
    \boldsymbol{e}_3 &= \boldsymbol{v}_2 - \boldsymbol{v}_3,
\end{aligned}`$  
所以  
$`\begin{aligned}
    \boldsymbol{u}_1 &= \boldsymbol{e}_1 &&= -\boldsymbol{v}_1, \\
    \boldsymbol{u}_2 &= \boldsymbol{e}_1 + \boldsymbol{e}_2 &&= -\boldsymbol{v}_1 + \boldsymbol{v}_2, \\
    \boldsymbol{u}_3 &= \boldsymbol{u}_2 + \boldsymbol{e}_3 &&= -\boldsymbol{v}_1 + 2\boldsymbol{v}_2 - \boldsymbol{v}_3,
\end{aligned}`$  
所以$`\left[\boldsymbol{I}\right]_{BB'} = \begin{pmatrix}
    -1 & -1 & -1 \\
    0 & 1 & 2 \\
    0 & 0 & -1
\end{pmatrix}`$。


##### (2) 对于投影算子$`\boldsymbol{P}, \boldsymbol{P}\begin{pmatrix}x \\ y \\ z\end{pmatrix} = \begin{pmatrix}x \\ y \\ 0\end{pmatrix}`$，计算$`\left[\boldsymbol{P}\right]_{BB'}`$。
$`\begin{aligned}
    \left[\boldsymbol{P}\right]_{BB'} &= \begin{pmatrix}
        \left[\boldsymbol{P}\boldsymbol{u}_1\right]_{B'} & \left[\boldsymbol{P}\boldsymbol{u}_2\right]_{B'} & \left[\boldsymbol{P}\boldsymbol{u}_3\right]_{B'}
    \end{pmatrix} \\
    &= \begin{pmatrix}
        \left[\boldsymbol{u}_1\right]_{B'} & \left[\boldsymbol{u}_2\right]_{B'} & \left[\boldsymbol{u}_2\right]_{B'}
    \end{pmatrix} \\
    &= \begin{pmatrix}
        -1 & -1 & -1 \\
        0 & 1 & 1 \\
        0 & 0 & 0
\end{pmatrix}.
\end{aligned}`$  




#### 4.4
**设$`\boldsymbol{T}`$为$`\mathbb{R}^3`$的一个线性算子，其定义为$`\boldsymbol{T}\left(x,y,z\right) = \left(x-y, y-x, x-z\right)`$，$`B = \left\{\boldsymbol{u}_1 = \begin{pmatrix}
    1 \\ 0 \\ 1
\end{pmatrix}, \boldsymbol{u}_2 = \begin{pmatrix}
    0 \\ 1 \\ 1
\end{pmatrix}, \boldsymbol{u}_3 = \begin{pmatrix}
    1 \\ 1 \\ 0
\end{pmatrix}\right\}`$为$`\mathbb{R}^3`$的一组基，$`\boldsymbol{v} = \begin{pmatrix}
    1 \\ 1 \\ 2
\end{pmatrix}`$为$`\mathbb{R}^3`$上的一个向量。**

##### (1) 分别计算$`\left[\boldsymbol{T}\right]_B`$和$`\left[\boldsymbol{v}\right]_B`$；
$`\begin{aligned}
    \boldsymbol{e}_1 &= &\frac{1}{2}\boldsymbol{u}_1 &&- \frac{1}{2}\boldsymbol{u}_2 &&+ \frac{1}{2}\boldsymbol{u}_3, \\
    \boldsymbol{e}_2 &= &-\frac{1}{2}\boldsymbol{u}_1 &&+ \frac{1}{2}\boldsymbol{u}_2 &&+ \frac{1}{2}\boldsymbol{u}_3, \\
    \boldsymbol{e}_3 &= &\frac{1}{2}\boldsymbol{u}_1 &&+ \frac{1}{2}\boldsymbol{u}_2 &&- \frac{1}{2}\boldsymbol{u}_3,
\end{aligned}`$  
$`\begin{aligned}
    \left[\boldsymbol{T}\right]_B &= \begin{pmatrix}
        \left[\boldsymbol{T}\boldsymbol{u}_1\right]_B & \left[\boldsymbol{T}\boldsymbol{u}_2\right]_B & \left[\boldsymbol{T}\boldsymbol{u}_3\right]_B
    \end{pmatrix} \\
    &= \begin{pmatrix}
        \left[\begin{pmatrix}1 \\ -1 \\ 0\end{pmatrix}\right]_B & \left[\begin{pmatrix}-1 \\ 1 \\ -1\end{pmatrix}\right]_B & \left[\begin{pmatrix}0 \\ 0 \\ 1\end{pmatrix}\right]_B 
    \end{pmatrix} \\
    &= \begin{pmatrix}
        \left[\boldsymbol{e}_1-\boldsymbol{e}_2\right]_B & \left[-\boldsymbol{e}_1+\boldsymbol{e}_2-\boldsymbol{e}_3\right]_B & \left[\boldsymbol{e}_3\right]_B
    \end{pmatrix} \\
    &= \begin{pmatrix}
        1 & -\frac{3}{2} & \frac{1}{2} \\
        -1 & \frac{1}{2} & \frac{1}{2} \\
        0 & \frac{1}{2} & -\frac{1}{2}
    \end{pmatrix},
\end{aligned}`$  
$`\begin{aligned}
    \left[\boldsymbol{v}\right]_B &= \left[\boldsymbol{e}_1 + \boldsymbol{e}_2 + 2\boldsymbol{e}_3\right]_B \\
    &= \left(1, 1, 0\right).
\end{aligned}`$

##### (2) 计算$`\left[\boldsymbol{T}\left(\boldsymbol{v}\right)\right]_B`$并验证$`\left[\boldsymbol{T}\left(\boldsymbol{v}\right)\right]_B = \left[\boldsymbol{T}\right]_B \left[\boldsymbol{v}\right]_B`$成立。
$`\begin{aligned}
    \left[\boldsymbol{Tv}\right]_B &= \left[\left(0, 0, -1\right)\right]_B \\
    &= \left[-\boldsymbol{e}_3\right]_B \\
    &= \left(-\frac{1}{2}, -\frac{1}{2}, \frac{1}{2}\right),
\end{aligned}`$  
满足$`\left[\boldsymbol{T}\right]_B \left[\boldsymbol{v}\right]_B = \left(-\frac{1}{2}, -\frac{1}{2}, \frac{1}{2}\right) = \left[\boldsymbol{Tv}\right]_B`$。




#### 4.5
**$`\boldsymbol{A}\left(x,y,z\right) = \left(x+2y-z, -y, x+7z\right)`$是$`\mathbb{R}^3`$的一个线性算子，记
$`B = \left\{\begin{pmatrix}
    1 \\ 0 \\ 0
\end{pmatrix}, \begin{pmatrix}
    0 \\ 1 \\ 0
\end{pmatrix}, \begin{pmatrix}
    0 \\ 0 \\ 1
\end{pmatrix}\right\},
B' = \left\{\begin{pmatrix}
    1 \\ 0 \\ 0
\end{pmatrix}, \begin{pmatrix}
    1 \\ 1 \\ 0
\end{pmatrix}, \begin{pmatrix}
    1 \\ 1 \\ 1
\end{pmatrix}\right\}`$。**

##### (1) 计算$`\left[\boldsymbol{A}\right]_B`$和$`\left[\boldsymbol{A}\right]_{B'}`$；
$`B`$是$`\mathbb{R}^3`$上的标准正交基，其中的基向量分别为$`\boldsymbol{e}_1, \boldsymbol{e}_2, \boldsymbol{e}_3`$，$`\left[\boldsymbol{A}\right]_B = \begin{pmatrix}
    1 & 2 & -1 \\
    0 & -1 & 0 \\
    1 & 0 & 7
\end{pmatrix}`$。  
记$`B'`$中的基向量分别为$`\boldsymbol{u}_1, \boldsymbol{u}_2, \boldsymbol{u}_3`$，有  
$`\begin{aligned}
    \boldsymbol{e}_1 &= &\boldsymbol{u}_1, \\
    \boldsymbol{e}_2 &= &-\boldsymbol{u}_1 &&+ \boldsymbol{u}_2, \\
    \boldsymbol{e}_3 &= && &-\boldsymbol{u}_2 &&+ \boldsymbol{u}_3,
\end{aligned}`$  
$`\begin{aligned}
    \left[\boldsymbol{A}\right]_{B'} &= \begin{pmatrix}
        \left[\boldsymbol{A}\boldsymbol{u}_1\right]_{B'} & \left[\boldsymbol{A}\boldsymbol{u}_2\right]_{B'} & \left[\boldsymbol{A}\boldsymbol{u}_3\right]_{B'}
    \end{pmatrix} \\
    &= \begin{pmatrix}
        \left[\begin{pmatrix}1 \\ 0 \\ 1\end{pmatrix}\right]_{B'} & \left[\begin{pmatrix}3 \\ -1 \\ 1\end{pmatrix}\right]_{B'} & \left[\begin{pmatrix}2 \\ -1 \\ 8\end{pmatrix}\right]_{B'} 
    \end{pmatrix} \\
    &= \begin{pmatrix}
        \left[\boldsymbol{e}_1+\boldsymbol{e}_3\right]_{B'} & \left[3\boldsymbol{e}_1-\boldsymbol{e}_2+\boldsymbol{e}_3\right]_{B'} & \left[2\boldsymbol{e}_1-\boldsymbol{e}_2+8\boldsymbol{e}_3\right]_{B'}
    \end{pmatrix} \\
    &= \begin{pmatrix}
        1 & 4 & 3 \\
        -1 & -2 & -9 \\
        1 & 1 & 8
    \end{pmatrix}.
\end{aligned}`$

##### (2) 求矩阵$`\boldsymbol{Q}`$使得$`\left[\boldsymbol{A}\right]_{B'} = \boldsymbol{Q}^{-1}\left[\boldsymbol{A}\right]_B\boldsymbol{Q}`$成立。
坐标变换矩阵  
$`\begin{aligned}
    \boldsymbol{P} &= \begin{pmatrix}
        \left[\boldsymbol{e}_1\right]_{B'} & \left[\boldsymbol{e}_2\right]_{B'} & \left[\boldsymbol{e}_3\right]_{B'}
    \end{pmatrix} \\
    &= \begin{pmatrix}
        1 & -1 & 0 \\
        0 & 1 & -1 \\
        0 & 0 & 1 \\
    \end{pmatrix}
\end{aligned}`$  
满足$`\left[\boldsymbol{A}\right]_B = \boldsymbol{P}^{-1}\left[\boldsymbol{A}\right]_{B'}\boldsymbol{P}`$，  
$`\begin{aligned}
    \boldsymbol{Q} &= \boldsymbol{P}^{-1} \\
    &= \left(\begin{pmatrix}
        1 & 0 & 0 \\
        0 & 1 & -1 \\
        0 & 0 & 1
    \end{pmatrix} \begin{pmatrix}
        1 & -1 & 0 \\
        0 & 1 & 0 \\
        0 & 0 & 1
    \end{pmatrix}\right)^{-1} \\
    &= \begin{pmatrix}
        1 & 1 & 0 \\
        0 & 1 & 0 \\
        0 & 0 & 1
    \end{pmatrix} \begin{pmatrix}
        1 & 0 & 0 \\
        0 & 1 & 1 \\
        0 & 0 & 1
    \end{pmatrix} \\
    &= \begin{pmatrix}
        1 & 1 & 1 \\
        0 & 1 & 1 \\
        0 & 0 & 1
    \end{pmatrix}.
\end{aligned}`$




#### 4.6
**设$`\boldsymbol{T}`$为$`\mathbb{R}^4`$的一个线性算子，其定义为$`\boldsymbol{T}\left(x_1, x_2, x_3, x_4\right) = \left(x_1+x_2+2x_3-x_4, x_2+x_4, 2x_3-x_4, x_3+x_4\right)`$。令$`\mathcal{X} = \mathrm{span}\left\{\boldsymbol{e}_1, \boldsymbol{e}_2\right\}`$，试说明$`\mathcal{X}`$为$`\boldsymbol{T}`$的一个不变子空间，并计算$`\left[\boldsymbol{T}|_\mathcal{X}\right]_{\left\{\boldsymbol{e}_1, \boldsymbol{e}_2\right\}}`$。**

对任意$`\boldsymbol{x}=\left(x_1, x_2, 0, 0\right) \in \mathcal{X}`$，有$`\boldsymbol{T}\left(\boldsymbol{x}\right) = \left(x_1+x_2, x_2, 0, 0\right)\in\mathcal{X}`$，所以$`\mathcal{X}\subseteq\mathbb{R}^4`$是$`\boldsymbol{T}`$的一个不变子空间。  

$`\left\{\boldsymbol{e}_1, \boldsymbol{e}_2\right\}`$是$`\mathbb{R}^2`$上的一组标准正交基，记为$`S`$，
$`\begin{aligned}
    \left[\boldsymbol{T}|_\mathcal{X}\right]_S &= \begin{pmatrix}
        \left[\boldsymbol{T}|_\mathcal{X}\left(\boldsymbol{e}_1\right)\right]_S & \left[\boldsymbol{T}|_\mathcal{X}\left(\boldsymbol{e}_2\right)\right]_S
    \end{pmatrix} \\
    &= \begin{pmatrix}
        \left[\boldsymbol{e}_1\right]_S & \left[\boldsymbol{e}_1 + \boldsymbol{e}_2\right]_S
    \end{pmatrix} \\
    &= \begin{pmatrix}
        1 & 1 \\
        0 & 1
    \end{pmatrix}.
\end{aligned}`$




#### 4.7
**$`B=\left\{\begin{pmatrix}
    1 & 0 \\ 0 & 0
\end{pmatrix}, \begin{pmatrix}
    0 & 1 \\ 0 & 0
\end{pmatrix}, \begin{pmatrix}
    0 & 0 \\ 1 & 0
\end{pmatrix}, \begin{pmatrix}
    0 & 0 \\ 0 & 1
\end{pmatrix}\right\}`$是$`\mathbb{R}^{2\times 2}`$的一组基，对于该空间中任意矩阵$`\boldsymbol{A}`$，线性算子$`\boldsymbol{T}`$定义如下：$`\boldsymbol{T}\left(\boldsymbol{A}\right) = \frac{\boldsymbol{A}+\boldsymbol{A}^\mathrm{T}}{2}`$，计算$`\left[\boldsymbol{T}\right]_B`$。**

$`\begin{aligned}
    \left[\boldsymbol{T}\right]_B &= \begin{pmatrix}
        \left[\boldsymbol{T}\begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix}\right]_B & \left[\boldsymbol{T}\begin{pmatrix}0 & 1 \\ 0 & 0\end{pmatrix}\right]_B & \left[\boldsymbol{T}\begin{pmatrix}0 & 0 \\ 1 & 0\end{pmatrix}\right]_B & \left[\boldsymbol{T}\begin{pmatrix}0 & 0 \\ 0 & 1\end{pmatrix}\right]_B
    \end{pmatrix} \\
    &= \begin{pmatrix}
        \left[\begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix}\right]_B & \left[\begin{pmatrix}0 & \frac{1}{2} \\ \frac{1}{2} & 0\end{pmatrix}\right]_B & \left[\begin{pmatrix}0 & \frac{1}{2} \\ \frac{1}{2} & 0\end{pmatrix}\right]_B & \left[\begin{pmatrix}0 & 0 \\ 0 & 1\end{pmatrix}\right]_B
    \end{pmatrix} \\
    &= \begin{pmatrix}
        1 & 0 & 0 & 0 \\
        0 & \frac{1}{2} & \frac{1}{2} & 0 \\
        0 & \frac{1}{2} & \frac{1}{2} & 0 \\
        0 & 0 & 0 & 1
    \end{pmatrix}.
\end{aligned}`$