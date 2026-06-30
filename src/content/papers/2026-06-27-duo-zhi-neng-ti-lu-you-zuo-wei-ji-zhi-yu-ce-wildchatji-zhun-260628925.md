---
title: 'Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware
  Evaluation'
title_zh: 多智能体路由作为集值预测：WildChat基准与成本感知评估
authors:
- Ananto Nayan Bala
- Faisal Muhammad Shah
affiliations:
- Ahsanullah University of Science and Technology
arxiv_id: '2606.28925'
url: https://arxiv.org/abs/2606.28925
pdf_url: https://arxiv.org/pdf/2606.28925
published: '2026-06-27'
collected: '2026-06-30'
category: MultiAgent
direction: 多智能体路由 · 成本感知预测
tags:
- Multi-Agent
- Routing
- Set-Valued Prediction
- Cost-Aware
- LLM Agent
one_liner: 将固定目录多智能体路由建模为集值预测问题，构建基准并验证成本感知路由的有效性
practical_value: '- 做多Agent工具路由时，可直接复用WAR（Weighted Agent Routing）作为轻量无训练成本的后处理层，能基于Agent的ordinal成本层级调整分数，在不重训backbone的前提下优化整体效用，适合电商多Agent场景降本提效

  - 固定Agent目录的路由任务不需要依赖零-shot LLM，工程上可按需求选方案：精度要求高用fine-tuned encoder，推理延迟比零-shot
  LLM低两个数量级；追求迭代效率和低开销用线性多标签SVM，是性价比极高的强基线

  - 多Agent路由天然是集值预测问题，不要强制选单个top1 Agent，用集级指标（F1/Jaccard）加成本效用评估比单标签准确率更贴合实际部署需求'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前多智能体系统需要将用户请求路由到对应能力的Agent/工具，但现有工作大多只做top1单Agent选择，忽略了实际场景中一个请求往往需要多个Agent协作完成，同时过多的Agent调用会增加延迟、货币调用成本，领域缺乏针对集值多Agent路由的标准化基准和成本感知评估方法，因此需要开展相关研究。

### 方法关键点
- 问题建模：将固定目录多Agent路由明确建模为集值预测问题，目标是在控制总执行成本的前提下，最大化预测Agent集与真实需求Agent集的重叠度
- 基准构建：基于WildChat的真实用户prompt，构建了包含3000个样本、固定12个Agent的基准数据集，做了重平衡处理，保证每个Agent覆盖均匀，集大小分布可控（1/2/3Agent占比6:3:1，平均集大小1.5）
- 算法设计：提出Weighted Agent Routing（WAR），这是一个无需训练的确定性成本感知后处理层，直接对backbone输出的Agent分数做调整：`˜s_i = s_i - λ*c_i`，其中`c_i`是Agent的序数成本层级，调整后再通过阈值化得到最终预测集

### 关键实验结果
对比了7类方法，核心结论：无约束设置下，fine-tuned encoder效果最佳，F1达89.59，精确率97.8%；零-shot GPT-4o路由F1仅41.51，远低于所有有监督方法；线性多标签SVM是强实用基线，F1达71.79，推理延迟仅61ms/query，远低于零-shot LLM的1979ms；加入WAR后，Encoder+WAR将任务成功率从74.33%提升到92.11%，整体效用从0.654提升到0.670，ML+WAR也在不损失覆盖率的情况下降低了平均调用成本。

最值得记住的结论：固定目录多Agent路由中，有监督方法大幅优于零-shot LLM，简单的成本感知后处理就能在不重训backbone的情况下提升部署效用。
