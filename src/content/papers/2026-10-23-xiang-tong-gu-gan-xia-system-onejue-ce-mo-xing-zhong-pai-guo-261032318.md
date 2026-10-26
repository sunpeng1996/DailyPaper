---
title: System One models Are Not Better Rerankers
title_zh: 相同骨干下System One决策模型重排效果不及专用重排微调模型
authors:
- Michael Dinzinger
- Kanishka Ghosh Dastidar
- Michael Granitzer
affiliations:
- University of Passau
- Interdisciplinary Transformation University Austria (IT:U)
arxiv_id: '2610.32318'
url: https://arxiv.org/abs/2610.32318
pdf_url: https://arxiv.org/pdf/2610.32318
published: '2026-10-23'
collected: '2026-10-26'
category: RecSys
direction: 搜索推荐重排 · 大模型微调效果对比
tags:
- Reranking
- SystemOne
- Fine-tuning
- LLM
- Calibration
one_liner: 基于Qwen全规模骨干验证决策类模型重排效果不及专用重排微调 仅27B规模二者持平
practical_value: '- 不要盲目跟风用System One类决策模型做召回后重排，9B参数量及以下的中小模型直接用专用重排微调方案，nDCG@10可提升5~29个点

  - 若业务需要校准的相关性概率（比如截断召回结果、统计相关内容数），27B及以上规模可选用决策模型，中小模型直接给LLM加二分类损失训练就能获得不错的校准效果，不用额外做决策微调

  - 决策模型的校准效果高度依赖prompt措辞，要和业务侧的相关性定义严格匹配，否则校准优势完全消失

  - 中小规模模型用joint模式（同时输入所有候选）做重排反而会掉点，只有27B及以上大模型能从joint输入获得收益'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
近期System One（决策）类模型因可输出校准概率被大量尝试用于检索重排，但之前的对比都没有控制骨干模型变量，无法区分效果来自决策微调还是骨干本身的能力，且其校准优势对重排业务的价值也未被验证。

### 方法关键点
- 控制变量设计：基于6种参数量（0.6B~27B）的Qwen系列骨干，分别对比三类变体：零样本原生LLM、决策微调模型（Kev、Clef）、专用重排微调模型（Qwen3-Reranker、Prism及作者自研版本）
- 两种推理模式：分别测试单候选孤立打分、100个候选联合输入打分的重排效果
- 多维度评估：同时测重排精度（nDCG@10）、概率校准度（ECE）、固定阈值截断效果（F1）

### 关键结果数字
在TREC DL 2019~2023、5个BEIR数据集上测试，所有模型均对BM25召回的Top100候选重排：
1. 0.6B~9B规模下，专用重排微调的nDCG@10比决策微调高5~29个点，决策微调效果和零样本原生LLM几乎无差异
2. 27B规模下二者nDCG@10持平，均比原生LLM高约3个点
3. 决策模型的校准优势仅在prompt措辞完全匹配相关性标注定义时存在，换措辞后校准度下降2~3倍，且校准度无法弥补中小模型的排序精度差距，固定阈值截断时专用重排的F1仍更高

**最值得记住的一句话**：如果你的业务需要重排器，直接微调专用重排模型就好，不用额外用决策类模型。
