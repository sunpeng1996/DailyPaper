---
title: 'EvoSkillRec: Skill-Genome Evolution for Recommender Architecture Discovery'
title_zh: EvoSkillRec：基于技能基因组演化的推荐架构自动发现框架
authors:
- Xiaopeng Li
- Kuo Cai
- Bo Chen
- Wenlin Zhang
- Mengyang Ma
- Yingyi Zhang
- Zichuan Fu
- Yu Yang
- Qidong Liu
- Yiyu Wang
affiliations:
- City University of Hong Kong
- Kuaishou Technology
- Xi'an Jiaotong University
arxiv_id: '2609.34552'
url: https://arxiv.org/abs/2609.34552
pdf_url: https://arxiv.org/pdf/2609.34552
published: '2026-09-28'
collected: '2026-09-29'
category: RecSys
direction: 推荐系统 · 架构自动搜索与知识复用
tags:
- AutoML
- NAS
- LLM4Rec
- Architecture Search
- Evolutionary Algorithm
one_liner: 通过双空间演化+可复用技能库实现推荐架构自动搜索与过往优化经验的跨任务复用
practical_value: '- 可复用模块抽象思路：可将业务沉淀的CTR、多任务、多场景推荐成熟模块拆解为带输入输出契约、适用场景、性能历史的可复用组件，替代NAS预定义算子集，降低架构迭代试错成本

  - 双空间优化架构迭代：做模型优化时可拆分「已知组件复用」和「创新模块探索」双路径，日常用成熟组件快速迭代，遇性能瓶颈时分配少量预算给LLM驱动的新模块探索，平衡效率与创新收益

  - 多目标约束搜索适配：对于生成式排序大模型的性能+效率联合优化场景，可直接复用框架的多目标约束演化搜索逻辑，在保证AUC不掉的前提下提升训练/推理MFU'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有推荐架构要么靠专家手动设计迭代效率低，要么NAS搜索被限制在预定义算子空间，近年的LLM驱动代码演化又缺乏架构知识沉淀，有效创新无法跨任务复用，无效修改占比高，难以支撑大规模业务的快速架构迭代需求。

### 方法关键点
- 技能基因组抽象：将成熟推荐模型拆解为原子可执行技能，每个技能带输入输出类型、语义标注、适用场景、实现代码和性能历史，存入双层技能库（Tier1为人工整理的成熟模块，Tier2为演化中验证有效的新发明模块）
- 双空间演化机制：技能空间通过增/替换/杂交/特化已有技能快速生成候选架构，代码空间在遇到性能瓶颈时调用LLM基于失败诊断生成新模块，通过自适应预算分配平衡两个空间的资源投入
- AutoResearch闭环：自动评估候选架构效果，诊断失败原因，将验证有效的新模块沉淀到Tier2技能库供后续迭代复用

### 关键实验
在CTR预测、多任务学习、多域学习三类公开任务上对比手动设计SOTA、NASRec、OpenEvolve三类基线，AUC最高提升0.81%（Amazon Books CTR）、1.26%（Amazon Beauty CTR）；工业级生成式排序场景下同时优化AUC和训练MFU，最优候选在AUC提升0.017%的同时MFU提升0.044个百分点。

最值得记住的一句话：推荐架构迭代的核心是可复用归纳偏置的沉淀，而非从零开始的随机搜索或无约束修改。
