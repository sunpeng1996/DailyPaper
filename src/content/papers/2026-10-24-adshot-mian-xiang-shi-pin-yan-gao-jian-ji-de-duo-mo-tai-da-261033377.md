---
title: 'AdShot: Benchmarking Multimodal Large Language Models for Video Advertisement
  Clipping'
title_zh: AdShot：面向视频广告剪辑的多模态大模型基准
authors:
- Wen Xie
- Om Rastogi
- Sai Siddhartha Vivek Dhir Rangoju
- Gijs Overgoor
- Yakov Bart
- Sarah Ostadabbas
affiliations:
- Northeastern University
- Southern Methodist University
arxiv_id: '2610.33377'
url: https://arxiv.org/abs/2610.33377
pdf_url: https://arxiv.org/pdf/2610.33377
published: '2026-10-24'
collected: '2026-10-27'
category: Eval
direction: 多模态大模型 · 广告剪辑基准评估
tags:
- MLLM
- Video Advertising
- Benchmark
- Shot Selection
- Multimodal
one_liner: 构建首个视频广告选镜剪辑MLLM基准，评估15款主流多模态大模型的任务表现与偏差
practical_value: '- 电商短视频广告剪辑场景可直接复用AdShot的「镜头粒度选剪+严格时长约束」任务范式，优先选择7B/8B级音视频MLLM（如Qwen2.5-Omni
  7B、MiniCPM-o 2.6 8B）做剪辑初筛，效果接近25B大模型，算力成本仅为后者的1/3，可大幅降低人工剪辑工作量。

  - 优化广告选镜策略时需针对性修正MLLM的固有内容偏差：现有模型普遍偏好信息、情感类镜头，可通过Few-shot提示注入业务规则，或用AdShot标注数据做LoRA微调，提升action（行动号召）、imagery（品牌视觉）类镜头的选择占比，匹配品牌向/效果向等不同营销目标。

  - 工程实现上无需过度追求高采样帧率，每镜头取1张中心帧（1FPS）即可满足多数业务需求，3/5FPS仅能小幅提升选镜精度，反而会提升时长控制误差与推理算力消耗。'
score: 9
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
全球视频广告市场2025年规模预计达2150亿美元，品牌通常需要为同一支广告制作30s、15s等多版本，适配不同平台规则与用户注意力特征，而人工选镜剪辑成本高、效率低，是广告生产流程的核心瓶颈。现有多模态大模型（MLLM）的视频理解能力多在通用场景验证，尚未针对广告剪辑这种兼具严格时长约束、强业务目标的垂类任务做系统性评估，缺乏专业基准衡量模型输出与专业剪辑师决策的对齐度。
### 方法关键点
- 构建AdShot基准数据集，包含823对专业剪辑的30s源广告、15s剪映广告对，覆盖194个品牌、17个行业，标注了精准的镜头边界，以及action（行动号召）、emotion（情感）、information（产品信息）、imagery（品牌视觉）四类与广告效果强相关的镜头属性。
- 标准化评估流程：给MLLM输入镜头元数据（序号、时长）+每镜头中心帧，要求输出总时长在14-16s区间的镜头选择结果，对比专业剪辑的ground truth计算Precision、Recall、F1、时长误差，以及四类内容维度的选择偏差。
- 共评估13款纯视觉MLLM、2款音视频MLLM，参数覆盖7B-72B，包含LLaVA、Qwen、InternVL、Aria等主流开源模型系列。
### 关键结果
- 最优纯视觉模型Aria 25.3B F1达0.676；7B/8B级音视频小模型Qwen2.5-Omni 7B、MiniCPM-o 2.6 8B F1分别达0.668、0.669，效果接近Aria，仅用1/3参数量；9款模型优于随机基线（F1=0.503），6款模型性能低于基线，证明模型架构的适配性远重要于参数量。
- 所有模型普遍存在系统内容偏差：过度选择信息、情感类镜头，对行动号召、品牌视觉类镜头选择不足；平均时长绝对误差5.39s，多数模型倾向超出15s目标时长。

**最值得记住的一句话**：广告剪辑这类垂类业务任务中，MLLM的架构与模态适配性远重要于参数量，音视频融合小模型即可逼近大模型的业务效果。
