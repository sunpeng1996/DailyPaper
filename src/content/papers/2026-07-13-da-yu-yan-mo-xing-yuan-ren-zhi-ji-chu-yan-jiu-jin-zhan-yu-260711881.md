---
title: 'Metacognition in LLMs: Foundations, Progress, and Opportunities'
title_zh: 大语言模型元认知：基础、研究进展与未来方向
authors:
- Gabrielle Kaili-May Liu
- Areeb Gani
- Jacqueline Lu
- Jordan Thomas
- Mark Steyvers
- Arman Cohan
affiliations:
- Yale University
- University of California, Irvine
arxiv_id: '2607.11881'
url: https://arxiv.org/abs/2607.11881
pdf_url: https://arxiv.org/pdf/2607.11881
published: '2026-07-13'
collected: '2026-07-14'
category: LLM
direction: 大语言模型元认知研究与应用
tags:
- Metacognition
- LLM
- Agent
- Evaluation
- Reasoning
- Self-Improvement
one_liner: 首个大语言模型元认知领域系统性综述，梳理定义、评估方法、实现路径及应用前景
practical_value: '- 搭建电商导购Agent、推荐解释系统时，可复用元认知校准方法，让模型输出对推荐结果、问答内容的置信度，高置信度内容直接透出，低置信度自动触发RAG召回商品库/规则库，减少推荐幻觉，提升用户信任

  - 设计Agent多轮交互流程时，可采用元认知的监测-控制环路：先让模型监测当前回答/推荐的合理性、用户需求匹配度，再自主选择是否调用商品搜索、优惠券查询等工具，或主动向用户澄清需求，降低无效交互占比

  - 优化LLM驱动的推荐召回/排序模块时，可参考元认知评估指标（如M-ratio、AUROC）衡量模型对候选item的置信度校准水平，针对性通过RLHF加入置信度准确性的奖励信号，减少低质量推荐的透出'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM在推理、Agent、生成式推荐等场景落地时，普遍存在幻觉、过度自信、无法感知自身能力边界等问题，元认知作为人类智能的核心组成，被认为是提升LLM可靠性、可控性与自主决策能力的关键路径，但现有相关研究碎片化，缺乏统一的定义、评估标准与落地框架，亟需系统性梳理。

### 方法关键点
- 明确LLM元认知核心框架：分为监测（不确定性评估、性能预判、知识边界感知）和控制（策略选择、资源分配、自我修正）两大交互模块，形成完整的元认知环路
- 梳理5类成熟的元认知评估方法：心理学驱动的SDT系列指标、神经反馈类指标、置信度校准指标、可解释性探针指标、任务专属评估指标，同时汇总了现有公开评估基准
- 系统归纳LLM元认知的4类主流实现路径：prompt引导、专项微调、外挂监测模块、多Agent协作校准
- 提炼元认知的4大落地应用方向：幻觉抑制、Agent能力提升、人机协同优化、可解释性增强

### 关键结果
- 现有LLM元认知灵敏度普遍偏弱，仅部分专有大模型在特定任务上超过人类，开源模型普遍存在过自信问题，推理步数增加会进一步降低元认知校准水平
- 模型尺寸与元认知能力整体正相关，但存在7-9B的容量阈值，小于该阈值的模型使用元认知prompt反而会引入更多错误
- RLHF后模型的元认知效率在STEM类任务上会出现明显下降，生成温度对元认知表现的影响随模型家族差异显著

### 核心结论
元认知是LLM从「被动响应工具」向「自主可控智能体」演进的核心能力，当前校准置信度、感知知识边界是最易落地的元认知应用方向
