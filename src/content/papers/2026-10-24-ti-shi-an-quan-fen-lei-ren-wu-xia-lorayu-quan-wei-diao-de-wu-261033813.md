---
title: 'Task Format as a Factor in Adaptation: A Controlled Comparison of LoRA and
  Full Fine-Tuning for Prompt-Safety Classification'
title_zh: 提示安全分类任务下LoRA与全微调的任务格式影响对照研究
authors:
- John Alderete
- Srirakshith Betageri
- Jennifer Flynn
- Alex Greenhalgh
- Josh Rubin
- Yoshita Varma Annam
affiliations:
- Fiddler AI
- Simon Fraser University
- Georgia Institute of Technology
arxiv_id: '2610.33813'
url: https://arxiv.org/abs/2610.33813
pdf_url: https://arxiv.org/pdf/2610.33813
published: '2026-10-24'
collected: '2026-10-27'
category: Training
direction: LLM微调 · LoRA与全微调对比
tags:
- LoRA
- Full Fine-Tuning
- Prompt Safety
- Task Format
- Fine-Tuning Comparison
one_liner: 通过受控对照实验揭示任务格式、学习率对LoRA与全微调性能差距的调控机制
practical_value: '- 做垂类分类任务（如电商违禁品识别、广告合规审核）用LoRA微调时，可在训练目标中增加标签后的短理由生成，无需修改推理逻辑即可提升2~4pp分类精度，同时降低误判率

  - LoRA微调效果对学习率的敏感度远高于全微调，不要直接使用通用默认学习率，在验证集上做小范围网格搜索最多可带来3pp+精度提升，甚至追平全微调效果

  - 小模型微调即使域内精度超过大模型prompting，分布外（如广告恶意变体query、用户异常话术）鲁棒性仍远逊于大模型，核心风控场景需优先用大模型prompting兜底'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LoRA与全微调的对比实验普遍存在变量混淆问题，极少考虑任务输出格式对性能差距的影响，无法明确两类微调方法的真实差距和适用场景，对业务侧选择微调方案缺乏可落地的参考依据。
### 方法关键点
- 选用同预训练语料、同Tokenizer、同参数量（400M）的Ettin编码器-解码器配对模型，控制架构差异带来的干扰
- 对照三类任务格式：分类头输出、单token判决生成、判决+1句理由生成，每类对比LoRA、全微调两种方案
- 严格控制变量：每类实验最多跑15个种子，两种微调方案采用相同超参搜索流程，学习率单独调优
- 覆盖域内、分布外（对抗越狱、类有害良性prompt）多维度评估
### 关键结果
- 采用默认学习率时，全微调域内平衡精度比LoRA高2~3pp；当两者学习率都经过相同流程调优后，编码器上两类微调精度差缩小到0.37pp，达到统计等价
- 为LoRA训练目标增加判决后的理由生成，可直接提升4pp域内精度，完全追平全微调性能；长度相同的无意义句子无任何增益
- 微调后的400M模型域内精度比prompted 8B大模型高1.2~7.8pp，但分布外对抗样本上落后8~23pp，良性误判率是大模型的10~33倍
### 核心结论
LoRA与全微调的性能差距远小于训练目标设计、学习率调优带来的影响，仅靠域内精度无法判断分类模型的真实鲁棒性
