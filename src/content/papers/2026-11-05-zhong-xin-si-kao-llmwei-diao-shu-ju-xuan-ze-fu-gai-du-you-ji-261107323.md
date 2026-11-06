---
title: 'Rethinking Data Selection: The Importance of Coverage over Difficulty in LLM
  Fine-Tuning'
title_zh: 重新思考LLM微调数据选择：覆盖度优先级高于难度
authors:
- Lalchand Pandia
- Kanishka Misra
- Allyson Ettinger
affiliations:
- University of Chicago
- The University of Texas at Austin
- Allen Institute for Artificial Intelligence
arxiv_id: '2611.07323'
url: https://arxiv.org/abs/2611.07323
pdf_url: https://arxiv.org/pdf/2611.07323
published: '2026-11-05'
collected: '2026-11-06'
category: Training
direction: LLM微调 · 训练数据选择优化
tags:
- LLM
- Fine-tuning
- Data Selection
- Clustering
- Coverage
one_liner: 验证LLM微调中难度导向数据选择效果弱于随机采样，提出覆盖度优先的聚类式选择方法
practical_value: '- 做电商/推荐场景的LLM微调（商品文案生成、query理解、Agent意图识别等）时，不要盲目采用难度优先的数据筛选策略，优先保证数据覆盖度的效果至少不差于随机采样

  - 多领域混合微调数据（覆盖电商搜索、推荐、客服多场景的SFT数据）场景下，可直接复用论文提出的聚类覆盖度选择方法：用目标LLM最后一层隐层向量做k-means聚类，每个簇采样1条数据，仅用5%数据就能达到甚至超过全量微调效果，大幅降低训练成本

  - 单领域微调数据场景下，直接随机采样即可获得和复杂筛选方法相当的效果，不需要额外投入工程资源做难度打分、复杂数据筛选流程

  - 数据筛选的计算成本要纳入ROI考量：难度类筛选方法往往需要预跑全量训练多轮，而覆盖度方法仅需一次前向传播，性价比更高'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有基于难度的数据选择方法在小分类模型上表现优异，但迁移到LLM微调场景时效果经常不如随机采样，核心原因是难度优先的筛选逻辑会导致数据覆盖度不足，无法支撑LLM的泛化能力要求；而降低微调数据量是控制大模型训练成本的核心路径，因此亟需明确LLM微调数据选择的核心优先级准则。

### 方法关键点
1. 复现5种主流难度打分方法（Perplexity、Confidence、Variability、VoG、PVI）并适配到LLM微调场景，统一和随机采样做对比；
2. 以目标LLM最后一层隐层向量为基础做k-means聚类，用全量数据和筛选子集的聚类分布JSD作为覆盖度量化指标，验证覆盖度和微调效果的强相关性；
3. 提出极简覆盖度选择方法：聚类后每个簇采样1条数据，保证筛选子集和全量数据的分布一致性。

### 关键结果
单域数据集（Social IQa、CommonsenseQA、CosmosQA）上，随机采样效果超过所有难度类方法，和覆盖度方法持平；多域混合数据集Tülu 3上，覆盖度方法仅用5%数据就在MMLU上达到62.6%（超过全量微调的62.2%），HumanEval上25%数据达到40.2%，显著优于随机采样和难度类方法。

**最值得记住的一句话**：LLM微调数据选择时优先保证数据覆盖度，难度导向的筛选策略性价比极低。
