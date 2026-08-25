---
title: 'FormuEvo: LLM-Guided Evolution for Discovering Solver-Efficient Mixed-Integer
  Programming Formulations'
title_zh: FormuEvo：LLM引导的演化框架 发现求解高效的混合整数规划公式
authors:
- Haofeng Yuan
- Jianing Peng
- Jieyi Bi
- Ni Zhang
- Shiji Song
- Zhiguang Cao
affiliations:
- Department of Automation, BNRist, Tsinghua University
- College of Computing and Data Science, Nanyang Technological University
- School of Computing and Information Systems, Singapore Management University
arxiv_id: '2608.23353'
url: https://arxiv.org/abs/2608.23353
pdf_url: https://arxiv.org/pdf/2608.23353
published: '2026-08-24'
collected: '2026-08-25'
category: Other
direction: LLM引导的混合整数规划公式优化
tags:
- MIP
- LLM
- Evolutionary Algorithm
- Operations Research
- Solver Optimization
one_liner: 提出融合求解器诊断、结构化记忆的LLM引导MIP公式演化框架，求解加速最高达5.5倍
practical_value: '- 可复用「下游任务细粒度性能统计作为 verbal gradient 引导 LLM 迭代优化」的思路，适配推荐/广告的规则生成、策略调优场景

  - 结构化记忆抽象可复用策略的设计，可直接迁移到 Agent 任务的历史经验沉淀模块，减少重复探索

  - LLM驱动的交叉、变异、修复的演化操作范式，可用于多候选排序策略、召回规则的自动化迭代'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM自动生成MIP模型仅优先语义正确性，忽略公式的求解效率，严重限制下游求解器性能，成为工业优化场景的核心瓶颈。
### 方法关键点
将MIP公式设计转化为符号空间的演化优化问题，公式被建模为可执行程序，通过LLM驱动的交叉、变异、修复操作迭代生成、评估、筛选更优候选；引入求解器感知的诊断机制，把细粒度求解器统计信息作为verbal gradient做定向优化；新增结构化记忆模块，将历史经验抽象为可复用建模策略，既减少冗余探索，也支持零样本迁移到未知问题，还可用于小LLM冷启动。
### 关键结果
在多类线性/非线性MIP问题上的实验显示，生成的公式性能显著优于专家设计方案和现有LLM方法，求解器速度最高提升5.5×，提炼的知识可在不同问题、不同规模模型间有效迁移。
