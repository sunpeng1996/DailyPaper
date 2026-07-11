---
title: Spectral Stability of Pseudoinverse-Based Extreme Learning Machine
title_zh: 基于伪逆的极限学习机（ELM）谱稳定性研究
authors:
- Bich Van Nguyen
- Ngoc Anh Khong
affiliations:
- Institute for Artificial Intelligence, VNU University of Engineering and Technology,
  Vietnam
arxiv_id: '2607.08581'
url: https://arxiv.org/abs/2607.08581
pdf_url: https://arxiv.org/pdf/2607.08581
published: '2026-07-09'
collected: '2026-07-11'
category: Training
direction: 极限学习机训练 · 数值稳定性优化
tags:
- Extreme Learning Machine
- Numerical Stability
- SVD
- Pseudoinverse
- Singular Value
one_liner: 从谱视角解析基于伪逆的ELM稳定性，验证病态条件下SVD法计算伪逆的可靠性优势
practical_value: '- 电商推荐场景下用ELM做轻量级排序/冷启动用户兴趣建模时，优先选择SVD法计算伪逆，避免隐层病态矩阵导致的预测结果波动

  - 调整ELM隐层宽度时可参考谱分析结论，通过设置最小奇异值阈值筛选配置，降低模型对输入扰动的敏感性

  - 在线推理场景如需采用迭代法加速伪逆计算，需提前校验隐层矩阵的谱特性，避免数值误差被放大影响推荐效果'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
极限学习机（ELM）通过Moore-Penrose伪逆解析计算输出权重，训练速度极快，但数值稳定性高度依赖隐层矩阵的条件数，病态矩阵易导致扰动、数值误差放大，现有研究对稳定性的谱层面作用机制缺乏系统分析。
### 方法关键点
1. 从谱视角推导证明：隐层矩阵最小奇异值直接决定输出权重的扰动放大程度，条件数可定量度量隐层不稳定性；
2. 对比SVD基伪逆计算方案与迭代超幂法的性能差异，结合随机特征理论解释隐层宽度对条件数的影响规律。
### 关键结果
合成矩阵与ELM基准集实验验证：病态条件下SVD基伪逆方法可靠性最优，迭代法对谱特性的敏感度显著高于SVD方案，ELM稳定性本质由隐层矩阵的奇异值结构决定。
