---
title: On the Opportunities and Challenges of Prefill-to-Autoregressive Cross-Model
  Transfer
title_zh: Prefill到自回归跨模型迁移的机遇、挑战与开源评估框架
authors:
- Zhenyi Shen
- Junru Lu
- Wei Liu
- Jiangnan Ye
- Jiazheng Li
- Di Yin
- Xing Sun
- Tameem Adel
- Yali Du
- Lin Gui
affiliations:
- King's College London
- Tencent Youtu Lab
- National Physical Laboratory
arxiv_id: '2611.06976'
url: https://arxiv.org/abs/2611.06976
pdf_url: https://arxiv.org/pdf/2611.06976
published: '2026-11-04'
collected: '2026-11-06'
category: LLM
direction: LLM跨模型协作 · 推理效率优化
tags:
- PACT
- Latent Communication
- LLM Inference
- PEFT
- Evaluation Protocol
one_liner: 开源轻量PACT框架PLatour，配套PACT-Check协议区分跨模型信息传递的真实增益
practical_value: '- 大小模型协作的低延迟生成方案可直接复用：大模型仅完成prompt prefill输出隐状态，小模型承接全量自回归生成，仅训练零初始化线性桥参数，兼顾大模型的理解能力和小模型的推理速度，适合电商Agent客服、定制化商品文案生成、搜索query改写等长文本场景

  - 可复用PACT-Check的四层校验逻辑验证跨模型协作的真实收益，避免将小模型侧的PEFT适配效果错当成大模型的信息传递增益，减少无效的大模型资源投入

  - 桥参数训练直接采用GRPO强化学习对齐业务奖励，无需额外的SFT蒸馏预热，训练成本低，可快速适配垂直场景的大小模型协作链路'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM推理成本与效果的矛盾是落地核心痛点，PACT（Prefill-to-Autoregressive Cross-model Transfer）通过大模型prefill、小模型生成的分工平衡效果与延迟，但现有开源框架能力不足，且无法区分性能增益来自大模型信息传递还是小模型自身适配，存在大量伪增益风险。
### 方法关键点
- 提出PLatour开源PACT框架：大小模型全量冻结，仅通过对应相对深度层的零初始化线性桥传递大模型prefill阶段的隐状态，直接用GRPO强化学习优化桥参数，无需蒸馏或对齐预热，兼容混合注意力架构。
- 提出PACT-Check评估协议：包含4个对照组（Dummy Transfer无输入相关sender信号、Irrelevant Transfer无关输入sender信号、Self-Communication小模型自身做sender、Trained Receiver小模型单独PEFT训练），通过PACT-Score量化真实来自大模型的信息传递增益。
### 关键结果
在GSM8K、MATH500、Chem-CoT、AIME、HumanEval、MBPP等数学、化学、代码生成任务上测试：
1. PLatour比开源基线C2C在GSM8K高14.3pp、MATH500高13.6pp、Chem-CoT高28.3pp；用35B sender的效果超过闭源Mostik 753B sender的结果，其中AIME高3.9pp、HumanEval高8.8pp、MBPP高7.9pp。
2. Prefill阶段的额外成本随生成长度快速摊销，长文本生成总延迟接近单独小模型。
3. 部分任务（如GSM8K）的增益可被小模型单独LoRA训练复现，PACT-Score接近0，无真实大模型信息传递收益；Chem-CoT任务PACT-Score为3.34pp，存在真实增益。
> 最值得记住的一句话：跨模型协作的性能提升不能直接等价于大模型的有效信息传递，必须通过严格对照组校验排除小模型自身适配的伪增益
