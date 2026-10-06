---
title: Word-Level Text Unmixing via Evidence-Preserving Ownership Routing with Language
  Models
title_zh: 基于证据保留归属路由的大模型词级别文本分离方法
authors:
- Jinglin He
- Siyang Jiang
- Lixing He
- Guoliang Xing
- Hongkai Chen
affiliations:
- The Chinese University of Hong Kong
arxiv_id: '2610.06603'
url: https://arxiv.org/abs/2610.06603
pdf_url: https://arxiv.org/pdf/2610.06603
published: '2026-10-05'
collected: '2026-10-06'
category: LLM
direction: 大模型文本分离 · 约束解码与归属路由
tags:
- LLM
- Constrained Decoding
- Text Unmixing
- Evaluation Benchmark
- Ownership Routing
one_liner: 提出EPOR框架实现多源交错文本词级精确分离，配套UNMIXBENCH评测基准
practical_value: '- 可复用EPOR「归属预测+内容重构解耦」思路，优化多Agent并发对话流拆分场景，完全避免生成式方法的丢消息、重复、幻觉问题

  - 约束解码+确定性索引重构的技术方案可直接迁移到搜索Query多意图拆分、用户交错会话行为序列拆分任务，保证原始数据100%保留

  - 精确重构的MP-WER评估方法可复用在推荐系统用户行为多源归因任务的效果评测，替代传统生成式评估指标减少偏差'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
多源交错文本（如重叠语音转写、并发Agent流、文档阅读流）丢失元数据后，需精确拆分出各源原始序列，现有LLM直接生成拆分结果易出现漏词、重复、幻觉，无法满足所有词精确保留、源内顺序完全一致的要求。
### 方法关键点
提出EPOR框架，解耦源归属预测和序列重构：训练阶段让因果LLM基于混合流和历史路由决策预测归属路径，不进行文本生成；推理阶段结合补全安全的约束解码+确定性索引重构，保证每个观测token恰好出现一次、源内顺序正确。同时发布UNMIXBENCH评测集，覆盖合成混合文本、AMI/ICSI语音流、ReadingBank文档流、模拟并发数字输出共5类评测轨道。
### 关键结果
4B参数EPOR模型在5个评测轨道的平均最小排列词错误率（MP-WER）为所有微调基线最低，相对紧凑源数组生成方法相对降低22.3%，性能与零-shot前沿大模型相当。
