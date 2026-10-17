---
title: 'Open Benchmark of AI Impact on Humans (ImpactBench): an expert-guided, open
  platform for the holistic evaluation of AI impact on humans'
title_zh: AI对人类影响公开基准（ImpactBench）：专家引导的全维度AI影响评估平台
authors:
- Chayapatr Archiwaranguprok
- Krystal Kirkland
- Rachel Poonsiriwong
- Stanley Huang
- Constanze Albrecht
- Jackson Trager
- Emillie de Keulenaar
- Sheer Karny
- Peter Baxter
- Nikos Bellos
affiliations:
- MIT Media Lab
- USC Marshall Neely Center
- UC Berkeley Haas School of Business
- Carnegie Mellon University
- Harvard University
arxiv_id: '2610.20690'
url: https://arxiv.org/abs/2610.20690
pdf_url: https://arxiv.org/pdf/2610.20690
published: '2026-10-14'
collected: '2026-10-17'
category: Eval
direction: 生成式AI · 多维度影响评估
tags:
- LLM Evaluation
- Generative AI
- AI Safety
- Benchmark
- LLM Judge
one_liner: 推出专家引导的公开基准ImpactBench，可规模化评估生成式AI对人类多维度福祉的影响
practical_value: '- 可复用「专家规则+LLM judge+抽样人工校验」的评估范式，搭建电商Agent/生成式推荐内容的合规性、用户体验影响评估流水线，降低人工标注成本

  - 借鉴多轮对话模拟+分人群（如青少年/成人/不同消费层级用户）的测试场景设计，更精准评估推荐/Agent服务对不同用户群体的潜在影响

  - 可参考多维度评估指标构建逻辑，针对推荐系统/Agent搭建覆盖消费决策、用户信任、长期满意度等多维度的效果评估体系'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有生成式AI评估缺乏规模化、多维度衡量AI对用户个体福祉影响的统一框架，无法系统判断AI行为对用户心理、生理、社交层面的正向/负向作用。

### 方法关键点
1. 专家引导将领域知识与现有基准转化为可落地的行为观测指标，覆盖正向行为促进、负向危害规避两类；
2. 设计匹配青少年、成人的多轮对话模拟场景，用LLM judge自动评分，搭配可靠性审计与专家复核校验结果；
3. 所有结果公开可追溯，支持基准持续迭代。

### 关键结果
当前基准包含26个现有基准衍生的809项指标，测试10个前沿LLM共48540轮对话，模型正向行为促进达标率68.7%，危害规避达标率仅53.1%；自动评分与专家判断一致率83.3%，Cohen's Kappa=0.667。
