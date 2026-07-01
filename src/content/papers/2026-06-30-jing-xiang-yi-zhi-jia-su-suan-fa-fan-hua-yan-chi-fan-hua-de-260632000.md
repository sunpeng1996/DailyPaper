---
title: 'Radial Suppression Accelerates Algorithmic Generalization: A Geometric Analysis
  of Delayed Generalization'
title_zh: 径向抑制加速算法泛化：延迟泛化现象的几何分析
authors:
- Srijan Tiwari
- Aditya Chauhan
- Manjot Singh
affiliations:
- Indian Institute of Technology Roorkee
arxiv_id: '2606.32000'
url: https://arxiv.org/abs/2606.32000
pdf_url: https://arxiv.org/pdf/2606.32000
published: '2026-06-30'
collected: '2026-07-01'
category: Training
direction: 深度学习训练优化 · 泛化加速
tags:
- Generalization Acceleration
- Grokking
- Activation Regularization
- Training Dynamics
- Geometric Analysis
one_liner: 从激活空间几何角度解释神经网络延迟泛化成因，提出径向抑制策略最高提速算法任务泛化6倍
practical_value: '- 针对LLM/推荐模型在算法类任务（如用户行为规律挖掘、语义匹配）上的泛化延迟问题，可引入激活范数惩罚约束隐层表征半径，加速低维结构化电路收敛

  - 训练小模型完成符号任务（如搜索Query语义归一、电商属性标准化）时，可复用单超参数的√d半径球约束，减少训练步数、降低训练成本

  - 做模型收敛分析时，可对激活空间做径向-角向分解，定位泛化延迟的具体成因，针对性调整正则策略'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
神经网络在算法类任务上普遍存在延迟泛化（grokking）现象：训练集快速拟合后，测试集需经历极多训练步才会突然提升，此前缺乏对其几何层面成因的清晰解释。
### 方法关键点
1. 对激活空间做径向-角向分解，证实交叉熵优化导致的隐层表征径向膨胀是延迟泛化的核心诱因；
2. 推导三个可验证命题，证明惩罚径向膨胀可实现数据依赖的各向异性权重正则，压制径向梯度能量、迫使更新以角向为主，引导收敛到更平坦的极小值；
3. 引入单超参数范数惩罚，将激活软约束在半径为√d的超球面上。
### 关键结果
模运算任务上，该策略使MLP、Transformer的grokking速度最高提升6倍；10M参数nanoGPT做3位数加法时训练步数减半。
