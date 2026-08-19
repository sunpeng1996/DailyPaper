---
title: 'The IOL-AI Challenge: An Open Challenge towards Advancing Linguistic Reasoning'
title_zh: IOL-AI挑战赛：推进大语言模型语言推理能力的开放竞赛
authors:
- Eduardo Sánchez
- Rita Berrada
- Dan-Mircea Mirea
- Sara Rajaee
- Alexander Piperski
- Ana Meta Dolinar
- Boris Iomdin
- Andrey Nikulin
- Mariya Shmatova
- Marzieh Fadaee
affiliations:
- Cohere Labs
- University College London
- Princeton University
- University of Amsterdam
- Stockholm University
arxiv_id: '2608.18011'
url: https://arxiv.org/abs/2608.18011
pdf_url: https://arxiv.org/pdf/2608.18011
published: '2026-08-18'
collected: '2026-08-19'
category: Eval
direction: 大模型通用语言推理能力评测
tags:
- Linguistic Reasoning
- LLM Evaluation
- Benchmark
- Open Challenge
- Reasoning Capability
one_liner: 首次基于国际语言学奥赛未公开题与官方评委打分构建LLM通用推理评测基准与竞赛
practical_value: '- 推理类任务在资源受限场景下，优化解码策略（调低重复惩罚、自适应token预算）、输出处理比提升模型规模性价比更高，可直接复用在搜索query理解、Agent推理链路优化

  - 自动指标和专家打分的排序一致性极高（Spearman ρ=1.00），但自动指标会高估弱系统、低估强系统，做RAG/Agent推理效果评估时可先用自动指标初筛，top结果再人工复核降低成本

  - 针对需要从稀疏样本归纳规则的任务（比如电商新类目语义匹配、小语种广告文案生成），无需强制使用Chain-of-Thought，该类任务中CoT反而会降低效果

  - 自研评测基准时，可参考该竞赛的「未公开测试集+严格沙箱运行」设计，彻底避免数据泄露问题，保障评测结果可信度'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM推理评测集中在数学、代码等给定规则的领域，忽略了「先从稀疏数据归纳规则再推理」的核心通用能力，而过往语言推理基准普遍存在数据泄露、仅靠自动指标打分偏差大的问题，缺乏权威无偏的评测基准。

### 方法关键点
- 联合国际语言学奥赛（IOL）组委会，使用2026年IOL个人赛完全未公开的5道低资源语言推理题作为测试集，彻底规避数据泄露
- 竞赛设置严格算力约束：单T4 GPU、30分钟运行时间，参赛方案需提交完整推理脚本与模型权重，沙箱无网络运行
- 评测采用两层体系：自动评测用ChrF与Exact Match的几何均值打分，top方案额外由IOL官方评委采用和人类选手完全一致的rubric人工打分
- 额外测试15款前沿开源/闭源大模型，覆盖不同参数规模与推理能力

### 关键结果
共收到46支队伍的731份提交，最优14B参数方案效果是同参数基线的2倍，提升全部来自解码与输出处理优化；闭源模型Claude Opus 4.8评委得分79.5，达到IOL金牌水平，排所有人类选手第4名，Gemini 3.6 Flash得分60.5达到银牌水平；自动指标和人工打分排序相关系数达1.00，但自动指标高估弱系统约13分，同时低估强系统的推理分析得分；大模型对测试语言的先验知识对任务效果影响极小，语言推理可作为通用推理能力的无偏代理指标。

### 核心结论
资源受限场景下，推理任务的收益核心来自推理链路与输出优化，而非模型规模提升；当前前沿闭源模型已达到人类顶级语言推理水平，但开源模型仍存在巨大差距
