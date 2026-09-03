---
title: 'oHC: Orthogonal Hyper-Connections on SO(4) via Quaternions'
title_zh: oHC：基于四元数实现SO(4)群的正交超连接
authors:
- Haoqiang Guo
- Xuyi Chen
- Bo Ke
- Yishu Lei
- Ziyang Xu
- Shikun Feng
- Ximen
- Wenhan Luo
affiliations:
- The Hong Kong University of Science and Technology
- Baidu Inc.
arxiv_id: '2609.02672'
url: https://arxiv.org/abs/2609.02672
pdf_url: https://arxiv.org/pdf/2609.02672
published: '2026-09-02'
collected: '2026-09-03'
category: Training
direction: 大模型训练 · 多流残差连接优化
tags:
- Hyper-Connections
- Orthogonal Constraint
- Quaternion
- Transformer
- MoE
- Training Stability
one_liner: 提出约束于SO(4)的正交超连接oHC，四元数闭形式参数化，效果性能均优于现有HC变体
practical_value: '- 基于LLM的生成式推荐、Agent多特征融合场景，可直接用oHC替换现有双随机约束mHC，避免多流用户/物品特征逐层同质化，提升召回排序效果

  - 多特征混合矩阵的正交化实现，可复用四元数闭形式参数化技巧，无需Sinkhorn迭代，计算速度最高提升20倍，降低线上推理延迟

  - 深层推荐大模型训练时，可借鉴正交约束思路限制混合矩阵奇异值恒为1，避免梯度消失/爆炸，提升训练稳定性与收敛效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有Hyper-Connections（HC）采用无约束残差混合矩阵会导致信号爆炸/消失，训练不稳定；mHC将矩阵约束为双随机矩阵虽抑制了信号爆炸，但会让多流特征逐层同质化，深度越大特征差异越小；iHC直接用单位矩阵关闭跨流混合，又损失了流间信息交互能力，三者均无法兼顾训练稳定性、流间多样性和混合效率。

### 方法关键点
1. 提出正交超连接oHC，将残差混合矩阵约束在SO(n)旋转群，所有方向奇异值恒为1，既不放大也不衰减信号，同时保留跨流混合能力；
2. 针对业界常用的4流HC场景，用一对单位四元数闭形式参数化SO(4)矩阵，无额外参数，无需迭代投影，初始化即可等价于标准残差网络；
3. 工程实现仅需手写Triton核，相比mHC的Sinkhorn迭代计算开销大幅降低。

### 关键实验
在3.9B总参数/0.4B激活参数的MoE大模型上训练73B token，对比单流残差（RC）、mHC、iHC三个基线：oHC下游16项任务平均BPB比RC低3.89%，训练损失比RC低2.063%，混合矩阵构造速度比Sinkhorn迭代快20.6倍。

**最值得记住的一句话**：多流特征融合的核心矛盾是既要跨流交互又要避免特征退化，正交约束是兼顾二者的高效解决方案。
