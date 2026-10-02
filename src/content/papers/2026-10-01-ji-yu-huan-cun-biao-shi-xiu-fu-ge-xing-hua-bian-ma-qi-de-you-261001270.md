---
title: 'Not All Is Lost: Repairing Lossy User Preference States of Personalization
  Encoders'
title_zh: 基于缓存表示修复个性化编码器的有损用户偏好状态
authors:
- Parthiv Chatterjee
- Dhiraj Golhar
- Ummesalma Diwan
- Sourish Dasgupta
- Manjunath Joshi
- Tanmoy Chakraborty
affiliations:
- Dhirubhai Ambani University
- Indian Institute of Technology Delhi
arxiv_id: '2610.01270'
url: https://arxiv.org/abs/2610.01270
pdf_url: https://arxiv.org/pdf/2610.01270
published: '2026-10-01'
collected: '2026-10-02'
category: RecSys
direction: 推荐系统 · 用户偏好状态修正
tags:
- Sequential Recommendation
- User Preference Modeling
- Model Editing
- Frozen Model Tuning
- Personalized Generation
one_liner: 冻结编码器与任务头前提下，利用缓存时间步表示修复压缩后的用户偏好状态提升推荐性能
practical_value: '- 已上线的推荐模型不需要改动原编码器和排序头，插入REPAIR模块即可复用原有推理产生的缓存中间表示提效，大幅降低迭代成本

  - 修正模块选择K=128的低秩空间即可达到最优效果，兼顾效果和性能，仅带来30%左右的参数和40%以内的latency开销

  - 偏好修正优先做编码器输出后、任务头前的预头状态修正，比后处理修正排序输出的收益更高

  - 个性化生成场景下，不要仅看ROUGE等通用生成指标，需搭配PerSEval类的个性化感知指标评估实际业务价值'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有个性化编码器会将用户长序列交互历史压缩成低维偏好状态输入下游任务头，压缩过程中丢失的有用偏好信息无法被下游利用，而改动已上线的成熟编码器重训、验证成本极高，亟需不需要修改原模型参数的偏好状态优化方案。

### 方法关键点
- 提出REPAIR轻量模块插在编码器与任务头之间，复用编码器推理时缓存的每步交互表示，不需要重编码用户历史或修改原模型任何参数
- 将压缩后的偏好状态和缓存时间步表示映射到共同的低秩修正空间（默认K=128），计算相对偏差作为修正信号
- 设计长时、短时、突发三类时间视角的权重函数，聚合不同时间跨度的修正信号，选通高价值修正项后残差叠加到原偏好状态上

### 关键结果
- 覆盖4类场景数据集：MovieLens（电影推荐）、MIND/PENS（新闻推荐）、Amazon Reviews 2023（电商商品推荐），验证12种主流推荐编码器
- 对比原模型、仅任务头微调基线，REPAIR在编码器+任务头全冻结时，平均MRR提升1.96~2.66，远高于仅任务头微调的0.29~0.76；Mamba4Rec在MovieLens上MRR提升3.96，是仅任务头微调提升量的20倍
- 个性化生成场景下，PerSEval个性化指标最高提升25.23%，而ROUGE等通用生成指标变化很小

**最值得记住的一句话**：已训练完成的个性化编码器压缩丢失的偏好信息，大部分仍保留在推理过程的缓存中间表示中，可通过极低成本的修正模块挖掘提效，不需要改动原模型
