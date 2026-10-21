---
title: 'Muse Glimmer 30B: An On-Device Agentic Model'
title_zh: Muse Glimmer 30B：面向消费级硬件的端侧智能体专用大模型
authors:
- Arash Ebrahim Abtahizadeh
- Muna Aghamelu
- Adil Ahmed
- Juan C. Angeles Acuna
- Alexis Audran-Reiss
- Asaf Avrahamy
- Yoram Bachrach
- Can Balioglu
- Amar Budhiraja
- Onur Çelebi
affiliations:
- Meta Superintelligence Labs
arxiv_id: '2610.24628'
url: https://arxiv.org/abs/2610.24628
pdf_url: https://arxiv.org/pdf/2610.24628
published: '2026-10-16'
collected: '2026-10-21'
category: Agent
direction: 端侧智能体 · 大模型蒸馏与量化优化
tags:
- On-Device Agent
- Knowledge Distillation
- Quantization
- Multimodal LLM
- Speculative Decoding
one_liner: Meta开源30B多模态端侧智能体模型，性能超同尺寸Gemma4、Qwen3.6，可在消费级GPU本地运行
practical_value: '- 开发端侧电商导购/推荐智能体时可直接复用4-bit量化+DFlash speculative decoding方案，在32GB消费级GPU上实现低延迟推理，无需依赖云服务即可保护用户行为隐私

  - 训练小参数业务智能体模型时可借鉴「大模型logit蒸馏+中期领域注入+后期智能体轨迹对齐+on-policy蒸馏」的pipeline，用更少参数逼近前沿大模型的工具调用、多步推理能力

  - 构建电商/广告场景智能体训练数据时可复用仿真环境+persona+场景生成的合成数据pipeline，低成本生成大量符合真实业务逻辑的多步交互轨迹'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前公开的消费级硬件适配大模型多为通用用途，缺乏智能体专用的多步推理、可靠工具调用、隐私上下文处理能力，存在云侧大模型能力和端侧本地智能体可用能力的缺口，同时端侧运行严格受限于32GB显存的消费级硬件天花板。

### 方法关键点
- 架构：采用30B参数稠密Transformer（同显存限制下比MoE架构计算效率高2~2.5倍），搭配1.8B参数冻结视觉感知编码器支持多模态输入，采用GQA+滑动窗口注意力控制KV cache开销，上下文长度达128K
- 训练：从Meta前沿大模型Muse Spark蒸馏，分为预训练logit蒸馏、中期领域/上下文扩展注入、后期SFT+on-policy蒸馏+多目标RL对齐三个阶段，配套生成式仿真环境产出高质量智能体交互轨迹数据
- 推理优化：支持4-bit量化（EvoPress方案精度损失<0.1%，Q4KM方案可适配24GB显存），搭配DFlash speculative decoding实现端侧可接受的推理速度

### 关键结果
在工具调用、多步规划、智能体任务完成指标上全面领先同尺寸Gemma4-31B、Qwen3.6-27B，多语言智能体评测领先竞品23~38个百分点，4-bit量化后平均准确率仅比BF16版本低0.1~0.9个百分点，可在单张RTX 5090上本地运行。

最值得记住的结论：针对32GB消费级显存约束，同参数规模下稠密Transformer架构比MoE架构的智能体任务计算效率高2~2.5倍，是端侧智能体模型的更优选择。
