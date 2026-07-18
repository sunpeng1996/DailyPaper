---
title: 'RetroHolmes: When Semantic Plausibility Fails Retrospective Physical Process
  Reasoning'
title_zh: RetroHolmes：语义合理性失效场景下的回溯式物理过程推理
authors:
- Ruoxuan Zhang
- Qiyun Zheng
- Siyu Wu
- Ling Zou
- Hongxia Xie
- Zhiyu Zhou
- Jian-Yu Jiang-Lin
- Zihan Li
- Zhengguang Wang
- Bin Wen
arxiv_id: '2607.11044'
url: https://arxiv.org/abs/2607.11044
pdf_url: https://arxiv.org/pdf/2607.11044
published: '2026-07-13'
collected: '2026-07-18'
category: Reasoning
direction: 多模态大模型 · 物理推理能力评估
tags:
- Multimodal Reasoning
- VLM Evaluation
- Physical Reasoning
- Benchmark
- Causal Reasoning
one_liner: 提出首个真实世界回溯式物理推理基准RetroHolmes，暴露多模态大模型物理推理系统性缺陷
practical_value: '- 多模态商品推荐/导购场景可复用基准的物理因果校验逻辑，排查生成的商品使用教程、DIY改装方案的可行性，避免语义通顺但物理不可实现的错误内容

  - 落地家装/手工/美食类导购Agent时，可新增「物理可信度中间校验层」，不直接依赖VLM的语义匹配结果，降低错误推荐、错误指导的概率

  - 做多模态模型业务侧评测时，可复用ED1-ED5五维评估框架，补充因果、物理约束类评测维度，避免仅评估语义匹配精度导致的上线后问题'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有VLM评测体系仅关注语义合理性，无法衡量模型是否真正掌握物理因果推理能力，无法检测语义通顺但物理层面不可行的推理错误。
### 方法关键点
1. 推出回溯式物理过程推理新范式，要求模型在明确物理约束下从最终结果反推前置变化过程
2. 开源首个真实场景基准RetroHolmes，覆盖14个领域4类物理转换，包含成对观测图像、可达性标注、完整因果步骤序列
3. 设计5个评估维度：基础因果建模、长程过程建模、信念冲突敏感度、时间可逆性感知、不可逆微观状态动力学
### 关键结果
SOTA VLM存在系统性推理缺陷，Gemini 3 Pro、Qwen3-VL-8B在信念冲突场景的可达性判断准确率不足30%，大量出现物理规则违背、身份识别错误、空间逻辑错误等问题。
