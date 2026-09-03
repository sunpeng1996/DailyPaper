---
title: 'Closing Cost-Quality Gap in Document VLMs: Difficulty-Aware Data Curation
  and Quality-Adjusted Deployment Economics'
title_zh: 缩小文档VLM成本质量差距：难度感知数据治理与质量调优部署方案
authors:
- Maksim Evdokimov
- Matvey Ivanov
- Dmitrii Tsiupin
- Olga Tsymboi
- Anatolii Potapov
- Aleksandr Ivanov
affiliations:
- T-Tech
arxiv_id: '2609.01575'
url: https://arxiv.org/abs/2609.01575
pdf_url: https://arxiv.org/pdf/2609.01575
published: '2026-09-01'
collected: '2026-09-03'
category: Multimodal
direction: 多模态大模型 · 生产部署优化
tags:
- VLM
- MoE
- DataCuration
- DeploymentOptimization
- DocumentUnderstanding
one_liner: 提出基于MoE的轻量化文档VLM系统，搭配难度感知数据流水线，大幅降低生产部署的成本质量比
practical_value: '- 大模型生产部署可优先选用MoE架构，控制单步激活参数规模（如单H100承载35B总参数仅3B激活），大幅降低推理成本同时保证效果

  - 领域微调数据可引入难度感知筛选pipeline，兼顾布局多样性、事实可提取性、跨模型一致性，无需盲目堆数据量即可提升域内效果

  - 落地成本核算需加入生产环境的错误确认、修正成本，做质量调整后的全链路成本测算，避免仅看模型参数/推理单价的片面评估'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
监管行业年处理亿级文档存在多重约束：隐私规则禁止使用外部模型，达标开源VLM推理成本高于人工标注，定制OCR流水线覆盖场景有限、维护成本高，无法支撑大规模异构文档处理。
### 方法关键点
1. 采用总参数35B、单步激活仅3B的MoE架构，单张H100即可部署，支持prompt适配多工作流，禁用复杂推理逻辑满足latency要求；
2. 构建难度感知数据筛选pipeline，混合内部生产数据与开源文档，兼顾布局多样性、事实可提取性、跨模型一致性做微调。
### 关键结果
效果优于参数规模大1个数量级的所有可部署基线；对比人工标注预期成本降低80%以上，对比最优开源竞品成本降低50%以上，更大参数基线无经济可行性。
