---
title: 'Beyond Geometric Complementarity: Coherent Overlap in Sparse Mixture-of-Experts
  Routing'
title_zh: 稀疏混合专家模型路由的相干重叠：打破几何互补性假设
authors:
- Huiyuan Tian
- Bonan Xu
- Shijian Li
affiliations:
- 浙江大学
- 香港理工大学
arxiv_id: '2607.28308'
url: https://arxiv.org/abs/2607.28308
pdf_url: https://arxiv.org/pdf/2607.28308
published: '2026-07-29'
collected: '2026-08-01'
category: Training
direction: 稀疏MoE路由机制 · 专家互补性分析
tags:
- MoE
- Sparse Routing
- Expert Subspace
- Geometric Complementarity
- Model Analysis
one_liner: 提出MoE路由分析框架，验证专家间存在相干重叠，推翻传统几何互补性假设
practical_value: '- 搭建LLM4Rec/电商排序侧的MoE模型时，可直接复用Top-2路由配置，同等计算量下效果优于Top-1，无需盲目追求专家几何正交的训练目标

  - 做MoE专家剪枝/压缩优化时，不能仅用输入子空间重叠度判断专家冗余，必须结合实际路由上下文的效果验证，避免误剪仍有功能价值的重叠专家

  - 分析推荐系统多路召回/多塔排序（类MoE结构）的互补性时，可复用ESSI指标和2×2因子实验框架，量化不同路/塔的实际价值，减少无效的多路设计'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统MoE设计默认专家间满足几何互补性，即每个专家覆盖不重叠的表征方向，这一假设支撑了路由设计、专家剪枝等大量工程实践，但此前研究混淆了路由一致性、候选专家质量、上下文交互三个独立维度，无法验证该假设是否成立，直接限制了MoE的效率优化和效果提升。

### 方法关键点
- 提出Expert Subspace Separation Index（ESSI），用专家内部局部切线离散度标准化专家间的子空间距离，解决原始子空间距离无基准的问题
- 设计前缀控制的2×2因子实验，交叉对比选中专家/未选中最优rival、实际前缀/匹配替代前缀四种组合，用差分法隔离候选质量、上下文效应、二者交互三个独立维度
- 结合冻结路由干预、控制变量训练实验，区分几何重叠度和实际功能价值的差异

### 关键结果
在OLMoE、Mixtral、DeepSeek-MoE等6个主流开源MoE模型上验证：1）所有模型的ESSI中位数为0.969，接近1，说明专家子空间重叠度和专家内部离散度相当，不存在强几何分隔；2）39组因子实验中，选中专家的残差解释能力全部优于未选中rival，但实际前缀会缩小该优势，交互项全部为负；3）24/39的冻结路由实验中，增加后续专家可降低next-token NLL，同等计算量下Top-2路由的验证损失比Top-1低0.1016±0.0025。

### 核心结论
几何相似度不能单独作为MoE专家冗余度、剪枝价值的判断依据，多专家收益可在重叠表征空间内通过不同非线性计算实现。
