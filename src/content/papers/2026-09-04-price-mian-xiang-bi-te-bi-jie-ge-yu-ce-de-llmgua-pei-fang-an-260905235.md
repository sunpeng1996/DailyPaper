---
title: 'PRICE: A Systematic Study of LLM Adaptation Choices for Bitcoin Price Forecasting'
title_zh: PRICE：面向比特币价格预测的LLM适配方案系统性研究
authors:
- Maryam Fakhari
- Mehran Safayani
affiliations:
- Isfahan University of Technology
arxiv_id: '2609.05235'
url: https://arxiv.org/abs/2609.05235
pdf_url: https://arxiv.org/pdf/2609.05235
published: '2026-09-04'
collected: '2026-09-07'
category: LLM
direction: LLM时序预测 · 适配方案优化
tags:
- LLM Adaptation
- LoRA
- Time Series Forecasting
- Prompt Engineering
- Inference Optimization
one_liner: 系统梳理LLM适配时序预测的5类关键选择，基于LLaMA-3 8B实现优于专用模型的比特币价格预测方案
practical_value: '- 电商流量/销量/价格等时序预测场景，可直接复用5项LLM适配组合：4-bit量化LLaMA+LoRA微调+整数化数值表示+CTF结构化提示+零温解码，效果优于专用时序模型

  - 数值类预测任务优先选择整数取整的数值表示方案，可稳定降低预测误差，无需额外开销

  - 多步时序预测任务采用递归多步推理+零温度解码组合，能大幅减少递归误差累积，提升输出稳定性

  - 结构化任务提示（CTF）效果优于CoT、iCoT、少样本提示，微调后仍保持优势，可迁移到各类数值任务的prompt设计'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
加密货币市场高波动、非平稳的特性对传统时序预测方法带来极大挑战，现有LLM应用于时序预测时，各类适配选择的组合效应在金融场景下尚未被系统性探索。
### 方法关键点
基于4-bit量化LLaMA-3 8B搭建PRICE框架，系统性验证微调策略、数值表示、提示方案、推理策略、解码方式5类适配选项的组合效果，集成LoRA参数高效微调、递归多步推理、整数取整数值表示、Context-Task-Format（CTF）结构化提示、零温解码5项优化。
### 关键结果
对比8个Transformer及专用时序基础模型，PRICE在验证集、测试集均取得最低预测误差，跨评估周期性能稳定性显著优于基线；仅用文本预训练的LLM效果超过专用时序基础模型；消融实验显示CTF提示效果优于CoT、iCoT、少样本提示，整数表示稳定降低预测误差，零温解码提升递归预测稳定性，LoRA可在有限硬件上完成高效训练
