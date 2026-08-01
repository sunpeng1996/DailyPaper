---
title: Can Large Language Models Execute Parent Orders?
title_zh: 大语言模型能否完成算法交易母订单执行任务
authors:
- Zane Shen
- Xinli Xu
- Guangyi Zhang
- Jialong Chen
- Jinsong Zhou
- Cong Chen
- Guibao Shen
- Dongyu Yan
- Luozhou Wang
- Zhen Yang
affiliations:
- Independent Researcher
- HKUST(GZ)
- ZJU
- SYSU
arxiv_id: '2607.28410'
url: https://arxiv.org/abs/2607.28410
pdf_url: https://arxiv.org/pdf/2607.28410
published: '2026-07-29'
collected: '2026-08-01'
category: Other
direction: LLM 算法交易母单执行策略优化
tags:
- LLM
- Hierarchical Framework
- Algorithmic Trading
- Decision Making
- Zero-shot
one_liner: 提出无需显式市场假设与任务特定训练的分层LLM母单执行框架PACE，效果优于现有各类基线
practical_value: '- 复杂动态场景决策可借鉴分层拆解思路：将长周期任务拆分为长horizon规划+短horizon执行模块，降低任务难度，无需场景强假设也能落地

  - 对动态变化的业务场景（如大促流量下的广告出价、库存分配），可复用无场景预定义假设、无需任务特定训练的LLM决策范式，降低适配新场景的成本

  - 搭建LLM决策系统时可加入置信度评估环节，高置信度输出直接执行、低置信度转人工兜底，提升整体决策效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
母单执行是算法交易核心任务，需将大额订单拆分为小额订单降低执行成本，现有方案要么依赖可能不成立的预设市场假设，要么需要任务特定训练、对新场景适配性差。

### 方法关键点
提出分层框架PACE，将母单执行任务拆解为长周期规划和短周期执行两个阶段，无需显式市场假设也不需要任务特定微调，是首个系统性将LLM应用于母单执行的工作，将LLM在金融领域的应用从「交易什么」拓展到「如何执行交易」。

### 关键结果数字
在深交所Level-1数据上实验，PACE效果优于TWAP、Almgren-Chriss及学习类基线，比最强基线表现高0.65bps；行为分析显示LLM决策逻辑与人类交易者差异显著：模型置信度越高表现越好，且模型倾向于更早执行交易而非拖延到截止期，可作为人类交易员的决策补充。
