---
title: 'Beyond Successor Accuracy: State Retention for Recursive Self-Improvement
  in Recommendation'
title_zh: 超越后继准确率：推荐系统递归自改进的状态保留方法
authors:
- Jinfeng Xu
- Zheyu Chen
- Ziyue Peng
- Zheng Lin
- Wenhao Yuan
- Jian Chen
- Shujie Li
- Edith Ngai
affiliations:
- The University of Hong Kong
- The Hong Kong Polytechnic University
- The Hong Kong University of Science and Technology
- University of Luxembourg
arxiv_id: '2610.07105'
url: https://arxiv.org/abs/2610.07105
pdf_url: https://arxiv.org/pdf/2610.07105
published: '2026-10-05'
collected: '2026-10-07'
category: RecSys
direction: 推荐系统 · 递归自改进机制
tags:
- Sequential Recommendation
- Recursive Self-Improvement
- State Retention
- Model Fusion
- Knowledge Distillation
one_liner: 提出跨代优势指标量化分布式进步，用无标签秩分离指标选择递归自改进推荐的最优状态保留策略
practical_value: '- 搭建自迭代推荐系统时，不要盲目替换为新训的后继模型，可尝试新旧模型对数概率等权融合，GRU4Rec、SASRec场景下实测NDCG@20最高提升1e-3量级，成本仅多1次前向计算

  - 无标签选择跨代/同代融合策略时，可直接用top20推荐列表的秩分离度Sep20做判断指标，无需下游反馈标签，12个测试场景下选择准确率达100%

  - 现有5种单模型知识蒸馏（数据重训、排序蒸馏、参数插值等）均无法稳定复现跨代融合的增益，追求极致效果的场景可优先保留轻量双模型融合架构，而非硬蒸馏到单模型'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐系统递归自改进（Rec-RSI）会把模型输出作为后续训练的监督信号，现有方案默认仅保留最新的后继模型即可继承全部改进效果，但实测新旧模型往往存在互补的排序能力，仅用新模型会丢失旧模型的有效行为，分布式进步的量化与保留是未被解决的核心问题。

### 方法关键点
- 定义跨代优势（CGA）：在边际曝光匹配、推理成本相同的前提下，对比跨代模型融合组与同代模型融合组的排序效用差，正CGA表示跨代融合效果更优
- 提出无标签秩分离指标Sep20：计算同代模型间top20推荐列表的平均重叠率减去跨代模型间的平均重叠率，正Sep20表示跨代排序分歧大于同代种子差异，无需标签即可在选择阶段计算
- 双模型采用对数概率等权融合（β=0.5）生成最终排序

### 关键实验
覆盖Amazon Toys、Beauty、Sports、Yelp4个公开数据集，测试GRU4Rec、SASRec、FMLP3种主流序列推荐编码器：跨代融合在GRU4Rec、SASRec的全部8个数据集场景下效果优于同代融合；Sep20选择最优融合策略在12个首次更新场景准确率100%，二次更新场景准确率5/6；最终选中的融合策略在34/36轨迹上优于直接使用后继单模型，NDCG@20平均提升2.018e-3（相对提升10.6%）；5种主流单模型蒸馏方案均无法稳定复现融合增益。

### 核心结论
递归自改进推荐系统的进步可能存在于多代模型的互补关系中，而非仅存在于最新的单模型里。
