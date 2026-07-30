---
title: 'Setoka: A Benchmark for Hierarchical User Understanding in Personalized Agents
  over Heterogeneous Data'
title_zh: Setoka：面向异构数据个性化Agent的分层用户理解基准
authors:
- Lingyang Zeng
- Guangze Chen
- Kaichen Yu
- Zhicheng Pan
- Siyang Weng
- Zirui Hu
- Xiangyun Du
- Hailin He
- Rong Zhang
- Chengcheng Yang
affiliations:
- East China Normal University
- The Chinese University of Hong Kong
arxiv_id: '2607.27056'
url: https://arxiv.org/abs/2607.27056
pdf_url: https://arxiv.org/pdf/2607.27056
published: '2026-07-29'
collected: '2026-07-30'
category: Agent
direction: 个性化Agent · 用户理解能力评估
tags:
- Personalized Agent
- User Understanding
- Memory System
- Benchmark
- Heterogeneous Data
one_liner: 提出首个覆盖四层用户理解层级的异构数据个性化Agent记忆能力评估基准
practical_value: '- 用户画像建模可直接复用四层分层框架：从语义记忆（显式属性）、Episodic Memory（单事件细节）、行为模式（跨时段行为规律）、人格特质（跨场景稳定偏好）四层构建用户标签体系，实现从显式事实到隐式特质的分层刻画

  - 记忆系统选型可参考实验结论：简单显式事实查询优先用DBQuery基线，跨记录事件关联任务选用带时序邻域检索的MemMachine类系统，跨域行为聚合、隐式特质推理任务优先选用图结构记忆系统

  - 合成用户数据集生成可复用其pipeline：采用相关性感知人格抽样+心理量表引导行为生成+事件树异构数据生成的流程，既能规避真实用户隐私风险，又能保证用户行为的一致性与合理性

  - 用户理解类Agent评估可复用分层指标体系：显式查询用LLM Judge做语义一致性打分，隐式特质类查询用排名相关性指标，同时单独统计回答率区分「不敢答」和「瞎猜」的系统'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有个性化Agent记忆基准仅评估对话历史的显式事实检索能力，无法衡量跨异构数据源整合隐式证据、推理用户抽象特征的能力。真实场景下用户的行为模式、人格特质等信息分散在文本、结构化记录、关系图等多源数据中，无法靠单条检索得到，缺乏分层的评估体系支撑深度用户理解能力的迭代。

### 方法关键点
- 基于认知心理学定义四层用户理解层级：语义记忆（SM，单条显式事实检索）、Episodic Memory（EM，跨记录关联单事件信息）、行为模式（BP，跨时段聚合同类事件规律）、人格特质（PT，跨场景泛化推理用户稳定特质），每层对应不同推理算子（选择、关联、聚合、泛化）。
- 提出心理测量学驱动的数据生成pipeline：相关性感知人格抽样（基于大五人格的真实协方差矩阵采样，保证人格组合符合真实分布）、心理量表引导行为生成（用BFI-2量表映射人格到具体行为模式，避免刻板印象）、事件树生成（粗到细生成时序事件，再映射到多源异构数据，保证跨数据一致性），无需人工标注自动生成带真值的查询集。
- 分层评估指标：SM/EM/BP用LLM Judge语义相似度打分，PT用用户人格排名的Kendall相关系数。

### 关键结果
基于10个合成用户（每个约1600条异构记录、1426个查询），评测3个LLM（DeepSeek-V4-Flash、Ministral 14B、Gemma 4B）搭配5个记忆系统+DBQuery基线，核心结论：
1. 性能随层级抽象度升高骤降：最优SM得分0.85，EM 0.46，BP 0.28，PT仅0.24，接近随机水平。
2. 不同记忆系统适配不同任务：DBQuery在SM任务最优（0.85），MemMachine在EM任务最优（0.46），图结构记忆系统在BP/PT任务上表现最优。

### 核心结论
仅靠检索无法实现深度用户理解，记忆系统需要针对不同推理层级维护多粒度的信息聚合与关联能力。
