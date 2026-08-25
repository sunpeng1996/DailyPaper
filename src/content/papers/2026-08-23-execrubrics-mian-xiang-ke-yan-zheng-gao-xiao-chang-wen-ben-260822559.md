---
title: 'ExecRubrics: Executable Tool-Augmented Rubrics for Verifiable and Efficient
  Long-Form Evaluation'
title_zh: ExecRubrics：面向可验证高效长文本评估的可执行工具增强评分框架
authors:
- Kaustubh D. Dhole
- Charles L. A. Clarke
- Eugene Y. Agichtein
affiliations:
- Emory University
- University of Waterloo
arxiv_id: '2608.22559'
url: https://arxiv.org/abs/2608.22559
pdf_url: https://arxiv.org/pdf/2608.22559
published: '2026-08-23'
collected: '2026-08-25'
category: Eval
direction: 大模型长文本评估 · 可解释可验证评审
tags:
- LLM Evaluation
- Executable Rubric
- Long-form Generation
- Model Judge
- Explainable Eval
one_liner: 将评估评分规则编码为可执行Python程序，替代黑盒LLM评审，大幅降延迟同时保证评估准确率
practical_value: '- 可迁移到电商LLM客服、生成式推荐文案自动评估场景，把业务规则（违禁词、价格正确性、合规要求）编码为可执行程序，替代黑盒LLM评审降本提效

  - 评估逻辑支持接入NLTK、spaCy等文本处理工具，可直接复用现有规则引擎能力，叠加语义校验提升评估准确率，适配高要求的合规类评审场景

  - 对于Agent工作流的多步输出评估，可自定义规则依赖、惩罚项、覆盖条件，替代传统线性加权评分，更贴合业务复杂评估逻辑'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
当前自然语言Rubric存在歧义，依赖黑盒LLM评审，且默认线性加权聚合，无法捕捉规则依赖、惩罚项、覆盖条件等复杂逻辑，长文本评估成本高、可解释性差，无法满足高风险场景的审计要求。

### 方法关键点
提出ExecRubrics框架，将评估逻辑编码为可验证的Python评分函数，给自然语言评分规则赋予可执行语义，支持人工检查、修改、运行，还可接入NLTK、spaCy等外部文本处理工具扩展能力。

### 关键结果
在HealthBench、HelpSteer、ArgQuality三个长文本基准上，偏好匹配精度最高分别达53%、78%、92%，匹配或超越自然语言规则基线，同时评估延迟最高降低320倍。
