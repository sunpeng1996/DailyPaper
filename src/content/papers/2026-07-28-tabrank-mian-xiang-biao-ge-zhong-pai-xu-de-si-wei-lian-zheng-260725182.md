---
title: 'TabRank: Chain-of-Thought Distillation for Table Re-Rankers'
title_zh: TabRank：面向表格重排序的思维链蒸馏框架
authors:
- Adarsh Singh
- Kushal Raj Bhandari
- Jianxi Gao
- Soham Dan
- Vivek Gupta
affiliations:
- Arizona State University
- Rensselaer Polytechnic Institute
- Scale AI
arxiv_id: '2607.25182'
url: https://arxiv.org/abs/2607.25182
pdf_url: https://arxiv.org/pdf/2607.25182
published: '2026-07-28'
collected: '2026-07-29'
category: RecSys
direction: 检索重排 · CoT蒸馏 结构化数据检索
tags:
- Reranking
- Chain-of-Thought
- Distillation
- Table Retrieval
- LoRA
one_liner: 提出条件式思维链蒸馏的表格重排框架，兼顾跨域泛化与低推理成本
practical_value: '- 做LLM-based生成式重排时，可直接复用CoTCond蒸馏trick：不强制学生生成教师CoT，而是将CoT作为输入上下文仅计算最终排序损失，能同时提升跨域泛化能力、降低推理延迟30%以上，适配电商多类目、跨场景重排需求

  - 结构化数据（电商商品属性表、商家资质表、运营规则表等）的检索重排，可基于单场景标注数据用该范式训练，无需修改架构即可泛化到多表、跨域场景，降低标注成本

  - 生成式重排线上服务可参考该方案优化错误率：推理蒸馏能将格式错误、重复输出等结构性故障降低90%以上，提升服务稳定性

  - 小样本重排场景可配合LoRA微调+大模型合成CoT标注的方案，无需大量人工标注即可获得明显效果收益'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统CoT蒸馏重排方法要求学生逐token复刻教师推理轨迹，域内效果尚可但跨域泛化性差，同时推理成本高；表格检索的语义不仅来自表面文本，还依赖schema、行列关系等结构特征，现有重排方法适配性差，跨场景（从通用表格到金融表格、多表格场景）效果衰减明显。

### 方法关键点
- 构建6728条DeepSeek-R1生成的表格重排推理轨迹数据集，覆盖单表格检索场景
- 对比3种蒸馏范式：Naive SFT（仅用最终排序标签训练）、CoTGen（传统CoT蒸馏，同时计算推理和排序损失）、CoTCond（条件式蒸馏，将教师CoT作为输入上下文，仅计算最终排序损失，推理无需生成CoT）
- 所有模型基于LoRA微调，训练成本低

### 关键实验
在4个跨域表格检索基准测试，对比仅在NQ-Tables上训练的Qwen3-8B baseline，CoTCond的Acc@10在HybridQA提升30.5%、SQA提升15.2%、金融域TATQA提升13.1%、TabFact提升52.9%；推理token数比CoTGen低30%左右，格式错误率下降超90%，仅用单表格数据训练即可天然支持多表格检索场景。

### 核心结论
CoT蒸馏的核心价值不是让学生复刻推理过程，而是让学生利用推理信号优化最终决策，条件式蒸馏可同时获得推理的效果收益和低推理成本的工程收益。
