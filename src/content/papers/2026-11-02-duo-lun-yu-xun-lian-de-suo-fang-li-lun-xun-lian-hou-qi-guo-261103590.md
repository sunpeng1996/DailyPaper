---
title: 'A Scaling Theory of Multi-Epoch Pretraining: Late-Time Overfitting and Ensembling'
title_zh: 多轮预训练的缩放理论：训练后期过拟合与模型集成优化
authors:
- Zhen Yang
- Yidi Miao
- Blake Bordelon
affiliations:
- University of Texas at Austin
- Carnegie Mellon University
arxiv_id: '2611.03590'
url: https://arxiv.org/abs/2611.03590
pdf_url: https://arxiv.org/pdf/2611.03590
published: '2026-11-02'
collected: '2026-11-03'
category: Training
direction: 大模型预训练 · 固定数据算力优化
tags:
- Scaling Laws
- Multi-Epoch Training
- Model Ensemble
- Overfitting
- DMFT
one_liner: 推导多轮SGD动态平均场理论，证明固定数据下集成优于单模型缩放
practical_value: '- 业务训练数据有限时（如新类目推荐、小样本场景finetune），优先采用小模型集成而非单大模型缩放，相同算力下可降低0.12~0.20
  nats的预测损失

  - 多轮训练时动态调整最优停止轮次：模型越大最优epoch越少，170M参数模型最优epoch约为6，避免后期过拟合导致推荐/生成效果衰减

  - 集成训练可适当延长训练时长：集成规模每提升1倍，最优停止epoch可提升约27%，充分挖掘固定训练数据的价值

  - 固定数据下的算力分配规则：集成规模的算力占比应不低于单模型训练时长的算力占比，最大化投入产出比'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大模型预训练即将进入高质量数据耗尽的约束阶段，传统Chinchilla缩放定律仅适配单轮训练场景，多轮数据复用带来的训练后期过拟合问题缺乏成熟理论指导，模型集成的收益量化与算力分配规则也无明确落地依据。
### 方法关键点
- 推导适配多轮SGD的动态平均场理论（DMFT），建模跨epoch、跨模型的误差相关性，量化过拟合的动态演化规律
- 提出固定数据下的算力分配定律，明确集成规模、单模型训练时长的最优配比关系
- 验证logit平均机制可抵消模型预测方差带来的后期误差增长，有效延迟最优停止时间
### 关键实验结果
在FineWeb数据集上训练11M~680M参数的Decoder-only Transformer，对比单模型缩放与集成方案：① 相同算力下，4个基础模型的集成比2倍宽度的单模型损失低0.16 nats；② 集成规模每提升1倍，最优停止epoch提升约27%；③ 模型大小每提升10倍，最优epoch降低约2.1倍，数据量每提升10倍最优epoch仅降低1.4倍。
### 最值得记住的结论
固定训练数据约束下，算力投入优先分配给小模型集成而非单模型缩放，可获得更优的泛化效果。
