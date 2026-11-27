---
title: 'MSRGF: Multi-Source Reconstruction with Reference-Guided Fusion for Incomplete
  Multimodal Sentiment Analysis'
title_zh: 面向不完备多模态情感分析的多源重建参考引导融合框架MSRGF
authors:
- Yan Zhuang
- Minhao Liu
- Yanru Zhang
- Li Ma
- Weilong Chen
- Xingyu Wu
- Jiawen Deng
- Fuji Ren
affiliations:
- University of Electronic Science and Technology of China
- The Hong Kong Polytechnic University
arxiv_id: '2611.32860'
url: https://arxiv.org/abs/2611.32860
pdf_url: https://arxiv.org/pdf/2611.32860
published: '2026-11-24'
collected: '2026-11-27'
category: Multimodal
direction: 多模态情感分析 · 模态缺失补全
tags:
- Multimodal Sentiment Analysis
- Missing Modality
- Feature Reconstruction
- Feature Fusion
one_liner: 提出MSRGF框架，通过多源重建与参考引导融合优化不完备多模态情感分析性能
practical_value: '- 多模态商品评论/内容情感分析场景下，若音频/图像/文本模态存在缺失，可复用SWR模块用已有模态生成缺失模态的多版本估计，提升特征完整性

  - 多源特征融合场景可借鉴RGF加权参考+差异修正的思路，替代直接拼接/平均融合，充分利用不同来源特征的关联信息提升效果

  - 用户行为/画像多源特征补全场景可复用共享生成器+模态专属Query的设计，降低多模态补全的模型参数量'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
多模态情感分析(MSA)场景常存在模态观测缺失问题，现有重建方法对同一缺失模态的多源估计直接融合，未充分利用不同估计间的关联关系，效果受限。
### 方法关键点
MSRGF框架包含三大模块：1) Source-Wise Reconstruction(SWR)：用模态专属Query+共享生成器，从每个可用模态单独生成各模态的估计值；2) Reference-Guided Fusion(RGF)：基于多源估计与观测值的关联构建加权参考，用差异信息选择性修正，同时保留已有观测特征；3) Global Context Modulation(GCM)：引入全局上下文调整各模态摘要用于最终情感预测。
### 关键结果
在MOSEI数据集上，随机模态内缺失场景准确率提升1.9%，随机整模态缺失提升0.6%，固定整模态缺失提升1.3%，全面优于现有方案。
