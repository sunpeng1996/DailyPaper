---
title: Just-In-Time Agent Memory with Runtime Agentic Research
title_zh: 支持运行时智能体检索的即时Agent内存框架JAM
authors:
- Bingyu Yan
- Chaofan Li
- Hongjin Qian
- Shuqi Lu
- Chaozhuo Li
- Zheng Liu
affiliations:
- Beijing Academy of Artificial Intelligence
- Peking University
- Hong Kong Polytechnic University
arxiv_id: '2609.34385'
url: https://arxiv.org/abs/2609.34385
pdf_url: https://arxiv.org/pdf/2609.34385
published: '2026-09-28'
collected: '2026-09-29'
category: Agent
direction: Agent 长时内存优化
tags:
- Agent Memory
- Long Context
- SFT
- Reinforcement Learning
- JIT Memory
one_liner: 提出运行时按需构建上下文的JIT Agent内存框架，性能优于AOT方案且延迟较基线降76%
practical_value: '- 电商/推荐场景的用户长程行为记忆可复用分层页存储架构：离线保留全量原始行为数据+目录式导航摘要，避免AOT预压缩丢失细粒度小众偏好，运行时再按需召回关联证据，比固定RAG召回更适配长尾用户query、跨会话偏好挖掘等场景

  - 内存探索Agent的两阶段训练范式可直接迁移：先通过验证轨迹SFT学习基础工具调用与探索逻辑，再用Hint-guided GRPO优化多步探索，解决稀疏奖励下长程记忆检索不稳定的问题，适合订单溯源、多session消费行为关联等多跳任务

  - 效果效率动态调优思路可复用：可通过调整运行时最大动作轮数、单次检索召回量动态平衡资源消耗和回答质量，适配大促/日常不同算力预算场景，JAM的性能延迟trade-off优于现有训练型内存Agent方案'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agent内存系统多采用Ahead-of-Time（AOT）预构建模式，请求无关的预处理会丢失后续可能关键的细粒度信息与跨会话依赖，在证据分散、需要多跳关联的长历史场景下表现不佳；同时训练型内存Agent存在训练数据覆盖场景有限、推理延迟过高的问题，难以落地。
### 方法关键点
- 双组件JIT架构：离线Memorizer将全量原始历史存储为分层页结构，每个目录维护README轻量导航摘要，既保留完整原始证据，又为运行时检索提供引导；运行时Researcher通过open、search、browse三类工具迭代探索内存空间，自主判断信息充足性后生成目标上下文。
- 训练流水线：构建Memory-Gym合成数据集，覆盖6个领域9类内存任务（单跳定位、多跳关联、多会话聚合）；采用两阶段优化，先通过验证轨迹SFT初始化Researcher的工具调用与探索逻辑，再用Hint-guided GRPO强化学习优化多步探索能力，hint仅在训练阶段注入不影响推理。
### 关键实验
在LoCoMo、LongMemEval、NarrativeQA、HotpotQA四个长上下文基准上对比10个基线：基于Qwen3.5-4B的JAM整体性能优于所有AOT内存系统，比14B参数的MemAgent F1高5.96，在线查询延迟从58.08s降至13.81s（下降76.2%）；Memory-Gym训练的策略跨领域迁移性强，在未见过的代码理解基准LongCodeQA上准确率从54.08%提升至75.54%。

> 最值得记住的一句话：Agent内存的核心价值不是静态存储历史，而是运行时根据请求动态构建最适配的上下文。
