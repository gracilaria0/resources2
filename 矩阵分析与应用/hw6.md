作业六
======

#### 6.1
**试判断矩阵$`\begin{pmatrix}
    \frac{1+\mathrm{i}}{\sqrt{3}} & \frac{1+\mathrm{i}}{\sqrt{6}} \\
    \frac{\mathrm{i}}{\sqrt{3}} & \frac{-2\mathrm{i}}{\sqrt{6}}
\end{pmatrix}`$是否为酉矩阵。**

$`\begin{aligned}
    \begin{pmatrix}
        \frac{1+\mathrm{i}}{\sqrt{3}} & \frac{1+\mathrm{i}}{\sqrt{6}} \\
        \frac{\mathrm{i}}{\sqrt{3}} & \frac{-2\mathrm{i}}{\sqrt{6}}
    \end{pmatrix} \begin{pmatrix}
        \frac{1+\mathrm{i}}{\sqrt{3}} & \frac{1+\mathrm{i}}{\sqrt{6}} \\
        \frac{\mathrm{i}}{\sqrt{3}} & \frac{-2\mathrm{i}}{\sqrt{6}}
    \end{pmatrix}^* &= \begin{pmatrix}
        \frac{1+\mathrm{i}}{\sqrt{3}} & \frac{1+\mathrm{i}}{\sqrt{6}} \\
        \frac{\mathrm{i}}{\sqrt{3}} & \frac{-2\mathrm{i}}{\sqrt{6}}
    \end{pmatrix} \begin{pmatrix}
        \frac{1-\mathrm{i}}{\sqrt{3}} & \frac{-\mathrm{i}}{\sqrt{3}} \\
        \frac{1-\mathrm{i}}{\sqrt{6}} & \frac{2\mathrm{i}}{\sqrt{6}}
    \end{pmatrix} \\
    &= \begin{pmatrix}
        \frac{2}{3}+\frac{2}{6} & \frac{1-\mathrm{i}}{3}+\frac{-2+2\mathrm{i}}{6} \\
        \frac{1+\mathrm{i}}{3}+\frac{-2-2\mathrm{i}}{6} & \frac{1}{3}+\frac{4}{6}
    \end{pmatrix} \\
    &= \begin{pmatrix}
        1 & 0 \\
        0 & 1
    \end{pmatrix} \\
    &= \boldsymbol{I},
\end{aligned}`$  
所以该矩阵是酉矩阵。



#### 6.2
**从向量$`\boldsymbol{x} = \begin{pmatrix}
    \frac{1}{3} \\ -\frac{2}{3} \\ -\frac{2}{3}
\end{pmatrix}`$出发使用初等反射矩阵构造$`\mathbb{R}^3`$的一组标准正交基。**

取  
$`\begin{aligned}
    \boldsymbol{u} &= \boldsymbol{x} - \left\Vert\boldsymbol{x}\right\Vert_2\boldsymbol{e}_1 \\
    &= \boldsymbol{x} - \boldsymbol{e}_1\\
    &= -\frac{2}{3}\begin{pmatrix}
        1 \\ 1 \\ 1
    \end{pmatrix}
\end{aligned}`$，  
初等反射矩阵  
$`\begin{aligned}
    \boldsymbol{R} &= \boldsymbol{I} - 2\frac{\boldsymbol{uu}^\mathrm{T}}{\boldsymbol{u}^\mathrm{T}\boldsymbol{u}} \\
    &= \boldsymbol{I} - \frac{3}{2}\frac{4}{9}\begin{pmatrix}
        1 & 1 & 1 \\
        1 & 1 & 1 \\
        1 & 1 & 1
    \end{pmatrix} \\
    &= \frac{1}{3}\begin{pmatrix}
        1 & -2 & -2 \\
        -2 & 1 & -2 \\
        -2 & -2 & 1
    \end{pmatrix}
\end{aligned}`$  
中的各列是$`\mathbb{R}^3`$的一组标准正交基。


#### 6.3
**设$`\boldsymbol{R} = \boldsymbol{I} - 2\boldsymbol{uu}^\mathrm{T}`$，其中$`\boldsymbol{u}\in\mathbb{R}^n, n\ge 1, \left\Vert\boldsymbol{u}\right\Vert = 1`$。证明若$`\boldsymbol{x}`$满足$`\boldsymbol{Rx} = \boldsymbol{x}`$，则$`\boldsymbol{u}\perp\boldsymbol{x}`$。**

