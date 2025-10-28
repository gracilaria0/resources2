作业三
======

#### 3.1
**试说明所有$`n\times n`$的实数矩阵构成的集合为一个线性空间。另外判断下列哪些是该空间的子空间，并给出理由。
①所有对称矩阵；②所有反对称矩阵；③所有可逆矩阵；④所有上三角矩阵；⑤所有下三角矩阵；⑥满足$`\mathrm{trace}{\boldsymbol{A}} = 0`$的所有矩阵。**

对于所有$`n\times n`$的实数矩阵构成的集合$`S = \left\{\boldsymbol{A} = \left(a_{i,j}\right) \mid a_{i,j}\in \mathbb{R}\right\}`$，可以在其上定义  
加法：$`+: S \times S \rightarrow S', \left(\left(a_{i,j}\right), \left(b_{i,j}\right) \right) \mapsto \left(a_{i,j} + b_{i,j}\right)`$。因为$`\mathbb{R}`$对加法有封闭性，$`a_{i,j} + b_{i,j} \in \mathbb{R}`$，所以$`\left(a_{i,j} + b_{i,j}\right) \in S, S' = S`$，对$`S`$加法封闭。
数乘：$`\cdot: \mathbb{R} \times S \rightarrow S'', \left(\alpha, \left(a_{i,j}\right)\right) \mapsto \left(\alpha a_{i,j}\right)`$。因为$`\mathbb{R}`$对乘法有封闭性，$`\alpha a_{i,j}\in \mathbb{R}`$，所以$`\left(\alpha a_{i,j}\right) \in S, S'' = S`$，对$`S`$数乘封闭。

在此基础上，$`S`$满足
1. 加法交换律：因为$`\mathbb{R}`$对加法有交换律，$`a_{i,j} + b_{i,j} = b_{i,j} + a_{i,j}`$，所以$`\left(a_{i,j} + b_{i,j}\right) = \left(b_{i,j} + a_{i,j}\right)`$，$`S`$上的加法满足交换律；
2. 加法结合律：因为$`\mathbb{R}`$对加法有结合律，$`\left(a_{i,j} + b_{i,j}\right) + c_{i,j} = a_{i,j} + \left(b_{i,j} + c_{i,j}\right)`$，所以$`\left(\left(a_{i,j}\right) + \left(b_{i,j}\right)\right) + \left(c_{i,j}\right) = \left(a_{i,j}\right) + \left(\left(b_{i,j}\right) + \left(c_{i,j}\right)\right)`$，$`S`$上的加法满足结合律；
3. 加法单位元存在：因为$`\mathbb{R}`$对加法有单位元$`0`$，$`a_{i,j} + 0 = a_{i,j}`$，所以所有元素全$`0`$的矩阵$`\boldsymbol{O} = \left(0\right)`$是$`S`$上的加法单位元；
4. 加法逆元存在：因为$`\mathbb{R}`$对加法有逆元，$`a_{i,j} + \left(-a_{i,j}\right) = 0`$，所以$`\left(a_{i,j}\right)`$的加法逆元是$`-1 \cdot \left(a_{i,j}\right)`$；
5. 数乘对数量的分配律：因为$`\mathbb{R}`$对乘法有分配律，$`\left(\alpha + \beta\right)a_{i,j} = \alpha a_{i,j} + \beta a_{i,j}`$，所以$`\left(\alpha + \beta\right)\left(a_{i,j}\right) = \alpha \left(a_{i,j}\right) + \beta \left(a_{i,j}\right)`$，$`S`$上的数乘对数量满足分配律；
6. 数乘对$`S`$中元素的分配律：因为$`\mathbb{R}`$对乘法有分配律，$`\alpha \left(a_{i,j} + b_{i,j}\right) = \alpha a_{i,j} + \alpha b_{i,j}`$，所以$`\alpha \left(\left(a_{i,j}\right) + \left(b_{i,j}\right)\right) = \alpha \left(a_{i,j}\right) + \alpha \left(b_{i,j}\right)`$，$`S`$上的数乘对$`S`$中的元素满足分配律；
7. 数乘结合律：因为$`\mathbb{R}`$对乘法有结合律，$`\alpha \left(\beta a_{i,j}\right) = \left(\alpha \beta\right) a_{i,j}`$，所以$`\alpha \beta \left(a_{i,j}\right) = \left(\alpha \beta\right) \left(a_{i,j}\right)`$，$`S`$上的数乘满足结合律；
8. 数乘单位元存在：因为$`\mathbb{R}`$对乘法有单位元$`1`$，$`a_{i,j}\cdot 1 = a_{i,j}`$，所以$`1 \cdot \left(a_{i,j}\right) = \left(a_{i,j}\right)`$，$`S`$上的数乘单位元是$`1`$。
   
