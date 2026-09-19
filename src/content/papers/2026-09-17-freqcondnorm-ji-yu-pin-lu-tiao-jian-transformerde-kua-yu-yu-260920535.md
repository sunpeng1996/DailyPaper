---
title: 'FreqCondNorm: Towards Cross-domain Predictive Maintenance through a Frequency-Conditioned
  Transformer Foundation Model'
title_zh: FreqCondNorm：基于频率条件Transformer的跨域预测性维护
authors:
- Zaynab Raounak
- Camille LHermine
- Zhiguo Zeng
affiliations:
- Laboratoire Génie Industriel, CentraleSupélec, Université Paris-Saclay, France
arxiv_id: '2609.20535'
url: https://arxiv.org/abs/2609.20535
pdf_url: https://arxiv.org/pdf/2609.20535
published: '2026-09-17'
collected: '2026-09-19'
category: Other
direction: 跨域时序建模 · 条件归一化Transformer
tags:
- Transformer
- Time-Series
- Cross-Domain
- Normalization
- Pre-training
one_liner: 提出带FiLM式频率条件归一化层的Transformer架构，实现跨采样频率的异构时序跨域迁移
practical_value: '- 跨域用户行为时序建模场景可复用FiLM式条件归一化思路，替代传统LayerNorm适配异构输入分布

  - 多源异构时序预训练可参考「掩码自编码+对比学习+平衡域采样」组合策略，提升小样本迁移效果

  - 涉及不同采样周期的时序数据（如秒级点击、日级交易）联合建模时，可借鉴频率条件对齐的架构思路，避免拆分多模型'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有预测性维护深度学习模型跨设备、工况迁移性差，工业时序采样频率跨度达5个数量级（1Hz~100kHz），标注数据稀缺。
### 方法关键点
1. 提出FreqCondNorm架构，用FiLM风格的频率条件归一化层替换PatchTST式Transformer的标准LayerNorm，统一异构时序输入
2. 基于5个公开预测维护数据集，采用掩码自编码+时序InfoNCE对比学习的组合训练目标，配合平衡域采样策略完成预训练
### 关键结果
故障诊断任务上，CWRU数据集准确率达99.2%，较CNN基线提升6.4pp；零样本迁移到未见过的MFPT数据集准确率达82.1%；剩余使用寿命预测任务无性能提升，说明预训练目标与该任务存在适配gap
