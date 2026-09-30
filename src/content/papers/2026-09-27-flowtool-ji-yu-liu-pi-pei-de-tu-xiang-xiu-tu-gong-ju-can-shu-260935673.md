---
title: 'FlowTool: Controlling Tool Parameter in Image Retouching via Flow Matching'
title_zh: FlowTool：基于流匹配的图像修图工具参数控制框架
authors:
- Thanh-Long V. Le
- Steven Walton
- Seunghyun Yoon
- Branislav Kveton
- Trung Bui
- Eunho Yang
- Viet Lai
affiliations:
- Adobe Research
- KAIST
arxiv_id: '2609.35673'
url: https://arxiv.org/abs/2609.35673
pdf_url: https://arxiv.org/pdf/2609.35673
published: '2026-09-27'
collected: '2026-09-30'
category: Agent
direction: 多模态Agent · 工具参数生成
tags:
- Flow Matching
- Multimodal Agent
- Tool Calling
- DiT
- VLM
- Inference Optimization
one_liner: 将图像修图的工具参数生成从自回归范式改为条件流匹配，精度提升的同时推理延迟降低50倍以上
practical_value: '- 工具调用类Agent涉及连续数值参数生成（如电商素材调节参数、广告出价、推荐策略调优参数等）时，可放弃自回归生成范式，改用条件流匹配直接输出结构化参数，既避免离散Token生成的数值精度差、级联错误问题，还能大幅降低推理延迟

  - 训练「预训练大模型+下游结构化生成头」的架构时，可复用两阶段训练策略：先冻结大模型主干训练下游模块，再开启主干LoRA联合微调，既能避免预训练知识被随机初始化的下游模块带偏，也能提升训练稳定性

  - 工具调用类场景如果有大量专家执行的结构化数据，可参考本文的无推理链标注方案，结合参考匹配奖励+大模型对齐度奖励做后训练，无需标注推理过程，大幅降低数据准备成本

  - 对延迟要求高的交互式Agent场景（如电商素材实时修图、广告素材动态调节），优先采用非自回归的结构化生成范式，相比MLLM自回归工具调用的延迟可降低1-2个数量级，内存占用也可减半'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于MLLM的工具类图像修图Agent采用自回归生成推理链、工具选择、参数的范式，存在三大核心缺陷：一是MLLM离散Token生成对连续数值参数的精度不足，无法满足修图的精细调节需求；二是自回归解码存在级联错误，早期预测偏差会导致后续参数全部失效；三是冗余推理链生成带来极高的推理延迟和内存开销，无法满足交互式修图的近实时要求，也难以落地到资源受限设备。
### 方法关键点
- 架构设计：融合VLM多模态理解模块+DiT流匹配参数生成器+工具存在预测头，直接建模「输入图像+用户指令」条件下的连续工具参数联合分布，完全跳过中间推理链生成步骤
- 训练策略：采用两阶段SFT课程，先冻结预训练VLM仅训练流生成器和工具预测头，再开启VLM的LoRA联合微调，避免预训练多模态知识被破坏，训练更稳定；SFT后结合「专家结果L1匹配奖励+VLM指令对齐度打分奖励」做RL后训练，进一步提升效果
- 推理逻辑：仅需3步ODE求解，即可从高斯噪声直接生成完整的连续参数向量和工具激活掩码，输入修图引擎直接执行
### 关键结果
在MMArt-Bench、ArtEdit-Bench、MIT-Adobe5K、FlowTool-Eval四个基准上对比商用MLLM（GPT-5.6 Sol、Gemini 3.1 Pro等）、专用修图Agent（JarvisArt、RetouchIQ等）：
1. 参考指标上比专用Agent的L1最多降28.8%、L2最多降47.4%，比商用MLLM的L1最多降13%、L2最多降21.7%，感知质量与商用MLLM相当
2. 推理延迟比所有基线低50倍以上，单样本仅需0.19s，GPU峰值内存比专用Agent少近一半，仅9.89GB

> 最值得记住的一句话：对于结构化连续参数的工具调用场景，放弃自回归语言生成范式、直接建模条件参数分布，能同时实现效果、效率的双重提升。
