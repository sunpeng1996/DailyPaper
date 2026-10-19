---
title: 'Belief-Trajectory Energy: Measuring the Path to a Prediction'
title_zh: 信念轨迹能量（BTE）：基于Transformer层间预测修正的输入度量方法
authors:
- Jiahao Ying
- Wei Tang
- Boxian Ai
- Yaoning Wang
- Haotian Chen
- Wenhe Sun
- Caijun Xu
- Haozhan Cai
- Changyi Xiao
- Yixin Cao
affiliations:
- Fudan University
- University of Science and Technology of China
- Shanghai Innovation Institute
arxiv_id: '2610.05114'
url: https://arxiv.org/abs/2610.05114
pdf_url: https://arxiv.org/pdf/2610.05114
published: '2026-10-03'
collected: '2026-10-19'
category: LLM
direction: LLM内部机制 · AIGC检测与度量
tags:
- BTE
- Transformer Interpretability
- LLM Evaluation
- AIGC Detection
- Difficulty Measurement
one_liner: 提出基于Transformer层间信念变化的BTE度量，可用于难度评估、AIGC检测与生成源归因
practical_value: '- LLM4Rec场景下可复用BTE层间JSD计算逻辑，量化prompt/候选item的模型感知难度，优化粗排阶段的候选过滤规则，减少无效推理

  - 电商营销文案、Agent客服回复等生成内容，可通过BTE深度特征做生成质量校验、生成源归因，降低低质/非合规生成内容的透出风险

  - 业务场景微调LLM时，可通过BTE的下降幅度量化模型对业务数据的熟悉度，判断微调收敛阈值，节省训练算力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM应用仅关注最终输出，完全丢弃了Transformer层间逐步修正预测的过程信息；传统内部特征要么人工构造缺乏理论支撑，要么维度过高难以跨任务复用，亟需兼具理论完备性、易用性的模型内部动态度量方法。
### 方法关键点
- 基于logit-lens思路，将每一层残差状态通过模型输出头投影为词表预测分布（即模型信念），统一层间状态的度量空间
- 用相邻两层预测分布的JSD计算单层BTE，表征该层的预测修正幅度，理论上符合Fisher-Rao几何下的有效预测更新度量
- 聚合所有token的单层BTE得到固定长度的BTE深度剖面，可压缩为中间层均值作为无需训练的标量信号
### 关键结果
- 无训练BTE标量与4类推理任务难度的斯皮尔曼相关最高达0.66，可直接度量模型感知的输入难度
- 人机评审检测任务上，BTE方法macro-AUROC最高达0.998，显著优于log-likelihood、Binoculars等基线
- 8源生成内容归因任务上，引入token级BTE统计特征后准确率最高达95.6%
### 核心结论
LLM不仅是预测工具，其内部预测动态本身就是反映输入属性、模型学习状态的可靠度量信号
