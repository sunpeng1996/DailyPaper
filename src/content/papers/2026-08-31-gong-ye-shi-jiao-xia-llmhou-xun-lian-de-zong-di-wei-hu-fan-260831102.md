---
title: 'LLM Post-Training as Brownfield Maintenance: An Industrial Perspective on
  Dataware Engineering'
title_zh: 工业视角下LLM后训练的棕地维护范式与数据工程实践
authors:
- Gopi Krishnan Rajbahadur
- Amir M. Ebrahimi
- Boyuan Chen
- Ahmed E. Hassan
affiliations:
- Queen's University, Canada
- Huawei Technologies Canada
arxiv_id: '2608.31102'
url: https://arxiv.org/abs/2608.31102
pdf_url: https://arxiv.org/pdf/2608.31102
published: '2026-08-31'
collected: '2026-09-01'
category: LLM
direction: LLM后训练 · 工业落地工程实践
tags:
- Post-Training
- Brownfield Maintenance
- Dataware
- Yield Engineering
- Synthetic Data
- LLM Evaluation
one_liner: 从工业落地视角提炼已部署LLM后训练的三大挑战与可落地工程规范
practical_value: '- 做垂域LLM（电商文案生成、推荐意图理解、Agent推理）微调时，遵循零和混合设计原则，新增训练数据必须替换等体积低价值旧数据，在固定计算预算下实现定向能力升级，同时避免全局能力退化

  - 合成训练数据/知识蒸馏环节落地yield engineering，提前增加测试用例校验、问题约束注入两个预处理步骤，可在相同计算成本下将可用有效训练数据量提升2.84倍，同时降低教师模型token消耗28%

  - 上线前模型评估采用方差感知方案，单任务跑多轮（如16次）随机生成统计置信区间，避免单次评估的噪声误导效果判断，尤其适合推荐、广告场景的生成类效果验收，同时设置明确的非目标能力回归门禁'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
工业场景下LLM后训练大多属于棕地场景：团队只能基于已上线的成熟checkpoint做定向能力升级，受限于固定计算、数据预算，不能全量重训，还要严格避免其他能力退化。现有研究大多聚焦从零训练的绿地场景，缺乏可落地的工程指引，实际落地普遍面临三大核心痛点：训练数据配额固定零和、知识蒸馏有效数据占比极低、升级后能力退化难排查。

### 方法关键点
- 零和混合设计：新增训练数据必须替换等体积的低价值旧数据，严格控制训练数据总规模，避免占用其他能力的训练配额
- 稳定失败挖掘：通过多轮重复评估锁定模型的稳定失败任务，而非单次评估的随机错误，避免数据生成资源浪费在偶发错误上
- 良率（yield）优化：蒸馏前加入测试用例修正、问题约束注入两个预处理步骤，大幅提升教师模型蒸馏输出的有效率
- 方差感知评估：每个checkpoint在每个基准上跑16次随机生成，统计置信区间判断效果提升是否显著，同时设置非目标能力波动不超过1个百分点的回归门禁

### 关键结果
基于内部7B通用推理模型做代码能力定向升级，仅替换1.5%的训练数据：相同教师模型与单问题4次尝试的预算下，可用训练数据量提升2.84倍，教师单请求token消耗降低28%；混合替换场景下CodeForces pass@1提升+2.59个点，域外LiveCodeBench v6 pass@1提升+6.11个点，同时数学推理能力波动控制在1个点的门禁范围内，完全满足上线要求。

最值得记住的一句话：LLM后训练的核心瓶颈从来不是单点算法创新，而是把现有方法在固定预算、无退化约束下落地的工程化能力。
