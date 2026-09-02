---
title: 'Beyond Scores: Understanding LLM-as-a-Judge Mechanisms in Summarization Evaluation'
title_zh: 超越分数：揭秘摘要评估场景下LLM-as-a-Judge内部运行机制
authors:
- Himil Vasava
- Ming Jiang
affiliations:
- University of Wisconsin-Madison
arxiv_id: '2609.01604'
url: https://arxiv.org/abs/2609.01604
pdf_url: https://arxiv.org/pdf/2609.01604
published: '2026-09-01'
collected: '2026-09-02'
category: Eval
direction: LLM评估 · LLM-as-a-Judge机制拆解
tags:
- LLM-as-a-Judge
- Evaluation
- Interpretability
- Causal Tracing
- Fine-tuning
one_liner: 通过可控扰动与归因实验拆解LLM-as-a-Judge分层评估流程，定位微调引入的核心机制
practical_value: '- 做生成式推荐/商品广告文案自动评估时，可复用论文的8类扰动测试集校验自家LLM评委的鲁棒性，降低错误打分率

  - 微调业务侧LLM评委（如推荐理由质量打分、直播间话术评估）时，可针对性抑制15层以下MLP在最终位置的贡献，加快决策收敛

  - 线上低延迟评估场景下，可在决策结晶层（L25/26）提前截断LLM评委推理，最高可降低30%左右的推理时延'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前LLM-as-a-Judge被广泛用于NLG质量打分、偏好标注、奖励模型训练，但内部打分逻辑为黑盒，鲁棒性、一致性问题无法定位，难以落地高可靠业务评估场景。

### 方法关键点
构建覆盖可读性、充分性两个评估维度的8类扰动攻击体系，生成带可控错误强度、token级修改标记的配对摘要样本；通过因果追踪、logit-lens词汇投影、注意力头敲除4组实验，对Themis（Llama-3-8B）、Prometheus（Mistral-7B）两类主流评委模型做机制拆解。

### 关键结果数字
两类微调后评委均采用两段式评估流程：15层以下注意力做局部错误对比并路由到最终输入位，15层以上MLP整合信号输出评分，决策分别在26层（Themis）、25层（Prometheus）的残差流固化；微调仅新增两个机制：抑制15层以下MLP在最终位的贡献、将决策结晶层提前2层，底层路由架构来自基础模型。
