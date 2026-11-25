---
title: Can a Frontier LLM Repair a Quantized Network by Tool-Free Weight-Space Programming?
title_zh: 前沿大语言模型无需工具通过权重空间编程修复量化网络
authors:
- Steffen Urban
affiliations:
- Independent Researcher
arxiv_id: '2611.33031'
url: https://arxiv.org/abs/2611.33031
pdf_url: https://arxiv.org/pdf/2611.33031
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: LLM · 无工具权重空间编程
tags:
- LLM
- Post-training Quantization
- Weight-space Programming
- PTQ
- Int4 Quantization
one_liner: 验证Claude系列LLM无需工具仅靠推理即可大幅修复4比特量化CNN的精度损失
practical_value: '- 做LLM离线优化类任务（如小模型量化、特征规则调优）时，可采用分块输入+逐块输出的prompt设计，突破单轮输出长度限制，提升任务完成度

  - 需LLM优化现有方案时，明确告知基线方案的效果差距，而非直接让LLM从头输出结果，可大幅激发LLM的优化能力

  - 无工具LLM做数值推理任务时，输入中提前预计算中间特征（如本文的量化残差u = w/s），可降低LLM计算负担，提升输出准确率'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有后训练量化（PTQ）方法要么依赖校准数据，要么是固定数值流程，无法自主根据权重特征做灵活优化。实验探索前沿LLM能否在无工具、无数据、无法运行推理的极端条件下，仅通过读取权重文本实现量化网络的精度修复，验证LLM在数值空间的推理优化能力。

### 方法关键点
- 训练20k参数量的CIFAR-10分类小CNN，浮点精度81.42%，4比特RTN量化后精度骤降至60.39%，完整权重转文本后输入Claude系列LLM
- 设计4种实验协议：P1（整网输入单轮输出优化）、P2（分层分块输入逐块输出优化）、P3（仅输入浮点权重直接量化）、P4（输入浮点权重+BN统计量直接量化），全程禁止LLM调用任何工具
- 基准对比覆盖RTN、无数据核平衡、AdaRound、GPTQ等主流PTQ方案

### 关键结果
- P2协议下Claude Opus 5.5自主采用核平衡策略调整量化权重，4比特量化精度达77.95%，仅比浮点模型低3.5pp，比无数据核平衡的代码实现高0.15pp，仅比用1k校准数据的AdaRound低2.8pp
- P4协议下Claude Fable 5.2自主采用行级离群值裁剪策略，无需RTN基线输入即可实现4比特精度69.97%，比MSE最优尺度搜索高5.4pp
- 整网单轮输出的P1协议下，LLM仅能优化第一层卷积，精度提升3.7~4.0pp

> 最值得记住：LLM在无工具条件下的数值优化能力远超预期，明确的缺陷提示+结构化中间输入+分块输出设计，可让LLM完成原本需要专用数值算法才能实现的优化任务
