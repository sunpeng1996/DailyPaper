---
title: 'CultureConverse: A Multilingual Multi-turn Simulation Harness for Culturally
  Grounded Assistance in East and Southeast Asia'
title_zh: CultureConverse：面向东亚东南亚的多语言文化对话评测框架
authors:
- Bryan Chen Zhengyu Tan
- Weihua Zheng
- Thong T. Doan
- Bich Ngoc Doan
- Jia Wang Peh
- Xiaoyuan Yi
- Jing Yao
- Xing Xie
- Nancy F. Chen
- Zhengyuan Liu
affiliations:
- Singapore University of Technology and Design (SUTD)
- Agency for Science, Technology and Research (A*STAR)
- Microsoft Research Asia (MSRA)
- Nanyang Technological University (NTU)
- Kyoto University
arxiv_id: '2608.28405'
url: https://arxiv.org/abs/2608.28405
pdf_url: https://arxiv.org/pdf/2608.28405
published: '2026-08-28'
collected: '2026-08-31'
category: Eval
direction: LLM评测 · 文化适配多轮对话基准构建
tags:
- Multilingual Evaluation
- Cultural Alignment
- Multi-turn Dialogue
- LLM Benchmark
- Dialogue Simulation
one_liner: 推出覆盖10个东亚东南亚区域的多轮文化适配对话评测基准与数据集
practical_value: '- 做跨区域出海电商Agent时，可复用该数据集的多区域文化约束规则库，优化多轮交互的文化合规性，降低客诉风险

  - 可借鉴其「模拟用户-助手多轮交互+自动打分」的评测框架，搭建自有Agent能力自动化评测pipeline，大幅降低人工标注成本

  - 小样本微调该数据集的高质量样本，可同时提升域内文化交互效果和跨域文化安全分类能力，适合出海业务快速迭代'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM文化能力评测多采用单轮选择题做事实召回，无法覆盖真实场景中用户多轮求助的文化适配需求，尤其缺乏东亚东南亚区域的针对性评测方案。
### 方法关键点
推出可扩展的多语言多轮文化适配对话模拟评测框架CultureConverse，覆盖10个东亚东南亚区域、58个子群体身份、7个业务领域，交互过程中会基于助手从部分信息推断文化约束的表现自动打分；配套开源CultureConverse-DS数据集，包含14610条基准评测样本、274295条oracle引导的黄金对话。
### 关键结果数字
18个参测模型中GPT-5 mini的文化辅助质量最高；人工标注验证评测框架与人类判断一致性达标；基于27860条高质量样本微调后，域内文化辅助效果提升，同时可迁移到文化选择题、安全分类等域外任务。
