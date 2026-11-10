---
title: 'Beyond Ranking: Are Decision Models Calibrated Relevance Scorers?'
title_zh: 排序之外：决策模型作为相关性打分器的校准性研究
authors:
- Shengyao Zhuang
- Xueguang Ma
- Matthias Petri
- Jimmy Lin
affiliations:
- Keenable
- University of Waterloo
arxiv_id: '2611.11480'
url: https://arxiv.org/abs/2611.11480
pdf_url: https://arxiv.org/pdf/2611.11480
published: '2026-11-08'
collected: '2026-11-10'
category: RecSys
direction: 搜索重排 · 相关性打分校准
tags:
- Reranking
- Calibration
- Decision Model
- Relevance Scoring
- BEIR
- TREC-DL
one_liner: 验证决策模型排序性能优于传统基线，指出原生概率过自信，给出可迁移校准与动态截断方案
practical_value: '- 做LLM重排时不要直接采信模型原生输出的置信度，即便是宣称校准的商用决策模型也普遍过自信，仅需2000条左右标注拟合Platt
  scaling两参数校准器，即可大幅降低概率误差，且校准规则可跨数据集迁移降低日志损失

  - 重排后截断无需固定topK或额外调参，基于校准后概率计算期望F1最优截断深度，可自适应每个query的召回质量，在电商搜索/广告/RAG场景下既能保障效果，又能降低后续推理、上下文占用成本

  - 决策类LLM做zero-shot重排时无需设置过细的相关性分级，2-3级即可，分级带来的排序增益远低于概率校准带来的全链路收益

  - 重排模型选型可优先考虑27B量级开源决策模型，实验表明pplx-decider的排序、校准效果均优于商用闭源Jev与传统cross-encoder，性价比更高'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM重排研究大多仅关注排序指标，忽略输出概率的校准性，但校准的相关性概率是动态截断、置信度过滤等业务操作的核心基础。商用决策模型Jev宣称原生输出校准概率，且此前分级标签重排研究未验证概率校准效果，因此需要系统性校验决策模型的打分可靠性。
### 方法关键点
- 复现《Beyond Yes and No》的FLAN-UL2分级重排实验，对比Jev、2款开源决策模型（9B Clef-flash、27B pplx-decider）、3款传统cross-encoder的排序与校准性能
- 基于TREC DL19的2257条标注拟合Platt scaling两参数校准器，直接迁移到DL20/DL21、BEIR数据集验证跨域效果
- 设计基于校准概率的期望F1最优动态截断规则，对比固定topK、域内调优阈值的截断效果
### 关键结果
- 排序性能：pplx-decider在8个BEIR数据集平均nDCG@10达0.548，优于Jev（0.520）、monoT5-3B（0.505）、FLAN-UL2（0.474）
- 校准效果：所有模型原生概率均过自信，Jev打分>0.9的样本仅66%实际相关；经DL19校准后，Jev在DL21上Brier score从0.213降至0.147，优于FLAN-UL2与所有cross-encoder
- 截断效果：校准后用期望F1规则截断，Jev在DL21上F1达0.638，优于固定top10的0.506，与DL19调优阈值的0.630相当
### 核心结论
排序性能好的模型概率校准性不一定好，仅需千级标注的两参数校准即可大幅提升概率可靠性，支撑更灵活的业务决策
