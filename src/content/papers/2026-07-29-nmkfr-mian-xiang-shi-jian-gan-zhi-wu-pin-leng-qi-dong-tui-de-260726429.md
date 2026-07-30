---
title: 'NMKFR: A Robust Framework for Time-Aware Cold-Start Recommendation'
title_zh: NMKFR：面向时间感知物品冷启动推荐的鲁棒框架
authors:
- Chengzhi Liu
- Ning Zeng
- Zehui Qu
affiliations:
- Southwest University
arxiv_id: '2607.26429'
url: https://arxiv.org/abs/2607.26429
pdf_url: https://arxiv.org/pdf/2607.26429
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 推荐系统 · 时间感知物品冷启动
tags:
- Cold-Start Recommendation
- Kalman Filter
- Semantic Encoding
- Temporal Recommendation
- Uncertainty Modeling
one_liner: 结合记忆增强语义编码与卡尔曼状态跟踪，实现时间感知下鲁棒的物品冷启动推荐
practical_value: '- 冷启动阶段可复用「不确定性加权多源特征融合」思路：用卡尔曼后验协方差作为置信度信号，动态调整静态内容特征、早期交互特征的权重，避免固定加权在冷启动不同阶段的效果波动

  - 物品文本编码可借鉴Titans双路结构：并行短程注意力+长程记忆模块，同时保留商品标题/属性的局部短语信息和跨样本通用语义模式，尤其适合新品缺少交互时的语义表征构建

  - 时间间隔建模可复用log压缩+矩阵指数过渡方案：将不规则的用户交互间隔映射到有界范围，避免时间差过大导致的模型数值不稳定，适配电商场景用户访问间隔差异大的特点'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商/内容平台新品冷启动时，早期交互稀疏且用户兴趣、流行度随时间动态变化，静态内容、早期反馈、时序上下文三类信号的可靠性在商品生命周期不同阶段差异极大，现有方法多聚焦单源信号增强，缺乏对多源信号可靠性的动态自适应协调，导致冷启动排序效果不稳定。
### 方法关键点
- 双路架构：语义分支采用反馈驱动Titans编码器（FD-TSE）从物品文本提取记忆增强的静态表征；时序分支采用时间感知卡尔曼动态跟踪器（TA-KDT）处理不规则交互间隔，估计用户侧隐式时序状态与对应后验协方差
- 不确定性引导机制：基于卡尔曼后验协方差的迹生成不确定性信号，一方面动态调制FD-TSE的记忆检索权重，另一方面驱动自适应比较融合模块（ACFM）调整静态/时序特征的融合比例
- 混合损失：结合listwise、pairwise、pointwise的混合监督目标，适配冷启动阶段少量交互下的稳定学习
### 关键实验
在Amazon Video Games、MovieLens-32M两个公开数据集上与12个主流基线（BERT4Rec、SASRec、Mamba4Rec等）对比，时间感知冷启动场景下较最优基线分别提升2.16%、3.39%，纯物品冷启动场景下分别提升3.10%、0.40%，在文本噪声、用户历史极短的鲁棒性测试中依然保持性能优势。
### 核心洞见
冷启动推荐的核心不仅是补充缺失信号，更要动态衡量不同信号的可靠性，用不确定性作为多源信号融合的自适应调节锚点。
