---
title: 'CROP: Task Relevance via Counterfactuals for Selective On-Policy Distillation'
title_zh: CROP：基于反事实任务相关性的选择性在策略蒸馏方法
authors:
- Enhan Li
- Junhao He
- Hongyang Du
affiliations:
- The University of Hong Kong
arxiv_id: '2608.13387'
url: https://arxiv.org/abs/2608.13387
pdf_url: https://arxiv.org/pdf/2608.13387
published: '2026-08-13'
collected: '2026-08-14'
category: Training
direction: 大模型训练 · 在策略蒸馏优化
tags:
- On-Policy Distillation
- Counterfactual Reasoning
- Token Selection
- Knowledge Distillation
- LLM Training
one_liner: 通过释义校准的反事实敏感度衡量token任务相关性，优化选择性在策略蒸馏的监督资源分配
practical_value: '- 做LLM/生成式推荐的SFT、蒸馏时，可复用CROP的三元组构造逻辑，识别与用户query语义强相关的输出token，将有限监督预算集中在高价值位置，降低训练成本同时提升输出相关性

  - 电商Agent的指令遵循、工具调用微调场景下，可借鉴该token选择策略，过滤通用客套话术、格式符号等无关token的监督信号，提升Agent对用户核心需求的响应准确率

  - 优化蒸馏的token选择策略时，可将任务相关性得分与传统的不确定性、师生差异等特征做融合，补充现有选择维度的盲区，进一步提升蒸馏效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有选择性在策略蒸馏（OPD）仅基于不确定性、师生差异等**优化需求**维度分配监督资源，忽略token的**任务相关性**维度——即监督信号是否与当前输入语义绑定，导致算力浪费在通用回复token上，高价值的任务相关token反而监督不足。

### 方法关键点
1. 离线构造每个prompt的「原句-语义保留释义-单条件改变反事实」三元组，通过LLM生成+独立校验保证三元组有效性，本次验证通过率达95.38%
2. 固定学生模型生成的响应序列，分别在三个prompt下重打分每个位置的token分布，用Top-K JSD计算反事实敏感度和释义敏感度
3. 任务相关性得分=反事实敏感度-释义敏感度，按固定监督token预算全局选择得分最高的token，仅对这些token计算OPD损失
4. 可选CROP-ent变体结合学生熵和相关性得分，补充优化需求维度的信号

### 关键实验
基于DAPO-Math-17K数据集构造16594个有效三元组，在Qwen3-4B→1.7B、Qwen3-8B GRPO→4B两个师生蒸馏场景下，对比纯OPD、Entropy、TIP、TA-OPD等基线；10%监督token预算下，CROP比最强非CROP基线分别高1.92、2.96分，比纯OPD分别高3.11、1.88分。

### 核心结论
token的监督价值同时包含「是否需要优化」和「是否和任务语义相关」两个互补维度，优先监督任务相关的低熵token往往能获得超预期的效果提升