$`\begin{aligned}
    \boldsymbol{Rx} &= \boldsymbol{x} \\
    \left(\boldsymbol{I} - 2\boldsymbol{uu}^\mathrm{T}\right)\boldsymbol{x} &= \boldsymbol{x} \\
    \boldsymbol{x} - 2\boldsymbol{uu}^\mathrm{T}\boldsymbol{x} &= \boldsymbol{x} \\
    \boldsymbol{uu}^\mathrm{T}\boldsymbol{x} &= \boldsymbol{0}
\end{aligned}`$  
因为$`\left\Vert\boldsymbol{u}\right\Vert \ne 0`$，所以$`\boldsymbol{u}^\mathrm{T}\boldsymbol{x} = 0`$，即$`\boldsymbol{u}\perp\boldsymbol{x}`$。



#### 6.4
**对于矩阵$`\boldsymbol{A} = \begin{pmatrix}
    0 & -20 & -14 \\
    3 & 27 & -4 \\
    4 & 11 & -2
\end{pmatrix}`$，使用Givens约化方法找到一个正交矩阵$`\boldsymbol{P}`$，使得$`\boldsymbol{PA} = \boldsymbol{T}`$，其中$`\boldsymbol{T}`$是上三角矩阵，且对角元素都是正数。**

取  
$`\begin{aligned}
    \boldsymbol{u}_1 &= \boldsymbol{Ae}_1 - \left\Vert\boldsymbol{Ae}_1\right\Vert_2\boldsymbol{e}_1 \\
    &= \boldsymbol{Ae}_1 - 5\boldsymbol{e}_1\\
    &= \begin{pmatrix}
        -5 \\ 3 \\ 4
    \end{pmatrix}
\end{aligned}`$  
$`\begin{aligned}
    \boldsymbol{R}_1 &= \boldsymbol{I} - 2\frac{\boldsymbol{u}_1\boldsymbol{u}_1^\mathrm{T}}{\boldsymbol{u}_1^\mathrm{T}\boldsymbol{u}_1} \\
    &= \boldsymbol{I} - \frac{1}{25}\begin{pmatrix}
        25 & -15 & -20 \\
        -15 & 9 & 12 \\
        -20 & 12 & 16
    \end{pmatrix} \\
    &= \frac{1}{25}\begin{pmatrix}
        0 & 15 & 20 \\
        15 & 16 & -12 \\
        20 & -12 & 9
    \end{pmatrix}
\end{aligned}`$  
此时有$`\boldsymbol{R}_1\boldsymbol{A} = \begin{pmatrix}
    5 & 25 & -4 \\
    0 & 0 & -10 \\
    0 & -25 & -10
\end{pmatrix}`$。  

显然$`\boldsymbol{T}_{2,3}\boldsymbol{R}_1\boldsymbol{A} = \begin{pmatrix}
    5 & 25 & -4 \\
    0 & -25 & -10 \\
    0 & 0 & -10
\end{pmatrix}`$是上三角矩阵，$`\boldsymbol{T}_2\left(-1\right)\boldsymbol{T}_3\left(-1\right)\boldsymbol{T}_{2,3}\boldsymbol{R}_1\boldsymbol{A} = \begin{pmatrix}
    5 & 25 & -4 \\
    0 & 25 & 10 \\
    0 & 0 & 10
\end{pmatrix}`$是对角线元素均为正数的上三角矩阵，其中初等矩阵都是正交矩阵。  
所以  
$`\begin{aligned}
    \boldsymbol{P} &= \boldsymbol{T}_2\left(-1\right)\boldsymbol{T}_3\left(-1\right)\boldsymbol{T}_{2,3}\boldsymbol{R}_1 \\
    &= \frac{1}{25}\begin{pmatrix}
        0 & 15 & 20 \\
        -20 & 12 & -9 \\
        -15 & -16 & 12
    \end{pmatrix}
\end{aligned}`$



#### 6.5
**对于矩阵$`\boldsymbol{A} = \begin{pmatrix}
    1 & 19 & -34 \\
    -2 & -5 & 20 \\
    2 & 8 & 37
\end{pmatrix}`$，使用Householder约化实现QR分解。**

