---
title: 'BamiBERT: A New BERT-based Language Model for Vietnamese'
title_zh: 面向越南语的新型BERT类预训练语言模型BamiBERT
authors:
- Dat Quoc Nguyen
- Thinh Pham
- Chi Tran
- Linh The Nguyen
affiliations:
- Qualcomm AI Research
- Virginia Tech
- Movian AI
arxiv_id: '2607.02259'
url: https://arxiv.org/abs/2607.02259
pdf_url: https://arxiv.org/pdf/2607.02259
published: '2026-07-02'
collected: '2026-07-04'
category: LLM
direction: 多语言预训练 · 小语种BERT优化
tags:
- BERT
- Pre-trained LM
- Vietnamese NLP
- Context Extension
- Low-latency Deployment
one_liner: 针对越南语优化的base尺寸BERT模型，无需分词、支持2048上下文，性能达新SOTA
practical_value: '- 针对越南市场的电商/广告/推荐业务，可直接替换现有PhoBERT作为文本Encoder，省去前置分词步骤，支持更长的商品描述、用户评论理解，提升分类、语义召回精度

  - 小语种轻量Encoder优化思路可复用：无需前置分词、扩展上下文窗口的训练方案，可迁移到其他东南亚小语种的预训练BERT迭代中

  - 低延迟/边缘端部署场景下，可作为LLM+RAG系统的轻量召回、粗排组件，相较大模型大幅降低计算成本，适配小语种本地化业务需求'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
当前越南语主流预训练Encoder PhoBERT存在上下文长度短、依赖外部分词的缺陷，缺乏高性能base尺寸的轻量模型，无法适配长文本理解、低延迟业务场景需求。
### 方法关键点
基于129GB通用域越南语文本从头预训练20轮，原生支持最长2048 tokens上下文输入，无需依赖外部分词组件处理原始文本，参数规模为base级。
### 关键结果
在8个越南语NLP基准任务的15项指标中，11项取得最优成绩、3项取得次优，成为base尺寸越南语Encoder的新SOTA，跨域泛化能力优异，模型已开源至Hugging Face。