所以所有$`n\times n`$的实数矩阵构成的集合$`S`$及其上定义的加法和数乘是一个线性空间$`\mathfrak{S}`$。

①②④⑤⑥都能够满足上述要求，它们以及$`S`$上定义的加法和数乘构成了$`\mathfrak{S}`$的子空间。

##### ③所有可逆矩阵
记$`S`$中所有可逆矩阵构成的集合为$`V`$。对任意$`\left(v_{i,j}\right) \in V`$，显然$`\left(-v_{i,j}\right) = -\left(v_{i,j}\right)`$也可逆，$`-\left(v_{i,j}\right) \in V`$。
但$`\left(v_{i,j}\right) + \left(-\left(v_{i,j}\right)\right) = \left(0\right) \notin V`$，$`V`$中无加法的单位元。所以$`V`$及$`S`$上的加法和数乘运算不构成$`\mathfrak{S}`$的子空间。



#### 3.2
**$`\boldsymbol{A}`$和$`\boldsymbol{B}`$分别是$`m\times n`$和$`n\times p`$矩阵，说明下面结论成立：**
此题中用线性空间的集合简化指代线性空间本身，例如$`\mathfrak{R}^n = \mathbb{R}^n`$。
##### (1) $`\mathrm{range}{\boldsymbol{AB}} \subseteq \mathrm{range}\boldsymbol{A}`$；
$`\mathrm{range}\boldsymbol{A} = \left\{\boldsymbol{Ax}\in \mathbb{R}^m \mid \boldsymbol{x}\in \mathbb{R}^n\right\}, \mathrm{range}{\boldsymbol{AB}} = \left\{\boldsymbol{ABx}\in \mathbb{R}^m \mid \boldsymbol{x}\in \mathbb{R}^n\right\}`$。
因为$`\boldsymbol{B}: \mathbb{R}^p \rightarrow \mathbb{R}^n, \mathrm{range}{\boldsymbol{B}} = \left\{\boldsymbol{Bx}\in \mathbb{R}^n \mid \boldsymbol{x}\in \mathbb{R}^p\right\} \subseteq \mathbb{R}^n`$，
所以$`\mathrm{range}{\boldsymbol{AB}} = \left\{\boldsymbol{ABx}\mid \boldsymbol{x}\in \mathbb{R}^n\right\} = \left\{\boldsymbol{A}\left(\boldsymbol{Bx}\right)\mid \boldsymbol{Bx}\in\mathrm{range}{\boldsymbol{B}} \subseteq \mathbb{R}^n\right\} \subseteq \mathrm{range}\boldsymbol{A}`$。

##### (2) $`\ker{\boldsymbol{B}} \subseteq \ker{\boldsymbol{AB}}`$。
$`\ker{\boldsymbol{B}} = \left\{\boldsymbol{x}\in \mathbb{R}^p \mid \boldsymbol{Bx} = \boldsymbol{0}\right\}, \ker{\boldsymbol{AB}} = \left\{\boldsymbol{x}\in \mathbb{R}^p \mid \boldsymbol{ABx} = \boldsymbol{0}\right\}`$。
任取$`\boldsymbol{x} \in \ker{\boldsymbol{B}}`$，有$`\boldsymbol{ABx} = \boldsymbol{A}\left(\boldsymbol{Bx}\right) = \boldsymbol{A0} = \boldsymbol{0}`$，所以$`\boldsymbol{x} \in \ker{\boldsymbol{A}}`$。
即$`\ker{\boldsymbol{B}} \subseteq \ker{\boldsymbol{AB}}`$。



#### 3.3
**有集合$`\left\{\begin{pmatrix}
    1 & 0 \\ 0 & 0
\end{pmatrix}, \begin{pmatrix}
    1 & 1 \\ 0 & 0
\end{pmatrix}, \begin{pmatrix}
    1 & 1 \\ 1 & 0
\end{pmatrix}, \begin{pmatrix}
    1 & 1 \\ 1 & 1
\end{pmatrix}\right\}`$，试判断该集合是否线性无关。**

