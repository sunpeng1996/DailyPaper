---
title: Hybrid Probabilistic Zonotopes for Identifiable and Refinable Predictive Uncertainty
title_zh: 用于可识别可优化预测不确定性的混合概率Zonotope方法
authors:
- Zhen Zhang
- Amr Alanwar
affiliations:
- Technical University of Munich, Germany
- School of Computation, Information and Technology, TUM
arxiv_id: '2608.05454'
url: https://arxiv.org/abs/2608.05454
pdf_url: https://arxiv.org/pdf/2608.05454
published: '2026-08-05'
collected: '2026-08-07'
category: Other
direction: 预测不确定性建模 · 神经网络输出头设计
tags:
- Uncertainty Estimation
- Probabilistic Prediction
- Neural Network Head
- Conformal Prediction
- Zonotope
one_liner: 提出可拆分三类不确定性源的神经网络输出头HProbZ，支持单步推理下分布迭代优化
practical_value: '- 推荐/广告排序场景可复用HProbZ拆分三类不确定性的思路，区分用户行为模态选择、特征漂移、随机噪声，优化冷启动、分布外样本的预估鲁棒性

  - 时序推荐（如用户下一个行为预测、履约时效预估）可复用跨步共享有界生成器的设计，单步观测即可快速修正全序列预测分布，降低推理开销

  - 线上决策场景可直接复用其无分布多模态保形集能力，替代传统高斯混合输出头，获得可解释的分模态风险量化结果，辅助流量调优、兜底策略配置'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
现有神经网络概率预测头普遍采用高斯混合或单保形区域输出，无法拆分真实任务中三类独立的不确定性源：模态离散选择、选中模态内的有界系统漂移、不可约随机噪声，也无法通过观测快速迭代优化预测分布，难以适配多模态时序预测等复杂场景。
### 方法关键点
提出混合概率Zonotope（HProbZ）输出头，将三类不确定性分别对应为zonotope的二元、有界、随机生成器，通过卷积得到闭式似然；跨预测步共享有界生成器，仅需单步观测即可通过一次前向传播完成所有剩余步的预测分布优化；三类生成器可从似然中唯一识别（排列不变），且表达能力与有限高斯互斥，推理时可直接输出分模态解析风险和无分布多模态保形集。
### 关键结果
在代表性预测基准上，效果优于同编码器的高斯混合基线，同时具备混合模型、凸保形预测器无法同时提供的结构特性。
