---
title: 'Reproducing human biases in route choice using large language models: Toward
  scalable behavioral modeling'
title_zh: 基于大语言模型复现路径选择中的人类偏差：面向可扩展行为建模
authors:
- Jiangtao Han
- Shoufeng Ma
- Shuxian Xu
- Geng Li
- Shuai Ling
- Ning Jia
- Zhengbing He
affiliations:
- Laboratory of Computation and Analytics of Complex Management Systems (CACMS), Tianjin
  University
- College of Management and Economics, Tianjin University
- Faculty of Science and Engineering, University of Nottingham Ningbo China
arxiv_id: '2607.11632'
url: https://arxiv.org/abs/2607.11632
pdf_url: https://arxiv.org/pdf/2607.11632
published: '2026-07-13'
collected: '2026-07-14'
category: Agent
direction: Agent 人类决策行为模拟建模
tags:
- LLM
- Behavioral Modeling
- Cumulative Prospect Theory
- Generative Agent
- Decision Simulation
one_liner: 验证通用LLM无需显式配置前景理论参数即可复现人类决策偏差，支撑大规模Agent模拟
practical_value: '- 搭建用户行为模拟Agent系统时，可直接用通用LLM替代传统参数化前景理论模型，省去个体级参数校准所需的高成本调研与实验工作

  - 电商/推荐场景的用户决策仿真（如促销路径选择、多商品对比决策模拟）可复用该思路，快速生成多样化非完全理性用户行为样本

  - 构建大规模多Agent仿真系统时，可直接基于通用LLM搭建用户决策模块，无需额外微调即可适配不同场景的行为偏差复现需求'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统基于累积前景理论（CPT）的非完全理性人类决策建模，需通过调研、受控实验校准个体级CPT参数，泛化性差、无法覆盖人类决策多样性，是大规模Agent模拟落地的核心瓶颈。

### 方法关键点
选取路径选择为典型决策场景，设计轻量化行为评估框架，直接调用通用LLM输出决策结果，与CPT预测的成熟人类行为模式做系统性对齐校验，全程无需为LLM显式注入任何CPT相关参数规则。

### 关键结果
实验验证LLM可稳定复现人类非完全理性选择偏差，其决策行为与不确定性下的前景理论各类效应高度匹配，可替代传统参数化CPT模型，为大规模多Agent仿真、AI驱动的行为研究提供可扩展的技术路径。
