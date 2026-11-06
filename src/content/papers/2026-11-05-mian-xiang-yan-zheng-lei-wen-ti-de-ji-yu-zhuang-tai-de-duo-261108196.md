---
title: 'SMART: State-based Multi Agent Reasoning Traces for Verification-oriented
  Problem-Solving'
title_zh: 面向验证类问题的基于状态的多智能体推理框架SMART
authors:
- Sai Vallurupalli
- Francis Ferraro
affiliations:
- University of Maryland Baltimore County
arxiv_id: '2611.08196'
url: https://arxiv.org/abs/2611.08196
pdf_url: https://arxiv.org/pdf/2611.08196
published: '2026-11-05'
collected: '2026-11-06'
category: MultiAgent
direction: 多智体协作 · 事实核查推理优化
tags:
- Multi-Agent
- Fact Verification
- LLM Reasoning
- Role Prompting
- Contrastive Knowledge
one_liner: 提出多智能体框架SMART，通过挖掘实体状态对比知识提升复杂验证类问题推理准确率
practical_value: '- 电商虚假营销内容、用户评论真伪核查场景可复用SMART的分角色专家+对比前提生成范式，替代单Prompt推理降低幻觉

  - 推荐系统的内容合规校验环节可直接套用「实体识别→对比知识生成→真值校验→元推理输出」四步流水线，准确率优于CoT/RAG

  - 多Agent系统设计可借鉴交叉模型Premise生成方案：用中小模型生成知识前提、大模型做最终推理，平衡效果与推理成本

  - 可复用对比前提生成技巧，让Agent同时生成正反两方证据，避免单视角推理的确认偏误，提升决策可解释性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM解决科学声明验证这类上下文有限、需专业背景的复杂问题时，存在知识激活不足、幻觉率高、推理依赖表面文本的缺陷，传统CoT、RAG方法无法有效挖掘隐式实体关联知识，验证准确率偏低。

### 方法关键点
- 四阶段流水线架构：1）识别问题核心实体，为每个实体分配专属专家Agent；2）各Agent迭代生成正反对比的实体状态前提对，覆盖多视角实体关联知识；3）校验前提真值（支持参数知识自校验/网页搜索校验两种模式），标注前提对问题的支持/反对/不确定 stance，筛选高置信度有效前提；4）元推理法官整合所有有效前提，输出最终验证结果、置信度和可解释性rationale。
- 支持跨模型异构配置：可由不同模型分别负责前提生成、校验、推理环节，灵活平衡效果与推理成本。

### 关键实验结果
在SFBench、SciFact、SciFact-Open三个科学声明数据集上对比CoT、RAG基线：
- 基于参数知识校验的SMART-PK平均比CoT提升10%（SFBench）、5%（SciFact）的平衡准确率，最高提升达20%；
- 对比单前提生成，对比前提模式平均提升准确率3%，前提真值校验环节平均提升准确率2-7%，最高达19%；
- 跨模型配置的X-SMART-PK在SciFact数据集上准确率最高可再提升6.2%。

### 核心结论
复杂验证类问题的推理效果提升，核心不在于用更大的模型，而在于通过结构化的多Agent分工显式挖掘、校验隐式知识，减少单模型的推理偏误。
