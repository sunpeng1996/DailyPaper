---
title: 'LOPA: Enhancing Spoken Language Assessment via Latent Ordinal Prototype Alignment'
title_zh: LOPA：基于潜在序数原型对齐的口语语言评估效果优化
authors:
- Hong-Yun Lin
- Fu-An Chao
- Bi-Cheng Yan
- Berlin Chen
affiliations:
- National Taiwan Normal University
arxiv_id: '2606.31310'
url: https://arxiv.org/abs/2606.31310
pdf_url: https://arxiv.org/pdf/2606.31310
published: '2026-06-30'
collected: '2026-07-05'
category: Training
direction: 口语评估 · 序数感知轻量建模优化
tags:
- Ordinal Regression
- Prototype Alignment
- Frozen Encoder
- Feature Routing
- Speech Representation
one_liner: 提出LOPA正则与SALR层路由框架，无需大模型微调即可匹敌十亿参数级口语评估系统性能
practical_value: '- 对有序数属性的打分任务（如商品星级预测、用户满意度评分、广告质量分层），可借鉴LOPA潜在序数原型对齐正则化，在隐空间注入序数先验，提升排序一致性，减少标注成本

  - 冻结大模型编码器的场景下（如冻结CLIP做商品多模态特征提取、冻结BERT做文本表征），可复用SALR语义锚定层路由方法，自适应融合不同深度层的特征，无需全量微调即可达到接近大模型微调的效果

  - 低资源小样本场景下的打分类任务，可参考「轻量正则+冻结基座特征路由」的架构，大幅降低训练和推理成本，适配资源受限的业务部署'
score: 4
source: arxiv-cs.MM
depth: abstract
---

## 动机
当前基于MLLM的口语能力评估（SLA）方案存在两大痛点：一是十亿级大模型微调、部署成本极高，低资源场景无法落地；二是把评分任务当作普通生成/回归问题，完全忽略语言能力递进的内在序数结构，打分一致性差。
## 方法关键点
1. 设计LOPA潜在序数原型对齐正则器，直接在隐空间引入序数几何先验，建模不同评分等级的递进关系；
2. 配套SALR语义锚定层路由机制，自适应从冻结的Whisper编码器中选取不同深度的特征表征，全程无需微调大模型参数。
## 关键结果
SLA任务RMSE达0.361，性能匹敌十亿参数级MLLM系统，同时输出可解释、与评估准则对齐的打分结果，训练推理成本大幅降低
