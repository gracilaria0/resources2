作业五
======

#### 5.1
**对于矩阵$`\boldsymbol{A} = \begin{pmatrix}
    1 & -2 \\
    -1 & 2
\end{pmatrix}, \boldsymbol{B} = \begin{pmatrix}
    0 & 1 & 0 \\
    0 & 0 & 1 \\
    1 & 0 & 0
\end{pmatrix}, \boldsymbol{C} = \begin{pmatrix}
    4 & -2 & 4 \\
    -2 & 1 & -2 \\
    4 & -2 & 4
\end{pmatrix}`$，分别计算Frobenius范数，$`1`$-范数， $`2`$-范数，无穷范数。**

###### ①$`\boldsymbol{A} = \begin{pmatrix}1 & -2 \\ -1 & 2\end{pmatrix}`$
$`\left\Vert\boldsymbol{A}\right\Vert_{\mathrm{F}} = \sqrt{10}`$，  

$`\left\Vert\boldsymbol{A}\right\Vert_1 = \left\Vert\begin{pmatrix}-2 \\ 2\end{pmatrix}\right\Vert_1 = 4`$，

$`\left\Vert\boldsymbol{A}\right\Vert_\infty = \left\Vert\begin{pmatrix}1 & -2\end{pmatrix}\right\Vert_\infty = 3`$，

$`\begin{aligned}
    \left|\boldsymbol{A}^*\boldsymbol{A} - \sigma^2\boldsymbol{I}\right| &= \left|\begin{pmatrix}
        2-\sigma^2 & -4 \\
        -4 & 8-\sigma^2
    \end{pmatrix}\right| \\
    &= \sigma^4 - 10\sigma^2 \\
    &= \sigma^2 \left(\sigma - \sqrt{10}\right) \left(\sigma + \sqrt{10}\right),
\end{aligned}`$  
令其为$`0`$，得$`\mathrm{sv}\boldsymbol{A} = \left\{0, \sqrt{10}\right\}`$，则$`\left\Vert\boldsymbol{A}\right\Vert_2 = \sigma_{\mathrm{max}} = \sqrt{10}`$。


###### ②$`\boldsymbol{B} = \begin{pmatrix}0 & 1 & 0 \\0 & 0 & 1 \\1 & 0 & 0\end{pmatrix}`$
$`\left\Vert\boldsymbol{B}\right\Vert_{\mathrm{F}} = \sqrt{3}`$，  

$`\left\Vert\boldsymbol{B}\right\Vert_1 = \left\Vert\begin{pmatrix}0 \\ 0 \\ 1\end{pmatrix}\right\Vert_1 = 1`$，

$`\left\Vert\boldsymbol{A}\right\Vert_\infty = \left\Vert\begin{pmatrix}0 & 1 & 0\end{pmatrix}\right\Vert_\infty = 1`$，

$`\begin{aligned}
    \left|\boldsymbol{B}^*\boldsymbol{B} - \sigma^2\boldsymbol{I}\right| &= \left|\begin{pmatrix}
        1-\sigma^2 & 0 & 0 \\
        0 & 1-\sigma^2 & 0 \\
        0 & 0 & 1-\sigma^2
    \end{pmatrix}\right| \\
    &= \left(-\sigma^2 + 1\right)^3 \\
    &= \left(-\sigma + 1\right)^3 \left(\sigma + 1\right)^3,
\end{aligned}`$  
令其为$`0`$，得$`\mathrm{sv}\boldsymbol{B} = \left\{1, 1, 1\right\}`$，则$`\left\Vert\boldsymbol{B}\right\Vert_2 = \sigma_{\mathrm{max}} = 1`$。


###### ③$`\boldsymbol{C} = \begin{pmatrix}4 & -2 & 4 \\-2 & 1 & -2 \\ 4 & -2 & 4\end{pmatrix}`$
$`\left\Vert\boldsymbol{C}\right\Vert_{\mathrm{F}} = 9`$，  

