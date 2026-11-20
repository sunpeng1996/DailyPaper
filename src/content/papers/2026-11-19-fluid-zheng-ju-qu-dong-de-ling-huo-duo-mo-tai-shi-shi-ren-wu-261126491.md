---
title: 'FLUID: Flexible, Evidence-Grounded Situated Task Guidance'
title_zh: FLUID：证据驱动的灵活多模态实时任务引导框架
authors:
- Yunqi Zhao
- Run Peng
- Ze Dong
- Ryan Lu
- Yinpei Dai
- Joyce Chai
affiliations:
- University of Michigan
arxiv_id: '2611.26491'
url: https://arxiv.org/abs/2611.26491
pdf_url: https://arxiv.org/pdf/2611.26491
published: '2026-11-19'
collected: '2026-11-20'
category: Agent
direction: 多模态实时任务引导 · 主动交互Agent
tags:
- Multimodal Agent
- Proactive Interaction
- Task Guidance
- Evaluation Framework
- Real-time Agent
one_liner: 提出统一的多模态任务引导框架，覆盖灵活交互的建模、评估与Agent实现
practical_value: '- 主动干预的必要性分类+时间窗口标注方法可直接迁移到电商AR导购、直播间智能助手场景，替代固定触发规则，根据用户操作行为（犹豫、错误操作、提问）动态决策是否推送引导话术、推送时机，降低对用户的不必要打扰

  - 基于证据的评估体系（非固定参考匹配、连续时序评分）可用于优化智能客服、导购Agent的效果评估，解决传统语义相似度、响应时长指标和真人体验不一致的问题

  - 异步模块化Agent架构可复用在实时互动推荐场景，比如直播间实时商品推荐、用户操作引导，平衡响应延迟和干预精准度，同时避免重复推送相同内容'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有实时任务引导评估依赖固定参考对话，忽略真实交互的灵活性（同一场景可选择不同话术、时机甚至沉默），和实际人-人交互的自然特性存在 mismatch，导致评估结果和真实用户体验偏差大，也难以训练出自适应的引导Agent。

### 方法关键点
- 建模层：设计4层标注体系，覆盖对话意图分类、用户动作/状态标注、干预触发证据关联、干预有效时间窗口标注，区分必要/可选/无效干预类型，明确不同类型干预的生效时序区间
- 评估层：放弃固定参考匹配，改为基于证据的匹配规则，结合LLM裁判判断内容一致性，采用余弦衰减+二次惩罚的连续时序评分替代二元窗口命中，覆盖内容正确性、干预精度、时序合理性、语音重叠率多维度评估
- Agent层：采用异步模块化架构，基于单视觉语言大模型，通过感知、任务记忆、用户意图理解、干预决策4个模块协同，动态决定是否干预、干预时机和内容，支持响应式+主动式引导

### 关键结果
在WTaG、HoloAssist两个真实人-人引导数据集上，对比ProAssist、VideoLLM、JoyAI、Gemini 3.8 Live四个基线，FLUID-Agent在WTaG数据集上LLM-Judged F1达到0.225，比次优基线高77%；响应延迟低至1.15s，比基线低15%以上；干预精度0.164，比基线高13%，是所有基线中综合表现最优的，不过和人类表现仍有较大差距（人类干预精度达0.83+）。

### 最值得记住的一句话
主动交互的核心瓶颈不是内容生成质量，而是对干预时机与必要性的判断能力
