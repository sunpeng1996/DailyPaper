---
title: 'Explanations that Transfer: Interpreting Medical Retrieval with Sparse AutoEncoders'
title_zh: 基于稀疏自编码器的可迁移医疗检索可解释性方法
authors:
- Diane Bouchacourt
- Gaëtan Brison
affiliations:
- Doctolib AI Research Lab, Paris, France
arxiv_id: '2611.18179'
url: https://arxiv.org/abs/2611.18179
pdf_url: https://arxiv.org/pdf/2611.18179
published: '2026-11-13'
collected: '2026-11-16'
category: RAG
direction: RAG检索模块可解释性与跨域优化
tags:
- Sparse AutoEncoder
- InfoNCE
- Information Retrieval
- Interpretability
- Cross-domain Generalization
one_liner: 将融合InfoNCE损失的稀疏自编码器用于医疗检索，产出可解释、跨域鲁棒的稀疏检索表示
practical_value: '- 垂直领域检索场景（如电商商品检索、问诊Agent知识库检索）可复用「SAE+InfoNCE损失」结构，将稠密嵌入转换为稀疏可解释表示，同时不损失检索相关性

  - 跨域迁移要求高的检索任务（如多品类电商跨类目检索）可优先采用SAE生成的稀疏编码，跨域性能掉点显著低于原稠密嵌入

  - 需满足合规要求的检索场景（如医药、金融、电商虚假宣传防控）可通过SAE激活特征反推检索匹配逻辑，快速定位结果合理性，降低合规风险'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
垂直领域检索系统依赖的稠密嵌入存在两个核心痛点：一是黑盒属性导致无法解释检索结果的匹配逻辑，难以适配合规要求高的场景；二是垂直域微调后跨新域泛化性差，性能掉点严重。
### 方法关键点
引入Sparse AutoEncoders（SAEs）处理检索嵌入，训练目标同时结合重构损失与InfoNCE对比损失，既保证嵌入重构精度，又直接保留query-文档的匹配相关性，将原稠密嵌入转换为语义可解释的稀疏表示。
### 关键结果
在3种基础嵌入模型、6个医疗检索数据集上测试：① 域内检索效果优于原始稠密嵌入；② 跨域性能掉点远低于稠密嵌入，尤其目标域与训练域差异大时优势更突出；③ 生成的稀疏特征语义可解释，解释能力可跨训练分布迁移。
