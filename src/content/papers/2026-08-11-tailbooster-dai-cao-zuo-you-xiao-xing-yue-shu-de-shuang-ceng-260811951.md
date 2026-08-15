---
title: 'TailBooster: A Dual-Layer Generative Framework for Extreme Value Augmentation
  with Operational Validity Enforcement'
title_zh: TailBooster：带操作有效性约束的双层极端值生成增强框架
authors:
- Karim Aly
- Alexei Sharpanskykh
- Jacco Hoekstra
affiliations:
- Delft University of Technology (TU Delft)
arxiv_id: '2608.11951'
url: https://arxiv.org/abs/2608.11951
pdf_url: https://arxiv.org/pdf/2608.11951
published: '2026-08-11'
collected: '2026-08-15'
category: Other
direction: 极端事件预测 · 合成数据增强
tags:
- Synthetic Data Augmentation
- Extreme Event Prediction
- Generative AI
- Anomaly Detection
- Tabular Data
one_liner: 提出双层生成增强框架，解决混合表格数据极端样本不足、生成样本不合规问题，提升极端事件预测效果
practical_value: '- 针对推荐/广告场景下稀疏极端样本（如极端高转化、极端大客单价用户行为）的模型训练，可复用「先统计提取尾部分布样本单独训练生成模型」的思路，解决尾部数据学习信号不足问题

  - 生成合成样本时，可新增基于历史数据训练的autoencoder校验层，自动过滤不符合业务逻辑的无效合成样本（如客单价远高于类目上限的异常数据），无需人工枚举规则

  - 小样本场景下将真实尾部数据与合成极端数据混合训练，可直接提升下游回归/分类任务在尾部样本上的预测精度，可复用到异常流量识别、大促峰值预测等场景'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
航空等领域极端事件（如严重航班延误）历史样本极稀疏，ML模型缺乏足够训练信号；传统生成式数据增强方法既欠拟合分布尾部，又无法保证生成样本符合业务逻辑（如长航程对应短飞行时间这类无效样本），现有方案无法同时解决混合类型表格数据的这两个痛点。

### 方法关键点
提出TailBooster双层生成框架：1）统计层通过四分位距提取真实尾部极端样本，给Tabular VAE提供尾部集中的训练信号，专门生成极端值样本；2）深度学习层用基于autoencoder的清洗模块，自动丢弃不符合历史数据学习到的业务操作边界的无效合成样本。框架完全数据驱动、模型无关。

### 关键结果数字
在美国航班数据集上验证：对比传统合成数据，用TailBooster生成的数据训练6种回归模型，极端飞行时间预测MAE降低47-49%，极端到达延误预测MAE降低29-57%；真实数据混合合成极端样本训练也能获得相当的精度提升。