$`\left\Vert\boldsymbol{C}\right\Vert_1 = \left\Vert\begin{pmatrix}4 \\ -2 \\ 4\end{pmatrix}\right\Vert_1 = 10`$，

$`\left\Vert\boldsymbol{C}\right\Vert_\infty = \left\Vert\begin{pmatrix}4 & -2 & 4\end{pmatrix}\right\Vert_\infty = 10`$，

$`\begin{aligned}
    \left|\boldsymbol{C}^*\boldsymbol{C} - \sigma^2\boldsymbol{I}\right| &= \left|\begin{pmatrix}
        36-\sigma^2 & -18 & 36 \\
        -18 & 9-\sigma^2 & -18 \\
        36 & -18 & 36-\sigma^2
    \end{pmatrix}\right| \\
    &= -\sigma^6 + 81\sigma^4 \\
    &= \sigma^4 \left(-\sigma + 9\right) \left(\sigma + 9\right),
\end{aligned}`$  
令其为$`0`$，得$`\mathrm{sv}\boldsymbol{C} = \left\{0, 0, 9\right\}`$，则$`\left\Vert\boldsymbol{C}\right\Vert_2 = \sigma_{\mathrm{max}} = 9`$。



#### 5.2
**对于向量空间$`\mathbb{R}^{2\times 2}`$，定义$`\left<\boldsymbol{A}, \boldsymbol{B}\right> = \mathrm{trace}\left(\boldsymbol{A}^\mathrm{T}\boldsymbol{B}\right)`$，**
##### (1) 简要说明$`\left<\boldsymbol{A}, \boldsymbol{B}\right>`$满足内积定义，是$`\mathbb{R}^{2\times 2}`$空间的一个内积；
对于$`\mathbb{R}^{n\times n}`$，
###### ①
$`\boldsymbol{S} = \boldsymbol{A}^\mathrm{T}\boldsymbol{A}`$对角线上的元素$`s_{i,i} = \left(\boldsymbol{A}\boldsymbol{e}_i\right)^\mathrm{T}\left(\boldsymbol{A}\boldsymbol{e}_i\right) \ge 0`$，当且仅当$`\boldsymbol{e}_i\boldsymbol{A} = \boldsymbol{0}`$；所以$`\left<\boldsymbol{A}, \boldsymbol{A}\right> = \mathrm{trace}\boldsymbol{S} = \sum_{i=0}^n{s_{i,i}} \ge 0`$，当且仅当$`\boldsymbol{A}\boldsymbol{e}_i = \boldsymbol{0}, \forall i\in \left\{1:n\right\}`$，即$`\boldsymbol{A} = \boldsymbol{O}`$。
###### ②
$`\begin{aligned}
    \left<\boldsymbol{A}, \alpha\boldsymbol{B}\right> &= \sum_{i=0}^n{\left(\boldsymbol{A}\boldsymbol{e}_i\right)^\mathrm{T}\left(\alpha\boldsymbol{B}\boldsymbol{e}_i\right)} \\
    &= \sum_{i=0}^n{\alpha\left(\boldsymbol{A}\boldsymbol{e}_i\right)^\mathrm{T}\left(\boldsymbol{B}\boldsymbol{e}_i\right)} \\
    &= \alpha\sum_{i=0}^n{\left(\boldsymbol{A}\boldsymbol{e}_i\right)^\mathrm{T}\left(\boldsymbol{B}\boldsymbol{e}_i\right)} \\
    &= \alpha\left<\boldsymbol{A}, \boldsymbol{B}\right>
\end{aligned}`$
###### ③
$`\begin{aligned}
    \left<\boldsymbol{A}, \boldsymbol{B}_1 + \boldsymbol{B}_2\right> &= \sum_{i=0}^n{\left(\boldsymbol{A}\boldsymbol{e}_i\right)^\mathrm{T}\left(\left(\boldsymbol{B}_1 + \boldsymbol{B}_2\right)\boldsymbol{e}_i\right)} \\
    &= \sum_{i=0}^n{\left(\boldsymbol{A}\boldsymbol{e}_i\right)^\mathrm{T}\left(\left(\boldsymbol{B}_1\boldsymbol{e}_i\right) + \left(\boldsymbol{B}_2\boldsymbol{e}_i\right)\right)} \\
    &= \sum_{i=0}^n{\left(\left(\boldsymbol{A}\boldsymbol{e}_i\right)^\mathrm{T}\left(\boldsymbol{B}_1\boldsymbol{e}_i\right) + \left(\boldsymbol{A}\boldsymbol{e}_i\right)^\mathrm{T}\left(\boldsymbol{B}_2\boldsymbol{e}_i\right)\right)} \\
    &= \sum_{i=0}^n{\left(\boldsymbol{A}\boldsymbol{e}_i\right)^\mathrm{T}\left(\boldsymbol{B}_1\boldsymbol{e}_i\right)} + \sum_{i=0}^n{\left(\boldsymbol{A}\boldsymbol{e}_i\right)^\mathrm{T}\left(\boldsymbol{B}_2\boldsymbol{e}_i\right)}\\
    &= \left<\boldsymbol{A}, \boldsymbol{B}_1\right> + \left<\boldsymbol{A}, \boldsymbol{B}_2\right>
\end{aligned}`$
###### ④
$`\begin{aligned}
    \left<\boldsymbol{B}, \boldsymbol{A}\right> &= \sum_{i=0}^n{\left(\boldsymbol{B}\boldsymbol{e}_i\right)^\mathrm{T}\left(\boldsymbol{A}\boldsymbol{e}_i\right)} \\
    &= \sum_{i=0}^n{\left(\boldsymbol{A}\boldsymbol{e}_i\right)^\mathrm{T}\left(\boldsymbol{B}\boldsymbol{e}_i\right)} \\
    &= \left<\boldsymbol{A}, \boldsymbol{B}\right>
\end{aligned}`$

