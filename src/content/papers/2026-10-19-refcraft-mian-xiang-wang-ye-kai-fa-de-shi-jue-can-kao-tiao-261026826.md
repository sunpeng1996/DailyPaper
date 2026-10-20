---
title: 'RefCraft: Benchmarking Visual-Reference-Conditioned Agentic Generation through
  Web Development'
title_zh: 《RefCraft：面向网页开发的视觉参考条件智能体生成基准》
authors:
- Yuchi Wang
- Rongyao Fang
- Weihao Yu
- Xilin Wei
- Tiancheng Gu
- Dingkang Yang
- Hang Zhang
- Dayiheng Liu
- Hongsheng Li
- Shuai Bai
affiliations:
- MMLab, CUHK
- Alibaba Token Foundry
- Fudan University
- The University of Sydney
- The Chinese University of Hong Kong
arxiv_id: '2610.26826'
url: https://arxiv.org/abs/2610.26826
pdf_url: https://arxiv.org/pdf/2610.26826
published: '2026-10-19'
collected: '2026-10-20'
category: Agent
direction: 智能体能力评估 · 多模态视觉参考生成
tags:
- Agent Benchmark
- Multimodal LLM
- Visual Reference
- Web Development
- Agentic Generation
one_liner: 构建含300个真实网页开发任务的基准，测评多模态智能体基于视觉参考的生成能力
practical_value: '- 做生成式页面/商品详情页Agent的团队可复用双轨评估方案：程序判断确定性规则（如颜色、交互逻辑）+ VLM判断感知类要求（如风格匹配度），大幅降低人工评估成本

  - 多参考融合的生成任务可借鉴「需求拆分为独立可验证keypoint」的方法，避免开放生成的评估歧义，尤其适配电商场景下复用多个参考设计元素的需求

  - 智能体迭代优化可参考本研究的能力瓶颈结论：交互属性迁移、参考属性适配（而非直接复制）是当前模型的薄弱点，可针对性做数据增强或prompt优化'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有AI Agent基准多聚焦纯文本指令生成或单目标重建，与真实开发场景中「基于多个视觉参考选择性复用/修改设计元素」的主流 workflow 差异大，缺乏可量化的测评方案来评估智能体结合视觉参考完成复杂生成任务的能力。

### 方法关键点
- 构建300个覆盖电商、教育、媒体等8大领域的网页开发任务，每个任务搭配1-5个带交互状态的视觉参考截图，要求智能体在「渲染-检查-迭代」的闭环中完成任务
- 评估体系将需求拆分为独立可验证keypoint，采用双轨判断：程序自动验证确定性要求（如响应式布局、交互逻辑、色值偏差），VLM评估感知类要求（如风格匹配、元素布局一致性）
- 最终得分取基础keypoint完成率、核心功能可用性、参考遵循度三者的最小值，避免平均得分掩盖核心能力缺陷

### 关键实验结果
测评9个前沿(M)LLM（含GPT-6 Astra、Qwen3.8-Max、 Claude Fable 5等），最强的GPT-6 Astra整体得分仅52.12/100；无参考输入时GPT-6 Astra得分骤降34.8分，迭代优化可带来4.7分提升；视觉维度中交互属性迁移得分最低（仅43.6），需求类型中参考属性适配（adapt）难度最高。

### 核心结论
当前前沿模型已能完成大部分单点设计要求，但同时满足核心功能可用、参考遵循度符合预期的端到端生成能力仍有巨大提升空间。
