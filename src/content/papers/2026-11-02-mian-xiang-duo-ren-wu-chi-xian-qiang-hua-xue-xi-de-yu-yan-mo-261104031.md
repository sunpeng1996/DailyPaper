---
title: Language Model Augmented Decision Transformer for Multi-Task Offline Reinforcement
  Learning
title_zh: 面向多任务离线强化学习的语言模型增强决策Transformer
authors:
- Xinbo Zhao
- Yuhang Liu
- Xin Zhang
- Lei Le
- Zhaohan Xi
- Yu Yang
- Yingxue Zhang
affiliations:
- State University of New York at Binghamton
- San Diego State University
- LinkedIn
- Lehigh University
arxiv_id: '2611.04031'
url: https://arxiv.org/abs/2611.04031
pdf_url: https://arxiv.org/pdf/2611.04031
published: '2026-11-02'
collected: '2026-11-04'
category: Agent
direction: 多任务离线RL · LLM增强决策Transformer
tags:
- OfflineRL
- DecisionTransformer
- MultiTaskLearning
- LoRA
- DataAugmentation
- LLM
one_liner: 基于单LLM统一实现任务对齐轨迹增强与多任务策略学习，提升低数据场景下离线MTRL泛化性
practical_value: '- 多任务推荐冷启动场景可复用「单LLM+多目标LoRA」架构：用任务自然语言描述引导生成用户交互/行为样本，解决单任务数据不足问题

  - 生成式数据增强可复用多维度打分过滤机制：从样本合理性、任务对齐度、时序连贯性等维度联合评分，仅保留Top-K高质量合成数据，避免引入噪声

  - 多任务序列建模可复用「专用LoRA+共享LoRA」参数隔离方案：既避免不同任务/目标的梯度冲突，又保留跨任务可迁移的通用知识

  - 低数据场景模型初始化可复用知识迁移思路：将数据增强阶段学到的共享LoRA直接作为下游策略/排序模型的初始化权重，提升冷启动效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
离线多任务强化学习可从静态异构数据集学习统一跨任务策略，但长期面临两大核心瓶颈：单任务轨迹数据采集成本极高、数据量普遍不足，且任务间分布偏移导致跨任务泛化能力弱，低数据场景下性能骤降问题尤为突出，现有方案仅能解决单一痛点，无法同时兼顾数据扩增与跨任务语义对齐。

### 方法关键点
- 提出LaMA-DT统一框架，复用单一LLM同时完成轨迹增强和多任务策略学习，全程以自然语言任务描述为语义锚点
- 轨迹增强阶段优化6个互补目标：4个动力学/时序学习目标（状态转移预测、轨迹插补、正向/反向生成）保证生成轨迹的合理性与连贯性，2个双向对齐目标（轨迹转描述、描述生成轨迹）避免生成轨迹偏离任务目标；采用「目标专属LoRA+共享LoRA」参数方案，既隔离梯度冲突又保留跨目标可迁移知识
- 新增多目标似然联合打分过滤机制，仅保留Top-K高质量合成轨迹，与原始数据混合后训练策略
- 策略学习阶段直接复用轨迹增强阶段的共享LoRA作为初始化，训练语言条件的Decision Transformer，新增数据来源标记实现源感知行为克隆

### 关键结果
在Meta-World、MuJoCo两大标准基准测试，对比7个SOTA基线：标准数据量下平均比最强基线高5.5%（Meta-World）、6.8%（MuJoCo）；低数据场景下优势更突出，1%数据量时相对次优模型提升22.7%~47.3%；低数据场景下最优增强数据比例为真实数据的1倍左右，标准数据场景下最优比例为0.5倍，比例过高会引入分布偏移导致性能下降。

> 最值得记住的结论：以自然语言为语义锚点的LLM增强方案，可同时解决多任务学习的数据稀缺与跨任务对齐两大痛点，低数据冷启动场景下收益最高
