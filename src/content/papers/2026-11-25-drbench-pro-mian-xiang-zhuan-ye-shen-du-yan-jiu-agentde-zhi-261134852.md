---
title: 'DRBench Pro: A Knowledge-Centric Benchmark for Professional Deep Research
  Agents'
title_zh: DRBench Pro：面向专业深度研究Agent的知识中心评测基准
authors:
- Han Huang
- Yuchen Yan
- Xingyu Wu
- Yijun Li
- Chao Deng
- Jie Liu
- Jin Ma
- Yongliang Shen
affiliations:
- Zhejiang University
- Tencent
arxiv_id: '2611.34852'
url: https://arxiv.org/abs/2611.34852
pdf_url: https://arxiv.org/pdf/2611.34852
published: '2026-11-25'
collected: '2026-11-26'
category: Eval
direction: 深度研究Agent · 知识覆盖评测
tags:
- Deep Research Agent
- Benchmark
- Knowledge Coverage
- Topology-aware Metric
- Automatic Evaluation
one_liner: 提出以结构化知识覆盖为核心的深度研究Agent评测基准，可区分报告覆盖的广度与深度
practical_value: '- 可借鉴拓扑感知的广度/深度度量方法，优化电商场景下用户研究Agent、商品调研报告、品类趋势分析报告的内容质量评估，避免仅靠平层得分掩盖内容结构缺陷

  - 复用「知识树采样→联合生成查询与评分规则」的自动化评测集构建流程，大幅降低垂类专业咨询Agent（如美妆/3C品类导购Agent、行业趋势分析Agent）的评测成本

  - 参考本地研究框架的设计，固定检索源、工具权限、交互预算来对比不同LLM底座的信息挖掘能力，可直接用于业务Agent的底座选型与迭代效果验证'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有深度研究Agent评测多聚焦事实性、行文质量等维度，缺乏知识中心的结构化评估逻辑，平层覆盖得分无法区分「广而浅」「窄而深」等不同的知识覆盖模式，且人工构建评测规则的成本高、难以跨领域扩展，无法准确反映Agent的信息挖掘与组织能力。

### 方法关键点
- 自动化构建pipeline：从Wikipedia根实体3跳扩展生成局部知识树，采样子图后联合生成研究查询与证据锚定的评分规则，每条规则对应知识树的一条边，保留结构位置与证据来源；
- 拓扑感知度量：自底向上聚合边的判定结果，广度衡量跨研究方向的覆盖全面性，允许后代节点覆盖部分补偿上层关系缺失；深度衡量知识链的连续覆盖程度，奖励连续性同时对缺失中间节点的情况做折扣，整体得分为二者几何平均；
- 配套本地研究框架：固定Wikipedia快照、工具集、工作流与交互预算，可控对比不同LLM底座的知识覆盖能力。

### 关键实验
基准覆盖24个领域共144个测试用例、44102条评分规则；评测16个深度研究Agent，最优的Claude Opus 5整体覆盖率仅57.04%，仍有较大提升空间；LLM判定与人工标注的Macro-F1达0.893，度量参数扰动下Agent排序的Spearman相关系数不低于0.976，稳定性强。

### 核心结论
相同整体覆盖率的深度研究报告可能存在完全不同的广度/深度trade-off，结构化的知识覆盖评估才能准确反映Agent的信息挖掘能力。