$`\begin{aligned}
    \boldsymbol{u}_1 &= \boldsymbol{Ae}_1 - \left\Vert\boldsymbol{Ae}_1\right\Vert_2\boldsymbol{e}_1 \\
    &= \boldsymbol{Ae}_1 - 3\boldsymbol{e}_1\\
    &= \begin{pmatrix}
        -2 \\ -2 \\ 2
    \end{pmatrix}
\end{aligned}`$  

$`\begin{aligned}
    \boldsymbol{R}_1 &= \boldsymbol{I} - 2\frac{\boldsymbol{u}_1\boldsymbol{u}_1^\mathrm{T}}{\boldsymbol{u}_1^\mathrm{T}\boldsymbol{u}_1} \\
    &= \boldsymbol{I} - \frac{2}{3}\begin{pmatrix}
        1 & 1 & -1 \\
        1 & 1 & -1 \\
        -1 & -1 & 1
    \end{pmatrix} \\
    &= \frac{1}{3}\begin{pmatrix}
        1 & -2 & 2 \\
        -2 & 1 & 2 \\
        2 & 2 & 1
    \end{pmatrix}
\end{aligned}`$  

此时  
$`\boldsymbol{R}_1\boldsymbol{A} = \begin{pmatrix}
    3 & 15 & 0 \\
    0 & -9 & 54 \\
    0 & 12 & 3
\end{pmatrix}.`$  

取子阵$`\begin{pmatrix}
    -9 & 54 \\
    12 & 3
\end{pmatrix}`$记为$`\boldsymbol{A}_1`$，

$`\begin{aligned}
    \boldsymbol{u}_2 &= \boldsymbol{A}_1\boldsymbol{e}_1 - \left\Vert\boldsymbol{A}_1\boldsymbol{e}_1\right\Vert_2\boldsymbol{e}_1 \\
    &= \boldsymbol{A}_1\boldsymbol{e}_1 + 15\boldsymbol{e}_1\\
    &= \begin{pmatrix}
        -24 \\ 12
    \end{pmatrix}
\end{aligned}`$  

$`\begin{aligned}
    \boldsymbol{R}_2 &= \boldsymbol{I} - 2\frac{\boldsymbol{u}_2\boldsymbol{u}_2^\mathrm{T}}{\boldsymbol{u}_2^\mathrm{T}\boldsymbol{u}_2} \\
    &= \boldsymbol{I} - \frac{2}{5}\begin{pmatrix}
        4 & -2 \\
        -2 & 1
    \end{pmatrix} \\
    &= \frac{1}{5}\begin{pmatrix}
        -3 & 4 \\
        4 & 3
    \end{pmatrix}
\end{aligned}`$  

此时$`\begin{pmatrix}1 & \boldsymbol{0} \\ \boldsymbol{0} & \boldsymbol{R}_2\end{pmatrix}\boldsymbol{R}_1\boldsymbol{A} = \begin{pmatrix}
    3 & 15 & 0 \\
    0 & 15 & -30 \\
    0 & 0 & 45
\end{pmatrix}`$

所以  
$`\begin{aligned}
    \boldsymbol{Q} &= \left(\begin{pmatrix}1 & \boldsymbol{0} \\ \boldsymbol{0} & \boldsymbol{R}_2\end{pmatrix}\boldsymbol{R}_1\right)^{-1} \\
    &= \frac{1}{15}\begin{pmatrix}
        5 & -10 & 10 \\
        14 & 5 & -2 \\
        -2 & 10 & 11
    \end{pmatrix}^\mathrm{T} \\
    &= \frac{1}{15}\begin{pmatrix}
        5 & 14 & -2 \\
        -10 & 5 & 10 \\
        10 & -2 & 11
    \end{pmatrix} \\
    \boldsymbol{R} &= \begin{pmatrix}
        1 & \boldsymbol{0} \\
        \boldsymbol{0} & \boldsymbol{R}_2
    \end{pmatrix}\boldsymbol{R}_1\boldsymbol{A} \\
    &= \begin{pmatrix}
        3 & 15 & 0 \\
        0 & 15 & -30 \\
        0 & 0 & 45
    \end{pmatrix}
\end{aligned}`$