所以，$`\left<\cdot, \cdot\right>`$是$`\mathbb{R}^{n\times n}`$上的内积。


##### (2) 证明$`B = \left\{\frac{1}{\sqrt{2}}\begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}, \frac{1}{\sqrt{2}}\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}, \frac{1}{2}\begin{pmatrix}1 & -1 \\ 1 & 1\end{pmatrix}, \frac{1}{2}\begin{pmatrix}1 & 1 \\ -1 & 1\end{pmatrix}\right\}`$是向量空间$`\mathbb{R}^{2\times 2}`$的一组标准正交基，并计算矩阵$`\boldsymbol{A} = \begin{pmatrix}1 & 1 \\ 1 & 1\end{pmatrix}`$在这组基下的Fourier展开；
将$`B`$中的矩阵依次记为$`\boldsymbol{B}_1, \boldsymbol{B}_2, \boldsymbol{B}_3, \boldsymbol{B}_4`$。

取$`c_i \in \mathbb{R}, i=1,2,3,4, \boldsymbol{c} = \left(c_i\right)`$，令$`\boldsymbol{B}_i`$的线性组合$`\sum_{i=1}^4{c_i\boldsymbol{B}_i} = \begin{pmatrix}
    \frac{1}{\sqrt{2}}c_2 + \frac{1}{2}c_3 + \frac{1}{2}c_4 & \frac{1}{\sqrt{2}}c_1 - \frac{1}{2}c_3 + \frac{1}{2}c_4 \\
    \frac{1}{\sqrt{2}}c_1 + \frac{1}{2}c_3 - \frac{1}{2}c_4 & -\frac{1}{\sqrt{2}}c_2 + \frac{1}{2}c_3 + \frac{1}{2}c_4
\end{pmatrix} = \boldsymbol{O}`$，  
得$`\begin{pmatrix}
    0 & \frac{1}{\sqrt{2}} & \frac{1}{2} & \frac{1}{2} \\
    \frac{1}{\sqrt{2}} & 0 & \frac{1}{2} & -\frac{1}{2} \\
    \frac{1}{\sqrt{2}} & 0 & -\frac{1}{2} & \frac{1}{2} \\
    0 & -\frac{1}{\sqrt{2}} & \frac{1}{2} & \frac{1}{2}
\end{pmatrix}\boldsymbol{c} = \boldsymbol{0}`$。  
方程只有零解，所以$`\boldsymbol{B}_i`$线性无关。又因为$`\mathrm{card}B = 4`$，所以$`B`$是$`\mathbb{R}^{2\times 2}`$的一组基。

