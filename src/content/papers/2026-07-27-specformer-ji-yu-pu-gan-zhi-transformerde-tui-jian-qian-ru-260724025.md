---
title: 'SpecFormer: Mitigating Embedding and Attention Collapse via Spectral-Aware
  Transformer for Recommendation'
title_zh: SpecFormer：基于谱感知Transformer的推荐嵌入与注意力坍塌缓解方法
authors:
- Yu Cui
- Yi Xu
- Jiahao Wang
- Hao Zhang
- Yu Zhang
- Xiaoyi Zeng
- Can Wang
- Jinxin Hu
- Jiawei Chen
affiliations:
- Zhejiang University
- Alibaba Group
arxiv_id: '2607.24025'
url: https://arxiv.org/abs/2607.24025
pdf_url: https://arxiv.org/pdf/2607.24025
published: '2026-07-27'
collected: '2026-07-28'
category: RecSys
direction: 推荐系统 · Transformer特征交互优化
tags:
- Transformer
- CTR Prediction
- Spectral Collapse
- Feature Interaction
- Recommendation System
one_liner: 从谱域视角解决推荐场景Transformer嵌入与注意力坍塌问题，已落地阿里电商广告
practical_value: '- 特征交互用Transformer遇到性能瓶颈时，可先通过有效秩(erank)、奇异值累积占比两个指标量化嵌入/注意力坍塌程度，定位问题根源

  - 工业CTR场景可直接复用SpecFormer的三个核心模块替换现有Transformer特征交互层，仅增加5ms推理延迟即可拿到CTR、订单量的大幅提升

  - 训练谱感知模型时可采用两阶段训练：先用5%数据warm-up空间残差分支稳定嵌入分布，再开启谱软化模块训练，避免数值不稳定

  - 堆叠Transformer层性能不升反降时，可优先考虑引入谱软化正则替代盲目加参，解锁模型深度缩放能力'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
推荐场景直接套用标准Transformer常出现性能不如简单模型、堆叠层后性能下降的问题，核心原因是推荐数据的异质性、长尾分布导致嵌入和注意力出现严重谱坍塌：少数主奇异值占据绝大部分表征能量，前向传播时注意力退化为低秩稀疏矩阵，反向传播时梯度集中在主成分导致长尾特征梯度饥饿，形成坍塌恶性循环，现有方案要么加参成本过高，要么未从根源解决谱坍塌问题。

### 方法关键点
1. **可学习谱软化模块**：对每一层输入嵌入做SVD，通过可学习的幂律变换动态平滑奇异值分布，压缩主奇异值、放大长尾奇异值，重构更均匀的谱空间
2. **谱软化注意力**：Query和Key在软化后的谱空间计算交互，Value保留原始嵌入避免信息损失，平衡谱空间交互均匀性和原始表征准确性
3. **谱残差位置编码**：通过奇异值的二阶泰勒展开构造谱域偏置，补充原始空间注意力残差，避免谱软化过度损失主成分有效信息

### 关键实验
在1.2B规模阿里工业数据集、Criteo、Avazu三个数据集上，对比DeepFM、AutoInt、RankMixer、OneTrans等12个SOTA基线，工业数据集AUC达0.7611，比最优基线RankMixer高0.24个千分点；线上A/B测试相比生产DLRM基线，CTR提升1.34%，订单量提升16.72%，仅增加5ms推理延迟；堆叠9层SpecFormer时AUC持续上涨，注意力有效秩随深度稳步提升，解决了标准Transformer越深性能越差的问题。

**最值得记住的一句话**：推荐场景Transformer性能瓶颈的核心不是注意力容量不足，而是谱坍塌导致的表征和交互能力被锁死，从谱域优化比盲目加参加层的ROI高得多
