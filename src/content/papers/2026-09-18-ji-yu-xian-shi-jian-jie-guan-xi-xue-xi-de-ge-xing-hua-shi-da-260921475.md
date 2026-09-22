---
title: Adaptive Preference Modeling via Explicit Indirect Relational Learning for
  Personalized Fashion Matching
title_zh: 基于显式间接关系学习的个性化时尚搭配自适应偏好建模
authors:
- Shuiying Liao
- Li Li
- P. Y. Mok
affiliations:
- The Hong Kong University of Science and Technology
arxiv_id: '2609.21475'
url: https://arxiv.org/abs/2609.21475
pdf_url: https://arxiv.org/pdf/2609.21475
published: '2026-09-18'
collected: '2026-09-22'
category: RecSys
direction: 互补品推荐·稀疏冷启动 多模态建模
tags:
- Contrastive Learning
- Multi-modal Recommendation
- Cold Start
- Complementary Recommendation
- Sparse Data
one_liner: 显式构建间接关系视图结合功能对比学习，优化稀疏场景下个性化时尚搭配推荐
practical_value: '- 关联采样策略可直接落地：针对交互稀疏/用户冷启动场景，通过用户共现交互加权计算相似度，挖掘相似用户历史行为作为补充信号，无需维护全量交互图，离线批计算、在线查询延迟低，工程适配性强

  - 多模态融合trick可复用：搭配类商品推荐场景下，视觉/文本特征的贡献可通过π参数灵活调节，针对服饰、家居等不同品类动态调整模态权重，无需重训全量模型

  - 功能对比学习范式可迁移：将直接交互表征与间接关联表征做对比对齐，无需额外标注就能提升稀疏场景表征鲁棒性，可嵌入现有召回/排序模型的预训练阶段'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
时尚电商互补品搭配推荐需同时建模用户个性化偏好与商品兼容性，但服饰品类生命周期短、新货迭代快，用户交互数据极度稀疏；现有方法要么隐式通过图传播捕捉高阶关系，特征纠缠不可控，要么仅依赖直接交互，冷启动效果差。
### 方法关键点
- 框架拆解为4个独立模块：直接用户偏好建模(P)、直接商品兼容性建模(C)、显式间接用户偏好建模(IP)、显式间接商品兼容性建模(IC)，分别捕捉直接/间接两类信号
- 设计关联采样策略：通过用户共现交互加权计算相似度，挖掘Top-K相似用户的行为序列，聚合生成间接偏好/兼容性视图，避免图传播导致的特征纠缠
- 引入功能视图对比学习：分别对齐P与IP、C与IC的表征，用InfoNCE损失拉通直接/间接信号的语义一致性，无需额外标注即可提升表征鲁棒性
- 多模态特征融合：基于CLIP预训练提取商品的视觉/文本特征，通过可调节权重π动态分配两类模态的贡献
### 关键实验
在IQON3000、Polyvore两个公开时尚推荐数据集上对比12个SOTA基线，IQON3000数据集上AUC达0.9739，较次优SOTA提升10.1%，HR@10达0.9509提升8.2%；Polyvore数据集上AUC达0.9832，较次优提升9.2%，HR@10提升5.0%，冷启动/稀疏交互场景下提升幅度更显著。
### 核心结论
显式构建间接关系视图并做功能级对比对齐，比隐式图传播能更高效地利用稀疏交互信号，大幅提升互补品推荐的冷启动性能