因为  
$`\begin{aligned}
    \left<\boldsymbol{B}_1, \boldsymbol{B}_1\right> &= \mathrm{trace}\left(\frac{1}{2}\begin{pmatrix}
        1 & 0 \\
        0 & 1
    \end{pmatrix}\right) = 1, \\
    \left<\boldsymbol{B}_1, \boldsymbol{B}_2\right> &= \mathrm{trace}\left(\frac{1}{2}\begin{pmatrix}
        0 & -1 \\
        1 & 0
    \end{pmatrix}\right) = 0, \\
    \left<\boldsymbol{B}_1, \boldsymbol{B}_3\right> &= \mathrm{trace}\left(\frac{\sqrt{2}}{4}\begin{pmatrix}
        1 & 1 \\
        1 & -1
    \end{pmatrix}\right) = 0, \\
    \left<\boldsymbol{B}_1, \boldsymbol{B}_4\right> &= \mathrm{trace}\left(\frac{\sqrt{2}}{4}\begin{pmatrix}
        -1 & 1 \\
        1 & 1
    \end{pmatrix}\right) = 0, \\
    \left<\boldsymbol{B}_2, \boldsymbol{B}_2\right> &= \mathrm{trace}\left(\frac{1}{2}\begin{pmatrix}
        1 & 0 \\
        0 & 1
    \end{pmatrix}\right) = 1, \\
    \left<\boldsymbol{B}_2, \boldsymbol{B}_3\right> &= \mathrm{trace}\left(\frac{\sqrt{2}}{4}\begin{pmatrix}
        1 & -1 \\
        -1 & -1
    \end{pmatrix}\right) = 0, \\
    \left<\boldsymbol{B}_2, \boldsymbol{B}_4\right> &= \mathrm{trace}\left(\frac{\sqrt{2}}{4}\begin{pmatrix}
        1 & 1 \\
        1 & -1
    \end{pmatrix}\right) = 0, \\
    \left<\boldsymbol{B}_3, \boldsymbol{B}_3\right> &= \mathrm{trace}\left(\frac{1}{2}\begin{pmatrix}
        1 & 0 \\
        0 & 1
    \end{pmatrix}\right) = 1, \\
    \left<\boldsymbol{B}_3, \boldsymbol{B}_4\right> &= \mathrm{trace}\left(\frac{1}{2}\begin{pmatrix}
        0 & 1 \\
        -1 & 0
    \end{pmatrix}\right) = 0, \\
    \left<\boldsymbol{B}_4, \boldsymbol{B}_4\right> &= \mathrm{trace}\left(\frac{1}{2}\begin{pmatrix}
        1 & 0 \\
        0 & 1
    \end{pmatrix}\right) = 1,
\end{aligned}`$  
满足$`\left<\boldsymbol{B}_i, \boldsymbol{B}_j\right> = \delta_{i,j}`$，所以$`B`$是$`\mathbb{R}^{2\times 2}`$的一组标准正交基。

