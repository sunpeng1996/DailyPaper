---
title: Prediction-Layer Branch Calibration for Multimodal Sentiment Analysis
title_zh: 面向多模态情感分析的预测层分支校准方法
authors:
- Yulin Sun
- Kele Xu
- Yong Dou
affiliations:
- National University of Defense Technology
arxiv_id: '2609.37100'
url: https://arxiv.org/abs/2609.37100
pdf_url: https://arxiv.org/pdf/2609.37100
published: '2026-09-29'
collected: '2026-10-04'
category: Multimodal
direction: 多模态情感分析 · 预测层校准
tags:
- Multimodal Sentiment Analysis
- Contrastive Learning
- Fusion Token
- Prediction Layer Calibration
- Multimodal Fusion
one_liner: 提出BC-MLF多模态融合框架，无需修改融合主干即可通过预测层分支校准提升情感分析性能
practical_value: '- 多模态用户反馈（评论文本+视频/语音评价）情感识别场景，可直接复用BCHead轻量分支融合逻辑，无需改动原有LLM融合主干就能快速提效

  - 多源信号（用户行为+内容+上下文）融合的推荐排序头设计，可借鉴样本自适应加权分支聚合思路，替换静态加权方案

  - 连续属性（用户满意度、购买意愿）预测的表征正则场景，可复用FTCL按连续标签亲和度构造对比学习样本的trick'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有基于LLM的多模态融合方法普遍对预测层的分支分配做隐式处理，未充分挖掘不同模态分支在不同样本上的适配性，性能天花板受限。

### 方法关键点
1. 提出BC-MLF框架，无需改动融合主干，新增BCHead显式建模预测层分支分配，通过轻量样本自适应约束融合方案，结合融合token、文本、音视频三路预测结果输出最终值；
2. 配套FTCL策略，按连续情感亲和度组织均值池化后的融合token表征做正则，强化情感感知能力。

### 关键结果
在CMU-MOSEI、CH-SIMS两个公开多模态情感数据集上，分类、回归全指标优于对比方法，相比复现的DeepMLF基线实现一致提升；ablation验证样本自适应预测层分支分配效果稳定优于静态分支聚合。
