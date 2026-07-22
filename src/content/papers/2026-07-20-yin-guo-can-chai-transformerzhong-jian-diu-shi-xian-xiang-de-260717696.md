---
title: An Adjoint-Sensitivity Framework for Lost-in-the-Middle Phenomena in Causal
  Residual Transformers
title_zh: 因果残差Transformer中间丢失现象的伴随灵敏度分析框架
authors:
- Cheng Huan
- Hongwei Yuan
affiliations:
- The Chinese University of Hong Kong
- University of Macau
arxiv_id: '2607.17696'
url: https://arxiv.org/abs/2607.17696
pdf_url: https://arxiv.org/pdf/2607.17696
published: '2026-07-20'
collected: '2026-07-22'
category: LLM
direction: 长上下文LLM · 位置偏差优化
tags:
- Lost-in-the-Middle
- Positional Bias
- Causal Transformer
- Adjoint Sensitivity
- Long Context
one_liner: 提出因果残差Transformer位置敏感性分析框架，推导Lost-in-the-Middle成因并给出缓解方案
practical_value: '- 长上下文RAG/电商导购Agent场景，可复用论文定义的伴随能量影响密度`m(p)`作为位置敏感性诊断指标，快速定位中间上下文的信息失效问题

  - 提出的三类正则器（影响平衡、位置重加权、任务对齐可观测性平衡）可直接嵌入现有长上下文推荐/搜索的LLM模块，无需重构架构即可缓解Lost-in-the-Middle问题

  - 有限token注意力到Volterra算子的收敛误差估计，可用来指导长上下文截断长度选择，在信息损失可控的前提下降低推理成本'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
长上下文大模型在检索、问答、生成式推荐等场景普遍存在Lost-in-the-Middle现象：上下文首尾内容对预测的影响远高于中间内容，现有研究多为实证观察，缺乏统一的理论框架量化位置敏感性、解释成因并指导可落地的优化方案。
### 方法关键点
- 将因果残差Transformer建模为连续深度动力系统，因果掩码对应注意力核的Volterra支撑条件，全批次梯度下降映射为连续时间梯度流极限，实现离散网络到连续模型的一致逼近
- 定义归一化伴随能量影响密度`m(p)`，量化不同上下文位置的损失敏感度，将其精确分解为残差传输、非局部Volterra、局部通道三类贡献，保留所有协方差交叉项
- 推导Lost-in-the-Middle现象的独立可检验充分条件，而非断言所有场景必然出现U型位置敏感度曲线；提出三类缓解正则器：有限token影响平衡、位置重加权、任务对齐可观测性平衡，明确各方法的微分要求、计算成本和适用边界
### 关键结果
- 理论证明有限token掩码注意力在远离左端点时收敛到连续Volterra算子的速度为`O(L⁻¹)`，左边界区域平均误差可控在`O(log n / n)`量级
- 受控仿真验证三类干预方法均可精准调控对应代理指标，位置重加权策略可将中间位置的平均敏感度相对提升35%以上，同时不显著增加训练开销
### 核心结论
Lost-in-the-Middle本质是训练过程中位置敏感度的不平衡，最直接的优化思路是让归一化影响密度匹配目标均匀分布，而非仅依赖注意力权重的事后调整
