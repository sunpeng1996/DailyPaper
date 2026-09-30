---
title: 'Jev thinks "I don''t know'''', but doesn''t say it: Introducing Sys1Cal-v1
  Dataset for Probability Calibration'
title_zh: Sys1Cal-v1：面向System One模型概率校准的专用评测数据集
authors:
- Riccardo Porcedda
affiliations:
- little-g.ai
- Sant'Anna School of Advanced Studies
- University of Pisa
arxiv_id: '2609.35342'
url: https://arxiv.org/abs/2609.35342
pdf_url: https://arxiv.org/pdf/2609.35342
published: '2026-09-27'
collected: '2026-09-30'
category: Eval
direction: 概率校准 · 结构化决策模型评测
tags:
- Probability Calibration
- Evaluation Dataset
- System One Model
- Decision Making
- Uncertainty Estimation
one_liner: 构建带已知真值概率的Sys1Cal-v1数据集，揭示Jev模型Choice接口隐藏的不确定态并给出校准方案
practical_value: '- 推荐/广告的点击率/转化率预估校准可复用该思路：当排序模型输出概率数值偏倚时，可新增多档位打分接口反推隐藏不确定度，修正后提升投放ROI

  - Agent决策模块可引入T/U/F三元概率框架，不确定度U超过阈值时触发人工审核、调用重模型或请求用户补充信息，降低电商风控、售后自动应答等场景的错误决策成本

  - 可复用Distributional Overlap（软准确率）作为概率类模型的评测指标，比传统准确率、ECE更贴合下游决策依赖概率数值的业务场景

  - 业务侧构造评测集时可参考Sys1Cal-v1的同问题多渲染设计，验证模型输出的语义一致性，避免文案表述波动导致的结果不稳定'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有System One类结构化决策模型（如Jev）宣称输出校准概率，但现有评测仅验证置信度校准，无法校验每个输出概率的数值准确性，也无法对比同模型不同接口的概率语义一致性，缺乏带已知真值概率的专用评测数据集。

### 方法关键点
- 构建Sys1Cal-v1合成数据集，包含92个概率问题、365个等价渲染样本，每个样本的命题真值概率P(A)已知，覆盖显式概率、计数频率、贝叶斯推理等6类场景，支持文本、表格、带干扰项等多种表述形式
- 设计三类评测接口对齐Jev的Noul（二分类概率输出）、Choice（多选概率输出）、Score（10级有序打分输出）原语，采用总变差距离（TV）和分布重叠度（OVL，软准确率）作为核心指标
- 提出隐式不确定态π_U假设：Choice接口的概率输出是排除不确定态后对True/False概率重归一化的结果，可通过Score的期望反推π_U，实现Choice输出的后校准

### 关键结果
在Sys1Cal-v1上评测Jev和开源基线SemIf：Jev的Noul接口平均OVL达0.918，Score接口达0.886，而Choice接口仅0.764；引入不确定态校准后，Choice的平均OVL提升至0.880，若保留三元T/U/F表示，平均OVL可达0.931，中位数OVL达0.978。

### 核心结论
如果模型输出的概率要直接用于下游自动化决策，概率本身的数值准确性比仅验证顶标签的置信度校准重要得多。
