---
title: 'Symbal: Detecting Systematic Misalignments in Model-Generated Captions'
title_zh: Symbal：多模态大模型生成字幕的系统性失配检测框架
authors:
- Maya Varma
- Jean-Benoit Delbrouck
- Sophie Ostmeier
- Akshay Chaudhari
- Curtis Langlotz
affiliations:
- Stanford University
- HOPPR
arxiv_id: '2607.15216'
url: https://arxiv.org/abs/2607.15216
pdf_url: https://arxiv.org/pdf/2607.15216
published: '2026-07-16'
collected: '2026-07-18'
category: Eval
direction: 多模态大模型生成内容偏差评测
tags:
- MLLM
- Caption Generation
- Misalignment Detection
- Evaluation Benchmark
- Model Auditing
one_liner: 提出两阶段无训练的字幕系统性失配检测框架Symbal及配套基准，性能较基线提升近4倍
practical_value: '- 可复用两阶段无训练依赖的偏差检测思路，审计电商场景下MLLM生成的商品文案、推荐理由的系统性错误，无需获取模型权重

  - 系统性偏差与特定输入特征绑定的分析逻辑，可迁移到搜索推荐场景，定位大模型召回/排序结果中与用户属性、item特征关联的重复错误

  - 基准数据集构建方法可参考，用于搭建业务侧生成式内容的自动化评测集，降低人工标注成本'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
MLLM生成图像字幕时频繁出现与特定视觉特征绑定的重复错误（系统性失配），现有方法难以在无模型访问权限的前提下批量识别这类问题，严重影响多模态数据集质量与下游任务效果。
### 方法关键点
Symbal采用双阶段架构，全程调用现成基座模型无需额外训练：第一阶段按视觉特征对图文对聚类分组，第二阶段统计组内错误模式并输出自然语言形式的总结；同时发布SymbalBench评测基准，覆盖170万自然/医疗领域图文对，包含420个带标注的评测数据集。
### 关键结果
Symbal在SymbalBench上的系统性失配识别准确率达63.8%，较最优基线提升近4倍；可准确检测4款主流MLLM生成字幕的系统性错误，可直接用于现成图文数据集的自动化审计。
