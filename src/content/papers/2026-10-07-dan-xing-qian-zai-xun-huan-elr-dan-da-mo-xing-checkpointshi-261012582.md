---
title: 'One Model to Loop Them All: Elastic Latent Recurrence for Language Models'
title_zh: 弹性潜在循环（ELR）：单大模型checkpoint实现推理深度弹性可调
authors:
- Faisal Ladhak
- Shantanu Acharya
- Santiago Akle Serano
- Simeng Sun
- Boris Ginsburg
- Krishna C Puvvada
affiliations:
- NVIDIA
arxiv_id: '2610.12582'
url: https://arxiv.org/abs/2610.12582
pdf_url: https://arxiv.org/pdf/2610.12582
published: '2026-10-07'
collected: '2026-10-12'
category: LLM
direction: 大模型优化 · 弹性深度推理
tags:
- Elastic Depth
- Latent Recurrence
- Looped LLM
- KV Cache
- MoE
one_liner: 消除单循环精度损失，单大模型checkpoint可通过调整循环次数动态平衡推理精度与算力
practical_value: '- 业务侧部署小参数LLM做Agent意图识别、商品文案生成、query改写等场景时，可复用ELR弹性深度设计，单checkpoint按流量峰谷调整循环次数，高峰开1循环降延迟、低峰开多循环提精度，无需部署多套模型

  - 训练MoE结构的LLM4Rec模型时，可复用跨循环路由重放技巧，复用首循环专家路由结果，可降低11.7%训练耗时且无精度损失，减少大模型推荐的训练成本

  - 长序列推理场景（如用户长期行为建模、长query理解）可复用last-loop KV cache优化，多循环推理时仅保留最后一轮KV cache，KV内存占用和单循环持平，降低长序列推理的内存开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有循环大模型存在「单循环精度税」，循环次数为1时精度远低于同参数非循环模型，导致低延迟场景需单独部署非循环模型，无法实现单checkpoint动态平衡精度与算力的弹性能力，难以适配业务侧不同流量、不同精度要求的多样场景。
### 方法关键点
- 架构拆分输入、共享循环、输出三模块，单循环时所有层仅执行一次，计算量和参数与同规模非循环模型完全对齐；采用门控自适应增量状态更新，为每个token、每个通道学习独立更新步长，保留单循环精度
- 训练时每步优化内混合不同循环次数样本：固定比例数据并行rank强制跑1循环，其余rank用采样循环次数，同时给每轮循环注入循环索引和总预算的条件信号，提升多循环精度增益
- 工程优化：预训练前75%步长仅跑单循环，最后25%开启混合深度训练，仅增16%训练开销；MoE模型复用首循环专家路由结果；推理侧仅保留最后一轮KV cache，内存与单循环持平
### 关键结果
在4B dense、30B MoE模型上验证，单循环时10任务平均精度分别比同参数基线低0.52、高1.04个百分点，4循环时分别提升7.25、4.75个百分点；最终Koi-4B模型单循环AA指数18（对齐Qwen3.5-4B），4循环达29，接近35B模型水平。
**最值得记住的一句话**：弹性深度大模型无需从零训练，仅在预训练后期开启混合循环训练+零初始化条件模块，就能以极低额外成本获得精度-算力动态可调能力
