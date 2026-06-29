---
title: An LLM-Powered Semantic Alignment Framework for Journal Recommendation
title_zh: An LLM-Powered Semantic Alignment Framework for Jo
authors:
- Yanglin Yan
- Zicheng Xie
- Tianchen Gao
- Rui Pan
- Hansheng Wang
arxiv_id: '2606.27930'
url: https://arxiv.org/abs/2606.27930
pdf_url: https://arxiv.org/pdf/2606.27930
published: '2026-06-26'
collected: '2026-06-29'
category: RecSys
direction: RecSys
tags:
- RecSys
- LLM
one_liner: Journal recommendation is an important task in scholarly information systems.
  Existing approach...
practical_value: '- 可先根据论文标题和摘要判断是否进入人工精读列表。

  - 当前未配置 LLM API Key，已使用规则摘要兜底；配置 Key 后会恢复中文精读、打分和业务可借鉴点生成。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 摘要

Journal recommendation is an important task in scholarly information systems. Existing approaches typically rely on supervised learning models, manually engineered features, or historical interaction data, which may limit their generalizability and interpretability. We propose an LLM-powered semantic alignment framework that formulates journal recommendation as a semantic matching problem between manuscript content and journal scope descriptions. The framework enables large language models (LLMs) to infer journal suitability directly from article titles, abstracts, keywords, and candidate journal information without task-specific training. Experiments are conducted using DeepSeek-V3 on a dataset of 23,609 articles from 49 journals in statistics and related fields. The proposed framework achieves Top-3, Top-5, and Top-10 accuracies of 40.23\%, 53.67\%, and 70.05\%, respectively. Additional analyses show that incorporating reference information generally improves recommendation performance and that recommendations remain highly stable across repeated runs, with an average Top-5 Jaccard similarity of 84\%. The framework also generates interpretable reasoning outputs that provide insights into the recommendation process. These findings demonstrate the potential of LLMs as a training-free and scalable paradigm for journal recommendation and scholarly decision support.

> 当前运行未检测到 LLM API Key，本卡片由规则降级流程生成。
