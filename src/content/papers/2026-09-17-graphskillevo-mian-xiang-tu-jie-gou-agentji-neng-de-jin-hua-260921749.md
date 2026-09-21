---
title: 'GraphSkillEvo: Evolutionary Optimization of Graph-Structured Agent Skills'
title_zh: GraphSkillEvo：面向图结构Agent技能的进化优化框架
authors:
- Rui Sun
- Zhi Zheng
- Zhenkun Wang
- Zhichao Lu
affiliations:
- City University of Hong Kong
- National University of Singapore
- Southern University of Science and Technology
arxiv_id: '2609.21749'
url: https://arxiv.org/abs/2609.21749
pdf_url: https://arxiv.org/pdf/2609.21749
published: '2026-09-17'
collected: '2026-09-21'
category: Agent
direction: Agent 技能优化 · 进化算法
tags:
- LLM Agent
- Skill Optimization
- Evolutionary Algorithm
- Graph Structure
- Cross Model Transfer
one_liner: 将Agent技能表示为图结构并用进化算法优化，大幅提升小模型执行效果与优化效率
practical_value: '- 电商场景Agent任务（如客服流程执行、商品信息抽取、售后问题处理）可直接复用图结构技能表示，将拆分的执行节点与条件分支显式建模，降低小模型执行长指令的出错率

  - 技能迭代优化可替换原有的纯LLM自反思流程，引入小种群（如N=4）的进化算子，通过交叉、突变组合不同优质技能的组件，用更少token消耗获得更高性能提升，尤其适合边缘侧小模型部署场景

  - 优化后的图结构技能支持跨模型迁移，无需为不同算力层级的模型单独训练技能，可降低业务中多模型部署的技能维护成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能多为无结构自然语言，存在两个核心问题：一是长指令缺乏明确工作流引导，小模型难以准确执行；二是无约束文本的搜索空间冗余大，纯LLM自反思的技能优化效率低、收敛差，难以发现最优流程。

### 方法关键点
- 提出图结构技能表示：每个技能由全局通用指导、执行节点（含单步操作规则与约束）、有向边（含场景触发的工作流跳转逻辑）三部分组成，消除指令冗余，显式给出不同场景下的执行路径
- 设计GraphSkillEvo进化优化框架：维护4个候选技能的种群，基于执行失败轨迹分别设计全局指导突变、图结构突变、全局指导交叉、图结构交叉4种算子，每轮保留验证集上最优的4个技能迭代5轮
- 新增图结构校验环节，确保生成的技能符合格式要求，避免无效结构的干扰

### 关键实验
在SearchQA、SpreadsheetBench等5个覆盖问答、工具操作、交互决策的Agent基准上对比SkillOpt等基线：1）比SkillOpt平均精度提升4.01%（GPT-5.4-nano）、1.76%（GPT-5.4），SpreadsheetBench等流程类任务提升最高达10.6%；2）优化阶段token消耗仅为SkillOpt的75%左右；3）小模型优化的技能可直接迁移到大模型使用，部分场景性能甚至超过大模型直接优化的技能。

**最值得记住的一句话：** 将技能的流程结构与文本内容解耦，用结构化搜索空间替代无约束文本优化，是提升Agent技能质量与优化效率的核心抓手。
