---
title: 'UniPolicy: Unified Objective-Specific Policies for Generative Search Advertising'
title_zh: UniPolicy：面向生成式搜索广告的统一目标专属多策略框架
authors:
- Kun Yao
- Yuhang Zhou
- Yichi Zhang
- Zeliang Tong
- Shengri Xue
- Haitao Wang
- Siyu Lu
- Qianlong Xie
- Xingxing Wang
affiliations:
- Meituan, Beijing, China
arxiv_id: '2609.20630'
url: https://arxiv.org/abs/2609.20630
pdf_url: https://arxiv.org/pdf/2609.20630
published: '2026-09-17'
collected: '2026-09-18'
category: GenRec
direction: 生成式推荐 · 多目标策略对齐
tags:
- Generative Recommendation
- Search Advertising
- MoE-LoRA
- Multi-Objective Optimization
- Preference Alignment
one_liner: 基于目标感知参数解耦与多阶段行为建模的生成式搜索广告多目标对齐框架，工业落地增益显著
practical_value: '- 多目标生成式检索/推荐场景可复用「目标前缀+MoE-LoRA+目标专属FFN」的参数解耦架构，无需维护多套模型，仅用轻量增量参数即可规避多目标梯度竞争问题

  - 训练侧可复用点击>曝光>未命中的行为漏斗成对偏好损失做辅助监督，无需额外标注即可提升生成候选的排序准确性，缓解仅用点击正样本的信息不足问题

  - 推理侧可复用共享KV cache+多目标并行beam search+动态配额分配机制，在固定候选预算下灵活平衡多业务目标，额外latency开销可控（实测P99仅涨2.5%）

  - 无需强行做多奖励加权融合，改为多策略独立优化后在推理层合并候选，可规避奖励融合的权重调优难题与单一目标偏好压制问题'
score: 10
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前生成式搜索广告的多目标优化存在三类痛点：单目标对齐（如仅优化eCPM）易损伤用户体验，简单加权融合奖励易出现梯度竞争导致弱目标信号被淹没，仅依赖点击正样本训练浪费大量曝光未点击等行为信号，推理时单策略beam search无法灵活分配候选配额，平衡用户体验与平台收益难度大。

### 方法关键点
- 目标感知多策略对齐：输入加入目标专属可训练前缀token，结合稀疏MoE-LoRA路由+顶层目标专属残差FFN，共享生成主干的同时为eCPM/CTR/相关性三类目标提供独立参数空间，各目标独立做GRPO强化学习对齐，避免梯度干扰
- 多阶段行为偏好优化：基于点击>曝光>未命中的行为漏斗构建带边际的成对偏好损失，补充仅点击监督缺失的相对排序信号，强化高价值候选的生成优先级
- 高效灵活推理：共享请求的KV cache，并行执行多目标beam search，按业务需求灵活分配各策略的候选配额，通过剪枝-回填机制保证固定候选预算下的候选质量，控制推理开销

### 关键结果
基于美团亿级搜索广告日志训练，对比单目标GRPO、奖励融合GRPO、MOPD等基线，离线NDCG@10最优，所有业务指标均超过对应单目标基线；7天线上A/B测试，CTR提升0.71%，RPS提升1.58%，广告收入提升1.32%，P99 latency仅上涨2.5%。

### 最值得记住的一句话
生成式广告/推荐的多目标优化，无需强行把多目标压缩到同一参数空间或奖励空间，改为参数侧解耦多策略、推理侧合并候选，是兼顾效果、灵活性与落地成本的可行工业路径。
