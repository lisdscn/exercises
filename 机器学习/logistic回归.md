# 6.3 写出最大熵模型学习的 DFP 算法

## 题目

写出最大熵模型学习的 DFP 算法。

## 解答

**最大熵模型学习的 DFP（Davidon-Fletcher-Powell）算法**

**输入：** 特征函数 $f_1,f_2,\cdots,f_n$；经验分布 $\tilde{P}(x,y)$；目标函数 $f(w)$，梯度 $g(w)=\nabla f(w)$，精度要求 $\varepsilon$；

**输出：** 最优参数值 $w^*$；最优模型 $P_{w^*}(y|x)$。

(1) 选定初始点 $w^{(0)}$，取 $B_0$ 为正定对称矩阵，置 $k=0$。

(2) 计算 $g_k=g(w^{(k)})$。若 $\|g_k\|<\varepsilon$，则停止计算，得 $w^*=w^{(k)}$；否则转 (3)。

(3) 由 $B_k p_k=-g_k$ 求出 $p_k$。

(4) 一维搜索：求 $\lambda_k$ 使得

$f(w^{(k)}+\lambda_k p_k)=\min_{\lambda\ge0} f(w^{(k)}+\lambda p_k)$

(5) 置 $w^{(k+1)}=w^{(k)}+\lambda_k p_k$。

(6) 计算 $g_{k+1}=g(w^{(k+1)})$，若 $\|g_{k+1}\|<\varepsilon$，则停止计算，得 $w^*=w^{(k+1)}$；否则按下式（DFP 校正公式）求出 $B_{k+1}$：

$B_{k+1}=B_k+\frac{y_k y_k^{\mathrm{T}}}{y_k^{\mathrm{T}}\delta_k}-\frac{B_k\delta_k\delta_k^{\mathrm{T}}B_k}{\delta_k^{\mathrm{T}}B_k\delta_k}$

其中

$y_k=g_{k+1}-g_k,\qquad \delta_k=w^{(k+1)}-w^{(k)}$

(7) 置 $k=k+1$，转 (3)。

算法终止后得到最优参数值 $w^*$，进而得到最大熵模型（最优模型）：

$P_{w^*}(y|x)=\frac{1}{Z_{w^*}(x)}\exp\left(\sum_{i=1}^{n}w_i^* f_i(x,y)\right)$

其中 $Z_{w^*}(x)=\sum_y\exp\left(\sum_{i=1}^{n}w_i^* f_i(x,y)\right)$ 为规范化因子。