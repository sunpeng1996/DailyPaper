---
title: 'MemOps: Benchmarking Lifecycle Memory Operations in Long-Horizon Conversations'
title_zh: MemOps：长时对话场景下生命周期内存操作评测基准
authors:
- Xixuan Hao
- Zeyu Zhang
- Zehao Lin
- Yihang Sun
- Ziliang Guo
- Xichong Zhang
- Yuxuan Liang
- Feiyu Xiong
- Zhiyu Li
arxiv_id: '2607.12893'
url: https://arxiv.org/abs/2607.12893
pdf_url: https://arxiv.org/pdf/2607.12893
published: '2026-07-14'
collected: '2026-07-15'
category: Eval
direction: Agent长时内存操作级评测
tags:
- Long-term Memory
- Agent Evaluation
- Conversational Agent
- Memory Operation
- Benchmark
one_liner: 提出操作级长时对话Agent内存生命周期评测基准MemOps，可定位记忆故障根因
practical_value: '- 电商导购/客服多轮Agent的长时记忆能力评测可复用MemOps的操作级trace标注方法，替代单一终态答准率，精准定位记忆故障（漏存、更新错误、检索偏差等）根因

  - 落地多会话Agent记忆系统时，优先选择会话级检索替代单轮级检索，可显著提升长时记忆召回准确率

  - 构建动态用户画像记忆模块时，可参考MemOps的记忆生命周期（记/忘/更新/反思）定义，设计结构化记忆状态流转逻辑，避免依赖过期用户特征'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有长时记忆基准仅通过下游QA终态准确率黑盒评测，无法区分记忆故障根因（漏存事实、操作目标错误、依赖过期值等），甚至会给依赖错误记忆的正确答案误判高分，无法支撑细粒度优化。
### 方法关键点
将长时对话记忆重构为包含记忆、遗忘、更新、反思的生命周期操作序列，每个记忆事件用结构化trace标注触发条件、目标、范围、状态转换、支撑证据；通过可控生成pipeline将操作嵌入长任务导向对话，生成金标trace与6类操作级探针，分近邻证据、长上下文两种场景开展评测。
### 关键结果
MemOps可拆解终态准确率掩盖的所有故障模式；会话级检索效果显著优于单轮级检索；长上下文模型在有序记忆状态轨迹重建任务上表现极差，当前各类长时内存系统整体可靠性仍存在明显短板
