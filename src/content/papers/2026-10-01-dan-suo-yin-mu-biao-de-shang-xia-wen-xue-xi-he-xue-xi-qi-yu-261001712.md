---
title: 'In-context Learning of Single-index Targets: Comparing Kernel and Feature
  Learners'
title_zh: 单索引目标的上下文学习：核学习器与特征学习器对比
authors:
- Haotian Gu
- Yizhou Xu
- Lenka Zdeborová
affiliations:
- École Polytechnique Fédérale de Lausanne (EPFL)
- University of Chinese Academy of Sciences
arxiv_id: '2610.01712'
url: https://arxiv.org/abs/2610.01712
pdf_url: https://arxiv.org/pdf/2610.01712
published: '2026-10-01'
collected: '2026-10-04'
category: LLM
direction: 大模型上下文学习 · 注意力架构对比
tags:
- In-context Learning
- Kernel Learner
- Feature Learner
- Attention Architecture
- Generalization Error
one_liner: 对比两类单层注意力架构的非线性ICL表现，给出不同场景下的最优架构选择相图
practical_value: '- 做Agent/生成式推荐的ICL Prompt工程时，可参考两类学习器的适用场景调整上下文样例数量与任务分布，提升少样本适配效果

  - 基于ICL做电商多任务推荐时，若任务池多样性高，优先选择特征学习器类架构：原始输入过注意力后接任务专属非线性读出层，泛化效果更优

  - 做ICL推理优化时，可根据两类学习器的上下文长度缩放规律，结合业务可用的推理窗口大小调整预训练阶段的任务池配置'
score: 7
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有ICL理论研究多聚焦线性目标函数，非线性场景下不同注意力架构的表现差异与适用边界尚不清晰，无法指导面向非线性任务的ICL架构选型。
### 方法关键点
对比两类单层注意力架构在单索引非线性任务上的表现：1）核学习器：输入先经固定非线性特征映射再做线性注意力；2）特征学习器：原始输入做注意力后接可学习非线性读出层；采用replica方法推导两类架构的记忆与泛化误差，纳入预训练数据量、任务池多样性、训练/推理上下文长度等变量的影响。
### 关键结果
理论预测与多场景数值实验高度匹配；给出不同预训练数据量、任务多样性、上下文长度下的最优架构选择相图；发现两类学习器的泛化误差随上下文长度的缩放规律存在本质差异