集合中元素所在的全空间是所有$`2\times 2`$的实矩阵$`\mathbb{R}^{2\times 2}`$空间，该空间是$`4`$维的，空间中的零元$`\boldsymbol{O} = \begin{pmatrix}
    0 & 0 \\ 0 & 0
\end{pmatrix}`$。  
用给定集合中的后一个元素减去前一个元素，可以得到$`\begin{pmatrix}
    0 & 1 \\ 0 & 0
\end{pmatrix}, \begin{pmatrix}
    0 & 0 \\ 1 & 0
\end{pmatrix}, \begin{pmatrix}
    0 & 0 \\ 0 & 1
\end{pmatrix}`$，它们与第一个元素恰好是每一个位置上的单位元素。  
取$`c_1, c_2, c_3, c_4 \in \mathbb{R}`$，有$`c_1 \begin{pmatrix}
    1 & 0 \\ 0 & 0
\end{pmatrix} + c_2 \begin{pmatrix}
    0 & 1 \\ 0 & 0
\end{pmatrix} + c_3 \begin{pmatrix}
    0 & 0 \\ 1 & 0
\end{pmatrix} + c_4 \begin{pmatrix}
    0 & 0 \\ 0 & 1
\end{pmatrix} = \begin{pmatrix}
    c_1 & c_2 \\ c_3 & c_4
\end{pmatrix}`$，无法相互消去，当且仅当$`c_1 = c_2 = c_3 = c_4 = 0`$时，$`\begin{pmatrix}
    c_1 & c_2 \\ c_3 & c_4
\end{pmatrix} = \boldsymbol{O}`$。  
所以集合线性无关，且是全空间$`\mathbb{R}^{2\times 2}`$的一个极大无关组。



#### 3.4
**对于矩阵$`\boldsymbol{A} = \begin{pmatrix}
    1 & 3 & 1 & -4 \\
    -1 & -3 & 1 & 0 \\
    2 & 6 & 2 & -8
\end{pmatrix}`$，验证$`\mathrm{rank}\left(\boldsymbol{A}^\mathrm{T}\boldsymbol{A}\right) = \mathrm{rank}\boldsymbol{A} = \mathrm{rank}\left(\boldsymbol{A}\boldsymbol{A}^\mathrm{T}\right)`$。**

用Gauss消元法求矩阵的行阶梯形得到秩，“$`\sim`$”代表等价。
$`\boldsymbol{A} \sim \begin{pmatrix}
    1 & 3 & 1 & -4 \\
    0 & 0 & 2 & -4 \\
    0 & 0 & 0 & 0
\end{pmatrix},`$

$`\begin{aligned}
    \boldsymbol{A}^\mathrm{T}\boldsymbol{A} &= \begin{pmatrix}
        6 & 18 & 4 & -20 \\
        18 & 54 & 12 & -60 \\
        4 & 12 & 6 & -20 \\
        -20 & -60 & -20 & 80
    \end{pmatrix} \\
    &\sim \begin{pmatrix}
        6 & 18 & 4 & -20 \\
        0 & 0 & 0 & 0 \\
        4 & 12 & 6 & -20 \\
        0 & 0 & 10 & -20
    \end{pmatrix} \\
    &\sim \begin{pmatrix}
        12 & 36 & 8 & -40 \\
        0 & 0 & 0 & 0 \\
        12 & 36 & 18 & -60 \\
        0 & 0 & 10 & -20
    \end{pmatrix} \\
    &\sim \begin{pmatrix}
        6 & 18 & 4 & -20 \\
        0 & 0 & 10 & -20 \\
        0 & 0 & 0 & 0 \\
        0 & 0 & 0 & 0
    \end{pmatrix},
\end{aligned}`$

$`\begin{aligned}
    \boldsymbol{A}\boldsymbol{A}^\mathrm{T} &= \begin{pmatrix}
        27 & -9 & 54 \\
        -9 & 11 & -18 \\
        54 & -18 & 108
    \end{pmatrix} \\
    &\sim \begin{pmatrix}
        27 & -9 & 54 \\
        -9 & 11 & -18 \\
        0 & 0 & 0
    \end{pmatrix} \\
    &\sim \begin{pmatrix}
        -9 & 11 & -18 \\
        0 & 24 & 0 \\
        0 & 0 & 0
    \end{pmatrix}.
\end{aligned}`$

所以$`\mathrm{rank}\left(\boldsymbol{A}^\mathrm{T}\boldsymbol{A}\right) = \mathrm{rank}\boldsymbol{A} = \mathrm{rank}\left(\boldsymbol{A}\boldsymbol{A}^\mathrm{T}\right) = 2`$。