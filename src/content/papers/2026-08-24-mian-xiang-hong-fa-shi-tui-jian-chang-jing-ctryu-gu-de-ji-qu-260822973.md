---
title: Cascading Relevance-driven Recommendation Network for CTR Prediction in Trigger-Introduced
  Recommendation
title_zh: 面向触发式推荐场景CTR预估的级联相关性驱动推荐网络
authors:
- Kaixuan Chen
- Wenwen Wang
- Xing Fang
- Yang Huang
- Jing Wang
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2608.22973'
url: https://arxiv.org/abs/2608.22973
pdf_url: https://arxiv.org/pdf/2608.22973
published: '2026-08-24'
collected: '2026-08-25'
category: RecSys
direction: 触发式推荐 · CTR预估优化
tags:
- CTR-Prediction
- Trigger-Induced-Recommendation
- Relevance-Modeling
- Attention-Mechanism
- Pairwise-Loss
one_liner: 针对触发式推荐场景提出CRRN模型，通过显式增强触发-目标相关性提升CTR预估效果
practical_value: '- 触发式推荐场景（点击商品后跳转的相关品推荐页）可直接复用CRRN的三层架构，线上仅增加2ms延迟，满足工业级服务要求

  - 类别辅助对偶损失可低成本迁移到所有需增强物品相关性的推荐场景，只需定义物品对的相关标签（如同类目、同品牌）即可生效，无需修改模型结构

  - 级联兴趣融合的自适应加权思路可复用：用预测的用户触发意图+触发-目标相似度，动态平衡即时兴趣和长期个性化兴趣，避免推荐结果要么偏历史要么过度同质化

  - 触发意图的弱监督标签构造技巧：用页面内点击物品是否和触发物同类目作为训练标签，不需要额外人工标注，仅训练时使用推理时无开销'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
电商触发式推荐（TIR）是用户点击触发商品后跳转的相关品推荐场景，是提升购物沉浸感的核心入口；传统CTR模型未显式建模触发物与目标品的相关性，要么过度偏向用户历史行为导致和触发物关联弱，要么过度拟合触发物导致推荐同质化，严重影响转化和用户体验。

### 方法关键点
1. **触发-目标交互层**：通过个性化门控网络融合显式共现特征（如同类目、同品牌）和隐式特征交互，提取两者的高阶关联特征
2. **级联兴趣融合模块**：先通过弱监督预测用户当前触发意图（标签为页面点击品是否和触发物同类目），再通过级联注意力块分别提取用户长期兴趣和触发相关即时兴趣，结合触发-目标的余弦相似度自适应加权融合两类兴趣
3. **类别辅助对偶损失**：重构排序偏序规则为「相关点击>非相关点击>相关曝光>非相关曝光」，显式增强模型对触发相关性的学习

### 关键实验结果
在天猫4.5亿条工业样本上，CRRN对比基线DIN+TAR的AUC相对提升6.31%，优于此前SOTA模型DEI2N；线上A/B测试显示，CTR提升3.87%，IPV提升5.75%，同/相关类目推荐占比从47.67%提升至88.76%，推理延迟仅增加2ms，完全满足线上要求。

### 最值得记住的一句话
触发式推荐场景的核心是在用户即时兴趣和长期个性化之间找平衡，显式增强触发-目标相关性的同时避免过度同质化，可同时提升转化和用户体验。
