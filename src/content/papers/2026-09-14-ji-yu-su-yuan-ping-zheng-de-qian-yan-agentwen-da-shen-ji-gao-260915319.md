---
title: 'Clean Scores, Buried Evidence, and Confident Wrong: A Receipt-Based Audit
  of Frontier Agentic QA'
title_zh: 基于溯源凭证的前沿Agent问答审计：高分下的隐藏证据误判问题
authors:
- Luis M. Sánchez
affiliations:
- Toryx Inc.
arxiv_id: '2609.15319'
url: https://arxiv.org/abs/2609.15319
pdf_url: https://arxiv.org/pdf/2609.15319
published: '2026-09-14'
collected: '2026-09-16'
category: Agent
direction: Agent 问答系统可解释性审计
tags:
- Agentic QA
- Evaluation
- Provenance
- Hallucination
- Confidence Calibration
one_liner: 通过带噪声的金融文档审计实验，证明现有Agent基准高估实际能力，提出凭证级审计规范
practical_value: '- 做电商合规审核、商品资质核查等高责任Agent应用时，不要依赖模型自报告的confidence，必须给每个输出结论绑定可第三方核验的来源receipt，避免高置信幻觉带来的合规风险

  - 内部Agent基准测试必须加入「证据埋入噪声」的测试组，仅测试黄金上下文的基准会严重高估模型真实业务表现，还会掩盖不同模型的成本-效率差异

  - 用多模型ensemble降低风险的方案要谨慎，不同前沿模型的错误存在正相关性，47%的错误会被≥4/6的模型同时命中，无法通过投票完全规避

  - 做多跳推理Agent的效果评估时，必须提前锁定评分规则、做盲审校验，可复现的评分逻辑不代表正确语义匹配，易出现错判误导模型选型'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前Agent基准测试普遍提供干净的黄金上下文，和真实业务中证据埋藏在大量噪声文档里的场景完全不符，且模型高置信幻觉、输出与来源脱节的问题无法通过传统准确率、置信度校准指标捕捉，在金融、合规等高责任场景下会带来严重风险。
### 方法关键点
- 构建全人工标注的金融文档数据集room02，包含41个2~5跳的多跳问答任务，所有事实都有明确来源，支持溯源；
- 测试6家头部厂商的旗舰大模型Agent，设置两组对照：clean组仅挂载含答案的文档，buried组挂载全量含噪声的文档库，Agent自主调用shell、grep等工具检索；
- 设计claim级的receipt审计机制，要求每个结论都能追溯到具体文档片段，而非仅看最终答案准确率，同时评估工具调用量、单正确答案成本、置信度校准等多维度指标。
### 关键结果
- 从clean到buried场景，6家模型准确率下降4.1~17.8pp，单正确答案成本上升1.6~7.0倍，工具调用量提升1.6~3.2倍；
- 72%的错误答案模型自报告置信度≥80分，传统置信度校准完全无法规避“自信错误”问题；
- 干净场景下6家模型准确率差距仅6.5pp，buried场景下4~5跳任务的准确率差距拉大到13.9pp，基准区分度显著提升。
### 核心结论
模型自报告的置信度不是凭证，可独立核验的来源链路才是高责任Agent应用的核心可靠性保障
