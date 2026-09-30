---
title: 'Correct Answers, Invalid Traces: What Verifiable Grade-School Math Reveals
  About Chain-of-Thought Traces'
title_zh: 小学数学可验证推理任务下正确答案对应思维链的有效性分析
authors:
- Ratish Puduppully
- Pranabendu Misra
- Paarth Iyer
- Durgesh Kalwar
- Vardhan Palod
- Subbarao Kambhampati
affiliations:
- IT University of Copenhagen
- Chennai Mathematical Institute
- Indian Institute of Technology Jammu
- Arizona State University
arxiv_id: '2609.38107'
url: https://arxiv.org/abs/2609.38107
pdf_url: https://arxiv.org/pdf/2609.38107
published: '2026-09-29'
collected: '2026-09-30'
category: Reasoning
direction: 大模型思维链可解释性 · 推理Trace验证
tags:
- Chain-of-Thought
- Reasoning Trace
- Interpretability
- OOD Generalization
- AI Safety
one_liner: 在可验证数学推理任务中证实正确答案常伴随无效思维链，推翻trace可信默认假设
practical_value: '- 做Agent推理监控时，不能仅以答案正确判定推理过程合法，必须加入step级语义依赖校验，尤其电商大促等分布外query场景，避免trace看似合理实际无效的隐患

  - 训练带CoT的业务LLM（如导购Agent、推荐解释生成模块）时，不要只做结果奖励，必须加入step级过程监督，否则分布外场景易出现结果正确但逻辑错误的问题，也难以排查定位

  - 生成推荐系统对外披露的可解释性文案时，不要默认LLM输出的推理路径是真实决策逻辑，需额外做规则校验确保解释与推荐结果的逻辑一致性，规避合规风险'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前Chain-of-thought（CoT）trace被广泛用于Agent审计、模型推理能力验证、可解释性分析，但行业默认假设「答案正确则trace有效」缺乏可验证场景下的系统性校验，且多数CoT训练仅用结果奖励，未约束trace本身合法性，会导致AI监控、可解释性等场景存在严重隐患。

### 方法关键点
- 基于可验证iGSM合成小学数学推理基准，每个问题自带完整依赖图，可对生成trace做step级语法、算术、语义依赖自动校验
- 训练124M参数量GPT-2风格模型，分别输入干净合法trace、跨问题交换trace、token打乱trace、非最小化trace做对照实验
- 评估维度区分答案正确率、trace有效率，对比分布内/分布外（推理长度超过训练集）表现差异

### 关键结果
- 干净trace训练的模型，分布内答案正确时trace有效率接近100%，但分布外最难样本中31.6%的正确答案伴随无效trace，其中超50%的无效trace可通过语法、算术校验，仅语义依赖不匹配
- 训练集使用跨问题交换的无效trace时，分布内答案正确率仍达82%，但无任何trace通过校验
- 训练trace的10%句子token打乱后，模型精度几乎与干净trace组一致，同样无有效trace输出

### 核心结论
思维链trace是模型行为的观测结果，而非内部推理过程的直接度量，其有效性、合理性会随分布shift显著下降，不能仅凭答案正确就信任trace内容。
