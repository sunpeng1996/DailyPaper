---
title: 'ReaORE: Reasoning-Guided Progressive Open Relation Extraction Empowered by
  Large Reasoning Models'
title_zh: 'ReaORE: Reasoning-Guided Progressive Open Relation'
authors:
- Xin Lin
- Liang Zhang
- Guoqi Ma
- Hongyao Tu
- Jinsong Su
arxiv_id: '2606.26986'
url: https://arxiv.org/abs/2606.26986
pdf_url: https://arxiv.org/pdf/2606.26986
published: '2026-06-25'
collected: '2026-06-27'
category: Reasoning
direction: Reasoning
tags:
- Reasoning
- LLM
one_liner: Open Relation Extraction (OpenRE) requires a model to extract unseen relations
  between head and...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 摘要

Open Relation Extraction (OpenRE) requires a model to extract unseen relations between head and tail entities from unstructured text for real-world applications. The core challenge of OpenRE lies in achieving reliable generalization to unseen relation types. Current OpenRE approaches either employ clustering techniques, which cannot generate relation labels and suffer from poor generalization, or rely on direct relation label generation via Large Language Models (LLMs), which lack sufficient discriminative capacity to distinguish easily confused relations. To address these limitations, we propose Reasoning-guided progressive OpenRE (ReaORE), a framework for performing relation extraction through coarse-to-fine relation reasoning. Specifically, ReaORE consists of two key stages: (i) relation filtering, which reasons over multiple aspects to understand relations and instances, yielding an initial relation set, and further supplements and filters relations via embedding-based similarity to ensure the target relation is included; (ii) relation prediction, which aims to predict the target relations from the above set via fine-grained comparative reasoning to better distinguish easily confused relations. Extensive experiments on two widely used OpenRE datasets demonstrate that ReaORE outperforms existing baselines.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
