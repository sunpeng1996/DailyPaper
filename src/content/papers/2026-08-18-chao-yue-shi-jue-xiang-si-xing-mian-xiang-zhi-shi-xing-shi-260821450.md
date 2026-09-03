---
title: 'Beyond Visual Similarity: Entity-Aligned Retrieval for Knowledge-Based Visual
  Question Answering'
title_zh: 超越视觉相似性：面向知识型视觉问答的实体对齐检索
authors:
- Hangrui Xu
- Zhengxian Wu
- Yunyao Yu
- Zhuohong Chen
- Rui Cong
- Xiangwen Deng
- Zhifang Liu
- Peng Jiao
- Haoqian Wang
affiliations:
- Tsinghua University Shenzhen International Graduate School
- University of Arizona
arxiv_id: '2608.21450'
url: https://arxiv.org/abs/2608.21450
pdf_url: https://arxiv.org/pdf/2608.21450
published: '2026-08-18'
collected: '2026-09-03'
category: Multimodal
direction: 多模态检索 · 实体对齐优化
tags:
- MLLM
- KB-VQA
- Entity Alignment
- Retrieval
- Semantic Distillation
one_liner: 提出首个面向KB-VQA的MLLM嵌入检索器KBMR，解决CLIP类检索实体语义对齐不足问题
practical_value: '- 电商多模态商品检索场景可复用MLLM语义嵌入思路，替代纯CLIP特征，解决同商品多外观、异商品同外观的检索错配问题

  - 大规模检索场景的监督信号优化可参考MLLM语义判别器生成连续权重的方式，用软监督替代刚性二元标签，降低标注噪声影响

  - 跨模态RAG系统召回模块可借鉴连续语义蒸馏+难负样本采样的训练范式，提升召回准确率'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
KB-VQA依赖外部信息检索回答长尾实体相关问题，现有CLIP类双编码器优先匹配表层视觉相似性，缺乏实体级语义对齐，易在同概念视觉差异大、不同实体视觉相似场景失效，且Wikipedia规模检索存在监督噪声问题。
### 方法关键点
1. 提出首个面向KB-VQA的MLLM嵌入检索器KBMR，利用MLLM自回归能力将图像映射到更能保留概念身份的语义空间；
2. 引入MLLM语义判别器生成连续实体一致性权重，基于此设计连续语义蒸馏目标，实现难负样本采样，用软监督替代刚性二元标签降低噪声影响。
### 关键结果
相比CLIP基线，检索Recall@1最高提升14.7%，端到端VQA准确率提升9.4%
