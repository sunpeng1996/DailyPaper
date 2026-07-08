---
title: 'Pluralis v0.1: Towards a Multicultural, Multimodal, Multilingual Benchmark
  for AI Risk and Reliability'
title_zh: Pluralis v0.1：面向多文化多模态多语言的AI风险与可靠性基准
authors:
- Alicia Parrish
- Rajat Shinde
- Sanket Badhe
- Xinyi Bai
- Sree Bhargavi Balija
- Hua-Rong Chu
- Emilio Ferrara
- Armstrong Foundjem
- Rajat Ghosh
- Aakash Gupta
affiliations:
- Google DeepMind
- Google
- Microsoft
- Seoul National University
- KAIST
arxiv_id: '2607.06196'
url: https://arxiv.org/abs/2607.06196
pdf_url: https://arxiv.org/pdf/2607.06196
published: '2026-07-07'
collected: '2026-07-08'
category: Eval
direction: AI安全评测 · 多文化多模态多语言
tags:
- LLM Evaluation
- Multimodal
- Multilingual
- Cultural Alignment
- AI Safety
- Benchmark
one_liner: 推出文化优先的亚太6国多模态多语言AI安全评测基准及配套自动判分模型
practical_value: '- 出海电商/内容推荐业务可复用多文化分层评测思路，拆分通用违规和本地化文化禁忌两个校验维度，大幅降低跨区域运营的合规风险

  - 多模态场景（如图文商品推荐、广告生成、智能客服）可参考文本+图片联合风险校验范式，覆盖单模态检测不到的组合式违规点

  - 小语种/小众文化区域的内容审核可借鉴agreement-gated LLM-as-Judge集成判分方法，降低本地化标注的人力与时间成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有AI安全评测框架多为西方中心、文化无关设计，忽略区域法律、社会语言差异和文化禁忌，导致VLM等多模态模型全球部署存在大量未被覆盖的风险。
### 方法关键点
1. 文化优先构建Pluralis v0.1数据集，原生采集6个亚太国家、8种语言的本地化安全风险样本，共6448条prompt，避免直接翻译西方数据集带来的偏差；
2. 首创多模态联合评测范式：单独无害的文本+图像组合可触发特定文化/法律违规，明确拆分通用安全违规与本地化文化适配性两个独立评测维度；
3. 配套训练基于经验化文化分类体系的agreement-gated LLM-as-Judge集成模型Judge-Pluralis，实现自动判分。
### 关键结果
测试发现VLM存在大量区域特有失败模式，包括图像识别错误引发下游危害、遗漏物品-上下文-区域关联风险、拒绝响应不充分等，这类本地化偏差完全被全局平均指标掩盖。
