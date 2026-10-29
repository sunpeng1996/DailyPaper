---
title: Self-Assessment Reinforcement Learning for Search-State Awareness in Retrieval-Augmented
  Large Language Models
title_zh: 面向检索增强大模型搜索状态感知的自评估强化学习框架
authors:
- Taewhoo Lee
- Minju Song
- Jungwoo Park
- Chanwoong Yoon
- Junha Jung
- Hyeon Hwang
- Sanghoon Lee
- Minbyul Jeong
- Jaewoo Kang
affiliations:
- Korea University
- Amazon
- AIGEN Sciences
- University of Massachusetts Amherst
- Meridian Intelligence Global Inc.
arxiv_id: '2610.30435'
url: https://arxiv.org/abs/2610.30435
pdf_url: https://arxiv.org/pdf/2610.30435
published: '2026-10-20'
collected: '2026-10-29'
category: Agent
direction: RAG Agent 搜索状态感知RL优化
tags:
- RAG
- Reinforcement Learning
- Search Agent
- GRPO
- Self-Assessment
one_liner: 通过双奖励强化学习让检索增强Agent内化搜索状态感知，推理无额外开销
practical_value: '- 电商搜索导购、商品问答类Agent可直接复用SARL范式：训练阶段新增自评估环节+双奖励约束，推理阶段移除自评估无额外开销，既提升多跳复杂查询准确率，又不影响线上响应速度

  - 奖励设计可直接迁移：用指数衰减惩罚过度自评估，基于自评估前后答案正确性变化做细粒度奖励，解决RL训练搜索Agent时提前终止、探索不足的问题，适配多轮检索的导购、售后咨询场景

  - 长horizon训练稳定性优化可参考：将自评估环节与主搜索轨迹解耦，不要inline生成反思内容，避免长上下文下的训练崩溃，适配电商长会话、多轮检索的Agent训练'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有RAG搜索Agent缺乏搜索状态感知，无法明确区分已获取和缺失的信息，易出现幻觉推理、提前终止检索等问题；传统SFT依赖大量标注的搜索轨迹泛化性差，普通RL基于稀疏最终奖励训练，在长搜索horizon下易出现训练不稳定、性能崩溃的问题，复杂多跳查询准确率低。
### 方法关键点
- 框架设计：在标准think-search-answer流程基础上新增训练期自评估环节，轨迹生成后模型在独立上下文评估信息完整性，不完整则触发轨迹修订，推理时完全移除该环节无额外开销
- 训练优化：基于GRPO做策略优化，适配长搜索轨迹做梯度掩码、非对称裁剪，训练集覆盖单跳、多跳、深度研究三类共45K样本
- 双奖励机制：用α=0.8的指数衰减项惩罚过度自评估，避免依赖重试；细粒度评估奖励基于自评估前后答案正确性变化赋值，错误→正确/正确→正确加1，错误→不变扣0.1，正确→错误扣2，引导模型主动识别信息缺口
### 关键实验结果
在10个覆盖单跳QA、多跳QA、深度研究的基准上对比SOTA搜索Agent，SARL相对最强基线平均提升24.3%，多跳QA平均提升35.9%，深度研究基准平均提升27.9%；长搜索horizon下训练稳定无性能崩溃，效果超过两阶段SFT+RL框架和70B参数的多Agent RAG方案。
### 最值得记住的一句话
通过训练期自评估+双奖励内化的搜索状态感知能力，比推理期叠加多Agent编排、盲目扩大模型参数的效率和效果更优
