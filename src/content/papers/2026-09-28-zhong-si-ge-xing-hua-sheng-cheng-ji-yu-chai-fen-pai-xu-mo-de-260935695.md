---
title: 'Rethinking Personalized Generation: Test-Time Alignment via Factorized Ranking
  Models'
title_zh: 重思个性化生成：基于拆分排序模型的测试时对齐
authors:
- Qiyao Ma
- Junshan Zhang
- Zhe Zhao
affiliations:
- University of California, Davis
arxiv_id: '2609.35695'
url: https://arxiv.org/abs/2609.35695
pdf_url: https://arxiv.org/pdf/2609.35695
published: '2026-09-28'
collected: '2026-09-29'
category: GenRec
direction: 生成式推荐 · 测试时个性化对齐
tags:
- Test-time Alignment
- Personalized Generation
- Lightweight Ranking
- LLM4Rec
- Efficient Inference
one_liner: 复用LLM生成器隐状态训练百万参数MLP排序模型，低成本实现个性化生成测试时对齐
practical_value: '- 电商个性化推荐理由、商品文案生成场景可直接复用该范式：无需微调基座LLM，仅复用其隐状态训练百万级参数MLP做Best-of-N选点，效果优于8B级通用Reward
  Model，成本可忽略

  - 训练优化可直接复用两个trick：一是用基座生成的同分布候选做硬负例，二是优先选pointwise MSE损失，训练效率比pairwise/listwise高，效果差距不超过0.012
  ROUGE-L

  - 低延迟场景可搭配引导解码方案：仅在LLM生成token的熵超过阈值时用排序模型干预，单趟生成即可获得Best-of-2~4的效果，平衡性能与推理耗时'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有RLHF等对齐范式面向全局统一偏好优化，会抹平用户个性化差异；主流方案将个性化不足归因为生成器能力缺陷，依赖训练时微调/per-user适配，成本极高。此外通用大参数Reward Model做Best-of-N选点时校准差、延迟高，仅能捕捉不到23%的个性化增益空间，大量基座已经生成的优质个性化候选无法被有效筛选。
### 方法关键点
- 拆分语言理解与偏好打分环节：直接复用生成器最后一层隐状态（query、用户profile、候选回复的最后token隐态拼接）作为特征，训练1M~30M参数的轻量MLP做个性化排序，无需重新编码文本，无额外用户参数
- 训练策略：用基座生成的候选集做硬负例，以候选与用户真实参考的ROUGE-L为监督做pointwise MSE回归，对每个候选池内的目标做标准化，提升同池排序区分度
- 支持两种推理模式：Best-of-N选点（打分延迟比8B Reward Model低4个数量级）、引导解码（仅在生成token熵超过阈值时干预，单趟生成即可获得部分增益）
### 关键实验
覆盖9个数据集，包含3类个性化生成场景（短文本生成、长文本个性化QA、可解释推荐），对比4个SOTA 8B通用Reward Model、微调后的8B Reward Model。核心结果：1M参数MLP排序模型在所有数据集上效果超过8B通用Reward Model，仅为后者参数的0.4%，打分latency低4个数量级；30M参数模型可恢复微调后8B Reward Model 45%~94%的增益；引导解码可达到Best-of-2~4的效果。

**最值得记住的一句话**：个性化生成的瓶颈往往不是基座LLM的生成能力，而是低成本筛选符合用户偏好候选的能力
