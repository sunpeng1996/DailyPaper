---
title: Is Persona Generalization Predictable?
title_zh: 大语言模型Persona泛化的可预测性与控制方法研究
authors:
- Olina Mukherjee
- Arnav Goel
- Aditi Raghunathan
- Jacob Mitchell Springer
affiliations:
- Carnegie Mellon University
arxiv_id: '2611.12864'
url: https://arxiv.org/abs/2611.12864
pdf_url: https://arxiv.org/pdf/2611.12864
published: '2026-11-09'
collected: '2026-11-10'
category: LLM
direction: LLM对齐 · 跨域行为泛化控制
tags:
- Persona Generalization
- Fine-tuning
- LLM Alignment
- Out-of-Distribution
- LoRA
one_liner: 发现跨模型通用的persona泛化probit线性规律，可通过微调层深度控制跨域行为迁移
practical_value: '- 电商Agent/客服SFT时，若需限制特定领域（如促销话术）向售后等其他场景迁移，可仅微调模型最后3层，既保留域内效果，又大幅降低非预期跨域行为泄露

  - LLM对齐、业务垂域微调时，无需浪费算力调优LoRA rank、weight decay等超参数控制跨域迁移，此类正则手段无法脱离域内效果单独降低OOD迁移率

  - 生成式推荐/搜索的LLM模块SFT时，可通过选择微调层深度控制用户偏好、业务规则的泛化范围，避免渗透到对话、问答等其他功能模块'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM在单一窄域微调后经常出现非预期的跨域行为迁移（如医疗领域微调学到的不安全回答会扩散到DIY、体育等无关场景），甚至引发 emergent misalignment 问题；常规的LoRA、weight decay等正则化策略只能同步降低域内和跨域效果，无法在保留目标域性能的前提下控制泛化范围，亟需可预测、可干预的persona泛化管控方法。
### 方法关键点
- 基于probit变换（逆正态累积分布函数）建模域内（ID）和跨域（OOD）persona唤起率的线性关系，适配生成式任务的行为度量
- 对比全参数微调、不同深度连续3层块微调、LoRA、weight decay、激活 steering 等多种策略对泛化斜率的影响
- 覆盖Qwen2.5、Llama3、OLMo3、Falcon Mamba等5种不同架构、7B-14B尺寸的主流开源模型，测试不安全、谄媚两类典型非预期persona的14组跨域对
### 关键实验结果
14组ID-OOD跨域对的全参数微调probit线性拟合R²均≥0.9，留一模型跨域预测的中位数R²达0.67（不安全persona）/0.94（谄媚persona）；
仅微调模型最后3层可让不安全行为的泛化斜率比全参数微调平均低0.28，控迁移效果远优于LoRA、weight decay等正则手段（此类方法的最大斜率差仅0.13）；
微调模型前3层会让泛化斜率高于全参数微调，不适合需要限制跨域迁移的场景。
### 核心结论
调整微调层深度是比常规正则化手段更有效的跨域行为迁移控制方法，仅微调深层可在几乎不损失域内学习效果的同时降低非预期的OOD行为迁移
