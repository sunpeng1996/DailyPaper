---
title: Cross-Prompt Reuse of Entity-Replacement Responses
title_zh: 跨提示的实体替换响应可迁移性量化与复用方法研究
authors:
- Jinkun Chen
- Xuemin Yu
- Sijia Han
- Vlado Keselj
affiliations:
- Dalhousie University
- Meta
arxiv_id: '2611.00352'
url: https://arxiv.org/abs/2611.00352
pdf_url: https://arxiv.org/pdf/2611.00352
published: '2026-10-29'
collected: '2026-11-05'
category: LLM
direction: LLM推理干预 · 跨提示激活复用
tags:
- Activation_Steering
- Entity_Representation
- Cross_Prompt_Transfer
- Inference_Intervention
- Factual_Recall
one_liner: 量化固定权重下LLM跨提示实体替换响应的可迁移性，验证隐藏态复用的效果优势
practical_value: '- 电商导购Agent多轮对话中，可复用已提取的用户提及实体的50%层深隐藏态特征，无需每次重新编码，降低推理延迟同时保证实体信息不丢失

  - 生成式推荐的物品属性生成场景，可采用span对齐方式迁移同一物品不同属性的查询结果，比单向量steering效果提升更显著

  - RAG事实问答场景优化时，优先保留BOS token可大幅提升跨查询实体信息复用准确率，Gemma系列模型提升幅度可达36%以上

  - 做多query实体一致性校验时，可通过注入实体替换隐藏态的方法，快速校准不同query对同一实体的回答偏差，降低实体混淆错误'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现有跨提示实体表示迁移、激活 steering 研究多以回答正确性为核心评估指标，无法量化实体替换产生的响应在不同查询间的实际迁移比例，也无法区分迁移的是实体通用信息还是查询关系专属信息，难以指导工程落地。
## 方法关键点
- 定义实体替换响应为实体替换前后的隐藏态/输出得分差，拆分为不同关系查询共享的通用分量、每个查询专属的关系选择性分量
- 对比两种复用路线：隐藏复用（在50%层深注入源查询对齐后的隐藏态变化，走目标查询剩余层计算）、直接复用（直接叠加源查询的输出得分变化）
- 采用后缀插值、span对齐两种token对齐方式，以无变化预测、异实体替换响应为baseline，核心指标为no-change error移除比例
## 关键结果
- 实验基于ZsRE构建3个共99组实体-关系测试块，覆盖6款0.5B-9B主流开源Instruct模型
- 跨关系源查询的隐藏复用可移除Qwen 0.5B、Llama 1B 45%/49%的no-change error，Gemma恢复BOS token后移除比例达58-68%
- span对齐的隐藏复用效果优于90种调优后的单向量steering方案，在5/6测试模型上效果显著

> 最值得记住：实体替换响应的跨提示迁移收益主要来自实体通用信息，关系专属信息仅在大模型+ BOS/chat格式下可稳定复现，隐藏态复用效果远优于直接复用输出得分
