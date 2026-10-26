---
title: 'Shorter Is Not Cheaper: A Controlled Comparison of Declarative Animation Specifications
  and Free-Form Code for LLM-Generated Explanations'
title_zh: 更短不等于成本更低：LLM生成解释的声明式动画与自由代码对比
authors:
- Jiantang Huang
affiliations:
- Northeastern University
arxiv_id: '2610.32129'
url: https://arxiv.org/abs/2610.32129
pdf_url: https://arxiv.org/pdf/2610.32129
published: '2026-10-23'
collected: '2026-10-26'
category: LLM
direction: LLM输出格式 · 推理开销与可靠性评估
tags:
- LLM Generation
- Output Format
- Reasoning Cost
- Declarative Specification
- Generation Reliability
one_liner: 通过受控对照实验推翻了LLM用更短声明式格式生成解释成本更低速度更快更可靠的普遍假设
practical_value: '- 设计LLM输出格式时不能仅核算最终输出token成本，需将推理token开销纳入整体计算，尤其是带思维链能力的模型，避免为压缩输出长度反而拉高整体推理成本

  - 业务中若用LLM生成交互组件（如电商商品动效、推荐理由可视化），优先选择模型预训练覆盖的自由格式（如HTML/JS），尽量不用仅通过上下文学习的自定义声明式格式，可靠性更高

  - 对生成延迟敏感的业务场景，不要盲目选择短输出格式，实测发现输出长度缩短不代表生成速度加快，需压测不同格式的端到端耗时再做选型'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
行业普遍认为LLM生成更短、约束性更强的声明式格式，比自由格式代码成本更低、速度更快、可靠性更高，该假设缺乏严格受控实验验证。
### 方法关键点
设计时间索引的声明式动画格式ExplainSpec与可程序化校验的观测协议，覆盖5个领域共20个解释生成请求，测试3个Claude模型（共360次任务）、开源Qwen3-14B（开启/关闭推理，共240次任务）在两种输出格式下的表现，实验假设与分析方案提前预注册。
### 关键结果
- 声明式格式输出token比自由格式短25~48%，但开启推理后仅最大的Claude模型总输出token显著下降，所有模型生成速度无显著提升
- 大尺寸Claude模型生成声明式格式时推理token占比从15~20%升至85~88%；Qwen3-14B两种格式推理token长度接近，推理trace是输出的2倍以上，节省的输出token几乎可忽略
- 可靠性方面自由格式经1轮修复后准确率达95~100%，Qwen3-14B生成的声明式格式仅33%有效，语义测试通过率仅17%（自由格式为62%）
