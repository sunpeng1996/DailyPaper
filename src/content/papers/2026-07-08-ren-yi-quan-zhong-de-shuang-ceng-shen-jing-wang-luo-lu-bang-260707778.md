---
title: A law of robustness for two-layer neural networks with arbitrary weights
title_zh: 任意权重的双层神经网络鲁棒性定律
authors:
- Yitzchak Shmalo
arxiv_id: '2607.07778'
url: https://arxiv.org/abs/2607.07778
pdf_url: https://arxiv.org/pdf/2607.07778
published: '2026-07-08'
collected: '2026-07-13'
category: Training
direction: 神经网络训练 · 鲁棒性理论下界
tags:
- Two-layer NN
- Robustness
- Lipschitz Constant
- ReLU
- Generalization Bound
one_liner: 证明无权重约束的双层分段线性激活网络鲁棒性下界猜想，误差仅含一个对数因子
practical_value: 主要是学术贡献，业务可借鉴点有限
score: 4
source: arxiv-stat.ML
depth: abstract
---

### 动机
Bubeck等人提出猜想：拟合n个带噪标签的m神经元双层神经网络，Lipschitz常数下界至少为√(n/m)，但已有的证明依赖参数多项式有界假设，无权重约束的双层场景无有效证明方案。
### 方法关键点
用函数空间覆盖替代不可行的无界权重参数空间覆盖，核心引入刚性引理：d≥3时，每个典型扭结的系数受实现函数的Lipschitz常数控制，不同超平面上的扭结无法在通用点抵消。
### 关键结果
对含ReLU在内的所有连续分段线性激活的任意权重双层网络，高概率下证明猜想成立，仅差1个对数因子；当拟合误差低于噪声水平ε时，Lip(f)≥cε√(n/(m log(Cmnd/ε)))；d=2时刚性引理失效，宽度2n的双层ReLU插值器可实现O(1) Lipschitz常数，符合过参数化端点的定律。
