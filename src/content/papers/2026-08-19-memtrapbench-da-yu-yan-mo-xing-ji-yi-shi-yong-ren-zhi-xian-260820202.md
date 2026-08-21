---
title: 'MemTrapBench: Benchmarking Cognitive Traps in LLM Memory Use'
title_zh: MemTrapBench：大语言模型记忆使用认知陷阱评测基准
authors:
- Mengru Wang
- Haozhe Luo
- Zhenqian Xu
- Zhixiang Cui
- Haoming Xu
- Qu Yang
- Jizhan Fang
- Junfeng Fang
- Ningyu Zhang
affiliations:
- Zhejiang University
- National University of Singapore
- Northeastern University
- Heriot-Watt University
- Tencent
arxiv_id: '2608.20202'
url: https://arxiv.org/abs/2608.20202
pdf_url: https://arxiv.org/pdf/2608.20202
published: '2026-08-19'
collected: '2026-08-21'
category: Agent
direction: Agent记忆认知陷阱评测与优化
tags:
- Memory System
- Cognitive Trap
- Benchmark
- Prompt Engineering
- LLM Agent
one_liner: 构建覆盖两类认知陷阱的LLM记忆评测基准，提出零架构修改的优化方案
practical_value: '- 电商客服/导购Agent上线前，可复用MemTrapBench的四类陷阱测试范式，提前排查记忆召回后是否会出现任务边界混淆、认知惯性等问题，避免用户切换需求后仍沿用旧的回答逻辑

  - AdaptiveMem的prompt设计可直接嵌入现有Agent记忆链路，无需修改架构，在记忆召回后给LLM增加风险检查system prompt，实测可提升10%+的陷阱规避率

  - 做长期用户记忆的个性化推荐时，需新增记忆适配性校验逻辑，不能仅以语义相关性作为召回依据，要判断历史记忆是否适配当前查询场景，避免用户需求变化后推荐结果过拟合历史'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM记忆评测仅聚焦存储、提取、检索环节的正确性，完全忽略了一类隐蔽失效模式：即使记忆本身事实正确、与当前查询语义相关，也可能通过固化推理路径、扭曲事实信念等方式诱导认知陷阱，导致当前任务性能显著低于无记忆状态，这类问题在长对话Agent、个性化推荐等场景普遍存在，但缺乏系统性评测与优化方案。
### 方法关键点
- 定义两类记忆认知陷阱：Reasoning Fixation（包含认知惯性、任务边界混淆、负反馈过拟合3个子场景）、Belief Distortion（对应错误安全信念泛化场景）
- 构建MemTrapBench基准，共1050个多轮对话实例，生成流程为种子设计→多轮对话生成（埋陷阱→插噪声→触发陷阱）→自动过滤+专家校验两阶段质控，所有实例的最终查询在无记忆条件下可被正确回答
- 提出AdaptiveMem推理优化方案，仅通过新增系统prompt引导LLM在使用记忆前检查四类风险，无需修改记忆框架底层架构或模型参数
### 关键实验
覆盖Gemini-3-Flash、Qwen3-30B两个主流模型，对比FullText、LightMem等5种主流记忆框架，所有记忆策略的平均性能均低于无记忆基线，最优记忆方案性能下降超10个百分点；AdaptiveMem可将Gemini上LightMem的MemTrapBench得分提升14.9个百分点，同时不降低常规记忆基准LongMemEval的性能。
### 核心结论
记忆不是越多越好，语义相关的正确记忆也可能损害当前任务性能，使用记忆前必须校验其与当前任务的适配性。
