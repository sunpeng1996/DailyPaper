---
title: 'Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability
  Composition'
title_zh: Sage-A1.5：基于能力组合的长周期执行到科学探索智能体模型
authors:
- Wenjie Lou
- Tianshuo Peng
- Shiyang Feng
- Shengji Tang
- Runmin Ma
- Ruizhe Chen
- Jinxin Shi
- Haoyang Peng
- Fangchen Yu
- Zhijie Zhong
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2610.28578'
url: https://arxiv.org/abs/2610.28578
pdf_url: https://arxiv.org/pdf/2610.28578
published: '2026-10-19'
collected: '2026-10-21'
category: Agent
direction: Agent 长周期任务与科学探索优化
tags:
- MoE
- Agent Orchestration
- Agent Verification
- Long-Horizon Reasoning
- Scientific Discovery
one_liner: 35B MoE智能体通过自适应编排与验证，实现长周期任务及科学探索能力升级
practical_value: '- 可复用Agentic Orchestration的并行子任务拆分逻辑，应用于电商大促活动策划、多维度用户洞察等复杂任务，将大任务拆分为独立子Agent并行处理，降低单Agent上下文干扰，提升执行效率

  - Agentic Verification的自适应校验逻辑可迁移到推荐系统多轮召回排序链路，中间结果校验环节自动识别无效搜索路径，实时调整召回策略，减少无效算力消耗

  - 跨域统一训练+混合奖惩RL的训练范式可用于优化电商多技能Agent，兼顾任务结果质量与执行过程规范性，降低多任务之间的能力干扰

  - pVisor沙箱的上下文暂停/加载机制可用于落地多轮交互导购Agent，解决长会话下环境资源占用过高问题，降低部署成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有单智能体处理长周期任务时普遍存在上下文膨胀、无效探索占比高、错误逐层累积的问题，依赖固定规则的外部编排框架灵活性不足，难以适配开放动态的复杂任务需求，且单纯扩大模型参数规模的边际收益持续降低，亟需更高效的Agent能力组织机制。
### 方法关键点
- 核心实现两大自适应能力：Agentic Orchestration支持自主拆分任务，委派独立上下文的子Agent并行执行，分为探索式多假设并行验证、构造式分模块并行开发两种模式，最终整合结果降低上下文干扰；Agentic Verification支持自主识别进度停滞或关键结论节点，主动校验证据、修正策略，无需依赖外部校验工具。
- 训练采用三阶段流程：多领域SFT建立各场景基础能力，统一结果-过程后训练结合结果导向RL与过程导向教师蒸馏，针对不同任务特点灵活选择监督信号，减少跨任务能力干扰。
- 配套pVisor沙箱基础设施，支持执行上下文暂停、内存卸载、按需恢复，降低长周期任务的运行资源开销。
### 关键实验结果
在12项公开基准上对比同参数基线（A1、Ornith-1.5）及更大参数模型（Kimi-K3、GLM-5.3、GPT-5.6-sol）：SWE-Pro准确率64.6%，SWE-Multilingual准确率81.3%，FS-Olympiad准确率73%，PinchBench准确率87.3%，全面超越同参数基线，多项指标领先更大参数模型。
> 最值得记住的结论：小参数MoE Agent模型可通过优化能力组合机制（而非单纯扩参）实现超越大模型的长周期复杂任务表现。
