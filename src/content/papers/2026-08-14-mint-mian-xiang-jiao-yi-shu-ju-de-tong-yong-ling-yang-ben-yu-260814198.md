---
title: 'MINT: A Universal Zero-Shot Predictor for Transaction Data'
title_zh: MINT：面向交易数据的通用零样本预测框架
authors:
- Parameswaran Kamalaruban
- Viktor Drobnyi
- Maeve Madigan
- Julia Rozanova
- David Sutton
- Stuart Burrell
affiliations:
- Visa Inc. Risk and Security AI Lab
arxiv_id: '2608.14198'
url: https://arxiv.org/abs/2608.14198
pdf_url: https://arxiv.org/pdf/2608.14198
published: '2026-08-14'
collected: '2026-08-17'
category: RecSys
direction: 多模态LLM 交易行为零样本预测
tags:
- Zero-Shot Prediction
- Transaction Modeling
- Multimodal LLM
- LoRA
- Embedding Injection
- Behavior Sequence
one_liner: 将预训练交易编码器与LLM通过轻量嵌入注入结合，实现交易数据高效零样本预测
practical_value: '- 可复用「预训练行为序列编码器+轻量MLP连接器+LoRA微调LLM」架构，将用户浏览/下单/加购等行为的预训练嵌入直接注入LLM，替代文本序列化，降低token消耗与推理延迟

  - 训练流程可参考两阶段设计：先通过行为序列caption数据训练连接器完成模态对齐，再混合caption、QA、CoT数据做指令微调，少量标注即可实现零样本行为预测

  - 可根据业务任务做针对性优化：预测类任务用编码器最后层嵌入、短历史长度；抽取类任务用倒数第二层嵌入、更长历史；OOD场景优先选LoRA rank=32、连接器隐藏层=512提升泛化性

  - 业务涉及行为序列问答（如用户消费预测、权益推荐理由生成）时，优先选择1B-2B量级小LLM，平衡推理成本与泛化性能'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有交易序列大模型方案多将交易文本序列化，token开销大、长序列推理效率低，无法充分利用预训练行为编码器的结构化信号；同时依赖任务专属架构，零样本泛化能力差，难以灵活适配风控、个性化推荐、用户行为分析等跨任务需求。

### 方法关键点
- 架构采用三模块冻结设计：预训练交易序列编码器（冻结，产出每笔交易嵌入）+ 轻量MLP连接器（将交易嵌入映射到LLM隐藏空间）+ decoder-only LLM（仅用LoRA微调，主干权重冻结）
- 采用嵌入注入方式：用<emb>占位符替换交易嵌入，无需序列化文本，大幅降低输入token数
- 训练分两阶段：第一阶段用交易caption数据做模态对齐，仅更新连接器；第二阶段混合caption、QA、带CoT rationale的QA数据做指令微调，同时更新连接器和LoRA参数

### 关键结果
基于Visa大规模匿名交易数据集训练，对比文本序列化LLM SFT、任务专属分类器等baseline：预测QA任务ID准确率83.0%、OOD准确率80.5%，比最优序列化基线分别高1.9pct、5.5pct；推理效率方面，比序列化LLM SFT（h=1）TTFT降低46%，解码吞吐量提升143%，VRAM占用降低15%，输入token减少60%；消融实验证实加入CoT数据可显著提升跨任务性能，小LoRA rank、中等连接器层更适配OOD场景。

**最值得记住的一句话：** 交易行为嵌入比文本序列化更适合预测类推理任务，而序列化更适合抽取类任务，二者可根据业务场景互补使用。
