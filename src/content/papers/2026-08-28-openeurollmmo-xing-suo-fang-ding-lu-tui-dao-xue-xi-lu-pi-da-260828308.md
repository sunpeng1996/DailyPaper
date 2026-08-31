---
title: 'Deriving Scaling Laws for OpenEuroLLM Models: Learning Rate, Batch Size and
  Loss'
title_zh: OpenEuroLLM模型缩放定律推导：学习率、批大小与损失
authors:
- Niccolò Ajroldi
- Diana Alexandra Onutu
- Haider Al-Tahan
- Jörg Franke
- Sampo Pyysalo
- Jenia Jitsev
- Aaron Klein
affiliations:
- ELLIS Institute Tübingen
- Eindhoven University of Technology
- Georgia Institute of Technology
- University of Freiburg
- Jülich Supercomputing Center
arxiv_id: '2608.28308'
url: https://arxiv.org/abs/2608.28308
pdf_url: https://arxiv.org/pdf/2608.28308
published: '2026-08-28'
collected: '2026-08-31'
category: Training
direction: LLM预训练 · 超参缩放定律
tags:
- Scaling Law
- LLM Pretraining
- Learning Rate
- Batch Size
- Loss Prediction
one_liner: 基于47M-1.7B LLM预训练实验，推导可落地的学习率、批大小与损失缩放公式
practical_value: '- 训练电商垂直域小LLM（导购/商品文案生成/推荐Agent）时，可直接复用论文给出的LR/批大小缩放幂律，减少全量超参扫参成本

  - 采用WSD学习率调度时，大LR、小批次、大模型、长训练token量的场景必须加LR退火，最多可降低0.2的验证loss

  - 预训练前估算模型最优loss优先选择Skaling公式，相比Chinchilla预测误差降低67%，可提前规避无效算力投入

  - 超参网格扫参后采用二次平滑方法拟合loss曲面，可降低种子、采样带来的波动，得到更稳定的最优超参'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM预训练的学习率、批大小选择直接决定训练效率和最终效果，但现有缩放定律结论因数据集、架构差异可迁移性弱，且缺乏Warmup-Stable-Decay（WSD）调度下退火阶段的超参偏移分析，中小团队训练垂直域LLM时扫参成本极高，亟需可落地的缩放规则指导。
### 方法关键点
- 实验覆盖47M~1.7B共6档参数量的decoder-only LLM，训练token数从6B到300B，在Nemotron-CC高质量英文语料上完成LR、批大小网格扫参
- 对LR和批大小的loss曲面做二次平滑，分别拟合联合最优、硬件约束下单变量固定时的LR/批大小缩放幂律
- 对比无交互项的Chinchilla公式、带模型-数据耦合项的Skaling公式的loss预测精度
- 分析WSD调度稳定阶段与退火阶段的超参偏移、loss增益规律
### 关键结果
- 联合最优LR、批大小缩放公式在1.7B held-out模型上的预测MAPE分别为28%、10%
- Skaling公式对1.7B模型的loss预测RMSE为0.0056，较Chinchilla的0.0174下降67.8%
- LR退火的loss增益最高可达0.2，退火后最优LR比稳定阶段最高提升4倍
### 核心结论
硬件约束下固定批大小训练时，不要直接套用联合最优LR公式，需改用带批大小调节项的边际LR缩放公式，可显著提升训练效率与最终效果。
