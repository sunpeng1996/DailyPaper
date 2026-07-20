---
title: 'Before the Action: Benchmarking LLMs on Prospective Hypothesis Discovery'
title_zh: 行动前决策：大语言模型前瞻性假设发现能力基准测试
authors:
- Tianyun Zhong
- Wangyi Jiang
- Wei Wang
- Xuanang Chen
- Yaojie Lu
- Shiwei Ye
- Yuzhen Shi
- Boyu Yang
- Jinghang Wang
- Han Li
affiliations:
- University of Chinese Academy of Sciences
- Institute of Software, Chinese Academy of Sciences
- Alibaba Group
arxiv_id: '2607.15766'
url: https://arxiv.org/abs/2607.15766
pdf_url: https://arxiv.org/pdf/2607.15766
published: '2026-07-17'
collected: '2026-07-20'
category: Eval
direction: LLM推理能力评测 · 开放场景假设生成
tags:
- LLM Evaluation
- Hypothesis Discovery
- Open-ended Reasoning
- Benchmark Dataset
- Reasoning
one_liner: 提出前瞻性假设发现任务与HypoArena基准，实现LLM开放探索推理能力的细粒度评测
practical_value: '- 可复用HypoEval的双向pairwise排序+BTD聚合评估框架，解决生成式推荐文案、Agent开放决策等开放式输出无统一评测标准的痛点

  - Retrospective Context Regression数据构造pipeline可直接迁移，用于从已结案的业务异常（如推荐点击率突降、广告转化波动）数据中生成无结论的训练/评测样本

  - PHD能力分层结论可指导业务Agent底座选型：复杂根因排查、未知用户需求挖掘场景优先选择PHD排名靠前的LLM，可提升探索效率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM能力评测多聚焦于预设问题的解答效果，针对开放无结论场景下（如异常排查、未知领域探索）的自主假设生成能力缺乏系统性度量标准。

### 方法关键点
1. 定义Prospective Hypothesis Discovery（PHD）任务，要求模型从零散非结论性证据（异常观测、碎片化记录）中自主构造可落地、可区分、可验证的假设集合，指导后续调研；
2. 推出HypoArena评测套件：含覆盖6个领域的988个标注样本的HypoData基准数据集，以及适配多有效输出场景的HypoEval评估框架；
3. 采用Retrospective Context Regression流水线规模化构造数据集：从已完成的专家文档中剥离明确结论、目标假设、回溯因果归因，仅保留事实基底；
4. HypoEval结合双向成对判断+Bradley–Terry–Davidson聚合排序+6维度评分规则，同时输出模型排名与能力诊断结果。

### 关键结果数字
测试15个前沿LLM，发现PHD能力分层明显，结构化分析技能对模型效果影响存在异质性；HypoArena排序结果与人类专家一致性高，相比绝对评分可识别更细粒度的模型能力差异。
