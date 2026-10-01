---
title: 'When the Label Ignores the Request: Auditing Policy-Selected Targets in Synthetic
  Conversational Music Recommendation'
title_zh: 合成对话音乐推荐基准中策略标签与用户请求的冲突审计及修复
authors:
- Sanjeev Suresh
affiliations:
- Independent Researcher, San Francisco, USA
arxiv_id: '2609.39696'
url: https://arxiv.org/abs/2609.39696
pdf_url: https://arxiv.org/pdf/2609.39696
published: '2026-09-30'
collected: '2026-10-01'
category: RecSys
direction: 对话式推荐 · 基准标签质量优化
tags:
- conversational_recommendation
- label_quality
- synthetic_benchmark
- music_recommendation
- behavioral_evaluation
one_liner: 审计RecSys2026音乐推荐基准的标签冲突，提出低成本训练增强方案修复且不损失官方指标
practical_value: '- 构建合成推荐数据集时，可增加显式指令校验环节，通过规则/轻量LLM检测标签与用户明确请求的一致性，避免训练模型学到错误的指令忽略行为

  - 针对用户显式指定物品的高优意图（如电商搜具体货号、音乐搜歌名、内容平台搜特定视频），可采用小样本补充训练的方式增强，仅用1.5%的训练样本即可获得50%+的相对指标提升，且不影响全局指标

  - 推荐系统评估不能仅关注全局NDCG等聚合指标，需针对高优意图单独做切片评估，这类请求占比低但直接决定用户对系统的信任度

  - 训练时对修正样本采用降权补充、保留原标签的方案，既能修正错误监督信号，又不会破坏原有数据集的分布一致性，避免全局指标劣化'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前合成对话推荐基准普遍采用LLM交互生成的 policy-selected 标签，仅记录生成策略输出的下一个物品，而非用户显式请求的内容。这类标签冲突在模糊请求下难以校验，但用户显式指定物品的意图占真实音乐搜索请求的80%以上，标签冲突会导致模型学到忽略用户指令的错误行为，严重损害用户信任与产品体验，且这类错误会被全局聚合指标完全掩盖。

### 方法关键点
- 构建确定性精确请求检测器：通过正则匹配用户query中的歌名指令+catalog元数据校验，仅在无歧义匹配时标记样本，保障检测精度
- 低侵入训练增强：仅对标签与请求冲突的样本补充请求对应目标，保留原有官方标签，将该类样本组权重降为0.1，仅占总训练样本的1.5%，不破坏原有数据分布
- 严格对照实验设计：对照组除训练标签外，特征、模型结构、训练流程完全一致，排除特征暴露导致的指标提升干扰

### 关键结果
实验基于RecSys Challenge 2026 TalkPlay基准开发集：
1. 开发集82个精确歌曲请求中，41个官方标签与用户请求冲突，冲突率达50%
2. 增强后冲突切片nDCG@20从0.523提升至0.802，相对提升53.3%
3. 全局官方nDCG@20仅波动+0.31%，完全符合预设的指标保留要求，无负向影响

### 核心结论
推荐系统的聚合指标会掩盖占比极低但对用户体验至关重要的高优意图错误，针对显式指令类请求的单独审计和增强是ROI极高的优化手段
