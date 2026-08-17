---
title: A Four-Axis Trustworthiness Benchmark for LLM-as-Judge in Principle-Based Regulation
title_zh: 面向原则型监管下LLM裁判的四维度可信度基准
authors:
- Dipankar Sarkar
affiliations:
- Independent Researcher
arxiv_id: '2608.14329'
url: https://arxiv.org/abs/2608.14329
pdf_url: https://arxiv.org/pdf/2608.14329
published: '2026-08-14'
collected: '2026-08-17'
category: Eval
direction: LLM-as-Judge 可信度评估与合规监管
tags:
- LLM-as-judge
- trustworthy evaluation
- calibration
- adversarial robustness
- AI governance
one_liner: 提出LLM-as-judge四维度评估框架，开源Principle-Bench数据集与可校准Ceca评估器
practical_value: '- 电商/广告合规审核场景的LLM-as-judge评估可直接复用四维度框架，除整体准确率外必须评估对抗鲁棒性、校准度，避免漏过「合规表演」类bad
  case

  - 构造合规测试集时可参考本研究的扰动方法：加入关键词堆砌、语义改写、边界样本，针对性检测模型对故意规避合规要求的物料的识别能力

  - 部署级合规LLM裁判可参考Ceca的可审计设计，输出单样本反事实归因，既方便bad case迭代，也能满足监管举证要求'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
原则型监管（如电商广告要求的「公平清晰不误导」）无法简化为二元判断规则，当前LLM-as-judge评估维度单一，缺乏鲁棒性、校准度相关的标准化测试基准。

### 方法关键点
1. 定义LLM-as-judge四维度评估框架：准确率、paraphrase鲁棒性、对抗鲁棒性、校准度；
2. 开源Principle-Bench数据集，包含168个金融推广场景，对齐2项英国FCA监管原则，构造改写、对抗关键词堆砌、边界扰动三类测试样本；
3. 提出Ceca可校准评估器，支持单样本反事实归因，满足审计要求。

### 关键结果数字
- 120B LLM裁判在良性样本上准确率0.74，在关键词堆砌的对抗测试集上准确率骤降至0.27，下降47个百分点；
- 不同模型家族的LLM裁判在对抗样本集上Cohen's kappa仅为0.16，一致性极低，失效原因来自模型本身而非数据集；
- 无单一方法能在四个评估维度上全部取得最优表现。
