---
title: Global Average Precision for Representation Learning
title_zh: 面向表征学习的全局平均精度可微损失gSAP
authors:
- Bill Psomas
- Mohammad Mahdi
- Michalis Thomas
- Danda Pani Paudel
- Giorgos Tolias
- Giorgos Kordopatis-Zilos
affiliations:
- Czech Technical University in Prague
- Sofia University "St. Kliment Ohridski"
arxiv_id: '2610.09863'
url: https://arxiv.org/abs/2610.09863
pdf_url: https://arxiv.org/pdf/2610.09863
published: '2026-10-07'
collected: '2026-10-08'
category: RecSys
direction: 度量学习 · 全局检索损失优化
tags:
- gAP
- Contrastive Loss
- InfoNCE
- Metric Learning
- Representation Learning
one_liner: 提出gAP可微surrogate损失gSAP，可直接替换现有对比损失，提升跨查询相似度一致性与检索效果
practical_value: '- 召回层双塔表征训练可直接替换InfoNCE/SigLIP为gSAP损失，无需改动其他训练逻辑，即可提升跨query相似度一致性，适合需统一相似度阈值的业务场景（如商品同款匹配、侵权内容检测）

  - 训练batch较大时可采用negative dropping策略，丢弃90%低相似度负样本仅保留高难负例，显存占用降低的同时几乎不损失效果，还可进一步扩大batch规模

  - 对存在大量无匹配结果query的场景（如电商冷门商品搜索、客服意图匹配），gSAP训练的模型gAP下降幅度比现有损失低1-5个百分点，可大幅降低误召回率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有的mAP、InfoNCE等检索指标与损失都是单query独立计算，不约束跨query的相似度分布一致性，而工业界检索系统大多依赖全局统一阈值做截断，单query优化的模型会出现不同query的正负样本相似度分布重叠，导致全局阈值下的召回精度骤降，且小温度下训练容易出现梯度消失问题。

### 方法关键点
- 提出全局平均精度gAP，将所有query-candidate对的相似度拉平后统一排序计算AP，天然约束跨query的相似度分布一致性
- 推导gAP的可微替代损失gSAP，输入仅需相似度矩阵与正负样本二值矩阵，可无缝替换现有所有基于相似度的损失，适配任意编码器、模态与监督方式
- 设计negative dropping策略，丢弃占比高达90%的低相似度负样本，大幅降低计算与显存开销，允许训练更大batch
- 低温度训练时gSAP的每个正样本会和全batch所有样本做比较，始终存在足够多未饱和的梯度项，解决单query损失在小温度下梯度消失的问题

### 关键结果
在跨模态检索（CLIP微调CC12M数据集）、自监督预训练（MoCo v3）、度量学习（SOP、iNaturalist数据集）、含干扰query的检索任务上验证：
- 跨模态零样本检索相比InfoNCE，gAP提升2-3.8个百分点，Recall@5提升0.5-2.1个百分点；零样本分类Top-1精度平均提升0.49个百分点
- 统一全局阈值下，gSAP在iNaturalist数据集上90%精度的召回率是mSAP的4倍，SOP数据集上提升12%
- 存在干扰query的任务中，gSAP的gAP下降幅度比基线低1-4.5个百分点，无需后处理分数校准即可获得高一致性

最值得记住的结论：单query优化的检索损失天然无法保证跨query的相似度一致性，针对全局阈值场景的检索系统，直接优化gAP比优化mAP/Recall@k能获得更显著的业务收益
