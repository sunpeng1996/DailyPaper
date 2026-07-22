---
title: 'ISO: An RLVR-Native Optimization Stack'
title_zh: ISO：面向可验证奖励强化学习（RLVR）的原生优化栈
authors:
- Hanqing Zhu
- Wenyan Cong
- Zhizhou Sha
- Sagnik Mukherjee
- Xinyuan Song
- David González-Martínez
- Xiaoxia Wu
- Yuandong Tian
- Shiwei Liu
- David Z. Pan
affiliations:
- The University of Texas at Austin
- UIUC
- Emory University
- Together AI
- ELLIS Institute Tübingen
arxiv_id: '2607.19331'
url: https://arxiv.org/abs/2607.19331
pdf_url: https://arxiv.org/pdf/2607.19331
published: '2026-07-21'
collected: '2026-07-22'
category: Training
direction: RLVR训练优化 · 固定频谱优化
tags:
- RLVR
- LLM Training
- Optimization
- Model Merging
- SVD
one_liner: 发现RLVR频谱继承特性，提出固定频谱优化栈ISO，加速训练并实现无数据专家合并
practical_value: '- 电商导购Agent、内容推荐大模型的RLHF/RLVR对齐阶段，可复用ISO的固定频谱优化思路，仅优化奇异帧U/V矩阵，训练步数可减少2~2.7倍，大幅降低对齐算力成本，不损失效果

  - 同底座的多场景LLM专家合并（比如电商场景下搜索、推荐、客服、合规4个专精模型合并），可直接用ISO-Merger无数据合并方案，无需额外标注、蒸馏或rollout，比现有基线合并效果高0.8~1个百分点

  - 低算力场景下的RL阶段迭代，可优先尝试冻结预训练频谱仅优化帧的参数化方式，相比全参数更新优化空间更小，收敛更快，适合快速验证策略效果'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RLVR（可验证奖励强化学习）是当前大模型推理、Agent能力提升的核心路径，但现有RLVR的优化层直接继承预训练的优化器与参数化方式，适配性极差：预训练基于稠密token级监督，RLVR仅用稀疏结果级奖励更新，两者的参数更新逻辑存在本质差异，长期缺少RLVR原生的优化框架。
### 方法关键点
- 明确RLVR的**频谱继承特性**：RLVR训练时模型权重的奇异值（频谱）几乎无漂移，仅输入、输出奇异帧（U/V矩阵）发生变化；仅调整帧即可获得几乎全部性能增益，仅调整频谱则增益可忽略。
- 推出ISO优化栈，包含两个互补组件：
  1. 离线ISO-Merger：合并同底座的多个RL专精专家，复用共享底座频谱，仅合并各专家的帧变化，无需后处理数据、rollout、梯度更新或蒸馏。
  2. 在线ISO-Optimizer：RL训练时固定底座频谱，用常规优化器（AdamW、Muon等）仅优化奇异帧，每次更新后通过极因子收缩保证U/V的正交约束。
### 关键结果
- 专家合并：Qwen2.5-7B底座合并3个RL专家，ISO-Merger平均得分63.80，超最优基线0.92；1.5B底座合并2个专家，平均得分44.38，超最优基线0.87。
- 在线训练：Qwen3-8B数学推理RL训练中，ISO-AdamW达到AdamW同等0.495精度仅需100步，训练步数减少2.7倍，210步达到0.509精度超基线。
- 开销：帧收缩的额外计算仅占端到端RL训练步时的7%，可与rollout生成并行，开销可控。

> 最值得记住的结论：RLVR阶段无需修改预训练模型的频谱，仅优化奇异帧即可实现更优收敛效率与专家合并效果，核心原则为「继承频谱，优化帧」
