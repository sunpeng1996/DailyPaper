---
title: 'PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception'
title_zh: 'PerceptionRubrics: Calibrating Multimodal Evaluati'
authors:
- Yana Wei
- Hongbo Peng
- Yanlin Lai
- Liang Zhao
- Kangheng Lin
- En Yu
- Keyu Lv
- Han Zhou
- Yin Tang
- Haodong Li
arxiv_id: '2606.28322'
url: https://arxiv.org/abs/2606.28322
pdf_url: https://arxiv.org/pdf/2606.28322
published: '2026-06-26'
collected: '2026-06-29'
category: RAG
direction: RAG
tags:
- RAG
- LLM
one_liner: We introduce PerceptionRubrics, a rubric-based evaluation framework that
  addresses the gap betw...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 8
source: arxiv-cs.CV
depth: abstract
---

### 摘要

We introduce PerceptionRubrics, a rubric-based evaluation framework that addresses the gap between saturated benchmark scores and real-world brittleness. Shifting evaluation from holistic semantic matching to rigorous atomic auditing, PerceptionRubrics pairs 1,038 information-dense images with over 12,000 instance-specific rubrics. These criteria are derived from golden captions constructed via a novel Circular Peer-Review consensus pipeline and then distilled into a dual-stream system of Must-Right (essential facts) and Easy-Wrong (fine-grained details) rubrics. Crucially, PerceptionRubrics implements a Gated Scoring mechanism: unlike linear averages, failure on mandatory visual facts triggers sharp binary penalties. Extensive evaluation yields critical insights: (1) The Reliability Gap: models often verify fragmented elements correctly yet fail strict conjunctive constraints, exposing brittleness in dense domains; (2) Open-Closed Stratification: contrary to reasoning trends, we reveal a persistent 8% perception deficit between open-source and proprietary frontiers; and (3) Human-Aligned Rigor: our gated metrics substantially out-align conventional benchmarks, validating that strict perceptual fidelity is the prerequisite for reliable generation.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
