---
title: 'ReproBridge: Building Reproducibility into ML Research Artifacts'
title_zh: ReproBridge：面向机器学习研究工件的可复现性构建框架
authors:
- Yubo Wang
- Rui Meng
- Jaehyun Nam
- Tomas Pfister
- Jinsung Yoon
affiliations:
- University of Waterloo
- Google
arxiv_id: '2611.08452'
url: https://arxiv.org/abs/2611.08452
pdf_url: https://arxiv.org/pdf/2611.08452
published: '2026-11-05'
collected: '2026-11-06'
category: Agent
direction: Agent 实验复现工作流优化
tags:
- AgentWorkflow
- Reproducibility
- MLArtifact
- CodeAgent
- Benchmark
one_liner: 提出标准化可复现工件规范与Agent构建流程，提升ML实验复现成功率并降低API成本
practical_value: '- 内部算法实验沉淀可复用四组件工件规范（优化代码、环境配置、启动器、复现指南），把推荐/广告模型迭代中的依赖版本、评估逻辑、调参决策等隐式信息显性化，避免后续复盘、新人接手时重复踩坑

  - 设计自动实验类Agent工作流时可参考三阶段+独立审核机制：Specify明确需求、Execute留痕所有决策、Preserve打包输出，加跨阶段校验可大幅降低Agent执行错误率，减少无效资源消耗

  - 搭建内部算法效果验证基准时可复用5次人工验证+数值兼容区间的评估方法，降低单次实验随机性对结论的干扰，提升推荐/广告离线AB、模型迭代的收益判断准确性'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
ML实验复现需要补全论文、代码、发布工件中大量缺失的隐式细节，现有原始代码通常不包含环境适配、执行逻辑、决策依据等信息，不仅人工复现成本高，编码Agent的复现成功率也高度依赖自身补全能力，重复劳动多、API开销大，且不同模型的复现效果差异极大。
### 方法关键点
- 定义标准化四组件可复现工件（RRA）：优化后代码库、环境配置脚本、实验启动器、复现指南，完整留存复现过程中的所有修复、决策逻辑与依据
- 设计ReproBridge Agent工作流：分为Specify（明确实验指标、执行逻辑）、Execute（执行实验并留痕所有调整）、Preserve（打包生成RRA）三阶段，引入独立审核员校验各阶段输出，避免错误传导
- 构建ReproBridge-Bench基准：覆盖36篇论文的387个实验、1029个任务，每个任务配置5次人工验证的参考分数，由独立审计员校验执行证据，避免仅数值匹配但实验逻辑错误的情况
### 关键结果
- 4款编码Agent使用RRA后，平均复现成功率从76.4%提升至92.6%，跨模型成功率差从21.6pp收窄至3.9pp，所有模型成功率均超过90%
- 下游API成本平均降低19.7%，首条成功实验的中位数执行时间最高缩短48%
- 消融实验显示移除代码/环境组件对成功率影响最大（下降5.2/4.5pp），移除指南/启动器也会带来3.8/3.1pp的下降

> 最值得记住的话：实验可复现性的核心不仅是发布代码，更是把复现过程中补全的所有隐式决策、修复逻辑显性化留存，才能大幅降低后续复现的成本与门槛。
