---
title: Training Trajectories Determine Circuit Removability in Annealable Soft-Prior
  Transformers
title_zh: 可退火软先验Transformer中训练轨迹决定电路可移除性
authors:
- Zonglin Yang
- Ziming Zhao
- Wei Tang
- Xunyu Jiang
- Yihong Liu
- Tailin Chen
- Zifu Yu
- Jiayu Liu
affiliations:
- Guangdong Police College
arxiv_id: '2609.10287'
url: https://arxiv.org/abs/2609.10287
pdf_url: https://arxiv.org/pdf/2609.10287
published: '2026-09-09'
collected: '2026-09-10'
category: Training
direction: Transformer训练动态 · 机制可解释性
tags:
- Transformer
- Training Trajectory
- Inductive Bias
- Mechanistic Interpretability
- In-context Learning
one_liner: 证明软位置先验的训练轨迹而非最终架构决定Transformer检索电路可移除性
practical_value: '- 业务中使用带位置先验的小Transformer做序列召回/ICL推理时，可采用渐变消隐先验的训练方案，既借助先验提升训练效率，又能在推理阶段移除先验降低计算开销

  - 做模型轻量化/结构重参数时，不要直接硬删训练阶段的辅助分支/偏置，采用平滑渐变的退火策略能保留更多性能，效果远好于硬切换或后补零门控训练

  - 针对离散检索类任务（如用户行为序列的物品关联召回），若从零训练无位置先验的小模型效果差，可先加先验训练再平滑消隐，能大幅提升最终无先验模型的准确率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
软位置先验可大幅降低小Transformer学习检索电路的难度，但常规训练下模型会对该先验产生强依赖，推理时移除先验会导致性能骤崩，此前业界未明确是否存在既能利用先验提升训练效率、又能在推理阶段完全移除先验的可行训练方案。
### 方法关键点
- 提出带门控的可退火软先验注意力机制，每个注意力头额外增加可调度门控的位置偏置、内容偏置项，门控支持自由学习、固定值、自定义调度三种模式
- 设计多组对照训练路径：无约束自由训练、全程强制零门控、固定0.5门控、线性衰减、先固定0.5门控再平滑衰减到0后继续训练（fade-to-zero路径）
- 覆盖关联召回、马尔可夫归纳、线性回归ICL三类任务测试门控移除后的性能，同时溯源注意力头的功能变化验证机制
### 关键结果
- 关联召回任务：无约束训练模型带先验准确率0.772，移除先验后骤降到0.095；fade-to-zero路径训练的模型移除先验后准确率仍达0.734
- 硬切门控、后补零门控训练的零门控准确率仅为0.293、0.178，远低于平滑渐变方案
- 马尔可夫归纳任务：fade-to-zero路径在p=0.2的难例场景下零门控准确率仍达0.83，大幅领先对照方案
- 线性回归ICL为边界场景，从零训练零门控模型即可收敛，渐变策略增益有限

最值得记住的结论：对于零门控从零训练难以收敛的离散检索类任务，先加软先验再平滑退火消隐的训练路径，可得到性能几乎无损的无先验模型，可移除性由训练轨迹而非最终架构决定。
