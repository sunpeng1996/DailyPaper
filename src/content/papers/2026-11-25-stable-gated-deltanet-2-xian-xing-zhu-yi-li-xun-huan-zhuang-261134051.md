---
title: 'Stable Gated DeltaNet-2: Understanding and Mitigating Recurrent State Instability'
title_zh: Stable Gated DeltaNet-2：线性注意力循环状态不稳定性的分析与缓解
authors:
- Xichong Zhang
- Xixuan Hao
- Zhichen Liu
- Le Zhou
- Zeyu Zhang
- Boyu Chen
- Mingfei Lu
- Zehao Lin
- Bo Tang
- Yonggang Zhang
affiliations:
- MemTensor
- USTC
- HKUST(GZ)
- SUSTech
- SJTU
arxiv_id: '2611.34051'
url: https://arxiv.org/abs/2611.34051
pdf_url: https://arxiv.org/pdf/2611.34051
published: '2026-11-25'
collected: '2026-11-26'
category: LLM
direction: 长上下文LLM · 线性注意力稳定性优化
tags:
- Linear Attention
- Long Context LLM
- Gated DeltaNet
- Recurrent State Stability
- Efficient Inference
one_liner: 提出对称擦除与衰减调控残差写入机制，解决GDN-2长上下文训练的循环状态爆炸问题
practical_value: '- 长上下文LLM服务优化：业务中若采用线性注意力轻量LLM做用户行为序列建模/Agent记忆，可直接复用对称擦除设计，避免长序列推理数值溢出，无需修改原有并行训练架构

  - 推荐长序列记忆模块设计：用户长行为序列记忆层可引入衰减调控残差写入机制，平衡记忆保留与新信息写入稳定性，避免记忆向量指数膨胀

  - 长序列模型训练监控：除loss外需额外监控循环状态范数与有效秩，提前发现潜在数值爆炸风险，避免无预警训练失败'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Gated DeltaNet-2（GDN-2）是性能优异的线性注意力架构，通过通道独立的擦除、写入门控提升长上下文检索能力，但长上下文训练时易出现无预警数值爆炸、训练失败；即使训练完成，内部循环状态也可能出现1e36级极值，严重降低记忆有效容量，现有loss监控无法提前发现该问题。

### 方法关键点
- 对称擦除设计：将擦除门拆分为两个平方根因子，分别作用于擦除读取和状态修改的key，对齐读写方向，保证擦除算子谱范数≤1，从理论上消除状态放大风险
- 衰减调控残差写入：引入受衰减因子约束的残差写入路径，补充对称擦除导致的写入能力损失，同时控制新增状态的能量
- 完全兼容原有chunkwise并行训练架构，训练推理复杂度与GDN-2一致，无额外 overhead

### 关键实验
在1.6B参数模型上开展64K上下文预训练，对比GDN-2、KDA、D-Clip、β-Guard等baseline：循环架构下128K上下文RULER平均得分提升6.80分，混合架构下9个下游任务平均准确率提升0.62个百分点，训练过程无任何数值失败案例。

最值得记住的一句话：线性注意力的循环状态稳定性不能只靠loss监控，非对称擦除算子的方向性增益会跨token累积，即使特征值都≤1也可能导致状态指数增长。
