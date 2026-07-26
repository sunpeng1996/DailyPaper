---
title: 'Capital Markets LLM Reliability Score (CM-LRS): From Plausible to Bankable'
title_zh: 资本市场大语言模型可靠性评分（CM-LRS）：从看似合理到合规可用
authors:
- Prerit Ahuja
arxiv_id: '2607.21340'
url: https://arxiv.org/abs/2607.21340
pdf_url: https://arxiv.org/pdf/2607.21340
published: '2026-07-23'
collected: '2026-07-26'
category: Eval
direction: 大语言模型垂直领域合规评估
tags:
- LLM
- Evaluation
- Rubric
- Finance
- Regulatory Compliance
one_liner: 提出覆盖7个合规维度的资本市场LLM工作流输出可靠性评估框架，量化模型落地可行性
practical_value: '- 可复用多维度 rubric 评估思路，针对电商/广告合规场景设计事实准确性、溯源性、可审核性等维度的模型输出评分体系，替代单一准确率指标

  - 针对生成式推荐/Agent 工作流输出做全链路评估，而非仅评估单轮问答结果，更贴合业务实际落地要求

  - 不同业务环节可单独调整评估维度权重，比如召回环节侧重溯源准确性、文案生成侧重合规性，适配不同模块的评估需求'
score: 4
source: arxiv-cs.CL
depth: abstract
---

### 动机
金融资本市场对LLM输出的核心要求是可应对监管、对手方核查的合规可用性，现有评估仅聚焦QA层面准确率，未覆盖实际工作流输出的全维度合规要求。

### 方法关键点
提出CM-LRS评估框架，覆盖事实准确性、证据可溯源性、数值一致性、工作流完整性、源数据合规性、决策有用性、可审计性7个维度，每个维度0-5分，总分可根据具体工作流调整权重；在5类资本市场工作流（条款抽取、先例检索、发行人画像合成等）上，用4个独立LLM评委对4款模型输出评分。

### 关键结果数字
1. 闭源前沿模型CM-LRS平均分差仅0.22，Llama 3.3 70B开源模型得分最低（3.15）；
2. 闭源与开源模型差距集中在检索（2.23分差）、合成（2.15分差）环节，抽取环节差距仅0.84；
3. 决策有用性维度跨模型分差最大（最高4.0），评委一致性最高（均值r=0.52）。
