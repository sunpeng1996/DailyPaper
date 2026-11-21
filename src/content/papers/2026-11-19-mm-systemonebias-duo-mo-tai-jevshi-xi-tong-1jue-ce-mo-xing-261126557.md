---
title: 'MM-SystemOneBias: Evaluating Bias in Multimodal Jev-Style System One Decision
  Models'
title_zh: MM-SystemOneBias：多模态Jev式系统1决策模型偏差评估框架
authors:
- Jinzhe Li
- Qi Wang
- Dandan Guo
- Li Liu
- Yuan Wu
- Yi Chang
affiliations:
- School of Artificial Intelligence, Jilin University
- Engineering Research Center of Knowledge-Driven Human-Machine Intelligence, Jilin
  University
- International Center of Future Science, Jilin University
- King Abdullah University of Science and Technology
- School of Big Data and Software Engineering, Chongqing University
arxiv_id: '2611.26557'
url: https://arxiv.org/abs/2611.26557
pdf_url: https://arxiv.org/pdf/2611.26557
published: '2026-11-19'
collected: '2026-11-21'
category: Eval
direction: 多模态模型 · 决策偏差评估
tags:
- Multimodal
- Bias Evaluation
- Decision Robustness
- Benchmark
- System One Model
one_liner: 提出多模态决策模型偏差评估基准，覆盖6类干预场景，量化13种模型的决策鲁棒性差异
practical_value: '- 做多模态电商内容审核、商品评分模型时，可复用6类干预测试集验证模型鲁棒性，避免选项顺序、无关信息干扰决策结果

  - 上线LLM决策类Agent（如智能选品、广告审核）前，可参考该框架做对抗性测试，排查仅靠准确率无法发现的输入扰动漏洞

  - 决策模型比原生LLM backbone对外部干扰的鲁棒性更高，业务场景选型时优先选经过决策适配微调的多模态模型'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有多模态决策模型的评估未统一决策界面偏差与模型行为的测试范式，无法公平对比决策模型与底座的实际任务表现，难发现准确率指标遗漏的输入扰动问题。

### 方法关键点
提出MM-SystemOneBias评估基准，覆盖11类任务场景、5323个实例，采用6类配对干预（选项顺序、选项标签、外部判断、图文描述、无关信息、评分尺度），测试13种模型、7组决策模型-底座配对的决策稳定性。

### 关键结果数字
全部7组配对的决策模型在选项标签、无关信息、评分尺度扰动下稳定性更高，6组配对选项顺序翻转率更低、冲突描述下精度损失更小；语义决策不变的样本中，回答概率平均绝对波动达4.56~11.55个百分点。
