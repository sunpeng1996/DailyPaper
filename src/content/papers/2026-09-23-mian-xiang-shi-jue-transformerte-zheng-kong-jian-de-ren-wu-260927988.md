---
title: Task-Induced Riemannian Metrics for Vision Transformer Feature Spaces
title_zh: 面向视觉Transformer特征空间的任务诱导黎曼度量方法
authors:
- Andrew Bond
- Ege Erdem Özlü
- Tuna Çimen
- Ilkin Umut Melanlioglu
- Tolga Birdal
- Erkut Erdem
- Aykut Erdem
affiliations:
- Koç University
- Imperial College London
- Hacettepe University
arxiv_id: '2609.27988'
url: https://arxiv.org/abs/2609.27988
pdf_url: https://arxiv.org/pdf/2609.27988
published: '2026-09-23'
collected: '2026-09-24'
category: Other
direction: 视觉Transformer · 特征空间度量优化
tags:
- Vision Transformer
- Riemannian Metric
- Low Rank Approximation
- Token Pruning
- Feature Representation
one_liner: 提出可低秩逼近的任务敏感ViT特征黎曼度量，附带仅310K参数的token重要性预测头
practical_value: '- 多模态电商推荐的商品图文特征匹配场景，可借鉴任务诱导度量替代传统余弦/欧氏距离，提升跨模态特征相关性判断准度

  - 多模态召回/粗排链路的ViT推理加速，可复用本文轻量化token重要性头实现无微调token剪枝，降低推理延迟不损效果

  - 大模型特征适配下游任务时，可参考$κ_{cap}$诊断判断低秩近似可行性，平衡计算成本与下游任务效果'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有ViT特征运算默认采用欧氏距离/余弦相似度，假设特征空间所有方向重要性一致，与下游任务实际特征敏感度不匹配，全量任务敏感拉回度量的计算、存储成本过高无法规模化落地。
### 方法关键点
1. 提出无矩阵诊断指标$κ_{cap}(r)$，仅需少量雅可比向量积即可判断给定模型-解码器对是否支持度量的低秩近似；
2. 对可低秩近似的组合，开发Spectral Pullback Network（SPN）基于随机幂迭代学习低秩度量，蒸馏为310K参数的轻量化重要性头，直接从特征预测token重要性；
3. 雅可比谱分布过散无法低秩近似时，可通过VAE瓶颈层降维恢复可计算性。
### 关键结果
- 重要性头在DINOv2 CLS上Spearman $ρ$达0.998；
- 0.5剪枝率下，几何token剪枝将DPT深度估计任务中ToMe选择方法的额外深度误差降低25%，无需微调ViT。