对$`\boldsymbol{A} = \begin{pmatrix}
    1 & 1 \\ 1 & 1
\end{pmatrix}`$，有  
$`\begin{aligned}
    a_1 &= \left<\boldsymbol{B}_1, \boldsymbol{A}\right> = \mathrm{trace}\left(\frac{\sqrt{2}}{2}\begin{pmatrix}
        1 & 1 \\
        1 & 1
    \end{pmatrix}\right) = \sqrt{2}, \\
    a_2 &= \left<\boldsymbol{B}_2, \boldsymbol{A}\right> = \mathrm{trace}\left(\frac{\sqrt{2}}{2}\begin{pmatrix}
        1 & 1 \\
        -1 & -1
    \end{pmatrix}\right) = 0, \\
    a_3 &= \left<\boldsymbol{B}_3, \boldsymbol{A}\right> = \mathrm{trace}\begin{pmatrix}
        1 & 1 \\
        0 & 0
    \end{pmatrix} = 1, \\
    a_4 &= \left<\boldsymbol{B}_4, \boldsymbol{A}\right> = \mathrm{trace}\begin{pmatrix}
        0 & 0 \\
        1 & 1
    \end{pmatrix} = 1,
\end{aligned}`$  
所以$`\boldsymbol{A} = \sqrt{2}\boldsymbol{B}_1 + 0\boldsymbol{B}_2 + \boldsymbol{B}_3 + \boldsymbol{B}_4`$。


##### (3) 试给出$`\mathbb{R}^{2\times 2}`$上一组新的标准正交基。
将$`\boldsymbol{B}_1`$取相反，则$`\left\{\frac{1}{\sqrt{2}}\begin{pmatrix}0 & -1 \\ -1 & 0\end{pmatrix}, \frac{1}{\sqrt{2}}\begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}, \frac{1}{2}\begin{pmatrix}1 & -1 \\ 1 & 1\end{pmatrix}, \frac{1}{2}\begin{pmatrix}1 & 1 \\ -1 & 1\end{pmatrix}\right\}`$是一组新的标准正交基。



#### 5.3
**设矩阵$`\boldsymbol{A} = \begin{pmatrix}
    1 & 0 & -1 \\
    1 & 2 & 1 \\
    1 & 1 & -3 \\
    0 & 1 & 1
\end{pmatrix}`$，向量$`\boldsymbol{b} = \begin{pmatrix}
    1 \\ 1 \\ 1 \\ 1
\end{pmatrix}`$，给出矩阵$`\boldsymbol{A}`$的QR分解；并给出$`\boldsymbol{Ax} = \boldsymbol{b}`$的最小二乘解。**

对$`\boldsymbol{A}`$进行Gram-Schmidt正交化，  
$`\boldsymbol{q}_1 = \frac{\boldsymbol{Ae}_1}{\sqrt{\left<\boldsymbol{Ae}_1, \boldsymbol{Ae}_1\right>}} = \frac{1}{\sqrt{3}}\begin{pmatrix}
    1 \\ 1 \\ 1 \\ 0
\end{pmatrix}, \\
\boldsymbol{q}_2' = \boldsymbol{Ae}_2 - \left<\boldsymbol{q}_1, \boldsymbol{Ae}_2\right>\boldsymbol{q}_1 = \boldsymbol{Ae}_2 - \sqrt{3}\boldsymbol{q}_1 = \begin{pmatrix}
    -1 \\ 1 \\ 0 \\ 1
\end{pmatrix}, \\
\boldsymbol{q}_2 = \frac{\boldsymbol{q}_2'}{\sqrt{\left<\boldsymbol{q}_2', \boldsymbol{q}_2'\right>}} = \frac{1}{\sqrt{3}}\begin{pmatrix}
    -1 \\ 1 \\ 0 \\ 1
\end{pmatrix}, \\
\boldsymbol{q}_3' = \boldsymbol{Ae}_3 - \left<\boldsymbol{q}_1, \boldsymbol{Ae}_3\right>\boldsymbol{q}_1 - \left<\boldsymbol{q}_2, \boldsymbol{Ae}_3\right>\boldsymbol{q}_2 = \boldsymbol{Ae}_3 + \sqrt{3}\boldsymbol{q}_1 - \sqrt{3}\boldsymbol{q}_2 = \begin{pmatrix}
    1 \\ 1 \\ -2 \\ 0
\end{pmatrix}, \\
\boldsymbol{q}_3 = \frac{\boldsymbol{q}_3'}{\sqrt{\left<\boldsymbol{q}_3', \boldsymbol{q}_3'\right>}} = \frac{1}{\sqrt{6}}\begin{pmatrix}
    1 \\ 1 \\ -2 \\ 0
\end{pmatrix},`$  
所以  
$`\begin{aligned}
    \boldsymbol{Q} &= \frac{\sqrt{3}}{6}\begin{pmatrix}
        2 & -2 & \sqrt{2} \\
        2 & 2 & \sqrt{2} \\
        2 & 0 & -2\sqrt{2} \\
        0 & 2 & 0
    \end{pmatrix}, \\
    \boldsymbol{R} &= \begin{pmatrix}
        \sqrt{3} & \sqrt{3} & -\sqrt{3} \\
        0 & \sqrt{3} & \sqrt{3} \\
        0 & 0 & \sqrt{6}
    \end{pmatrix} = \sqrt{3}\begin{pmatrix}
        1 & 1 & -1 \\
        0 & 1 & 1 \\
        0 & 0 & \sqrt{2}
    \end{pmatrix}.
\end{aligned}`$



