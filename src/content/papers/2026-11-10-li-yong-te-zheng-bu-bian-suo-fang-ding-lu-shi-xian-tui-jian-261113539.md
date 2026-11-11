---
title: Exploiting Feature-invariant Scaling Laws for Efficient A/B Experimentation
  in Recommendation Systems
title_zh: 利用特征不变缩放定律实现推荐系统高效A/B实验
authors:
- Zhiliang Chen
- Sammy Nammari
- Jiahao Su
- Xiaoqiang Luo
affiliations:
- Meta
- National University of Singapore
arxiv_id: '2611.13539'
url: https://arxiv.org/abs/2611.13539
pdf_url: https://arxiv.org/pdf/2611.13539
published: '2026-11-10'
collected: '2026-11-11'
category: RecSys
direction: 推荐系统 · 低算力A/B实验优化
tags:
- Scaling Law
- A-B Testing
- Recommender System
- LLM4Rec
- Efficient Evaluation
one_liner: 通过多组小尺度实验拟合特征不变缩放定律，预测推荐算法全量效果，大幅降低A/B实验算力成本
practical_value: '- 新特征/模型迭代时无需直接跑全量训练，可跑0.1~0.5尺度的多组小实验，用幂律拟合预测全量效果，相比全量训练节省45%左右算力

  - 可自定义决策阈值，例如要求新特征全量降损≥1%的概率超过90%才进入下一阶段，快速过滤无效迭代，避免被小尺度反向信号误导

  - 方法对传统CTR模型、序列推荐模型、LLM-based推荐模型均适用，可扩展到HR@10、AUC等业务指标的预测，无需局限于验证损失

  - 小尺度实验建议同时缩放模型参数量和训练数据量，比单独缩数据更省GPU显存，适合大模型迭代时显存不足的场景'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐系统迭代新特征、模型结构、优化器时，全量A/B实验算力成本极高，单组小尺度实验结果经常出现信号反转（比如小尺度效果差但全量效果好，反之亦然），容易误筛有效迭代，亟需低成本、高可靠的实验效果预判方法。

### 方法关键点
- 推荐模型存在特征不变缩放定律：不同特征改动后的模型，性能随训练尺度（模型参数量×训练数据量）的变化符合同一幂律函数族，仅系数不同，拟合R²普遍≥0.98
- 仅需训练0.1~0.5尺度的多组小模型，通过线性回归拟合幂律参数，结合统计推断预测全量尺度的性能分布及置信区间，计算新特征优于基线的概率
- 支持自定义决策阈值，可要求新特征全量降损≥指定比例的概率大于阈值才进入全量验证，适配业务收益要求

### 关键实验结果
在Wukong（CTR预测）、HSTU（序列推荐）、LLaMA-3.1/Qwen（LLM4Rec）三类模型，共40+种特征改动上验证：仅用不到全量55%的算力，就能准确区分有效/无效特征，预测全量性能的误差随小尺度实验数量增加持续下降；用该方法筛选出多个HSTU的优化点，在MovieLens-20M上HR@10最高提升1.01%，刷新SOTA；对LLM4Rec的HR@10等业务指标也能稳定拟合缩放定律，适用场景覆盖传统推荐到生成式推荐。

### 核心结论
小尺度单组实验的信号极不可靠，利用特征不变的缩放规律做多尺度外推，是平衡推荐迭代效率和准确率的最优路径之一
