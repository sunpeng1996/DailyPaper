---
title: 'Generate What You Can Trust: Content Credibility in Generative Recommenders'
title_zh: 生成可信内容：生成式推荐系统的内容可信度优化
authors:
- Zhuo Cai
- Guanghao Wu
- Shoujin Wang
- Peilin Zhou
- Victor W. Chu
affiliations:
- University of Technology Sydney
- New York University Abu Dhabi
arxiv_id: '2610.05670'
url: https://arxiv.org/abs/2610.05670
pdf_url: https://arxiv.org/pdf/2610.05670
published: '2026-10-05'
collected: '2026-10-06'
category: GenRec
direction: 生成式推荐 · 内容可信度优化
tags:
- Generative Recommendation
- Semantic ID
- Content Credibility
- Discrete Diffusion
- RQ-VAE
one_liner: 首个在生成式推荐全流程优化内容可信度的方案，兼顾推荐准确率与可信度
practical_value: '- 做资讯、健康、知识付费、二类电商等强合规场景的生成式推荐，可直接复用可信度感知tokenizer设计：在现有Semantic
  ID生成的RQ-VAE流程中加入可信度正则项，无需改动整体架构即可实现可信/不可信内容的token级分离，避免后过滤易被对抗样本绕过的问题

  - 生成阶段的非对称掩码概率优化思路可迁移到低质/违规内容抑制场景：仅降低对应内容细粒度token的掩码权重，保留编码用户偏好的粗粒度语义token不受影响，比直接删除训练数据的准确率掉点低80%以上

  - 可根据业务监管要求选择两种加权策略：强管制内容用hard加权直接清零不可信token贡献，弱管制内容用soft加权按可信度分数动态降权，适配不同场景的平衡需求

  - 无全量可信度标注的业务可复用其抗噪结论：15%以内的标签噪声下，CR@5仅下降不到1个百分点，可配合LLM自动打弱标签使用，无需完全依赖人工标注'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐（GR）以Semantic ID生成替代传统嵌入匹配，性能优异但仅优化准确率，完全忽略内容可信度，易向用户推送假新闻、虚假宣传内容，带来用户信任流失、平台合规风险。现有可信推荐均基于传统匹配范式，和GR的直接生成架构不兼容，且后过滤方式治标不治本，容易被对抗样本绕过。

### 方法关键点
- 可信度感知tokenizer：在RQ-VAE的item token化流程中新增可信度正则项，强制可信/不可信item的token实现类内紧凑、类间分离，从token源头解决可信度特征纠缠问题，同时融合内容语义+协同过滤特征降低token碰撞率
- 保准确率的可信度导向生成器：基于离散扩散架构，利用RQ-VAE前几层存主题偏好、最后一层存细粒度可信度特征的特性，设计非对称掩码策略：仅降低不可信item最后一层token的掩码概率，其余token保持原权重，既抑制不可信内容生成，又不损失用户偏好匹配准确率
- 适配两种业务场景的加权实现：hard策略直接清零不可信item最后一层token贡献，适合强监管场景；soft策略按token到可信/不可信簇中心的距离动态分配权重，平衡效果更平滑

### 关键结果
在3个公开带可信度标签的数据集（PolitiFact新闻、GossipCop娱乐新闻、MHMisinfo健康内容）上对比12个SOTA基线：CR@5（推荐列表可信率）最高比基线提升10.7pct，NDCG@5仅损失不到0.4pct，HC@5（准确率+可信度综合指标）最高领先基线2.2pct，token碰撞率降至0%~0.1%，推理耗时和原生生成式推荐几乎一致，15%标签噪声下CR@5仅下降0.75pct。

**最值得记住的一句话**：生成式推荐的可信度优化不需要牺牲准确率，仅通过token级的特征分离和细粒度掩码控制即可实现效果平衡，远优于直接删数据或后过滤方案。