#### 5.4
**对于向量组$`\left\{\boldsymbol{x}_1 = \begin{pmatrix}
    1 \\ 0 \\ 10^{-3}
\end{pmatrix}, \boldsymbol{x}_2 = \begin{pmatrix}
    1 \\ 0 \\ 0
\end{pmatrix}, \boldsymbol{x}_3 = \begin{pmatrix}
    1 \\ 10^{-3} \\ 0
\end{pmatrix}\right\}`$，在三位有效数字情形下，分别使用传统Gram-Schmidt方法和修改后的Gram-Schmidt方法，把上述向量组正交化。**

###### ①传统Gram-Schmidt正交化
$`\begin{aligned}
    \boldsymbol{u}_1 &= \frac{\boldsymbol{x}_1}{\sqrt{\left<\boldsymbol{x}_1, \boldsymbol{x}_1\right>}} \\
    &= \frac{1}{\sqrt{1 + 10^{-6}}}\begin{pmatrix}
        1 \\ 0 \\ 10^{-3}
    \end{pmatrix} \\
    &= \frac{1}{1.00}\begin{pmatrix}
        1 \\ 0 \\ 10^{-3}
    \end{pmatrix} \\
    &= \begin{pmatrix}
        1 \\ 0 \\ 10^{-3}
    \end{pmatrix}
\end{aligned} \\
\begin{aligned}
    \boldsymbol{u}_2' &= \boldsymbol{x}_2 - \left<\boldsymbol{u}_1, \boldsymbol{x}_2\right>\boldsymbol{u}_1 \\
    &= \begin{pmatrix}
        1 \\ 0 \\ 0
    \end{pmatrix} - 1\begin{pmatrix}
        1 \\ 0 \\ 10^{-3}
    \end{pmatrix}\\
    &= \begin{pmatrix}
        0 \\ 0 \\ -10^{-3}
    \end{pmatrix}
\end{aligned} \\
\boldsymbol{u}_2 = \frac{\boldsymbol{u}_2'}{\sqrt{\left<\boldsymbol{u}_2', \boldsymbol{u}_2'\right>}} = \begin{pmatrix}
    0 \\ 0 \\ -1
\end{pmatrix} \\
\begin{aligned}
    \boldsymbol{u}_3' &= \boldsymbol{x}_3 - \left<\boldsymbol{u}_1, \boldsymbol{x}_3\right>\boldsymbol{u}_1 - \left<\boldsymbol{u}_2, \boldsymbol{x}_3\right>\boldsymbol{u}_2\\
    &= \begin{pmatrix}
        1 \\ 10^{-3} \\ 0
    \end{pmatrix} - 1\begin{pmatrix}
        1 \\ 0 \\ 10^{-3}
    \end{pmatrix} - \boldsymbol{0} \\
    &= \begin{pmatrix}
        0 \\ 10^{-3} \\ -10^{-3}
    \end{pmatrix}
\end{aligned} \\
\begin{aligned}
    \boldsymbol{u}_3 &= \frac{\boldsymbol{u}_3'}{\sqrt{\left<\boldsymbol{u}_3', \boldsymbol{u}_3'\right>}} \\
    &= \frac{1}{\sqrt{10^{-6} + 10^{-6}}}\begin{pmatrix}
        0 \\ 10^{-3} \\ -10^{-3}
    \end{pmatrix} \\
    &= \frac{1}{1.41}\begin{pmatrix}
        0 \\ 1 \\ -1
    \end{pmatrix} \\
    &= \begin{pmatrix}
        0 \\ 0.709 \\ -0.709
    \end{pmatrix}
\end{aligned}`$

