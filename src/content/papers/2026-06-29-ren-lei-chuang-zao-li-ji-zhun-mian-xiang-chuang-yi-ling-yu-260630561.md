---
title: The Human Creativity Benchmark
title_zh: 人类创造力基准：面向创意领域的AI评估框架
authors:
- Aspen Hopkins
- Allison Nulty
- Alexandria Minetti
- Anoop Pakki
- Angad Singh
affiliations:
- Contra
- Massachusetts Institute of Technology
arxiv_id: '2606.30561'
url: https://arxiv.org/abs/2606.30561
pdf_url: https://arxiv.org/pdf/2606.30561
published: '2026-06-29'
collected: '2026-06-30'
category: Eval
direction: 创意AI能力评估 · 专业标注体系
tags:
- Generative AI
- Creative Evaluation
- Human-AI Collaboration
- Benchmarking
- Design Workflows
one_liner: 提出区分专业共识与个体审美差异的创意AI评估基准HCB，覆盖5领域3创作阶段共1.5万份专业标注
practical_value: '- 电商广告创意生成评估可复用「硬规则共识+审美分歧」分层逻辑，合规、卖点对齐等硬指标走统一校验，审美类指标保留多版本输出供选择

  - AI创意Agent工作流设计可参考3阶段（ideation/mockup/refinement）拆分能力要求，不同阶段匹配适配模型，无需追求单一模型全流程最优

  - 广告素材/文案A/B测试可借鉴HCB的标注维度（prompt adherence、usability、visual appeal）设计分层评估指标，避免单一打分丢失优化方向'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有AI评估框架默认将评估者分歧视为需消除的噪声，但创意领域的专业人士分歧多为真实审美差异，并非测量误差，单一质量打分机制会丢失大量有效优化信息。
### 方法关键点
提出HCB评估基准，拆分两类核心信号：一是专业共识（从业者对齐的通用最佳实践要求），二是合理分歧（个体审美差异导致的判断不同）；覆盖5个创意领域、3个创作阶段（构思/原型/打磨），收集1.5万份专业标注，包含pairwise偏好、prompt对齐度/可用性/视觉吸引力量化打分、定性判断理由三类数据。
### 关键结果
共识信号集中在技术正确性、视觉层级等可验证维度，分歧信号集中在审美方向、概念风险等主观维度；无模型可在全流程所有阶段都达到最优表现；将两类信号合并为单一质量分，会丢失「模型哪里必须严格符合要求、哪里需要保留可操控性」的关键 actionable 信息。
