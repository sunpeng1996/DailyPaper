---
title: 'Reading Decisions Before Spans: Efficient Generative Verification'
title_zh: 生成式核验优化：提前读取决策，无需生成全错误片段
authors:
- Yanbin Gong
- Lei Chen
affiliations:
- ADIA
- The Hong Kong University of Science and Technology (Guangzhou)
- The Hong Kong University of Science and Technology
arxiv_id: '2611.32931'
url: https://arxiv.org/abs/2611.32931
pdf_url: https://arxiv.org/pdf/2611.32931
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: LLM推理优化 · 结构化输出早停
tags:
- Hallucination Detection
- Inference Optimization
- Early Stopping
- Structured Decoding
- Cost Reduction
one_liner: 预填充生成式核验器的固定语法前缀，仅生成决策token即可大幅降本且精度无明显损失
practical_value: '- 电商/Agent系统中的二分类结构化任务（如RAG幻觉核验、广告文案合规校验、UGC审核），可先梳理输出的固定语法结构，将决策前的固定token预填充到输入，仅生成1个决策token，推理成本降80%+且精度无明显损失

  - LLM推理优化不要只追求减少逻辑token总量：将串行生成的固定语法token转移到prompt预填充阶段并行处理，同等逻辑token量下可再省30%左右的推理时间

  - 业务可按需选择生成停止点：仅需告警用PREFILL1，需定位错误用FIRSTQUOTE（生成到第一个错误引用结束），全量分析才用全生成，平衡成本与功能'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
生成式幻觉核验器通常需要输出完整的错误片段、分类等结构化内容，但多数业务场景仅需要「是否存在错误」的二分类告警，全量生成会浪费大量推理资源；直接修改prompt要求输出布尔值会改变模型原生输出契约，易导致精度下降。

### 方法关键点
- 针对输出JSON格式固定的2B参数生成式核验器，定位到决策分支（是否有错误的列表开头符号）前存在7个固定语法token，无需生成
- NATIVE8方案：生成到第8个决策token即停止，跳过后续错误片段生成步骤
- PREFILL1方案：将7个固定语法token直接拼接到prompt输入中，仅需生成1个决策token，无需串行生成固定语法token
- 两种方案均保留模型原生权重和指令，无需微调，仅修改推理阶段的输入拼接和停止逻辑

### 关键实验
在2015条code-agent TEST响应数据集上对比全生成、NATIVE8基线：eager模式下PREFILL1比全生成减少84.84%的服务时间，F1为83.43 vs 全生成的83.41，精度几乎无损失；比NATIVE8进一步节省31.98%的服务时间；编译执行模式下额外收益为6.74%~26.73%，F1波动仅在-0.12到+0.27个百分点之间。

### 核心结论
对固定格式的结构化生成任务，通过预填充固定语法前缀、提前抽取决策分支的方式，可以在几乎不损失精度的前提下实现数量级的推理成本下降。
