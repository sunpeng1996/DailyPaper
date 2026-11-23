---
title: 'PURE: A Diagnostic Benchmark for Multi-Granularity Multimodal Identity Matching'
title_zh: PURE：面向多粒度多模态身份匹配的诊断基准
authors:
- Hengyu You
- Xintong Wang
- Jin Cao
- Liang Ding
affiliations:
- Alibaba Group
arxiv_id: '2611.22343'
url: https://arxiv.org/abs/2611.22343
pdf_url: https://arxiv.org/pdf/2611.22343
published: '2026-11-16'
collected: '2026-11-23'
category: Eval
direction: 多模态身份匹配 · 评测基准
tags:
- Multimodal Matching
- Benchmark
- E-commerce
- MLLM
- Evaluation
one_liner: 推出电商场景多粒度多模态身份匹配诊断基准，可拆解4维度能力定位模型短板
practical_value: '- 电商SPU/SKU/同款分层匹配场景可复用PURE的4维度能力拆解框架，定位现有匹配模型的短板，针对性优化

  - 多模态商品匹配任务可参考基准的细粒度标注逻辑，区分基础款/变体款匹配规则，提升标注数据质量

  - 基于MLLM做商品匹配时，可重点优化视觉差异定位、变体层级规则判断两个薄弱模块，优先提升Judgment维度能力'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
电商场景多模态身份匹配结果依赖目标粒度（基础款/变体款），传统聚合准确率无法拆解模型各环节能力短板，缺乏针对性诊断工具。
### 方法关键点
推出PURE诊断基准，覆盖Perception、Understanding、Reasoning、Evidence-grounded Judgment 4个能力维度，包含14个任务共1457道来自真实业务的匹配选择题，经2位领域专家校验。
### 关键结果数字
测试10款最新MLLM，整体得分区间47.1%~86.0%；其中Understanding维度平均得分最高，Judgment维度得分最低，视觉差异定位、变体层级规则判断是普遍短板；模态消融实验显示多模态证据能提升效果，但模型易误判匹配记录间的冲突；基础款匹配下模型识别正样本更准确，变体款匹配下识别负样本更准确。
