---
title: 'MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights
  and Activations'
title_zh: MACaQ：面向低精度权重与激活的快速模型无关校准量化
authors:
- Lorenz K. Muller
- Philippe Bich
- Chiara Boretti
- Hyun-Min Chang
- Jiawei Zhuang
- Lukas Cavigelli
affiliations:
- Huawei Technologies Switzerland Computing Systems Lab
arxiv_id: '2611.10649'
url: https://arxiv.org/abs/2611.10649
pdf_url: https://arxiv.org/pdf/2611.10649
published: '2026-11-06'
collected: '2026-11-11'
category: LLM
direction: LLM推理优化 · 4位后训练量化
tags:
- MXFP4
- Post-training Quantization
- LLM Inference
- vLLM
- Low-bit Quantization
one_liner: 提出层独立W4A4 MXFP4量化方案，量化速度提11倍，推理开销仅2.3%
practical_value: '- 业务侧部署LLM驱动的推荐/Agent服务时，可直接复用MACaQ的W4A4量化方案，仅增加2.3%推理overhead即可实现3倍推理提速，大幅降低大模型部署成本

  - 低资源场景下量化超大规模LLM时，可借鉴其层独立量化设计，仅需32.5GB显存即可完成122B参数模型量化，无需全量加载模型到GPU

  - 量化精度优化可复用Flip-Refinement的Hessian感知坐标下降思路，基于round-to-nearest初始结果做快速贪心微调，用极低计算成本提升量化精度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
W4A4量化是降低LLM推理存储与计算成本的核心技术，但现有方案普遍存在跨层依赖，需要针对模型架构做定制适配、量化时间长、显存占用高，无法快速落地到不同模型架构。

### 方法关键点
- 采用层独立量化设计，每个线性层单独处理，在线对激活做逐通道缩放+块Hadamard变换，对应逆变换离线吸收到权重，消除跨层依赖，支持流式逐层量化
- 提出Flip-Refinement快速优化策略：基于Hessian感知的坐标下降，将FP4编码贪心调整到相邻可表示值，大幅降低量化重建误差
- 提供vLLM适配的Triton核，量化后的模型可直接部署

### 关键结果
对比MR-GPTQ、DuQuant++等SOTA量化方案，Llama-3-8B上达到同等perplexity的速度快11倍，Qwen3-32B端到端推理仅比纯MXFP4增加2.3% overhead，相比FP16提速3倍；无需架构修改即可量化FLUX扩散模型，效果优于官方NVFP4量化；单张96GB GPU仅用32.5GB显存、64分钟即可完成122B参数Qwen3.5模型量化。

**最值得记住的一句话**：接受极少量的在线变换开销，换取层独立量化的高通用性、低显存占用、极快量化速度，是工业级LLM量化的性价比极高的选择
