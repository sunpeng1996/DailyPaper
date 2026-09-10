---
title: 'DiSCo: A Distribution-First Steering and Cultural Prior Evaluation Framework
  for Measuring Cultural Preference Bias in LLMs'
title_zh: DiSCo：度量LLM文化偏好偏差的分布优先引导与评估框架
authors:
- Bhuvan Arora
- Devesh Saraogi
- Sravya Varada
- Dhruv Kumar
affiliations:
- BITS Pilani, Pilani, India
arxiv_id: '2609.10253'
url: https://arxiv.org/abs/2609.10253
pdf_url: https://arxiv.org/pdf/2609.10253
published: '2026-09-09'
collected: '2026-09-10'
category: Eval
direction: LLM文化偏好偏差评估与适配验证
tags:
- LLM Bias
- Cultural Evaluation
- Distributional Metric
- Prompt Steerability
- Benchmark
one_liner: 提出分布优先的LLM文化偏好偏差评估框架DiSCo，验证仅靠prompt无法消除文化偏倚
practical_value: '- 跨境电商/多区域LLM推荐应用避免仅依赖prompt做文化适配，需在预训练/微调阶段注入低资源文化数据

  - 多文化场景LLM效果评估可复用DiSCo的分布优先+四级上下文梯度范式，解决单答案评估的偏差问题

  - 出海Agent产品的文化适配效果可采用DiSCo的强制选择评估法，快速量化不同文化的偏好覆盖度'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM文化基准仅对标单一正确答案，无法刻画多有效回复场景下的模型文化先验偏好，也混淆了默认偏好与上下文引导的适配能力，严重影响全球化部署的本地化效果与用户信任。
### 方法关键点
提出DiSCo分布优先强制选择评估框架，通过C0-C3四级上下文梯度隔离默认文化先验、测试引导可调性，配套推出覆盖12种文化、含304条样本的DiSCo-Bench评估基准。
### 关键结果
6款指令微调LLM的默认文化先验高度集中，英美仅占12种文化的2席，却占据35%的选择占比；prompt引导反而会扩大高低资源文化的选择差距，注入显式文化事实对分布影响可忽略，仅靠prompt个性化无法解决文化偏好偏差。
