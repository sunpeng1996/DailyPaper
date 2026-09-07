---
title: 'Distill Globally, Adapt Locally: Reasoning Distillation and Product-Type Test-Time
  Training for Scalable Trade-Up Recommendation'
title_zh: 全局蒸馏+本地适配：面向可扩展升级推荐的推理蒸馏与品类级测试时训练
authors:
- Siliang Liu
- Mohammad Ghasemi
- Sapan Patel
- Amin Banitalebi-Dehkordi
affiliations:
- Amazon
arxiv_id: '2609.05363'
url: https://arxiv.org/abs/2609.05363
pdf_url: https://arxiv.org/pdf/2609.05363
published: '2026-09-04'
collected: '2026-09-07'
category: RecSys
direction: 电商升级推荐 · LLM知识蒸馏
tags:
- Knowledge-Distillation
- Test-Time-Training
- LoRA
- E-commerce-Recommendation
- LLM4Rec
one_liner: 将LLM推理知识蒸馏至轻量化分类器，结合品类级测试时训练实现低成本高可用的电商升级推荐
practical_value: '- 做LLM赋能大规模推荐时，可复用「离线蒸馏LLM知识到轻量化判别模型+在线仅用预计算embedding推理」的架构，彻底规避线上LLM调用的成本和延迟问题

  - 知识蒸馏时除标签外可引入LLM生成的rationale embedding作为辅助监督，搭配对齐+对比损失优化表征，注意保留细粒度标签空间（如本文4分类而非2分类）才能最大化rationale增益

  - 品类规则差异大的推荐场景（如美妆/家居/家电的升级判断标准完全不同），可复用PT-TTT思路：全局模型冻结，仅用少量品类标注样本训练LoRA适配器，成本低还能提2个点左右AUC

  - 大规模商品对关系建模（替代/互补/升级）场景，可直接复用本文的embedding对分类器架构，仅输入预计算的商品embedding就能完成分类，适配亿级对的批量计算'
score: 10
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
电商升级款（Trade-up）推荐需要识别保留用户购买意图、同时在品质/配方/品牌等维度有升级的替代商品，LLM虽能理解商品属性的细微差异，但直接在亿级商品对规模调用LLM推理成本超百万、延迟达数周，完全无法落地。
### 方法关键点
- Level1 全局推理蒸馏：用RAG增强的LLM教师生成商品对4类关系标签+自然语言推理理由，将理由编码为固定维度embedding，通过「任务损失+理由对齐损失+对比蒸馏损失」训练仅输入预计算768维商品embedding的轻量化判别学生模型，推理时无需任何LLM调用或文本生成。
- Level2 品类级测试时训练（PT-TTT）：针对不同品类升级规则差异大的问题，每个品类仅用少量专家标注样本，在冻结的全局学生模型上训练极小的LoRA适配器，适配成本仅和品类数挂钩，而非商品对数量。
### 关键结果
基于8352条人工标注金标测试集评估：15.5M参数的4分类推理蒸馏学生AUC达0.924，较仅用标签训练的同架构模型提升0.012；加PT-TTT后AUC进一步提升至0.941，平均精度达0.940；10万对商品推理比直接调用LLM快5000倍、成本低10000倍。
**最值得记住的结论**：面向大规模推荐场景的LLM赋能，核心是把LLM的语义能力转移到离线的轻量化模型中，线上完全规避生成式推理开销，才能兼顾效果、成本和可扩展性。
