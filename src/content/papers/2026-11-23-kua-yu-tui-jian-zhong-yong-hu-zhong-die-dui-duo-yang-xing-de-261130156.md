---
title: 'Beyond Knowledge Transfer: How User Overlap Shapes Diversity in Cross-Domain
  Recommendation'
title_zh: 跨域推荐中用户重叠对多样性的影响机制及优化框架
authors:
- Yuhan Zhao
- Weixin Chen
- Shu Chen
- Li Chen
affiliations:
- Hong Kong Baptist University
- Shenzhen University
arxiv_id: '2611.30156'
url: https://arxiv.org/abs/2611.30156
pdf_url: https://arxiv.org/pdf/2611.30156
published: '2026-11-23'
collected: '2026-11-24'
category: RecSys
direction: 跨域推荐 · 多样性优化
tags:
- Cross-Domain Recommendation
- Diversity
- Negative Sampling
- Data Augmentation
- User Overlap
one_liner: 提出模型无关的DivCDR Push-Pull框架，解决跨域推荐双多样性瓶颈，兼顾精度与多样性
practical_value: '- 可直接复用DivCDR的模型无关设计，无需修改现有CDR backbone，仅在正负采样和训练目标上做增量改造，落地成本低

  - 针对重叠用户的置信度门控虚拟正样本增强方法，可迁移到单域推荐的多样性优化场景，平衡准确率与多样性的trade-off

  - 针对稀疏非重叠用户的重叠密度引导负采样策略，可用于冷启动用户的推荐去同质化，降低信息茧房效应

  - 双瓶颈诊断思路可直接用于现有跨域推荐系统的多样性问题归因，快速定位是重叠用户偏好覆盖窄还是非重叠用户信号被压制'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有跨域推荐(CDR)依赖重叠用户作为知识迁移桥梁，长期聚焦精度优化，普遍存在多样性不足甚至推荐同质化问题，其底层机制此前未被明确。经分析存在两个核心瓶颈：一是重叠用户覆盖的目标域偏好范围有限导致迁移桥过窄，二是重叠迁移信号压制非重叠用户的稀疏个性化证据导致迁移桥过响，共同制约推荐多样性表现。
### 方法关键点
- 整体为模型无关的Push-Pull双路框架，无需修改原有CDR backbone结构，仅通过正负样本干预和增量训练目标实现优化
- Pull模块面向重叠用户：基于用户表示生成个性化增强方向，结合正样本置信度门控控制扰动范围，构造合规虚拟正样本，同时优化单用户和重叠用户群的曝光熵增益，拓宽迁移桥的偏好覆盖
- Push模块面向非重叠用户：计算用户与重叠用户群的曝光相似度作为茧房强度，沿梯度下降方向引导负采样，采样温度自适应匹配茧房强度，推动非重叠用户的表示远离重叠密集区
### 关键结果
在Amazon、Epinions、TenRec 3个公开跨域数据集，5种主流CDR backbone上验证，对比3种现有多样性优化CDR方法：Shannon@5最高提升77.32%（DTCDR+DivCDR在TenRec），Gini系数平均降低5%以上，绝大多数场景下精度持平或提升，最高精度提升36.56%（CLFM+DivCDR在TenRec），仅少数场景精度下降幅度低于2.3%。
> 最值得记住：跨域推荐的多样性优化不能只依赖通用正则，要针对性解决重叠用户偏好覆盖窄、非重叠用户信号被压制两个独立瓶颈，才能在极少损失精度的前提下大幅提升多样性
