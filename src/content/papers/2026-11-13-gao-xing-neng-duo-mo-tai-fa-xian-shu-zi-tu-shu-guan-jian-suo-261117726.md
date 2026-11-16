---
title: 'Towards High-Performance Multimodal Discovery: Evaluating Retrieval Efficacy
  and Operational Scalability in Digital Libraries'
title_zh: 高性能多模态发现：数字图书馆检索效果与可扩展性评估
authors:
- Krishna Priya
- Sai Navya Jyesta
- Sachith Withana
- Neelesh Karthikeyan
- Beth Plale
affiliations:
- Indiana University Bloomington
- University of Oregon
arxiv_id: '2611.17726'
url: https://arxiv.org/abs/2611.17726
pdf_url: https://arxiv.org/pdf/2611.17726
published: '2026-11-13'
collected: '2026-11-16'
category: Multimodal
direction: 多模态检索 · 效果与可扩展性评估
tags:
- Multimodal Retrieval
- Vector Database
- VLM
- Embedding
- Scalability
one_liner: 评估百万级多模态馆藏的检索精度与架构扩展性，给出生产级多模态检索部署优化路径
practical_value: '- 电商商品多模态检索场景可复用「整页/商品图直接生成embedding+融合图文语义」思路，规避OCR错误遗漏卖点图、参数表信息的问题

  - 生产级大规模多模态检索系统可参考结论，将Vector Database优化作为核心投入方向，实现检索耗时随规模增长的亚线性扩展性

  - 版权敏感的多模态内容检索场景，可直接采用原始图像生成embedding的方案，规避OCR文本二次分发的版权风险'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
百万级规模数字馆藏依赖传统倒排索引实现文本检索，完全无法识别页面内图表、版式等视觉语义信息，多模态内容检索精度极低；且OCR提取文本存在版权侵权、内容遗漏（如手写标注、特殊格式图表）等问题，难以满足生产级检索需求。
### 方法关键点
1. 采用VLM直接对整页图像生成多模态embedding，同时捕捉页面内文本、图像、版式的全局语义，无需OCR提取文本，规避版权风险；
2. 从语义检索精度、架构可扩展性两个维度，完整验证大规模多模态检索方案的落地可行性。
### 关键结果
图文特征融合的多模态检索在图表密集领域的相关内容发现效果显著优于纯文本检索；系统检索耗时随数据规模增长呈亚线性扩展；优化Vector Database配置是将VLM embedding方案落地为百万级规模生产检索系统的核心影响因素。
