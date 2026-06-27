---
title: 'OracleAnalyser: Analysing Implicit Semantics of Oracle Bone Scripts through
  MLLMs with Post-training'
title_zh: 'OracleAnalyser: Analysing Implicit Semantics of Or'
authors:
- Zijia Song
- Yelin Wang
- Zhengyi Ma
- Zitong Yu
- Tianheng Wang
- Jiahuan Zhang
- Taorui Wang
- Kaicheng Yu
arxiv_id: '2606.25906'
url: https://arxiv.org/abs/2606.25906
pdf_url: https://arxiv.org/pdf/2606.25906
published: '2026-06-24'
collected: '2026-06-27'
category: Training
direction: Training
tags:
- Training
- LLM
one_liner: With the advancement of artificial intelligence, research on oracle bone
  scripts has entered a...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 摘要

With the advancement of artificial intelligence, research on oracle bone scripts has entered a new era. However, existing methods and benchmarks remain largely confined to recognition tasks, overlooking the equally crucial aspect of oracle bone analysis. To address this gap, we propose OracleAnalyser, a reasoning framework for oracle bone analysis based on post-training techniques. Specifically, we fine-tune Qwen2.5-VL-3B-Instruct through multiple post-training stages and introduce a new preference optimization algorithm, Stable Focal Preference Optimization (SFPO), tailored to the characteristics of oracle bone datasets. In addition, we release both an oracle bone reasoning dataset and an oracle bone preference dataset, and further construct a new benchmark to evaluate models' analytical capabilities for oracle bone scripts. Extensive experiments validate the superior analytical performance of OracleAnalyser, which achieves remarkable results with only 3B parameters, surpassing models with substantially larger scales.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
