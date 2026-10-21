---
title: 'HybridResearcher: Bridging the Structured-Unstructured Boundary for Deep Research
  Agents'
title_zh: HybridResearcher：打通结构化-非结构化边界的深度研究Agent框架
authors:
- Soyoung Yoon
- Peiran Xu
- Han Wang
- Ruofan Wu
- Xiaodong Yu
- Feng Yan
- Mohit Bansal
- Debiao Li
- Seung-Won Hwang
- Yuxiong He
affiliations:
- Seoul National University
- University of California, Los Angeles
- University of North Carolina at Chapel Hill
- University of Houston
- Snowflake AI Research
arxiv_id: '2610.24899'
url: https://arxiv.org/abs/2610.24899
pdf_url: https://arxiv.org/pdf/2610.24899
published: '2026-10-16'
collected: '2026-10-21'
category: Agent
direction: Agent 跨异构数据源推理优化
tags:
- LLM-Agent
- Cross-Source-Reasoning
- Synthetic-Data
- SFT
- RL
- Tool-Use
one_liner: 基于严格质控的跨源轨迹合成训练4B小模型，跨结构化/非结构化推理性能超越397B大模型
practical_value: '- 跨源任务数据构造可直接复用防shortcut门控机制：做电商场景「用户行为库+商品舆情/公开信息」跨源任务时，可通过规则校验确保单数据源无法得到答案，避免模型靠参数记忆投机跳过工具调用。

  - 小模型Agent的RL优化方案可落地：RL训练时引入多数投票Judge降低奖励噪声、加硬门控提前惩罚无效/重复工具调用，能显著提升电商导购、运营分析Agent的工具使用效率和准确率。

  - 跨能力训练无灾难性遗忘的经验可参考：给垂直领域Agent叠加跨源推理能力时，原有单源SQL查询、检索能力不仅不会下降，还会因逻辑强化得到小幅提升。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent仅支持单源（结构化数据库/非结构化文本）推理，但真实业务（如电商供应链风险评估、用户行为归因）往往需要同时跨两类数据源获取证据，现有方法即便合并单源训练数据也无法学会跨源依赖，还容易出现shortcut learning（靠参数记忆直接回答，跳过跨源调用），缺乏成熟的跨源Agent训练框架。

### 方法关键点
- 数据合成：从已验证的单源Text2SQL、深度搜索任务种子出发，围绕种子输出的桥接实体构造另一数据源的任务，仅保留通过严格门控的样本（确保单源无法得到答案，必须跨源调用），从根源避免shortcut。
- 训练流程：先基于高质量合成轨迹做SFT，再筛选SFT阶段未解决的难例，经严格质控（难度、质量、分布平衡）后做RL训练；RL阶段引入5票多数投票Judge降低奖励噪声，加硬门控提前终止无效工具调用并给0奖励。

### 关键结果数字
- 跨源基准HybridDeepResearch上，4B参数量的HybridResearcher比底座Qwen3.5-4B提升30.0 pass@8，比同系列397B大模型高8.3 pass@8，接近Claude Sonnet 4.6水平。
- 单源能力不降反升：BrowseComp搜索基准pass@8从54.03%提升到62.24%，Spider 2.0-lite Text2SQL准确率从59.26%提升到62.96%，无灾难性遗忘。
- RL阶段0.7K高质量难例比21K未过滤样本的训练效果高6.2个avg@8，数据质量远重于规模。

**最值得记住的一句话**：训练跨源推理Agent时，明确教跨源依赖的桥接逻辑，比单纯合并单源训练数据、堆数据规模的效果好得多，小模型也能超过大几十倍的大模型。
