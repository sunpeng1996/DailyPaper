---
title: 'LLaDA-UI: Bringing Block-wise Diffusion to Vision-Language GUI Agents'
title_zh: LLaDA-UI：将分块扩散引入视觉语言GUI智能体
authors:
- Zhangxuan Gu
- Haoxing Chen
- Qi Qin
- Yi Xin
- Kai Gan
- Lin Liu
- Long Cui
- Xiaomei Wang
- Beitong Zhou
- Yunzhu Zhang
affiliations:
- Inclusion AI AGI Research Center
- Venus Team
- Westlake University
arxiv_id: '2609.13287'
url: https://arxiv.org/abs/2609.13287
pdf_url: https://arxiv.org/pdf/2609.13287
published: '2026-09-08'
collected: '2026-09-15'
category: Agent
direction: 多模态GUI Agent · 分块扩散建模
tags:
- Diffusion LLM
- MoE
- GUI Agent
- Vision-Language Model
- Block-wise Decoding
one_liner: 首个16.7B MoE分块扩散多模态GUI Agent，6个公开基准中4个超越同规模自回归Qwen3-VL-8B
practical_value: '- 做电商端内自动化操作Agent（如自动上架商品、客服工单自动执行、竞品页面自动爬取解析）可直接复用两阶段训练框架：先完成视觉编码器与扩散LLM的跨模态对齐预训练，再用业务场景GUI轨迹数据SFT，落地效率更高

  - 低延迟要求的实时多模态交互场景（如直播实时交互、端内操作实时引导）可借鉴分块扩散并行解码方案，无缓存场景下比同规模自回归VLM延迟降低70%以上，满足实时性要求

  - 结构化输出范式可复用：统一<think>推理+<action>结构化输出的格式设计，能保证98%+的动作可解析率，大幅降低业务侧动作执行的错误率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态GUI Agent普遍依赖自回归VLM顺序生成范式，推理延迟高、长序列生成效率低，难以满足实时GUI交互的低 latency 要求；扩散大语言模型（dLLM）的块并行生成特性天然适配低延迟场景，但此前未有成熟的多模态GUI Agent落地方案。

### 方法关键点
- 架构：16.7B MoE结构，包含三部分：原生分辨率ViT视觉编码器（SigLIP初始化，2D RoPE捕捉空间关系）、LLaDA2.0-mini-base分块扩散语言骨干、视觉-文本投影层（相邻4个视觉特征分组拼接后经2层MLP投影，大幅降低计算量）
- 训练流程：两阶段训练，第一阶段三阶段多模态预训练：S0对齐视觉编码器与LLM（仅训练投影层，5B token）→S1感知增强（全参数训练，70B token，引入OCR、grounding、图文交错数据）→S2多任务预训练（全参数训练，70B token，引入VQA、多模态推理数据）；第二阶段GUI Agent SFT，覆盖170+中英文APP、桌面、Web场景共6M+轨迹数据，全参数微调3轮

### 关键结果
- 6个公开GUI基准测试中，全面超越Qwen2.5-VL-7B，4个基准超越同规模自回归Qwen3-VL-8B，WebVoyager准确率56.9%，MobileWorld准确率25.6%
- 无缓存推理延迟比Qwen3-VL-8B快3.5~9倍，不同场景中位数加速3.4~8.8倍
- 动作解析率98.65%，输出坐标100%落在有效区间

**最值得记住的结论：分块扩散生成范式完全可以替代自回归范式落地低延迟多模态交互Agent，在性能不落后的前提下延迟优势极其显著**
