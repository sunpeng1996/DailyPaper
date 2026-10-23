---
title: Predictable performance is suboptimal, and what it means for model routing
title_zh: 可预测性能的次优性及其对模型路由的启示
authors:
- Guanhua Zhang
- Moritz Hardt
affiliations:
- Max Planck Institute for Intelligent Systems, Tübingen
- Tübingen AI Center
arxiv_id: '2610.31428'
url: https://arxiv.org/abs/2610.31428
pdf_url: https://arxiv.org/pdf/2610.31428
published: '2026-10-22'
collected: '2026-10-23'
category: LLM
direction: LLM性能预测 · 模型级联路由
tags:
- performance_prediction
- model_routing
- LLM_cascade
- self_confidence
- suboptimality
one_liner: 证明性能预测器与路由的收益上限由模型次优性和新增参数容量决定
practical_value: '- 业务多模型路由场景中，若基础模型已完成充分业务finetune，无需额外开发复杂性能预测器，直接用模型self-confidence做路由阈值即可，可大幅降低开发与推理成本

  - 针对未充分finetune的7-12B小模型，可搭配4B左右的小性能预测器获得可观路由收益，次优性高的模型可提升0.5~1.4pp的级联准确率

  - 若性能预测器效果优于self-confidence，可直接用其输出对模型置信度做重校准，无需重新训练大模型即可等价降低模型回答损失

  - 路由系统优化优先迭代基础模型效果：finetune后路由收益平均降至0.1~0.2pp，模型本身效果足够优时，复杂路由的额外价值极低'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM多模型路由系统普遍依赖独立性能预测器做模型选择，但业界缺乏对预测器收益上限的明确认知，常出现过度设计路由系统却收益甚微的问题，亟需明确什么时候值得投入资源做独立性能预测器和复杂路由。
### 方法关键点
- 定义「超额可预测性」为独立预测器相对模型self-confidence的正确性对数损失降低值，证明该值可通过重校准1:1转化为模型本身的回答损失降低值
- 基于模型缩放定律推导上界：超额可预测性 ≤ 模型次优性（当前模型损失与同参数规模最优损失的差值） + 预测器新增参数带来的容量增益
- 扩展至双模型级联路由场景，证明预测器路由相对self-confidence路由的准确率提升，同样受限于弱模型次优性与路由器新增参数容量
### 关键实验
在WinoGrande、CommonsenseQA、GSM8K、MMLU-Pro四个基准上测试16个7-12B参数的LLM，对比4B独立预测器与self-confidence的效果：
- 模型次优性与超额可预测性正相关，皮尔逊系数0.65~0.98
- 任务finetune后，55/59的模型-任务对的超额可预测性下降，预测器路由收益平均从0.52~1.38pp降至0.07~0.2pp
- 路由收益与模型次优性正相关，皮尔逊系数0.66~0.91
### 核心结论
提升基础模型本身的效果，通常比额外开发独立性能预测器和复杂路由系统的性价比更高，当模型足够优时，self-confidence路由的效果几乎与复杂预测器路由持平
