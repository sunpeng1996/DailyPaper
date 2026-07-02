---
title: 'Towards Developing a Multimodal Chat Assistant for University Stakeholders:
  RAG-based Approach'
title_zh: 面向高校利益相关方的多模态聊天助手：基于RAG的实现方案
authors:
- Md Abu Hanif Shaikh
- Abdullah Al Shafi
affiliations:
- Khulna University of Engineering & Technology
arxiv_id: '2607.01115'
url: https://arxiv.org/abs/2607.01115
pdf_url: https://arxiv.org/pdf/2607.01115
published: '2026-07-01'
collected: '2026-07-02'
category: RAG
direction: 多模态问答助手 · RAG落地实践
tags:
- RAG
- Multimodal
- Vision-Language Model
- Quantized Inference
- LLM
- Chatbot
one_liner: 基于RAG与视觉语言模型实现多模态高校问答助手，大幅降低幻觉，支持受限硬件部署
practical_value: '- 多模态RAG场景下可复用「视觉语言模型 + 语义检索 + LLM生成」架构，适配文本/图像混合输入的电商客服、商品咨询类业务场景

  - 面向低资源硬件部署时可直接套用量化推理方案，搭配FastAPI+Next.js前后端架构实现快速上线

  - 垂直领域RAG的幻觉抑制方案可直接复现，用私有知识库做检索grounding可降低70%+的幻觉率'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
高校尤其是发展中国家高校缺乏智能信息支持系统，现有规则式chatbot无法处理复杂领域查询，也难以适配动态更新的政策规则。
### 方法关键点
1. 采用RAG架构，将LLM与语义检索结合，基于高校手册等私有领域资源生成上下文相关回答；
2. 接入视觉语言模型支持文本、图像双输入，采用量化推理适配低资源硬件部署；
3. 后端基于FastAPI、前端基于Next.js搭建，保障实时可用性。
### 关键结果
1. 多模态评估显示文本、图像查询均获得较高用户满意度，仅图像输入响应时延有所上升；
2. 幻觉率从无RAG的31.7%降至6.6%，检索grounding效果显著。
