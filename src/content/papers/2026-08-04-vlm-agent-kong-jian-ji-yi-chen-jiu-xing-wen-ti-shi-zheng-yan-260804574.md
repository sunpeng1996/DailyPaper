---
title: 'When Memory Lies: An Empirical Study of Spatial Memory Staleness in VLM Agents'
title_zh: VLM Agent 空间记忆陈旧性问题实证研究
authors:
- Yushi Sun
- Yanjie Zhang
affiliations:
- LIGHTSPEED, Shenzhen
- The Hong Kong University of Science and Technology
arxiv_id: '2608.04574'
url: https://arxiv.org/abs/2608.04574
pdf_url: https://arxiv.org/pdf/2608.04574
published: '2026-08-04'
collected: '2026-08-06'
category: Agent
direction: VLM Agent 空间记忆安全优化
tags:
- VLM Agent
- Memory Staleness
- Spatial Reasoning
- Safety Alignment
- Embodied AI
one_liner: 通过动态网格环境实验揭示VLM Agent空间记忆陈旧的安全风险，提出OMCD读时过滤机制
practical_value: '- 给记忆增强Agent加读时一致性审计层：结构化记忆（如电商推荐的用户历史兴趣标签、商户库存/位置记忆）每次调用前和当前实时状态做批量校验，直接过滤冲突条目，避免给下游决策输入错误信息。

  - 空间类Agent（如到店履约Agent、线下探店内容推荐Agent）优先做文本模态的陈旧性检测：当前VLM视觉模态空间感知稳定性差异极大，低性能VLM的视觉检测结果不可靠时，过滤策略反而会引入更多噪声，不要盲目上视觉记忆校验。

  - 决策错误归因可增加轨迹长度维度：短路径致命错误大概率是错误记忆引导，长路径失败多是探索/动作选择问题，可针对性优化上游记忆校验或下游规划模块，该思路也可迁移到推荐bad
  case归因：快速转化的bad case多是历史标签错误，长路径转化失败多是排序逻辑问题。

  - 批量校验记忆时控制单批条目数：实验显示单批10条时可在9倍推理成本下降和2.7pp F1损失之间取得最优平衡，适合工程落地时做成本效果tradeoff。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前记忆增强VLM Agent的评估多聚焦记忆构建、检索与复用，忽略了动态环境下空间记忆会随环境变化失效的问题，错误的陈旧记忆会引导Agent做出致命决策，甚至比没有记忆的安全性更差，但该问题的量化风险和优化路径尚未被系统研究。

### 方法关键点
- 构建SpatialSTALE动态FrozenLake测试床，设置L1（随机单点变化）、L2（局部集群变化）、L3（在线动态变化）三种环境变化范式，记忆全程为文本格式，观测支持文本、图像两种模态，可控量化记忆陈旧对决策的影响。
- 对比4种记忆策略：无记忆（NoMemory）、直接用原始记忆（NoFilter）、单次自校验过滤（SelfVerify）、批量事件触发的OMCD读时过滤机制，OMCD会将记忆分批校验，在线变化场景下事件触发重新审计，仅保留与当前观测一致的记忆条目。
- 评测覆盖3个闭源模型（GPT-4o、Claude-Sonnet-4.6、Qwen3.6-Plus）、3个开源VLM（GLM-5.1、InternVL3-2B、InternVL3-8B），累计1800次检测实验、12000次文本模态导航实验。

### 关键结果
- 文本模态下高性能模型陈旧记忆检测F1可达0.88以上，但视觉模态下检测性能差异极大，Qwen3.6-Plus视觉F1可达0.887，GLM-5.1仅为0.067，几乎完全忽略图像输入。
- 不加校验直接用陈旧记忆的安全性远低于无记忆：GPT-4o L2场景下NoFilter策略死亡率达74.4%，是NoMemory策略28.0%的2.7倍，OMCD可将死亡率降至31.6%。
- 文本模态下OMCD过滤效果已接近Oracle（真值标注）性能，剩余瓶颈不在检测精度，而在过滤后记忆的动作选择环节。

**最值得记住的一句话**：记忆是把双刃剑，不加校验的陈旧记忆比没有记忆的风险更高。
