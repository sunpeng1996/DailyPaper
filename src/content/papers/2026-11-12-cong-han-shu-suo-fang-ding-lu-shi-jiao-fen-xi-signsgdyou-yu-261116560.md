---
title: 'When and How SignSGD Outperforms SGD: A Functional Scaling Law Perspective'
title_zh: 从函数缩放定律视角分析SignSGD优于SGD的场景与机制
authors:
- Zilin Wang
- Binghui Li
- Jia-Nan Wang
- Lean Wang
- Jinbo Wang
- Lei Wu
affiliations:
- Peking University
- AI for Science Institute, Beijing
arxiv_id: '2611.16560'
url: https://arxiv.org/abs/2611.16560
pdf_url: https://arxiv.org/pdf/2611.16560
published: '2026-11-12'
collected: '2026-11-14'
category: Training
direction: 大模型训练 · 优化器缩放定律
tags:
- SignSGD
- SGD
- Scaling Law
- Optimizer
- LLM Training
one_liner: 揭示SignSGD噪声诱导预条件机制，给出其优于SGD的任务场景与batch size适用规则
practical_value: '- 优化器选型参考：训练难任务（比如冷启动召回模型、小样本Agent微调）优先选SignSGD类优化器提升数据效率

  - 大batch训练场景（比如电商亿级用户行为的召回排序模型分布式训练）用SignSGD可在不降低数据效率的前提下减少训练步数

  - LLM/垂域大模型预训练时可基于该缩放定律调整SignSGD的学习率schedule，平衡信号学习与噪声遗忘速度'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有SignSGD理论多聚焦全批次确定性动态或通用收敛性，缺乏对其缩放行为、相对SGD优势场景的清晰解释，难以指导工业界优化器选型。

### 方法关键点
推导幂律核回归场景下SignSGD的通用函数缩放定律（FSL），核心机制为噪声诱导预条件：梯度噪声平滑sign算子，将有效Hessian从$oldsymbol{H}$转换为$oldsymbol{H}^{1/2}$，动态表现为信号学习更快、噪声遗忘更慢的tradeoff。

### 关键结果
1. 难任务场景下SignSGD数据效率显著优于SGD；
2. 简单任务场景二者数据效率相当，但SignSGD支持更大batch size，相同数据预算下训练步数可进一步减少；
3. LLM预训练实验验证该FSL比SGD的FSL更准确拟合Sign类优化器的loss动态与batch size依赖关系。
