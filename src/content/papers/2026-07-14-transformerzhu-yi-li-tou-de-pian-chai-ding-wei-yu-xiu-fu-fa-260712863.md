---
title: Toward Localizing and Repairing Bias in Transformer Attention Heads
title_zh: Transformer注意力头的偏差定位与修复方法研究
authors:
- Sigma Jahan
arxiv_id: '2607.12863'
url: https://arxiv.org/abs/2607.12863
pdf_url: https://arxiv.org/pdf/2607.12863
published: '2026-07-14'
collected: '2026-07-15'
category: LLM
direction: 大语言模型公平性 · 注意力头偏差修复
tags:
- LLM Fairness
- Attention Head
- Inference Optimization
- Bias Mitigation
- Transformer
one_liner: ROBIN白盒头级公平性调试方法，推理阶段干预偏置子空间，降偏差同时保留LLM性能
practical_value: '- 做LLM4Rec/Agent推理优化时，可借鉴头级子空间剪修思路替代整头归零，在过滤广告/推荐敏感偏置的同时保留排序/生成效果

  - 公平性探针敏感度排序的方法可复用，用于定位搜推场景下影响性别/地域等公平性的模型关键参数模块，减少全量调优成本

  - 推理时干预的思路适配上线场景，无需全模型重训即可快速修复线上已部署LLM/推荐Transformer模型的突发偏差问题'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
Transformer大模型已广泛应用于各业务场景，但现有偏差修复方法多在输入输出层调整或全量重训，成本极高；过往注意力头级别的偏差修复采用整头归零方案，会严重损伤模型原生性能。

### 方法关键点
ROBIN白盒头级公平性调试框架思路为：
1. 基于公平性探针的敏感度排序，快速定位和偏差高度关联的注意力头子集；
2. 仅从选中头的输出中移除极小偏差子空间，而非直接屏蔽整头。

### 关键结果
在4款Transformer模型的测试中，ROBIN可降低所有模型的WinoBias偏差gap，且语言建模性能保留效果显著优于整头归零的基线方案。
