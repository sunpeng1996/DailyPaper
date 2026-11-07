---
title: Polarity Classification with Multitask Learning Syntax Augmentation
title_zh: 基于多任务学习句法增强的情感极性分类方法
authors:
- Muhammad Imran
- Carlos Gómez-Rodríguez
affiliations:
- Universidade da Coruña
- CITIC
arxiv_id: '2611.08323'
url: https://arxiv.org/abs/2611.08323
pdf_url: https://arxiv.org/pdf/2611.08323
published: '2026-11-05'
collected: '2026-11-07'
category: Training
direction: 多任务学习 · 情感极性分类
tags:
- Multitask Learning
- Sentiment Analysis
- Syntax Augmentation
- Sequence Labeling
- Contrastive Learning
one_liner: 提出两种多任务句法增强的情感极性分类方案，验证隐式句法监督的性能与效率优势
practical_value: '- 电商评论、用户反馈的情感极性分类场景可直接复用Contrastive-MTL方案，训练期注入句法知识，推理无额外解析开销，适配线上高吞吐需求

  - 处理搜索query、商品描述、UGC内容等文本语义任务时，可借鉴隐式多任务监督思路，避免推理链路引入额外NLP模块降低时延

  - 跨境多语言电商的情感分析场景可直接迁移该方案，覆盖7种主流语言，降低跨语言标注与模型开发成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
传统情感分析引入句法解析解决否定、强度词等语义误判问题，但推理阶段依赖外部解析器，计算开销高，手工构造的组合规则泛化性差。

### 方法关键点
提出两种多任务学习句法增强方案：
1. Standard-MTL：共享编码器搭配双任务头，联合训练序列标注形式的依存句法解析、极性分类任务
2. Contrastive-MTL：通过对比辅助目标+句法偏置注意力池化实现隐式句法引导，无需显式预测句法标签
两种方案仅训练阶段用到句法标注，推理无需外部解析模块或手工规则。

### 关键结果
在7种语言的11个数据集上，Contrastive-MTL在10个数据集上优于无句法基线，在所有6个适用数据集上性能超过推理时解析的SELSP流水线，推理速度提升1.5~9倍
