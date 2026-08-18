---
title: 'Ask to Be Sure: Informative Interactions for Confident Multi-Turn LLM Recommendation'
title_zh: 基于熵减奖励的多轮LLM对话式推荐交互优化方法
authors:
- Cedar Site Bai
- Duanshun Li
- Zhenyu Liao
- Sheikh Sarwar
- Huiyuan Chen
- Yuan Chen
- Changhe Yuan
- Haiyang Zhang
- Qilin Qi
affiliations:
- Amazon
arxiv_id: '2608.15949'
url: https://arxiv.org/abs/2608.15949
pdf_url: https://arxiv.org/pdf/2608.15949
published: '2026-08-16'
collected: '2026-08-18'
category: GenRec
direction: 生成式推荐 · 多轮对话交互优化
tags:
- Conversational Recommendation
- Multi-turn Interaction
- Entropy Reduction
- DPO
- Uncertainty Estimation
one_liner: 以推荐结果分布的熵减为奖励微调LLM，提升多轮对话式推荐的准确率与交互效率
practical_value: '- 电商导购/对话推荐场景可复用加权熵指标：无需ground truth，通过多次采样推荐结果的排名加权熵判断当前对用户偏好的确定程度，决定是否继续追问或直接推荐，降低用户交互成本

  - 微调多轮推荐LLM时，可直接用单轮/全对话熵减作为奖励，用于SFT样本筛选或DPO偏好标注，替代成本较高的LLM judge或人工标注，适配现有微调流程

  - 熵计算时引入排名对数衰减权重，优先保障top推荐结果的确定性，更符合推荐业务重视头部结果准确率的需求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多轮LLM对话式推荐的交互策略存在两类缺陷：要么依赖独立RL agent与固定问答模板，限制对话自然度；要么用LLM judge评估交互性，无法量化实际获取的用户偏好增益，且普遍依赖业务中难以获取的ground truth推荐标签，导致交互效率低、推荐准确率提升有限。
### 方法关键点
- 不确定性量化：基于当前对话上下文，n次采样生成top-m推荐列表，计算带排名对数衰减加权的香农熵，作为当前推荐的不确定性度量，排名越靠前的结果权重越高
- 熵减奖励设计：计算单轮交互（助手提问+用户回复）后或全对话结束后的熵降，作为该轮助手交互的信息增益，无需ground truth即可作为奖励信号
- 微调适配：将熵减奖励直接用于SFT样本筛选（保留高熵减样本）或DPO偏好标注（高熵减回复为优选），无需改动基础LLM架构，适配现有微调流程
### 关键结果
在INSPIRED、ReDial两个公开对话推荐数据集上对比Vanilla LLM、原始SFT、CollabLLM等基线：
- DPO+轮级熵减奖励在INSPIRED数据集上Hit@1达3.32%、Hit@5达5.21%、模拟对话命中率达27.94%，相比CollabLLM DPO分别提升5.4%、2.4%、5.0%，到达ground truth的平均轮数减少0.05
- DPO+对话级熵减奖励在ReDial数据集上模拟对话命中率达32.83%，平均交互轮数低至2.74，交互效率最优

多轮对话式推荐的交互价值，本质是降低推荐结果的不确定性，而非单纯提升对话的流畅性或互动性
