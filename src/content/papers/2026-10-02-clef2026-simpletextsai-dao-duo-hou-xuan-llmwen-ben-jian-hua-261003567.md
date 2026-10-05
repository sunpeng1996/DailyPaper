---
title: 'Writerslogic at the CLEF 2026 SimpleText Track: Multi-Candidate LLM Simplification
  and Stacked Complexity Spotting'
title_zh: CLEF2026 SimpleText赛道多候选LLM文本简化与堆叠复杂度检测方案
authors:
- David L. Condrey
affiliations:
- WritersLogic Inc, San Diego, CA, USA
arxiv_id: '2610.03567'
url: https://arxiv.org/abs/2610.03567
pdf_url: https://arxiv.org/pdf/2610.03567
published: '2026-10-02'
collected: '2026-10-05'
category: LLM
direction: LLM文本简化 · 幻觉检测
tags:
- LLM
- Text Simplification
- Hallucination Detection
- DeBERTa
- NLI
one_liner: 提出多候选LLM简化+无参考打分方案与DeBERTa复杂度检测方案，在CLEF2026 SimpleText赛道获多项Top排名
practical_value: '- 多候选生成+无参考多维度打分的选优框架可直接复用到电商商品文案简化、push文案生成的最优候选筛选，打分维度可自定义替换为合规性、点击率预估特征

  - 将幻觉检测转化为NLI任务的思路可复用在RAG生成商品/活动介绍的事实性校验环节，避免虚假宣传风险

  - 不同temperature生成多候选再筛选的策略，可直接用于搜索推荐query改写、问答式导购回复生成场景，平衡生成多样性与准确性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
生物医学等领域专业文本术语多、结构复杂，非专业用户难以理解，亟需自动化文本简化与事实性校验能力，对应CLEF2026 SimpleText赛道两个任务。
### 方法关键点
- 文本简化任务：用GPT-4o-mini在不同temperature下生成5个简化候选，通过无参考启发式打分（压缩率、原词保留率、Cochrane通俗词表匹配度、词汇简单度）选优
- 复杂度/幻觉检测任务：将任务转化为NLI任务，在35万标注（源文本，候选）对微调DeBERTa-v3-large，以源文本为premise、候选为hypothesis判断是否符合事实
### 关键结果
- 句子级简化任务获SARI 47.43、BLEU 14.21，为句子级系统Top1，总榜Top3
- 二分类过生成检测最高macro F1 0.8085，为检测赛道Top1、总榜Top2
- 多分类错误检测准确率0.804，总榜Top2
