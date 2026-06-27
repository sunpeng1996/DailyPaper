---
title: 'FedReLa: Imbalanced Federated Learning via Re-Labeling'
title_zh: FedReLa：基于样本重标注的非平衡联邦学习方法
authors:
- Guangzheng Hu
- Patricia Menéndez
- Feng Liu
- Mingming Gong
- Guanghui Wang
- Liuhua Peng
affiliations:
- University of Melbourne, School of Mathematics and Statistics
- University of Melbourne, School of Computing and Information Systems
- Nankai University, School of Statistics and Data Science
arxiv_id: '2606.26037'
url: https://arxiv.org/abs/2606.26037
pdf_url: https://arxiv.org/pdf/2606.26037
published: '2026-06-24'
collected: '2026-06-27'
category: Training
direction: 联邦学习 · 非平衡数据训练优化
tags:
- Federated Learning
- Class Imbalance
- Label Reallocation
- Long-tailed Data
- Privacy-Preserving Training
one_liner: 提出无需全局类别分布先验的样本重标注方法，解决联邦学习下数据异构与类别不平衡共存问题
practical_value: '- 跨端联邦推荐场景下遇到小众商品点击、低频次用户行为等长尾类别问题时，可直接复用FedReLa的特征依赖重标注逻辑，无需收集全局数据分布，完全符合隐私合规要求

  - 该方法为模块化、模型无关设计，可直接叠加到现有联邦推荐的重采样、权重调整类优化算法上，无额外通信开销，工程落地改造成本极低

  - 跨域隐私保护推荐场景下，不同域数据分布差异大、类别不平衡时，可借鉴重标注思路修正全局排序决策边界，提升小众类目推荐的召回和准确率'
score: 6
source: arxiv-stat.ML
depth: abstract
---

### 动机
联邦学习是隐私保护分布式训练的主流方案，实际场景中普遍存在全局类别不平衡、跨客户端数据异构共存的问题，本地与全局分布不匹配会严重降低聚合模型性能，现有数据层面方法依赖全局类别分布先验，在客户端存在严重类别缺失的极端场景下无法落地。

### 方法关键点
FedReLa为数据层面优化框架，通过基于特征的标签重分配器对样本重标注，无需感知全局类别分布即可修正有偏的全局决策边界；框架模块化、模型无关，可与现有算法类优化方法结合，无额外通信开销。

### 关键结果
在阶梯式不平衡、长尾数据集上，少数类准确率、整体准确率均显著超越此前SOTA，在极端类别缺失场景下仍保持稳定性能增益。
