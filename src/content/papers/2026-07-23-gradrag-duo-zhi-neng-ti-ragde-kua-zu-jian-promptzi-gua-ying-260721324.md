---
title: 'GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG'
title_zh: GRADRAG：多智能体RAG的跨组件Prompt自适应框架
authors:
- Paolo Pedinotti
- Enrico Santus
affiliations:
- Bloomberg
arxiv_id: '2607.21324'
url: https://arxiv.org/abs/2607.21324
pdf_url: https://arxiv.org/pdf/2607.21324
published: '2026-07-23'
collected: '2026-07-24'
category: Agent
direction: Agent 多智能体RAG跨组件优化
tags:
- MultiAgent
- RAG
- PromptOptimization
- GraphRAG
- TestTimeAdaptation
one_liner: 通过下游评价反馈反向更新RAG全链路各智能体prompt，无参数微调即可提升效果
practical_value: '- 可直接复用Evaluator+Prompt Optimizer的反馈架构，将电商搜索、客服问答等场景的RAG链路抽象为计算图，用下游用户/系统评价反向更新上游检索、意图理解模块的prompt，无需微调模型即可快速迭代效果

  - 针对电商商品检索、咨询问答中常见的上游召回信息缺失问题，无需改动检索底层逻辑，仅通过跨组件prompt优化即可补全用户关注的信息维度，相比仅优化生成回答的方案效果更显著

  - 线上部署时设置2~3轮迭代+早停机制，在获得12~15pp的效果提升的同时，仅增加约10%的latency，平衡效果与响应速度，满足电商场景的实时性要求

  - 对于商品知识图谱、属性图谱支撑的GraphRAG场景，可基于用户查询反馈动态调整实体-关系抽取的prompt，针对性补全用户关注的商品属性、关联信息，提升问答准确性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前多智能体RAG系统普遍采用组件孤立优化的模式，下游生成阶段的评价反馈无法传导到上游检索、证据结构化模块，导致上游的召回缺失、实体遗漏等错误持续向下传递，仅优化生成模块无法根本解决问题，亟需全链路协同的优化机制。

### 方法关键点
- 将RAG链路抽象为计算图，各LLM智能体的prompt支持自适应更新，全程不修改模型参数，适配向量RAG、GraphRAG两种主流范式
- 设计Evaluator智能体，同步评估最终回答与支撑证据的完整性、准确性，输出结构化反馈与早停决策，无需访问标注答案避免数据泄露
- Prompt Optimizer根据反馈同时更新上游（检索/图提取）、下游（生成）智能体的prompt，实现全链路协同优化

### 关键实验
在SQUALITY长文本问答、QMSUM会议摘要两个数据集上，对比仅更新生成模块的单步优化基线，GRADRAG在LLM pairwise偏好评估中取得12~15个百分点的净偏好优势，大部分增益在2轮迭代内即可实现，额外latency仅增加约10%，LLM评估结果与人类偏好的一致性达75.86%。

### 核心结论
RAG优化不能局限于生成模块，将下游评价信号传导到上游检索等组件的协同优化，可在无参数微调的前提下实现显著效果提升。
