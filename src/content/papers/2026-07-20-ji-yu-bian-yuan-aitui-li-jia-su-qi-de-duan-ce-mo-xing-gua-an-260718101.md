---
title: Empowering On-Device Model Adaptation with an Edge AI Inference Accelerator
title_zh: 基于边缘AI推理加速器的端侧模型适配优化方案
authors:
- Mateusz Piechocki
- Alessandro Capotondi
- Marek Kraft
affiliations:
- Poznan University of Technology
- University of Modena and Reggio Emilia
arxiv_id: '2607.18101'
url: https://arxiv.org/abs/2607.18101
pdf_url: https://arxiv.org/pdf/2607.18101
published: '2026-07-20'
collected: '2026-07-22'
category: Training
direction: 端侧模型训练 · 边缘硬件加速
tags:
- On-Device Training
- Edge AI
- Model Adaptation
- Hardware Acceleration
- Quantization
one_liner: 复用商用边缘推理加速器做冻结主干特征提取，实现低功耗高速度的端侧模型训练适配
practical_value: '- 端侧个性化推荐/Agent场景可直接复用「冻主干+轻量头微调」的异构训练架构：将大模型主干INT8量化后下沉到端侧NPU/边缘加速器运行，仅轻量适配头在CPU微调，大幅降低端侧更新的功耗与延迟

  - 端侧用量化模型做特征提取时，必须配套训练后量化恢复步骤，可有效缓解量化敏感架构的特征质量下降问题，保障个性化适配的精度

  - 端侧小样本动态更新场景可参考计算图拆分思路：将固定计算逻辑下沉到专用加速硬件，仅需动态更新的模块在通用处理器运行，平衡效率与迭代灵活性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
端侧终身个性化需要模型持续适配新数据，但端侧硬件算力、内存、功耗限制下，现代DNN的端到端反向传播落地可行性极低，现有商用边缘加速器大多仅支持推理，不直接适配训练任务。
### 方法关键点
1. 异构适配管线：复用商用边缘推理加速器Hailo-8L做冻结主干的INT8量化特征提取
2. 计算图拆分：预训练主干量化后跑在加速器，仅轻量FP32分类头在宿主CPU微调，大部分权重固定，支持高频低功耗现场更新
3. 新增训练后量化恢复步骤，保障加速器生成的特征质量，缓解量化敏感架构的精度损失
### 关键结果
对比Raspberry Pi 5 CPU基线，管线训练墙钟速度最高提升15.4倍，单样本功耗持续降低，适配场景下吞吐量表现具备竞争力。
