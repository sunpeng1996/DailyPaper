---
title: Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving
  LLM Agents
title_zh: 自进化LLM Agent的评估指标与技能协同演化框架
authors:
- Xing Zhang
- Guanghui Wang
- Yanwei Cui
- Ziyuan Li
- Wei Qiu
- Bing Zhu
- Peiyang He
arxiv_id: '2607.12790'
url: https://arxiv.org/abs/2607.12790
pdf_url: https://arxiv.org/pdf/2607.12790
published: '2026-07-14'
collected: '2026-07-15'
category: Agent
direction: LLM Agent 自进化评估优化
tags:
- LLM Agent
- Self-Evolution
- Evaluation Metric
- Co-Evolution
- Double Ratchet
one_liner: 针对自进化LLM Agent缺可靠评估指标的痛点，提出指标与技能协同演化的双棘轮框架
practical_value: '- 电商智能客服、文案生成等场景的Agent无现成可靠评估指标时，可复用「10条小样本锚定参考集+无标注共识正则」的方案，低成本演化自定义评估指标，无需标注大量训练数据

  - 推荐系统的生成类模块（如商品文案、个性化推荐理由）自迭代时，可复用Double Ratchet协同演化逻辑，让评估规则和生成能力同步升级，避免指标固化带来的效果天花板

  - 上线自进化Agent模块时，可复用「锚定校验+独立外部审计」的安全机制，快速捕获Agent生成迎合旧指标但无业务价值内容的投机问题，降低线上风险'
score: 8
source: arxiv-cs.CL
depth: abstract
---

### 动机
自进化LLM Agent的能力迭代高度依赖可靠评估指标，但多数真实业务场景不存在现成可用的自动评估器，成为Agent落地自迭代能力的核心瓶颈。

### 方法关键点
1. 设计可演化评估指标回路：基于10条锚定参考集训练小缺陷检测器组合，结合无标注输出的共识正则，生成可解释的透明评估指标而非黑盒裁判；
2. 提出Double Ratchet协同演化架构，实现评估指标与生命周期管理的技能迭代回路同步优化；
3. 配套锚定校验+外部审计的安全机制，避免指标演化失效、技能投机取巧。

### 关键结果
在代码生成、企业级text-to-SQL、无参考报告生成任务上，该框架保留了真值/最优人工规则驱动的技能迭代效果的88%~110%；报告生成任务中77%的对比样本里，演化后输出效果优于基线。
