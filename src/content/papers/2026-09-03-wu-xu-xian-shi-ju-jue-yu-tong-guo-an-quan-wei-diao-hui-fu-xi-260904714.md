---
title: 'Refuse without Refusal: A Structural Analysis of Safety-Tuning Responses for
  Reducing False Refusals in Language Models'
title_zh: 无需显式拒绝语：通过安全微调回复结构分析降低大模型误拒率
authors:
- Minji Kim
- Hyounghun Kim
affiliations:
- POSTECH人工智能研究生院
- POSTECH计算机科学与工程系
arxiv_id: '2609.04714'
url: https://arxiv.org/abs/2609.04714
pdf_url: https://arxiv.org/pdf/2609.04714
published: '2026-09-03'
collected: '2026-09-08'
category: LLM
direction: LLM安全对齐 · 误拒率优化
tags:
- LLM-alignment
- false-refusal
- safety-tuning
- QLoRA
- ICL
one_liner: 拆分安全微调回复为拒绝模板与解释理由，仅用理由训练可大幅降误拒且不损失安全性能
practical_value: '- 面向C端的电商导购/客服Agent做安全微调时，去掉固定拒绝模板、仅用请求相关的解释理由训练，可降低30%+的正常用户请求误拒率，几乎不损失安全合规性

  - 安全微调数据集建议使用请求特定的理由，替换泛化表述（如不说“这类请求违法”，直接说“伪造货币违法”），可进一步提升10%左右的语义区分准确率

  - 不想做全量微调的场景，可直接在ICL示例中去掉拒绝模板、仅保留理由，同等安全水平下误拒率降低20%+，无额外推理开销

  - 现有推理时安全缓解方法可和Rationale-Only训练兼容，二者结合可进一步降低误拒率，无需重构现有安全策略'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM经安全微调后普遍存在误拒问题：对包含敏感词汇但语义完全无害的用户请求（如“哪里能拍好照片”含“拍”被误判为暴力相关请求）错误拒绝，现有解决方案多为推理时干预，开销高且未从训练数据根源解决问题，严重影响C端用户体验与模型可用性。

### 方法关键点
- 将安全微调数据的回复拆分为两个独立组件：固定格式的 boilerplate 拒绝模板（如“抱歉我无法提供相关帮助”）、解释拒绝原因的 rationale
- 构造多组对比训练集：仅含拒绝模板、仅含理由、同时包含模板+理由，额外拆分理由为泛化表述、请求特定表述两类变体
- 分别在全量微调、ICL 两种场景下测试效果，同时验证与现有推理时安全缓解方法的兼容性

### 关键实验
- 测试模型覆盖 Llama-3.1-8B、Mistral-7B-v0.3 等主流开源模型，采用 QLoRA 微调，训练数据为 Alpaca 通用指令集 + Safety-Tuned LLaMAs 安全数据集
- 有害请求测试集采用 AdvBench、MaliciousInstruct，误拒测试集采用 XSTest-Safe、OKTest
- 核心结果：仅用理由训练的模型，相比基线（模板+理由），伪有害请求合规率提升21~24pct，有害请求合规率仅提升0~4pct，几乎不损失安全性能；使用请求特定理由的模型，伪有害合规率进一步提升9~10pct；ICL 场景下仅用理由示例的模型，伪有害合规率提升22~24pct，和现有推理时缓解方法结合后优势依然保留

### 核心结论
安全微调中的固定拒绝模板会引导模型依赖表层词汇特征而非语义判断，去掉模板仅用请求相关的理由训练，是平衡安全与可用性的低成本高效方案
