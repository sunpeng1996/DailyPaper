---
title: Jailbreak Detection on Large Language Models via Contrastive Prototype Structures
title_zh: 基于对比原型结构的大语言模型越狱攻击检测方法
authors:
- Yan Qiu
- Yuanyuan Li
affiliations:
- Technical University of Munich
- Munich Re
- Insure AI
arxiv_id: '2611.24936'
url: https://arxiv.org/abs/2611.24936
pdf_url: https://arxiv.org/pdf/2611.24936
published: '2026-11-18'
collected: '2026-11-19'
category: LLM
direction: 大语言模型安全 · 越狱攻击检测
tags:
- Jailbreak Detection
- Contrastive Learning
- Prototype Learning
- LLM Safety
- Cross-domain Robustness
one_liner: 提出无需额外下游分类器的对比原型推理越狱检测方法JDPI，跨数据集鲁棒性更优
practical_value: '- 电商Agent/LLM导购场景搭建安全围栏时，可复用JDPI的原型对比思路，无需额外训练下游分类器，减少标注数据需求量，降低部署成本

  - 多轮对话类推荐/导购场景的用户输入安全检测，可借鉴其累积历史对话特征做全局判断的策略，提升对话级恶意输入识别准确率

  - 跨业务场景的违规内容检测需求，可复用其对比微调+原型匹配的框架，相比传统分类器获得更强的跨域鲁棒性，减少适配新场景的标注成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM安全部署面临越狱攻击、有害输入的严峻挑战，传统检测方法需训练额外下游分类器，标注成本高、跨场景适配性差。
### 方法关键点
JDPI仅基于二分类安全标签完成编码器适配、有害/安全两类原型构建，通过输入表征与两类原型的相对距离直接输出检测结果，无需额外下游分类器，省去分类器训练所需的独立数据拆分，标注样本需求量更低。
### 关键结果
- 对比微调可将检测准确率提升9.1~18.0个百分点
- 相同编码器下ROC-AUC与基线差值不超过0.017，数据集适配后较Llama Guard 3-8B高0.173~0.310
- 多轮对话引入历史信息后，对话级检测准确率显著优于仅用当前轮输入
- 12组跨数据集迁移实验平均准确率比传统分类器高1.59个百分点，跨域鲁棒性更强
