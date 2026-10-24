---
title: High-Value Training Data from Noisy, Diverse Sources
title_zh: 面向异质噪声数据源的高价值训练数据自动加权方法
authors:
- Hedi Driss
- Evan Frick
- Anastasios N. Angelopoulos
- Cho-Jui Hsieh
- Yejin Huh
- Tijana Zrnic
- Andrew Ilyas
affiliations:
- Hiddenweights
- Arena
- UCLA
- Stanford
- CMU
arxiv_id: '2610.30421'
url: https://arxiv.org/abs/2610.30421
pdf_url: https://arxiv.org/pdf/2610.30421
published: '2026-10-21'
collected: '2026-10-24'
category: Training
direction: 训练数据权重优化 · 跨模型跨域迁移
tags:
- Data-Weighting
- Meta-Gradient
- Reward-Modeling
- Transfer-Learning
- Synthetic-Data
one_liner: 基于元梯度的参数化数据权重学习方法，可跨模型跨数据迁移，高效利用异质噪声训练数据
practical_value: '- 电商/广告垂类大模型RLHF对齐时，可复用该方法自动过滤噪声偏好数据、分配人类/合成偏好数据权重，无需人工设计复杂过滤规则，实测效果优于纯用人类标注数据

  - 小样本垂直领域适配（如电商3C/美妆垂类偏好模型、Agent专属技能训练）时，可先用小参数模型学习数据权重再迁移到大模型，大幅降低元优化的算力成本

  - 业务场景需要优化与训练损失不一致的下游指标（如推荐GMV、搜索排序相关性）时，可将下游指标封装为可微代理作为目标损失优化数据权重，无需修改原有训练主流程'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
当前大模型训练依赖异质混合数据源（人类标注、合成数据、多来源爬取数据等），传统人工设计过滤规则、数据混合比例的方式成本高、泛化性差，现有数据加权方法难以扩展到大规模场景，且缺少可跨模型、跨数据流迁移的方案。

### 方法关键点
- 基于元梯度计算每个训练样本对目标域小高质量数据集性能的影响，迭代优化样本权重，通过训练过程反向传导目标域损失梯度
- 提出参数化数据权重：用小映射头将样本嵌入映射为权重，而非为每个样本单独学习权重，支持流式新数据直接赋权，大幅降低优化维度
- 训练轨迹分段优化，平衡计算效率与效果；支持将小模型学到的权重直接迁移到大模型训练，无需在大模型上做昂贵的元优化
- 支持自定义下游目标，可直接优化与训练损失不一致的下游指标（如排序相关性），仅需提供可微的目标损失代理

### 关键结果
实验以Reward Modeling为核心场景，对比TRAK、TracIn等数据选择基线及常规微调方案：
- 异质人类偏好数据训练下，STEM领域测试损失比无权重训练低15%，比最强基线TRAK低6.6%
- 混入噪声bot数据时，数据加权可完全恢复无噪声场景下的性能
- 混合人类+合成数据训练，加权后效果比纯用人类数据高2.9%
- 0.5B小模型学到的权重迁移到7B大模型仍可稳定提升性能，参数化权重可直接泛化到3倍以上未见过的训练数据

高价值训练数据的筛选不需要依赖人工先验规则，直接通过目标域性能的元梯度反向传导即可自动实现，且可跨规模迁移大幅降低算力成本
