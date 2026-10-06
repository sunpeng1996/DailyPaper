---
title: 'Towards Looped Models Done Right, Part II: Rethinking at Fixed Points'
title_zh: 循环大语言模型优化（下篇）：基于固定点的全链路降本方案
authors:
- Benhao Huang
- Chufan Shi
- Junlin Chen
- Shicheng Wen
- Zhengzhong Liu
- Eric Xing
- Xuezhe Ma
affiliations:
- Institute of Foundation Models
- University of Southern California (USC)
- Carnegie Mellon University (CMU)
arxiv_id: '2610.06833'
url: https://arxiv.org/abs/2610.06833
pdf_url: https://arxiv.org/pdf/2610.06833
published: '2026-10-04'
collected: '2026-10-06'
category: LLM
direction: 循环LLM · 训练推理效率优化
tags:
- Looped-LLM
- KV-cache
- Training-Efficiency
- Inference-Optimization
- Fixed-Point
one_liner: 通过优化深度先验与输入注入，利用循环模型固定点特性实现训练推理微调全链路降本提速
practical_value: '- 电商/推荐场景的LLM服务（导购Agent、文案生成、生成式推荐）可复用终端KV cache，3倍缩小KV缓存容量，下游平均精度损失小于0.4个点，大幅提升单卡并发能力

  - 实时query理解、生成式推荐的prompt Prefill阶段，可蒸馏固定点得到轻量学生模型，8K prompt下Prefill速度最高提升1.79倍，下游指标仅掉1.0-4.5个点，满足低延迟要求

  - 做Agent RL对齐（如导购Agent策略优化）时，复用rollout的固定点状态计算梯度，速度提升2倍，GSM8K精度损失小于1.6个点，大幅降低大模型微调成本

  - 自研小参数量循环LLM做垂类推荐任务时，可复用正交输入注入+带熵正则的可学习深度先验trick，同等参数量下提升下游效果，同时支持低内存部署'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
循环大语言模型通过复用共享层扩展逻辑深度，但每轮循环都会额外增加训练内存、解码KV缓存、Prefill计算、RL微调重放的开销，现有训练方案要么固定循环深度破坏终端KV共享能力，要么固定宽分布深度先验稀释监督信号，输入注入策略不稳定，无法充分利用固定点收敛后的路径无关特性降本。
### 方法关键点
- 基于固定点路径无关特性提出4类效率优化：训练阶段截断反向传播仅回传最后b步，解码阶段仅保留每个token的终端KV缓存，Prefill阶段蒸馏固定点得到轻量学生模型直接输出终端状态，RL微调阶段复用rollout的终端固定点状态计算梯度，无需重放全循环轨迹
- 优化固定点塑造策略：采用带熵正则的可学习深度先验，平衡目标深度预测精度与KV共享兼容性；提出正交输入注入，消除携带状态对输入的抵消/放大效应，保证每轮循环输入强度一致
### 关键结果
在100M/400M/1.6B参数量循环Llama模型上验证，对比固定深度训练、Huginn固定PLN先验、Parcae注入等baseline：
1. 1.6B模型用可学习深度先验+终端KV共享，KV缓存缩小3倍的情况下，与固定深度训练全缓存的下游平均效果持平
2. 蒸馏Prefill学生模型在8K prompt下速度最高提升1.79倍，下游平均指标仅下降1.0-4.5个点
3. RL微调时复用固定点状态，梯度计算速度提升2倍，GSM8K pass@1损失小于1.6个点
4. 正交输入注入相比Parcae基线，验证集困惑度降低0.3-1.4%，下游效果全面领先
### 核心结论
循环大模型的固定点特性可实现训练、推理、微调全链路低损降本，核心是训练阶段主动塑造兼容固定点复用的模型行为。
