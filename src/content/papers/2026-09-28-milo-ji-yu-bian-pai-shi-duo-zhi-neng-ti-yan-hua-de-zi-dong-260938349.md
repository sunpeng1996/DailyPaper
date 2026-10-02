---
title: 'MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution'
title_zh: MILO：基于编排式多智能体演化的自动化Harness发现框架
authors:
- Prithwish Jana
- Mononito Goswami
- Hao Liu
- Xinyu Li
- Langlin Huang
- Zhehui Huang
- Zhishen Huang
- Patrick Blöbaum
- Anoop Deoras
- Purak Jain
affiliations:
- Georgia Institute of Technology
- AWS AI Labs
- Carnegie Mellon University
- Washington University in St. Louis
arxiv_id: '2609.38349'
url: https://arxiv.org/abs/2609.38349
pdf_url: https://arxiv.org/pdf/2609.38349
published: '2026-09-28'
collected: '2026-10-02'
category: Agent
direction: 多智能体协作 · Agent Harness自动优化
tags:
- MultiAgent
- EvolutionarySearch
- AgentHarness
- MetaEvolution
- AutoOptimization
one_liner: 提出元演化多智能体框架MILO，自动化发现Agent最优Harness，性能与效率均大幅超越现有SOTA
practical_value: '- 业务Agent优化可跳过高成本模型微调，复用MILO多岛演化思路自动迭代Harness层（prompt、工具调用逻辑、控制流等），投入产出比远高于模型训练

  - 演化搜索可复用其负向记忆设计：留存所有失败Harness变体与执行trace，指导mutator规避重复错误，大幅提升搜索效率，适合电商导购、客服Agent的Harness迭代

  - 多目标（准确率+token消耗+延迟）Pareto准入规则可直接复用，平衡业务效果与推理成本，适配推荐/广告场景低延迟、高吞吐要求

  - 搜索停滞时的Orchestrator干预逻辑（更换mutator、跨岛嫁接、物种分化、课程调整）可迁移到推荐超参调优、召回策略迭代等场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
Agent性能由底层模型和Harness层（控制流、prompt、工具调用逻辑、记忆规则等）共同决定，Harness优化成本远低于模型训练却能带来同等收益，但手工设计Harness依赖专家经验、迭代效率低，且随模型升级需反复调整；现有自动Harness搜索方法存在探索空间有限、易陷入局部最优、无法利用失败案例等问题。

### 方法关键点
- 分层谱系记忆：采用岛式树结构存储所有生成的Harness变体（含被拒的失败样本），记录每个变体的评估结果、编辑路径、执行trace，用失败突变作为负向证据剪枝无潜力的搜索路径
- 岛级mutator智能体：每个演化岛分配专属mutator，结合全局搜索历史、父Harness的失败反馈重写完整Harness，支持从局部修复到结构重设计的全范围修改
- 编排器Agent：当某个演化岛连续多轮无收益时，自动诊断停滞原因，通过跨岛嫁接优秀变体、拆分独立子谱系为新岛、重分配mutator、调整任务课程（优先搜索高收益任务）自适应优化搜索策略
- 双循环架构：内循环按多目标Pareto增益（准确率、token消耗、延迟）准入新Harness，外循环动态调整搜索策略，平衡探索与利用

### 关键实验
在Terminal-Bench 2.1、PaperBench、DeepSWE三个长程任务基准测试，对比8个SOTA手工Harness和6个自动搜索方法：采用Opus 4.8 backbone时，较初始Harness分辨率率分别提升12.0%、28.3%、10.3%，远超此前最优搜索方法的4.5%、18.3%、0%；Terminal-Bench 2.1上达到86.1±2.0%，超过官方榜单Top1的83.8±2.3%，同时token消耗降低26%；采用开源gpt-oss-120b backbone在DeepSWE上达到15.6%，是初始Harness的20倍，此前方法结果均低于1%。

### 核心洞见
优化Agent的Harness层成本远低于模型训练，且能带来同等甚至更高的性能收益，自动化元演化搜索是Harness优化的高效路径
