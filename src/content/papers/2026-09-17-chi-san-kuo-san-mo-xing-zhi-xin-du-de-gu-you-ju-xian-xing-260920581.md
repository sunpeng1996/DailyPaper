---
title: Limits of Confidence in Diffusion
title_zh: 《离散扩散模型置信度的固有局限性》
authors:
- Russ Webb
- Amitis Shidani
- Alice Bizeul
- Dan Busbridge
affiliations:
- Apple
arxiv_id: '2609.20581'
url: https://arxiv.org/abs/2609.20581
pdf_url: https://arxiv.org/pdf/2609.20581
published: '2026-09-17'
collected: '2026-09-19'
category: Other
direction: 离散扩散采样 · 分布偏移理论分析
tags:
- Discrete Diffusion
- Distribution Shift
- Sampling
- Token Dependency
- Total Variation
one_liner: 证明离散扩散单步多token生成因token依赖产生分布偏移，且单样本指标无法识别该偏差
practical_value: '- 用离散扩散做生成式推荐文案、item Semantic ID生成时，不能仅用单样本相关性、通顺度做验收，需补充整体分布一致性校验，避免样本多样性不足或重复

  - 做扩散生成加速时，单步并行生成多个token的策略需先校验目标token组的条件独立性，不可直接用逐位置置信度选生成位置

  - 若用扩散模型做用户行为序列补全、召回候选生成，需引入联合分布校验逻辑，避免隐性分布偏移导致的推荐效果衰减'
score: 4
source: arxiv-cs.AI
depth: abstract
---

### 动机
离散扩散模型通过单步生成多个token实现采样加速，现有方案依赖逐位置分布选择生成位置与内容，未考虑token间固有依赖，且常规单样本评估指标无法检测潜在分布偏差。
### 方法关键点
1. 理论证明：仅当单步生成的所有位置在已固定token条件下独立时，生成分布才能匹配训练分布；逐位置分布乘积无法拟合存在依赖的token组联合分布，且逐位置边缘分布无法反映组间依赖关系。
2. 在可闭式计算联合分布的合成任务ScanAndAdd上验证理论结论，对比生成分布与真实分布的差异。
### 关键结果
生成分布与真实分布的总变异是采样噪声底限的29×，但单样本指标可达1.0，完全无法检测该分布偏移。
