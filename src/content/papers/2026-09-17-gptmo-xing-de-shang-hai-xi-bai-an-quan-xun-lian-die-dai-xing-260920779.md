---
title: 'Harm Laundering in GPT Models: Evidence That Gender Discrimination Is Transformed
  Rather Than Reduced Across Safety-Trained Generations'
title_zh: GPT模型的伤害洗白：安全训练迭代中性别歧视仅被转化未被消除
authors:
- Sarah Wyer
- Sue Black
- Noura Al Moubayed
affiliations:
- Durham University
arxiv_id: '2609.20779'
url: https://arxiv.org/abs/2609.20779
pdf_url: https://arxiv.org/pdf/2609.20779
published: '2026-09-17'
collected: '2026-09-18'
category: LLM
direction: LLM安全评估 · 偏见检测
tags:
- LLM Safety
- Bias Detection
- Gender Fairness
- Safety Alignment
- Harm Evaluation
one_liner: 发现GPT系列安全训练未消除性别歧视，仅将显性伤害转为隐性，提出伤害洗白检测框架
practical_value: '- 业务中使用GPT做文案生成、推荐理由产出时，不能仅用通用毒性检测工具做合规校验，需补充群体代表性公平性校验，避免隐性性别/地域歧视

  - 对齐自研LLM时，需新增代表性伤害维度的评估指标，避免过度修正显性歧视反而导致特定群体的内容多样性下降，例如电商场景女性相关推荐话题窄化问题

  - 可复用论文提出的三阶段伤害洗白检测协议，对业务落地的LLM应用做全链路公平性审计'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM安全评估仅依赖表层毒性分类器，错误认为模型迭代中伤害持续下降，无法识别隐性歧视。

### 方法关键点
分析GPT-2到GPT-5共15个模型的45万条性别定向生成内容，对比不同性别定向输出的主题分布、情感、代表性伤害指标，提出三标准伤害洗白定义与三阶段检测协议。

### 关键结果数字
GPT-4对齐后女性定向输出的主题多样性较男性低36%（W/M从GPT-2的0.91降至0.58）；REGARD代表性伤害差异与模型发布时间正相关（ρ=+0.55，p=0.034），但Detoxify毒性指标无显著相关性，即显性毒性下降的同时隐性代表性伤害持续上升；GPT-5中出现将乳腺癌归为男性权利议题的隐性歧视内容，被通用毒性分类器判定为无毒。
