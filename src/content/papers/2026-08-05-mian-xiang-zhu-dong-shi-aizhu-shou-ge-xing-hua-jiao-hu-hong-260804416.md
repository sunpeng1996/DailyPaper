---
title: Preference-Driven Online Adaptation for Personalized Interaction Initiation
  in Proactive AI Assistants
title_zh: 面向主动式AI助手个性化交互触发的偏好驱动在线适配方法
authors:
- Yufeng Wang
- Wei Zhang
- Zhiquan Wen
- Jinwu Hu
- Linhui Xiao
- Tianlu Pan
- Qingfang Zheng
- Mingkui Tan
affiliations:
- South China University of Technology
- Pengcheng Laboratory
arxiv_id: '2608.04416'
url: https://arxiv.org/abs/2608.04416
pdf_url: https://arxiv.org/pdf/2608.04416
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: 主动Agent · 个性化交互时序适配
tags:
- Proactive Agent
- Online Adaptation
- Personalization
- Preference Modeling
- Efficient Inference
one_liner: 提出证据驱动的在线偏好适配框架EOPA，无需LLM重训即可实现主动交互时序的个性化适配
practical_value: '- 交互触发类场景（如APP主动push、智能导购触达）可复用双证据载体设计：时间偏好锚记录「时段+行为进度」的交互统计，活动原型存储语义相关行为的反馈数据，解决稀疏触发时刻建模问题

  - 在线偏好估计可复用用户先验平滑+不确定性加权的trick：小样本下用全局用户偏好稳定局部估计，证据权重随样本量自动调整，降低冷启动偏差

  - 轻量化在线适配方案可直接迁移：无需LLM重训/每步调用LLM做决策，仅更新统计量与决策阈值，端侧Agent也能实现毫秒级延迟，大幅降低计算成本'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前主动式AI助手的交互时序偏好高度个性化，稀疏的有效交互时刻分散在细粒度用户状态中，现有方法要么依赖LLM微调（稀疏样本下无法学到细粒度偏好），要么用自然语言总结反馈（适用边界模糊易过泛化），同时每步调用LLM推理延迟高、适配成本高，无法满足线上实时性要求。

### 方法关键点
- 设计两类互补证据载体：时间偏好锚按「时段+活动进度」双维度存储交互/沉默统计值，带证据的活动原型存储语义活动中心及对应进度下的反馈统计
- 证据计算采用用户先验平滑+不确定性缩放：小样本下用全局用户交互率作为先验平滑局部统计，再根据Beta分布后验方差缩放证据值，样本量越大证据权重越高
- 自适应融合双证据做决策，收到反馈后仅更新载体统计量、融合权重与决策阈值，无需LLM推理或重训，仅在确定触发交互后才调用LLM结合历史优质回复生成内容

### 关键实验
在ProPerSim基准32个用户14天模拟数据集上，对比Reflexion、EvoTest等主流自改进Agent基线，EOPA的交互时序F1提升19.80个百分点，沉默步骤推理延迟从688ms降至1.96ms，日均适配时间从11.41s降至0.39s，即使仅保留50%反馈仍能保持83.9%的全量性能。

### 核心洞察
将用户对交互时机的偏好锚定到可量化的上下文统计证据上，比LLM生成的自然语言经验能更精准地识别细粒度状态下的差异化交互需求
