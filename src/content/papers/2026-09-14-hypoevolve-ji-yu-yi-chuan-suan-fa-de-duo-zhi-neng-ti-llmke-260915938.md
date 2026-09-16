---
title: 'HypoEvolve: Genetic Algorithms Enable Multi-Agent LLMs to Discover Scientific
  Hypotheses'
title_zh: HypoEvolve：基于遗传算法的多智能体LLM科学假设发现框架
authors:
- Jieyuan Liu
- Mengzhou Hu
- Jefferson Chen
- JungHo Kong
- Pratibha Jagannatha
- Yiming Gao
- Dexter Pratt
- Hsin-Yuan Lee
- Zhiting Hu
- Trey Ideker
affiliations:
- University of California San Diego
- Texas A&M University
- Carnegie Mellon University
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2609.15938'
url: https://arxiv.org/abs/2609.15938
pdf_url: https://arxiv.org/pdf/2609.15938
published: '2026-09-14'
collected: '2026-09-16'
category: MultiAgent
direction: 多智能体协作 · 遗传算法优化
tags:
- Multi-Agent
- Genetic Algorithm
- LLM
- Evolutionary Search
- Hypothesis Generation
one_liner: 用世代遗传算法协调多专用LLM智能体协作，大幅提升科学假设发现质量
practical_value: '- 可直接复用「多智能体分工+遗传算法种群迭代」架构优化推荐/广告场景的创意生成、商品组合选品、营销策略迭代：将交叉算子对应优质候选的卖点/属性组合，变异算子对应单候选的局部调整/方向创新，每代保留Top候选持续迭代，大幅提升优质产出率

  - 「成对比较+Bradley-Terry建模」的打分方案可替代绝对评分，仅需LLM完成两两对比即可得到候选的可靠相对排序，适合文案、创意、小众商品的打分场景，大幅降低标注/人工评估成本

  - 适应度引导的父代选择策略可直接用于冷启动场景的候选迭代：在保证业务算子不变的前提下，该策略可显著提升种群的平均和最低分，降低劣质候选的比例，减少不必要的测试成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前多智能体科学发现系统的性能受智能体本身能力和协作机制的双重影响，二者效果难以拆分，缺乏可控的协作框架可量化不同协作策略的增益；同时科学假设发现需要兼顾证据支撑、可测试性和创新性，现有方法的迭代效率和产出质量均存在明显短板。

### 方法关键点
- 解耦智能体能力与种群搜索规则：基于世代遗传算法构建HypoEvolve框架，LLM智能体负责内容生成、评估、语义变异，算法负责种群选择、迭代规则，可单独调整协作策略验证其效果。
- 定义三类专用LLM智能体：生成Agent基于检索文献初始化假设种群；对比Agent成对评估假设的证据匹配度、可测试性；进化Agent实现语义交叉（合并两个假设的合理机制/灵感启发新假设）和语义变异（替换干预方案/推翻原假设前提）。
- 打分与迭代机制：用Bradley-Terry模型将成对比较结果转化为假设的适应度得分，每代合并父代和子代种群后保留Top μ的优质假设进入下一轮，迭代过程全程可追溯。

### 关键实验
在34种癌症的药物重定位任务上对比6种基线（单轮生成、自一致性、静态重排序、多智能体辩论、Co-Scientist、思维树），DepMap选择性得分达0.171，超过最强基线思维树的0.115；Open Targets关联得分达0.426，超过思维树的0.329，优势在未参与训练的癌症类型上依然泛化。

多智能体系统的性能提升不仅来自单个智能体的能力增强，协作机制的优化同样能带来显著增益，将进化算法与业务语义算子结合是提升LLM系统迭代产出质量的高性价比路径
