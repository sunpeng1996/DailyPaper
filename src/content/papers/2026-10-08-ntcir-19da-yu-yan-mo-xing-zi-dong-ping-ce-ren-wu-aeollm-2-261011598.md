---
title: Overview of the NTCIR-19 Automatic Evaluation of LLMs 2 (AEOLLM-2) Task
title_zh: NTCIR-19大语言模型自动评测任务(AEOLLM-2)概述
authors:
- Junjie Chen
- Yuxi Dong
- Haitao Li
- Yiqun Liu
- Qingyao Ai
affiliations:
- DCST, Tsinghua University
- Quan Cheng Laboratory
- University of Science and Technology Beijing
arxiv_id: '2610.11598'
url: https://arxiv.org/abs/2610.11598
pdf_url: https://arxiv.org/pdf/2610.11598
published: '2026-10-08'
collected: '2026-10-09'
category: Eval
direction: LLM自动评测 · 长文本生成场景
tags:
- LLM Evaluation
- Long-form Generation
- Automatic Evaluation
- Benchmark
- Research Report
one_liner: 发布NTCIR-19 AEOLLM-2评测任务，聚焦LLM长文本生成及深度研究报告自动评测方法探索
practical_value: '- 可复用AEOLLM-2的长文本评测框架，对电商场景下LLM生成的商品详情页、种草文案、营销活动话术做自动质量校验，大幅降低人工审核成本

  - 深度研究报告的评测指标可直接迁移到Agent生成的用户消费洞察、品类运营调研报告的自动评估，快速对齐人工判断标准

  - 可参考本次评测中参赛队伍的最优实现，优化现有业务中LLM生成内容的自动评测pipeline，提升评测结果与人工标注的相关性'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有LLM自动评测方案多适配短文本场景，针对长文本生成尤其是专业深度研究报告的自动化评测缺乏统一验证基准，难以对齐人工评估标准。此前NTCIR-18 AEOLLM任务已验证了LLM自动评测的可行性，因此推出迭代版本AEOLLM-2进一步拓展场景边界。

### 方法关键点
新增「深度研究评估」子任务，聚焦LLM生成的长文深度研究报告自动评测，要求参赛队伍设计模型自动输出报告质量评分，以人工标注的质量标签为ground truth，通过评分与人工结果的相关性等指标衡量评测方法性能。

### 关键结果
本次任务共收到10支参赛队伍提交的91组有效评测跑批结果，完整公开了数据集构建逻辑、评估指标、参赛技术方案及最终排名，为长文本LLM自动评测提供了公开可复用的行业基准。
