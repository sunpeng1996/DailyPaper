---
title: 'EmbodiedMemory-Bench: Benchmarking Embodied Memory for Long-Horizon Embodied
  Tasks'
title_zh: EmbodiedMemory-Bench：面向长程具身任务的具身记忆评测基准
authors:
- Lizhou Liang
- Xinyu Zhong
- Miao Pan
- Xiaohe Zhou
- Xuanyu Liu
- Qinfeng Li
- Peng Li
- Jintao Chen
- Xuhong Zhang
- Wenqi Zhang
affiliations:
- Zhejiang University
- Central South University
- Institute of Software, Chinese Academy of Sciences
arxiv_id: '2609.28236'
url: https://arxiv.org/abs/2609.28236
pdf_url: https://arxiv.org/pdf/2609.28236
published: '2026-09-22'
collected: '2026-09-29'
category: Agent
direction: 具身Agent · 长程任务记忆评测与优化
tags:
- Embodied Agent
- Memory System
- Benchmark
- Long-Horizon Task
- Multimodal
one_liner: 推出含2554个交互片段的具身记忆评测基准，配套三层结构EMem外部记忆系统提升长程任务表现
practical_value: '- 电商线下导购/仓配具身Agent可直接复用EMem的三层记忆架构：空间记忆存商品/货位实时状态、事件记忆存操作失败/用户反馈记录、场景记忆区分不同门店/库区的同名物品，减少重复操作错误

  - 长程多轮交互推荐Agent（如家电选购全流程顾问）可参考本文的四类记忆能力维度做离线能力验证，优先优化占比最高的记忆类错误

  - 多模态长上下文Agent不要盲目堆砌历史输入：实验证明直接塞入全量历史视觉信息会降低10.4%成功率，同时token量涨4.9倍、延迟涨9.5倍，应做结构化记忆提取而非全量输入'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前长程具身交互任务中，Agent普遍存在细粒度视觉记忆弱、动态世界状态追踪不可靠、交互结果揭示的状态未记录、历史经验泛化性差四类问题，占所有失败案例的91%，但现有基准未针对性评测这四类具身记忆能力，无法支撑相关系统优化。

### 方法关键点
- 构建EMem-Bench评测基准：包含2554个交互片段，覆盖被动观察（测细粒度视觉记忆）、动态追踪（测状态更新能力）、交互失败（测交互结果记录）、经验泛化（测规则迁移能力）四类任务族，要求Agent从历史交互中提取记忆指导后续环境操作
- 提出Embodied-Memorizer（EMem）外部记忆系统：分三类互补记忆，空间记忆维护实体图追踪对象位置/状态、事件记忆按时间存动作/反馈/可复用规则、场景记忆绑定实体与所属场景避免重名混淆，配套训练8B参数的EMem-8B策略模型负责记忆的读写检索

### 关键结果
评测16款主流开源/闭源MLLM，最强闭源模型Gemini-3-Flash平均成功率仅64.2%，开源模型除Qwen3.6-27B外平均成功率均低于45%，61.3%的失败源于记忆与交互历史冲突；EMem可显著提升各基线表现：开源Mistral-Small-3.1-24B成功率涨16.4个点，闭源GPT-5.4-mini涨23.6个点，训练后的EMem-8B比Qwen3-VL-8B基线高20.6个点。

**最值得记住的一句话**：长程多模态交互Agent的核心瓶颈不是上下文长度，而是能否结构化提取、动态更新、正确复用交互记忆，盲目堆全量历史输入只会降低性能提升成本。
