---
title: KV-streams for Efficient Compaction in Agentic Reinforcement Learning
title_zh: 面向智能体强化学习的KV-streams高效上下文压缩方法
authors:
- Emiliano Penaloza
- Dane Malenfant
- Dheeraj Vattikonda
- Roger Creus Castanyer
- Siddarth Venkatraman
- Abhay Puri
- Jonathan Light
- Matthew James Sargent
- Augustine N. Mavor-Parker
- Massimo Caccia
affiliations:
- Mila
- Microsoft
- McGill University
- Polytechnique Montréal
- Université de Montréal
arxiv_id: '2609.35750'
url: https://arxiv.org/abs/2609.35750
pdf_url: https://arxiv.org/pdf/2609.35750
published: '2026-09-28'
collected: '2026-09-29'
category: Agent
direction: Agent强化学习 · KV cache 性能优化
tags:
- KV cache
- Context Compaction
- Agentic RL
- LLM Training
- Throughput Optimization
one_liner: 兼容任意压缩策略的KV流式复用方案，最高实现5倍Agent训练加速
practical_value: '- 工程侧可直接复用KV-streams思路：上下文压缩后不刷新KV cache，仅通过自定义attention mask屏蔽已删除上下文，完全规避重复预填充开销，适配任意现有压缩策略

  - 训练链路可简化：LLM Agent的RL训练无需额外SFT预热阶段，仅靠RL即可让KV缓存自发传递长程信息，降低训练成本与链路复杂度

  - 高并发Agent部署优化：KV-streams支持的并发rollout数是全上下文模式的3-4倍，相同GPU资源下可承载更多电商导购、广告生成类Agent请求

  - 长会话推荐场景适配：电商多轮会话推荐的上下文压缩可直接套用该方案，在不损失推荐准确率的前提下降低30%-80%的推理显存占用'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
长 horizon Agentic LLM 的训练与推理严重受限于GPU显存容量，现有上下文压缩方案每次压缩后都需要重新预填充保留的上下文片段，产生大量重复计算，拖累训练吞吐量最高可达数倍；部分方案还要求在RL训练前增加SFT阶段适配压缩后的KV状态，进一步提升了训练链路的复杂度与成本。
### 方法关键点
- 推理侧直接在引擎中删除被淘汰的KV条目，保留有效KV并向前流式传递，彻底消除重复预填充开销
- 训练侧通过自定义attention mask完全复现KV淘汰逻辑，无需拆分训练轨迹，保证训练推理一致性
- 完全兼容所有主流上下文压缩策略（摘要压缩、Markovian Thinker、滑动窗口、自定义内容选择），无需修改原有策略逻辑
- 无需额外SFT预热，仅通过RL训练即可让保留的KV缓存自发形成伪循环状态，承载已被删除的长程上下文信息
### 关键实验
在TextWorld、ALFWorld、SWE-bench Verified三个长程Agent基准上测试，对比传统重预填充压缩、全上下文基线：TextWorld场景下最高获得5倍 wall-clock 训练加速，ALFWorld最高3倍加速，SWE-bench场景下达到峰值性能的速度比全上下文方案快3倍，最终性能与基线持平甚至更优，跨任务迁移无性能损失。
### 核心结论
KV-streams作为纯插件式优化，无需修改模型结构、压缩策略和训练流程，即可在不损失效果的前提下大幅降低长程LLM Agent的训练与推理成本。
