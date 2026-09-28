---
title: Structured Reasoning Agentic Framework for Interpretable Critical View of Safety
  Assessment
title_zh: 面向可解释手术安全临界视图评估的结构化推理智能体框架
authors:
- Qing Xu
- Yuxiang Luo
- Zhen Chen
affiliations:
- School of Computer Science, University of Nottingham, UK
- Department of Data Science and Artificial Intelligence, The Hong Kong Polytechnic
  University, Hong Kong SAR
arxiv_id: '2609.31524'
url: https://arxiv.org/abs/2609.31524
pdf_url: https://arxiv.org/pdf/2609.31524
published: '2026-09-25'
collected: '2026-09-28'
category: Agent
direction: 多模态Agent 结构化推理可解释评估
tags:
- Agent
- VLM
- LLM
- Structured Reasoning
- Interpretability
one_liner: 提出ReasonCVS结构化推理Agent框架，将手术CVS评估拆解为可解释细粒度验证任务，性能超越现有SOTA
practical_value: '- 复杂多模态决策任务可采用「中心决策LLM+专用感知工具」的拆分架构，解决端到端黑盒可解释性差的问题，可迁移到电商商品合规检测、多模态内容审核场景

  - 业务场景可先将实体、关联关系抽象为结构化场景图作为中间表示，提升LLM推理的可溯源性，适合推荐可解释性生成、用户意图拆解等场景

  - 垂直领域Agent可采用rationale distillation微调核心决策LLM，兼顾推理可解释性与决策准确率，适配小样本业务场景的定制化需求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有腹腔镜胆囊切除术安全临界视图（CVS）评估采用端到端黑盒预测范式，直接映射视觉特征到标签，缺乏解剖关系显式推理，可解释性与泛化性受限。
### 方法关键点
1. 提出ReasonCVS结构化推理Agent框架，将CVS评估拆解为细粒度解剖验证子任务
2. 设计ASGA（Anatomical Scene Graph Abstraction）模块，结构化表示解剖实体及空间关系
3. 基于rationale distillation微调LLM作为中心决策Agent，调用VLM驱动的子准则验证工具完成单维度评估，再通过校准软推理合成最终结果，同步输出可追溯推理依据
### 关键结果
在Endoscapes-CVS201基准上达到68.1% mAP，性能优于现有SOTA，同时支持准则级可解释说明
