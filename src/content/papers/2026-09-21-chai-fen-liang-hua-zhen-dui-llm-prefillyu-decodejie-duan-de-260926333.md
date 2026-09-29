---
title: 'Disaggregated Quantization: Specializing LLM Prefill and Decode'
title_zh: 拆分量化：针对LLM Prefill与Decode阶段的专属优化
authors:
- Andrei Panferov
- Maximilian Kleinegger
- Sweta Priyadarshi
- Tijmen Blankevoort
- Dan Alistarh
affiliations:
- NVIDIA
- ISTA
arxiv_id: '2609.26333'
url: https://arxiv.org/abs/2609.26333
pdf_url: https://arxiv.org/pdf/2609.26333
published: '2026-09-21'
collected: '2026-09-29'
category: LLM
direction: LLM推理量化 · Prefill/Decode分阶段优化
tags:
- Quantization
- LLM Inference
- Prefill
- Decode
- TTFT
one_liner: 为LLM推理的Prefill、Decode阶段设计独立量化策略，兼顾精度、速度与显存开销
practical_value: '- 自研LLM服务可优先落地格式拆分量化：Prefill阶段用NVFP4等硬件原生低精度格式加速，Decode阶段关闭激活量化提升精度，无需额外显存或训练成本，直接适配vLLM/llama.cpp等主流框架

  - 单卡部署大模型的Agent/生成式推荐场景可复用ODP方案：将Prefill专属权重存SSD分块加载，复用Decode阶段闲置显存做缓冲，长上下文下TTFT最高提升1.78×，不增加显存占用

  - 已有量化LLM部署可直接训练Prefiller适配：针对已上线的低bit GGUF解码权重，仅训练NVFP4 Prefill权重适配，1-bit解码精度最高提升32.5个点，同时加速Prefill阶段'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM推理中Prefill为计算密集型、Decode为内存密集型，传统统一量化无法同时适配两个阶段的特性，低bit量化下精度损失严重，单卡部署时显存、速度、精度三者矛盾突出。

### 方法关键点
- 提出量化感知拆分蒸馏（QADD）：通过SFT标签掩码区分Prefill/Decode路径，单次前后向传播即可联合优化两个阶段的量化策略，支持共享/独立权重、仅训练Prefill权重适配冻结的Decode checkpoint。
- 三层拆分量化体系：格式拆分（共享权重，Prefill用NVFP4等硬件原生低精度格式，Decode关闭激活量化用权重-only压缩，无额外成本）；全拆分（两个阶段用独立专属权重，分别适配最优格式）；ODP卸载方案：Prefill权重存SSD分块加载，双缓冲重叠IO与计算，无额外显存占用。
- 可插拔Prefiller：针对已上线的预量化Decode权重，仅训练NVFP4 Prefill专属权重，无需修改Decode逻辑即可提精度、加速Prefill。

### 关键实验结果
在Qwen3、Gemma3全系列验证：格式拆分量化比统一NVFP4在解码-heavy任务精度提升1.9~3.1个点，Prefill速度保持为BF16的1.49~1.67倍；全拆分量化在2bit解码下精度较统一方案提升7.4~10.7个点；ODP在Qwen3.8-27B 8K上下文下TTFT较权重-only基线提升1.78×；训练Prefiller适配1bit GGUF解码器，MMLU-Pro精度提升32.5个点、MMMU-Pro提升35.3个点，方案在2.8T参数模型上通过PTQ验证有效。

### 核心结论
Prefill与Decode阶段的量化需求天然存在差异，分阶段优化可在几乎无额外成本的前提下同时提升LLM推理的精度和速度。
