---
title: The Rise of Verbal Reinforcement Learning
title_zh: 语言强化学习（VRL）全景综述：范式分类、技术路径与落地方向
authors:
- Kshitij Tayal
- Arun Sharma
- Genta Indra Winata
- Anirban Das
- Sambit Sahu
affiliations:
- Capital One
- University of Minnesota, USA
arxiv_id: '2609.01597'
url: https://arxiv.org/abs/2609.01597
pdf_url: https://arxiv.org/pdf/2609.01597
published: '2026-09-01'
collected: '2026-09-02'
category: Agent
direction: Agent 语言反馈优化 · VRL 范式分类
tags:
- Verbal Reinforcement Learning
- LLM Agent
- RLHF
- Self-Correction
- Taxonomy
one_liner: 首次提出VRL三支柱统一分类框架，系统性梳理语言反馈优化Agent的全路径技术
practical_value: '- 可直接复用VRL三支柱框架搭建电商Agent反馈链路：任务定义阶段用自然语言落地用户个性化需求（Pillar1接地），推理阶段用用户实时评论/搜索反馈修正推荐结果（Pillar2推理反馈），训练阶段用偏好反馈做SFT/DPO迭代推荐策略（Pillar3学习信号）

  - 推理阶段优先选择externally grounded critique方案：接入订单/库存/售后等确定性工具数据生成反馈，比纯self-critique更能避免大模型幻觉，适配电商推荐的高准确性要求

  - 训练阶段优先采用反馈条件建模保留用户完整评价文本：相比直接压缩为偏好标量的DPO，可更好捕捉用户细粒度属性偏好，适配电商多品类、多属性的推荐场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统RL高度依赖人工定义的MDP结构、奖励函数，域适配成本极高，是Agent落地的核心瓶颈；LLM兴起后自然语言作为可解释的反馈信号被广泛应用，但相关研究分散在自纠错、RLHF、具身Agent等多个领域，缺乏统一框架指导落地。
### 方法关键点
- 首次明确定义Verbal Reinforcement Learning（VRL）范式，按语言反馈作用的Agent生命周期阶段，提出三支柱分类框架
- Pillar1 语言作为接地信号：任务定义阶段明确目标、状态、动作、奖励，直接构造MDP，无需人工形式化
- Pillar2 语言作为推理反馈：推理阶段通过自纠错、工具接地反馈、多智能体辩论、记忆检索、搜索引导等方式修正单次输出，不更新模型参数
- Pillar3 语言作为学习信号：训练阶段通过反馈条件建模、自迭代过滤、过程监督、偏好塑形等方式更新模型参数，长期优化策略
### 核心结果
整理现有研究的核心收益：1.3B参数模型基于语言偏好训练后效果超过175B GPT-3基线，实现130倍参数效率提升；自反思VRL方法在HumanEval上pass@1达91%；多智能体辩论方法在数学推理任务上相比单Agent提升12%以上。
### 最值得记住的结论
语言反馈将成为下一代Agent架构的第一类设计原语，瓶颈将从反馈生成转向反馈验证，工具接口需要优先适配Agent可消费性而非人类可读性。
