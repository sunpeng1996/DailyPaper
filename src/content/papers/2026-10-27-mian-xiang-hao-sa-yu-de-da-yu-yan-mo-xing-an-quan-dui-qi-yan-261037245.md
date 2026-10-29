---
title: 'Aligning Large Language Models for Safety in African Languages: A Case Study
  of Hausa'
title_zh: 面向豪萨语的大语言模型安全对齐研究：数据集构建与方法对比
authors:
- Valdini Douglace Lemofouet
- Blessing Ngozi Uzor
- Paula Chikaodinaka Anyanwu
- Danielle Blanche Kapsa
- Saminu Mohammad Aliyu
- Seid Muhie Yimam
- Shamsuddeen Hassan Muhammad
affiliations:
- African Institute for Mathematical Sciences (AIMS), Cameroon
- Bayero University Kano
- University of Hamburg
- Imperial College London
arxiv_id: '2610.37245'
url: https://arxiv.org/abs/2610.37245
pdf_url: https://arxiv.org/pdf/2610.37245
published: '2026-10-27'
collected: '2026-10-29'
category: LLM
direction: 低资源语言 LLM 安全对齐
tags:
- LLM Safety Alignment
- Low-resource Language
- SFT
- DPO
- LoRA
- Hausa
one_liner: 构建豪萨语安全偏好数据集HausaSafeLM，对比验证SFT与DPO在低资源语言安全对齐的trade-off
practical_value: '- 低资源语言/垂直场景的LLM对齐评估，不要仅用拒绝率单一指标，需叠加回答流畅度、有用性维度，避免把模型生成能力不足误判为安全对齐效果好

  - 对齐 pipeline 数据分配可复用结论：SFT阶段可加入大量低质量银标数据提升回答流畅度，DPO阶段仅用高质量金标数据即可，银标无增益

  - 若需平衡安全、有用性、回答流畅度三个目标，优先选择SFT+金+银标数据的配置，比叠加DPO的综合表现更优

  - 跨境电商多语种Agent对齐可参考本文的本地化数据集构建方法，先翻译通用安全数据集再做本地文化适配+人工校验'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM安全对齐研究集中在英语等高资源语言，低资源、文化差异大的场景对齐效果未知，豪萨语有超2亿使用者，但缺乏专用安全对齐数据集与方法验证，现有对齐方法的跨语言迁移性、指标可靠性都待验证。

### 方法关键点
- 构建HausaSafeLM数据集：基于PKU-SafeRLHF过滤适配豪萨本地文化的6大类危害，共1万条样本，分3千条人工校验的金标、7千条仅机器翻译的银标，支持SFT和DPO两种训练格式
- 对齐方案对比：基于Qwen2.5-7B-Instruct用LoRA微调，对比5种配置：零样本基线、仅金标SFT（SFT-G）、金+银标SFT（SFT-GS）、SFT-G后加DPO（DPO-G）、SFT-GS后加DPO（DPO-GS）
- 评估维度：用Gemini做LLM法官，评估拒绝率（RR）、误拒率（FRR）、有用率（HR）、有害问题回答质量（SafeQ）、良性问题回答质量（AyaQ）5个维度

### 关键结果
- 基线模型RR达1.0，但96.2%的拒绝回答质量为低，SafeQ仅0.021，本质是豪萨语生成能力不足而非真正对齐
- SFT-GS比SFT-G的FRR降0.16、SafeQ升0.112，银标数据对SFT增益显著；DPO阶段加银标几乎无增益，FRR稳定在0.11，比SFT低但SafeQ降至0.023-0.036，回到基线水平
- 无配置能同时满足安全、有用、流畅三个目标：DPO提升拒答精度但严重损失语言质量，SFT兼顾流畅度但误拒率更高

**最值得记住的一句话**：低资源场景下，现有对齐方法更容易迁移「什么时候拒绝」的决策边界，而非「如何流畅拒绝」的语言能力，仅用拒绝率衡量安全完全不可靠。
