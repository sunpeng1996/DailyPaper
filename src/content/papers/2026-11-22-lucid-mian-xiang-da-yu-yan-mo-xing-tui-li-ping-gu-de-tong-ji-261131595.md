---
title: 'LUCID: Statistically Grounded Self-Correction for LLM Reasoning Evaluation'
title_zh: 《LUCID：面向大语言模型推理评估的统计驱动自校正框架》
authors:
- Satiyabooshan Murugaboopathy
- Adel Daoud
- Connor T. Jerzak
affiliations:
- AI and Global Development Lab
- Linköping University
- Chalmers University of Technology
- The University of Texas at Austin
arxiv_id: '2611.31595'
url: https://arxiv.org/abs/2611.31595
pdf_url: https://arxiv.org/pdf/2611.31595
published: '2026-11-22'
collected: '2026-11-25'
category: Eval
direction: LLM推理评估 · 偏差校准
tags:
- LLM Evaluation
- Calibration
- Self-Correction
- Debiasing
- Statistical Inference
one_liner: 基于小样本专家标注的LLM推理步级评分偏差校准框架 无需模型重训
practical_value: '- 做Agent推理路径/生成内容自动评分时，可复用LUCID的偏差诊断+提示词自校正流程，仅需小批量专家标注就能大幅降低评分校准gap，无需微调模型

  - 可复用DSL（Design-based Supervised Learning）的小样本去偏思路，在标注预算有限的场景下提升下游排序/指标回归的准确率，降低对全量专家标注的依赖

  - 可复用预/后校验逻辑：校正前先判断初始偏差是否显著，校正后验证效果是否正向，避免过校正浪费算力或引入新偏差'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
用LLM做Chain-of-Thought推理的步级自动评分成本远低于人工，但存在系统性偏差（如过严/过松、特定类型步骤评分失真），会导致推理审计、路径排序结果偏离真实水平；现有校正方法要么需要模型重训，要么牺牲错误检测能力。

### 方法关键点
1. 提出LUCID闭环校准流程：从少量专家标注子集中诊断评分偏差（整体偏差、分步骤类型偏差、位置相关性偏差），生成纯文本偏差提示词追加到评分指令中，让rater重新打分，无需重训模型
2. 新增双校验机制：预校验仅当初始偏差>2pp且统计显著时才启动校正，避免过校正；后校验仅当校正后验证集偏差缩小才保留结果，否则回滚
3. 搭配DSL去偏框架：复用同一份专家标注，通过交叉拟合的梯度提升树生成校准后的步级合理度概率，支撑下游回归、推理路径排序等任务

### 关键实验结果
- 在PRM800K数学推理数据集上，1轮LUCID校正将GPT-5-mini的评分校准gap从7.8pp降到0.9pp，非合理步检测F1,−提升32%
- 小样本场景下，DSL在n=200标注量时比仅用专家标注的回归RMSE降低7.2倍；用1000条专家标注的DSL校准分数做推理路径best-of-K排序，top-1准确率提升13.7pp，效果对齐全量专家标注
- 可跨模型跨领域迁移：将GPT-5-mini的偏差剖面应用到GLM-5.2，同样能降低PRM800K上的校准gap，适配数学、科学、网页、逻辑多场景

**最值得记住的一句话**：提示词类校正仅能调整评分阈值校准偏差，无法提升类平衡下的判别能力，仅适合有能力但评分过严/过松的rater，判别能力不足时仍需微调
