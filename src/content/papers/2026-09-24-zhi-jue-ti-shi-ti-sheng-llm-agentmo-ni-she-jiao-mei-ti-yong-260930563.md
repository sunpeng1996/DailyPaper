---
title: 'Thinking Less to Simulate Better: Intuitive Prompting Improves LLM Agents
  Simulating Individual Social Media Reactions, Including Unfamiliar Content'
title_zh: 直觉提示提升LLM Agent模拟社交媒体用户反应的保真度及泛化能力
authors:
- Ljubisa Bojic
- Tijana Stanic
- Joerg Matthes
- Agariadne Dwinggo Samala
- Bojana Dinic
- Jue Wang
affiliations:
- 塞尔维亚人工智能研发研究所
- 贝尔格莱德大学
- 维也纳大学
- 巴东国立大学
- 诺维萨德大学
arxiv_id: '2609.30563'
url: https://arxiv.org/abs/2609.30563
pdf_url: https://arxiv.org/pdf/2609.30563
published: '2026-09-24'
collected: '2026-09-28'
category: Agent
direction: Agent 用户行为模拟 · Prompt优化
tags:
- LLM Agent
- Prompt Engineering
- User Simulation
- Fidelity Optimization
- Generalization
one_liner: 通过直觉式prompt替代推理指令，大幅提升LLM Agent模拟真实用户社交媒体反应的保真度与泛化性
practical_value: '- 做用户行为模拟类Agent（如电商用户评论预测、新商品偏好预判）时，可直接复用「直觉响应、无需分析推理、允许和画像存在一定偏离」的prompt模板，无需额外成本即可提升保真度，同时降低个体差异压缩率

  - 构建用户画像时，若需要Agent处理陌生类目/场景的用户反应，除结构化属性外补充访谈、自我陈述等非结构化叙事内容，可提升跨领域泛化能力，适合解决推荐系统冷启动问题

  - 评估用户模拟类Agent时，不要盲目追求“和给定画像100%一致”，真实人类的态度-行为匹配度约为70%，显著高于该阈值的Agent说明存在机械查表问题，模拟失真'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前平台政策、推荐算法测试大量依赖模拟用户，现有LLM Agent模拟普遍存在两个核心问题：一是仅用人口属性构建画像导致保真度极低，二是要求模型推理决策会严重压缩个体差异，且对陌生内容的泛化能力不足；同时现有评估只关注和人类行为的匹配度，忽略了“和给定画像一致性过高反而不符合真实人类行为规律”的问题。

### 方法关键点
- 招募8名塞尔维亚用户，通过结构化问卷、深度访谈、自我陈述构建分层画像，采集用户对68条社交媒体帖子（34条匹配问卷主题、34条为陌生主题）的点赞/点踩真实反应作为ground truth
- 测试4款主流LLM（Claude Sonnet 5、DeepSeek Instant、GPT 5.6 Terra、Grok Fast），设置5组对照prompt：仅人口属性、仅结构化问卷、问卷+访谈文本、问卷+访谈+要求推理决策、问卷+访谈+要求直觉响应
- 核心评估指标：MCC（保真度）、画像一致性、个体差异压缩率

### 关键结果数字
- 直觉提示组平均MCC达0.473，比推理组高0.039，比仅人口属性组高0.173，个体差异压缩率从7倍降至3倍
- 陌生内容场景下，直觉提示组MCC达0.399，远超crowd baseline的0.265，比仅用结构化问卷组高0.075
- 传统监督模型（随机森林）在同数据集下MCC仅0.302，远低于所有带态度画像的LLM Agent
- 真实用户的自身画像一致性仅71.3%，仅用结构化问卷的Agent一致性可达90.4%，画像一致性高于阈值后和保真度呈负相关

**最值得记住的一句话：对于模拟人类快速直觉决策的任务，要求LLM增加推理反而会降低保真度，匹配人类决策模式的prompt增益远大于增加画像信息的增益**
