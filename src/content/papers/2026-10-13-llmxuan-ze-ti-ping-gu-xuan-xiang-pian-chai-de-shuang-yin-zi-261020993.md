---
title: 'One Bias Score, Two Factors: How Mitigations Affect Option Bias in Multiple-Choice
  Evaluation'
title_zh: LLM选择题评估选项偏差的双因子分解与缓解策略效果分析
authors:
- Hyunjong Ok
- Minjae Park
- Jaeho Lee
affiliations:
- Pohang University of Science and Technology (POSTECH)
arxiv_id: '2610.20993'
url: https://arxiv.org/abs/2610.20993
pdf_url: https://arxiv.org/pdf/2610.20993
published: '2026-10-13'
collected: '2026-10-17'
category: Eval
direction: LLM 评估优化 · 选项偏差缓解
tags:
- LLM Evaluation
- Option Bias
- Multiple Choice Testing
- Bias Mitigation
- Model Ranking
one_liner: 将LLM选择题评估的选项偏差分解为翻转率与位置偏移两个无标签因子，明确不同缓解手段的作用路径
practical_value: '- 做LLM驱动的多分类任务（如商品类目判等、候选排序）内部评估时，可采用双因子分解法区分输出不稳定性与固有偏差，避免评估结果失真

  - 用LLM生成多候选内容（如商品卖点、搜索query排序）时，可落地「先验偏差校正+正反序聚合」流程，降低选项顺序对结果的干扰

  - 多LLM服务选型做性能排名时，优先选用正反序聚合的评估方案，可减少60%+的模型排名反转概率，提升选型决策可靠性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有LLM选择题评估存在显著选项偏差：仅调整选项顺序即可改变模型输出，甚至颠覆最终模型排名，过往研究分为选择偏差、顺序敏感性两个独立方向，缺乏统一度量与分解框架。
### 方法关键点
提出pooled SD作为统一的选项偏差度量，当每个选项在各位置出现频率均等时，该值可完全分解为两个无标签因子：1）翻转率：选项重排后答案发生变化的问题占比；2）位置偏移：答案变化的问题中各选项字母被选率的标准差。
### 关键结果数字
在41个模型checkpoint、12个基准测试集上验证：先验校正方案主要降低位置偏移，正反序聚合方案主要降低翻转率；二者均可缩窄不同正确选项对应的准确率范围，其中聚合方案可减少60%以上的模型排名反转；先做先验校正再做聚合可同时降低两类因子，进一步缩小准确率波动，但需注意聚合可能将部分问题固定为错误答案，评估时需同步上报准确率与两个偏差因子。