###### ②改进的Gram-Schmidt正交化
$`\boldsymbol{u}_1 = \frac{\boldsymbol{x}_1}{\sqrt{\left<\boldsymbol{x}_1, \boldsymbol{x}_1\right>}} = \begin{pmatrix}
    1 \\ 0 \\ 10^{-3}
\end{pmatrix} \\
\begin{aligned}
    \boldsymbol{u}_2' &= \left(\boldsymbol{I} - \boldsymbol{u}_1\boldsymbol{u}_1^*\right)\boldsymbol{x}_2 \\
    &= \begin{pmatrix}
        1-1 & 0 & -10^{-3} \\
        0 & 1 & 0 \\
        -10^{-3} & 0 & 1-10^{-6}
    \end{pmatrix}\boldsymbol{x}_2 \\
    &= \begin{pmatrix}
        0 & 0 & -10^{-3} \\
        0 & 1 & 0 \\
        -10^{-3} & 0 & 1.00
    \end{pmatrix}\begin{pmatrix}
        1 \\ 0 \\ 0
    \end{pmatrix} \\
    &= \begin{pmatrix}
        0 \\ 0 \\ -10^{-3}
    \end{pmatrix}
\end{aligned} \\
\boldsymbol{u}_2 = \frac{\boldsymbol{u}_2'}{\sqrt{\left<\boldsymbol{u}_2', \boldsymbol{u}_2'\right>}} = \begin{pmatrix}
    0 \\ 0 \\ -1
\end{pmatrix} \\
\begin{aligned}
    \boldsymbol{u}_3' &= \left(\boldsymbol{I} - \boldsymbol{u}_1\boldsymbol{u}_1^* - \boldsymbol{u}_2\boldsymbol{u}_2^*\right)\boldsymbol{x}_3 \\
    &= \begin{pmatrix}
        0 & 0 & -10^{-3} \\
        0 & 1 & 0 \\
        -10^{-3} & 0 & 1.00 - 1
    \end{pmatrix}\boldsymbol{x}_3 \\
    &= \begin{pmatrix}
        0 & 0 & -10^{-3} \\
        0 & 1 & 0 \\
        -10^{-3} & 0 & 0
    \end{pmatrix}\begin{pmatrix}
        1 \\ 10^{-3} \\ 0
    \end{pmatrix} \\
    &= \begin{pmatrix}
        0 \\ 10^{-3} \\ -10^{-3}
    \end{pmatrix}
\end{aligned} \\
\boldsymbol{u}_3 = \frac{\boldsymbol{u}_3'}{\sqrt{\left<\boldsymbol{u}_3', \boldsymbol{u}_3'\right>}} = \begin{pmatrix}
    0 \\ 0.709 \\ -0.709
\end{pmatrix}`$  

与传统的Gram-Schmidt方法结果相同。