---
title: 'RICoT: Recurrent Interleaved Chain-of-Thought for Page Stream Segmentation'
title_zh: RICoT：面向页面流分割的循环交错思维链框架
authors:
- Prashant Khatri
- Bhavana Malagavalli
- Saiful Haq
- Niyati Chhaya
affiliations:
- Hyperbots
- Indian Institute of Technology Bombay
arxiv_id: '2611.22382'
url: https://arxiv.org/abs/2611.22382
pdf_url: https://arxiv.org/pdf/2611.22382
published: '2026-11-17'
collected: '2026-11-18'
category: Reasoning
direction: 大模型推理 · 长序列流分割
tags:
- Chain-of-Thought
- Page-Stream-Segmentation
- LLM-Prompting
- Knowledge-Distillation
- Sequential-Classification
one_liner: 提出循环交错CoT推理框架实现低成本长页面流分割，配套公开金融场景测试基准
practical_value: '- 长序列类业务（用户行为流分段、多轮会话分割、长文档拆分）可复用RICoT的「滑动窗口+跨窗口轻量状态传播」架构，平衡长上下文依赖和token成本

  - 高要求序列决策场景可采用每页/每步推理+决策交错的prompt模式，相比整段CoT推理准确率更高，输出token成本仅增加约30%

  - 大模型prompt方案落地时，可采用「大模型教师标注无标注数据+小模型QLoRA蒸馏」的路径，2B参数模型性能可达大模型prompt版95%以上，推理成本降一个数量级

  - 决策输出可拆分主/子决策维度，下游业务可通过后处理阈值调整适配不同规则，无需重新跑推理'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
现有页面流分割（PSS）方法存在明显缺陷：成对分类仅依赖相邻两页上下文，无法捕捉长距离依赖；全流/固定窗口处理要么token成本随长度飙升，要么受窗口边界限制推理效果。同时现有公开PSS基准缺少真实金融场景数据，商用拆分方案不开源，无法满足企业财务自动化等场景的落地需求。
## 方法关键点
- 自适应滑动窗口：按token预算+页面数上限动态打包页面，单页截断保留首尾信号（前500+后300token），窗口间1页重叠避免边界漏判
- 页级交错CoT推理：窗口内每页先输出推理过程再输出决策，确保决策与页面证据绑定，避免整段推理与局部脱节
- 跨窗口状态传播：传递最近6条推理-决策对和当前活跃片段摘要，突破单窗口上下文限制，支持任意长流处理
- 双轴决策设计：拆分主/子文档边界输出维度，下游可通过后处理调整分割粒度，无需重新推理
- 轻量化蒸馏：用大模型教师输出蒸馏2B小模型，支持推理时开/关CoT两种模式，效果差异极小
## 关键结果
在自研真实金融基准FinancePSS-205上，RICoT比同骨干的成对/窗口prompt基线DocF1最高提升0.154；GLM-5作为骨干时DocF1达0.826，边界F1达0.915。在公开TABME基准上，RICoT+GLM-5的DocF1达0.847，比此前最优零-shot方案高0.144。蒸馏后的Qwen-3.5-2B小模型DocF1仅比最强prompt大模型低0.047，推理成本大幅降低，无需目标域训练数据。
最值得记住的结论：对长序列分类任务，逐样本交错推理+轻量状态传播的设计，可在严格控本的同时大幅超过固定窗口或成对分类基线性能。
