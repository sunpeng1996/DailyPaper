---
title: 'CPAgents: Agentic Composite Phenotype Generation for Cardiac Disease Association'
title_zh: 'CPAgents: Agentic Composite Phenotype Generation f'
authors:
- Zuoou Li
- Wenlong Zhao
- Kelly Yu
- Weitong Zhang
- Paul M. Matthews
- Wenjia Bai
- Bernhard Kainz
- Mengyun Qiao
arxiv_id: '2606.28179'
url: https://arxiv.org/abs/2606.28179
pdf_url: https://arxiv.org/pdf/2606.28179
published: '2026-06-26'
collected: '2026-06-29'
category: Agent
direction: Agent
tags:
- Agent
- LLM
one_liner: Identifying robust associations between cardiac imaging phenotypes and
  clinical diseases is fun...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 摘要

Identifying robust associations between cardiac imaging phenotypes and clinical diseases is fundamental to population-scale cardiovascular research and reliable risk stratification. However, current phenome-wide association studies rely on pre-defined, single-variable phenotypes or expert-crafted features, which limits their ability to capture clinically meaningful non-linear effects and cross-phenotype interactions. To address this, we propose CPAgents, an iterative phenotype-Composition framework for cardiovascular Phenome-wide association study (PheWAS) that automatically constructs and validates interpretable composite phenotypes (e.g., polynomial, ratio, and interaction forms) from base imaging features. Specifically, our system coordinates three agents: (i) an Analyst that identifies statistical pathologies and nominates candidate transformations; (ii) a Proposer that generates constrained, medically and statistically motivated expressions under numerical safety rules; and (iii) a Verifier that evaluates candidates using multi-stage criteria and produces transparent evidence trails for accepted phenotypes. Evaluated on a population-scale cardiac imaging cohort, the discovered composite phenotypes markedly improve disease discrimination: across 72 classifier-disease-metric combinations, our variants achieve the top rank in 56 cases versus 18 for baselines, with gains observed across all nine clinical disease categories. Our framework yields compact, clinically interpretable phenotype formulas with transparent evidence trails, enabling scalable discovery of stronger phenotype-disease associations beyond expert-driven feature selection.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
