---
title: Heterogeneous Co-Evolution Learning for Tool-Efficient Search Agents with Zero
  Labels
title_zh: 零标注下异构协同进化的工具高效搜索Agent训练框架
authors:
- Qin-Wen Luo
- Sheng Ren
- Xiang Chen
- Rui Liu
- Jun Fang
- Naiqiang Tan
- Jun Wang
- Hua Chai
- Sheng-Jun Huang
affiliations:
- Nanjing University of Aeronautics and Astronautics
- Didichuxing Co. Ltd
arxiv_id: '2610.39682'
url: https://arxiv.org/abs/2610.39682
pdf_url: https://arxiv.org/pdf/2610.39682
published: '2026-10-29'
collected: '2026-10-30'
category: Agent
direction: 搜索Agent · 零标注协同进化训练
tags:
- SearchAgent
- ZeroLabel
- CoEvolution
- ReinforcementLearning
- ToolEfficiency
one_liner: 零标注场景下通过异构提题-解题协同进化，同时提升搜索Agent准确率与工具调用效率
practical_value: '- 可复用异构proposer-solver架构训练电商搜索Agent，用小模型做提题器降低训练成本，无需人工标注QA对

  - 工具感知奖励可直接迁移到电商导购Agent的RAG调用优化，减少冗余检索降低推理成本，同时不降低答案准确率

  - 中间难度奖励设计可用于推荐系统的用户交互样本自动生成，始终围绕模型能力边界构造训练任务提升训练效率

  - 证据路径引导的任务生成方法可用于多跳商品查询的训练集构造，无需标注就能生成高难度多跳检索训练样本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有搜索Agent训练存在两大核心痛点：一是固定标注训练集无法随模型能力进化自适应调整，易陷入训练瓶颈；二是仅基于最终回答正确性的RL奖励无法区分冗余检索与有效检索，导致准确率与工具调用效率难以同时优化，且专业标注成本极高。

### 方法关键点
- 采用异构proposer-solver协同进化范式，全程无需标注QA对或专家检索轨迹
- 任务生成采用答案优先+证据路径引导流程：先基于无标注参考问题生成可检索的目标实体，递归构造多跳实体关联证据路径，再生成可验证的多跳QA对，验证仅用轻量NLP/检索组件，无额外LLM推理开销
- 双角色定制奖励：proposer采用中间难度奖励`4*Acc*(1-Acc)`，优先生成solver准确率约50%的能力边界任务；solver采用工具感知奖励，正确回答下检索次数越少奖励越高，抑制冗余检索

### 关键实验结果
在NQ、TriviaQA等3个通用QA、HotpotQA等4个多跳QA基准测试：
- 零标注从头训练7B Base模型，7个基准平均EM提升16.4%，平均检索调用量降低0.43次/样本
- 3B小模型作为proposer即可训练7B/8B大模型solver，训练成本远低于同规模自play方案
- 对已训练的搜索专用Agent（Search-R1、ZeroSearch）仍可提升EM 3.9~4.9%，同时降低检索调用量0.03~0.68次/样本

### 核心结论
异构协同进化的零标注训练范式，可在不依赖人工标注的前提下，同时实现搜索Agent的能力提升与工具调用效率优化
