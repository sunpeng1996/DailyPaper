---
title: Personalized Deep Research Query Refinement with Graph-Scaffolded Evidence
  Grounding
title_zh: 基于图结构证据落地的个性化深度研究查询优化方法
authors:
- Soojin Yoon
- Dongha Lee
affiliations:
- Department of Artificial Intelligence, Yonsei University
arxiv_id: '2608.05876'
url: https://arxiv.org/abs/2608.05876
pdf_url: https://arxiv.org/pdf/2608.05876
published: '2026-08-06'
collected: '2026-08-07'
category: QueryRec
direction: 个性化查询优化 · 深度研究Agent输入增强
tags:
- Query Refinement
- Personalization
- Intent Elicitation
- Graph Scaffold
- Reinforcement Learning
one_liner: 提出G-STEER框架无侵入优化深度研究Agent输入，以更少提问实现更高个性化覆盖率
practical_value: '- 电商搜索Query改写/对话式推荐的主动意图澄清模块，可复用Intent Elicitation Graph构建依赖感知的训练轨迹，解决关联意图的有序澄清问题，减少无效用户提问

  - 目标锚定的GRPO优化策略可直接迁移到Agent类交互系统，在reward中加权核心意图覆盖率、用户交互成本，平衡个性化效果和用户负担

  - 无侵入的输入层优化思路可直接落地到现有电商推荐/搜索系统前置环节，无需改动下游召回排序逻辑即可快速提升个性化匹配效果

  - 训练时用图结构做依赖建模、推理时不依赖图的设计，解决了线下依赖标注和线上轻量化部署的矛盾，适合工业级大规模落地'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前深度研究Agent（DRA）的个性化方案大多需要改造内部检索、合成链路，无法适配闭源商业黑盒DRA；现有主动澄清类方案仅聚焦补全任务缺失信息，未平衡个性化因子覆盖度、证据获取成本（用户提问/历史记忆检索）、因子间依赖关系三者的协同决策，普遍存在用户提问冗余、个性化匹配度低的问题，难以落地到实际交互场景。

### 方法关键点
- 提出两阶段训练框架G-STEER：线下构造Intent Elicitation Graph（IEG）建模用户个性化因子的激活依赖关系，生成覆盖不同证据场景、因子组合、终止条件的轨迹数据用于SFT warm-up，让模型学会三大决策：判断哪些个性化因子相关、现有证据是否充足、下一步该检索记忆/提问用户/终止优化。
- 第二阶段采用目标锚定的GRPO强化学习优化，奖励函数同时加权高重要度因子覆盖率、误匹配惩罚、交互成本（用户提问权重高于内存检索）、重复/多目标提问惩罚，平衡效果和用户负担。
- 推理阶段完全不需要依赖IEG，模型自动维护因子证据状态，生成的优化后查询可直接输入下游黑盒DRA，无侵入适配任意现有系统。

### 关键结果
在PDR-Bench数据集上对比7个基线方案：加权目标覆盖率WCov达0.4253，较最优基线提升4.7%；平均用户提问量仅4.1次，为强基线CEP-Clarify+Rewrite的1/3；下游黑盒OpenAI DRA、开源OAgents的报告个性化得分分别达4.35、5.70，均为所有方案最高。

> 最值得记住：对黑盒系统的个性化优化，在输入层做轻量化的意图澄清和证据落地，ROI远高于改造系统内部链路
