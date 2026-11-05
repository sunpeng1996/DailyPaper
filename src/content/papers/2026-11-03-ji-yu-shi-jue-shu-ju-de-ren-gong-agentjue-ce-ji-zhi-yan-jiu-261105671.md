---
title: How Do Artificial Agents Make Decisions in Light of Visual Data?
title_zh: 基于视觉数据的人工Agent决策机制研究
authors:
- Keyty Loza
- Shayan Monadjemi
affiliations:
- Lamar University
- Oak Ridge National Laboratory
arxiv_id: '2611.05671'
url: https://arxiv.org/abs/2611.05671
pdf_url: https://arxiv.org/pdf/2611.05671
published: '2026-11-03'
collected: '2026-11-05'
category: Agent
direction: Agent 视觉数据决策机制评估
tags:
- VLM
- Agent Decision Making
- Uncertainty Visualization
- Model Evaluation
- Rational Choice Theory
one_liner: 量化不同VLM对可视化图表的概率感知误差，及Agent决策与理性理论的对齐表现
practical_value: '- 业务中需要Agent处理可视化报表（如销量柱状图、转化率饼图）做自动决策时，优先选择饼图/柱状图传递概率类信息，GPT-4o对这类图表的概率感知MAE仅0.083，误差最低

  - 搭建Agent自主决策系统时，不能仅评估VLM的视觉理解准确率，需增加端到端决策合理性校验，避免感知误差传导导致最终决策偏差

  - 若用Agent做风险类决策（如营销预算分配、优惠券投放ROI判断），优先用圆形图/图标数组/纯文本传递不确定性信息，决策与理性理论的对齐度更高'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前VLM驱动的Agent已被广泛应用于含视觉数据的自主决策场景（如科研图表分析、业务报表自动决策），但学界与工业界均缺乏对Agent在视觉数据下的不确定性感知能力、决策逻辑的量化评估，也不清楚可视化设计、模型选型对最终决策合理性的影响，存在决策可靠性不可控的风险。
### 方法关键点
- 两组对照实验设计：第一组测试4款主流VLM（Gemma-4、Granite3.2-Vision、GPT-4o、Qwen3-VL:8b）对5类常见可视化图表（图标数组、饼图、圆形图、三角形图、柱状图）的概率感知误差；第二组测试GPT-4o驱动的Agent基于可视化数据的赌博决策，对比其与理性决策理论的对齐度。
- 评估指标：概率感知实验计算预测概率与真实值的MAE评估准确率；决策实验设置10-100美元参与成本、固定100美元奖金，Agent通过MCP工具调用输出Bet/Not Bet决策，统计决策符合理性预期的比例。
### 关键结果
- 概率感知层面：GPT-4o准确率最高，MAE为0.083；不同图表的感知误差差异显著，饼图、柱状图MAE接近0，三角形图误差最高，图标数组存在普遍的概率高估偏差。
- 决策层面：Agent整体80%的决策符合理性决策理论，其中理性决策为Not Bet时准确率达84.5%，为Bet时准确率为74.1%；圆形图、图标数组、纯文本场景下的决策合理性最高。
### 核心结论
VLM驱动的Agent的决策合理性同时受模型选型和可视化设计的双重影响，仅评估VLM的视觉理解能力不足以保障端到端决策效果。
