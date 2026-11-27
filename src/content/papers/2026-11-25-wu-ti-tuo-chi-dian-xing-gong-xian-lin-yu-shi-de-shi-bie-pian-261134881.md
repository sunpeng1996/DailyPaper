---
title: 'Stranger Things: When Objects Appear Without Their Typical Neighbors'
title_zh: 物体脱离典型共现邻域时的识别偏差诊断与缓解方法
authors:
- Siddhartha Gairola
- Jiahao Xie
- Anna Kukleva
- Francesco Locatello
- Bernt Schiele
affiliations:
- Max Planck Institute for Informatics
- Institute of Science and Technology Austria
arxiv_id: '2611.34881'
url: https://arxiv.org/abs/2611.34881
pdf_url: https://arxiv.org/pdf/2611.34881
published: '2026-11-25'
collected: '2026-11-27'
category: Multimodal
direction: 多模态识别 · 共现偏差优化
tags:
- Multimodal Model
- Bias Mitigation
- Data Augmentation
- Evaluation Benchmark
- Robustness
one_liner: 构建典型性偏差诊断基准STRANGE-Bench，提出AAS采样增强缓解多模态模型共现shortcut偏差
practical_value: '- 电商多模态商品识别/审核场景可复用NPMI计算物体共现度，定位模型共现shortcut偏差，优化直播等混合非相关商品场景的识别准确率

  - 训练多模态召回/排序模型时可引入AAS采样增强，刻意构造非典型共现训练样本，避免模型过度依赖上下文共现特征，提升跨场景泛化性

  - 多模态Agent做场景理解任务时，可复用STRANGE-Bench构造逻辑定制业务非典型样本评估集，提前发现模型鲁棒性缺陷'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
多模态模型识别物体时易过度依赖典型共现邻域的上下文特征，而非物体本身视觉特征，产生典型性偏差。此前缺乏针对现代视觉/多模态模型的系统性偏差诊断方案，行业普遍认为模型扩大会自然解决该问题。
### 方法
1. 采用物体对的归一化点互信息（NPMI）量化典型性偏差，构建包含17个从典型共现到从未共现物体对层级的真实感可控基准STRANGE-Bench；
2. 提出Anchor-Atypicality Sampling（AAS）数据增强方法，基于NPMI信号调整训练时物体共现分布，增加非典型共现样本占比，打破共现shortcut。
### 结果
5类主流模型在3类识别任务上均存在显著典型性偏差，脱离典型邻域时识别准确率下降5-11 p.p，且偏差不随模型规模扩大而稳定下降；AAS方法可在不损失整体性能的前提下，将COCO自然图像集的典型性偏差最多降低1.6 p.p，STRANGE-Bench合成集上最多降低23.0 p.p。
