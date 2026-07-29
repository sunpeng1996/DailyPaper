---
title: 'HiEviDR-Bench: A Benchmark for Hierarchical Evidence Aggregation in Deep Research'
title_zh: HiEviDR-Bench：面向深度研究场景的分层证据聚合评测基准
authors:
- Yubo Sun
- Chunyi Peng
- Yukun Yan
- Zhenghao Liu
- Sen Mei
- Bangrui Xu
- Xuanhe Zhou
- Chi Chen
- Maosong Sun
affiliations:
- 中国科学院大学
- 东北大学
- 清华大学
- 上海交通大学
arxiv_id: '2607.25151'
url: https://arxiv.org/abs/2607.25151
pdf_url: https://arxiv.org/pdf/2607.25151
published: '2026-07-27'
collected: '2026-07-29'
category: Eval
direction: 大模型评测 · 深度研究Agent证据聚合
tags:
- Benchmark
- Deep Research Agent
- Evidence Aggregation
- Multimodal LLM
- RAG Evaluation
one_liner: 提出带分层证据图的可溯源深度研究评测基准，支持多模态多维度细粒度错误定位
practical_value: '- 电商导购/商品攻略类Agent的效果评估可复用分层证据图+渐进门控范式，避免仅看回复流畅度，漏判引用错误、论据虚标等问题

  - 多模态RAG系统迭代可参考证据溯源三指标（证据召回率、证据节点识别准确率、无关证据过滤准确率）做效果拆解，快速定位召回/排序/生成阶段的瓶颈

  - 高可信度生成场景（如商品测评、选购指南）可引入「证据-中间论点-最终结论」三级结构做生成约束，降低虚假宣传、内容 hallucination 风险'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有深度研究Agent的评测多为结果导向，仅评估最终报告质量、答案正确率，无法定位错误来源是检索失败、推理偏差还是引用失准，也缺乏对多模态证据、分层聚合过程的度量，难以支撑系统的针对性优化。

### 方法关键点
- 为每个查询构建三级有向无环证据图：原子证据节点（支持文本/图像）、中间论点节点、最终结论节点，边代表支持关系，完整记录推理链路
- 设计5维可溯源评估体系：报告质量、证据可溯源性、引用准确率、论点正确性、答案准确率，总分100分
- 新增渐进门控机制：上一阶段（如引用）不达标则后续阶段（如论点、答案）直接计0分，实现细粒度错误定位
- 构建2000条人工验证的数据集，覆盖开放域（维基百科）、学术域（arXiv），分纯文本/多模态、易/中/难三个难度等级

### 关键结果数字
- 测试16款主流MLLM，对比普通RAG和深度研究Agent范式，后者整体得分平均高2-4分，但最优模型Grok-4.5总分也仅41.18分
- 模型报告质量得分普遍在17-19分（满分20），但引用、论点、答案得分骤降，答案阶段通过率仅3.8%~11.5%
- 深度研究Agent的优势不在于召回更多证据，而在于无关证据过滤准确率更高，证据到报告的链接更有效

高表面质量的生成报告不代表真实的证据聚合和推理能力，核心瓶颈在于关键证据识别和中间论点构建。
