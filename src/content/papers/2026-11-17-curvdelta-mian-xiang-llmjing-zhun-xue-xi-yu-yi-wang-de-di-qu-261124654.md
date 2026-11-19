---
title: 'CurvDelta: Low-Curvature Delta Modeling For Surgical Learning and Unlearning'
title_zh: CurvDelta：面向LLM精准学习与遗忘的低曲率参数更新框架
authors:
- Zeguan Xiao
- Zhuocheng Liang
- Yun Chen
- Yong Wang
- Guanhua Chen
- Pinyan Lu
affiliations:
- Shanghai University of Finance and Economics
- Alibaba Group
- Southern University of Science and Technology
arxiv_id: '2611.24654'
url: https://arxiv.org/abs/2611.24654
pdf_url: https://arxiv.org/pdf/2611.24654
published: '2026-11-17'
collected: '2026-11-19'
category: Training
direction: LLM低曲率微调 · 知识保留与选择性遗忘
tags:
- LoRA
- Parameter Efficient Fine-tuning
- Unlearning
- K-FAC
- Knowledge Preservation
one_liner: 基于低曲率子空间约束的LLM参数更新方法，兼顾目标任务性能与通用能力保留
practical_value: '- 电商场景LLM微调（如商品文案生成、导购Agent）可直接复用CurvLoRA方案，在新增下游能力的同时减少通用对话/推荐能力的衰减，避免全量微调导致的历史效果波动

  - 针对合规要求的用户隐私数据遗忘、违规商品知识删除场景，可采用CurvDelta框架做选择性unlearning，相比基线方法遗忘准确率提升40%+的同时保留95%以上的模型原有性能，避免重训成本

  - 曲率估计无需大样本，仅用数百条代表性保留数据即可构建低曲率子空间，可复用同一基模型的曲率投影矩阵适配多下游任务，大幅降低多场景微调的计算开销'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM预训练后适配新任务、做选择性知识遗忘时，现有微调方法普遍存在目标任务提升但通用能力大幅衰减的问题，全量重训成本极高，传统正则、replay等方案无法在任务性能和能力保留之间取得最优trade-off。

### 方法关键点
- 基于K-FAC近似估计预训练模型在保留数据集上的损失曲率，将参数更新约束在曲率最低的子空间内，从参数结构上保证更新对原有能力的影响最小
- 提出两种适配方案：全量更新版CurvDelta，将训练的稠密参数矩阵通过两侧投影约束到低曲率空间；低秩版CurvLoRA，将LoRA的A、B矩阵分别做投影，无需生成稠密矩阵，参数效率与原生LoRA相当
- 曲率投影矩阵仅需基于保留数据集预计算一次，可跨任务、跨超参数复用，自适应优化器下也能保证更新始终落在低曲率空间内

### 关键实验结果
- 能力学习任务：基于Gemma-3-1B、Llama-2-7B在数学推理、代码生成数据集微调，对比LoRA、OPLoRA、CrispEdit等基线，CurvDelta下游性能与全量微调持平，通用知识保留率平均提升8-12个百分点；CurvLoRA参数效率与原生LoRA相当，保留率最高提升15个百分点
- 选择性遗忘任务：在TOFU、MUSE基准测试，CurvDelta相比基线方法目标知识遗忘率提升40%以上，保留集性能接近从零重训的效果，端到端训练耗时比同类曲率方法CrispEdit降低59.5%，峰值显存占用降低36.5%

将参数更新约束在预训练模型的低曲率子空间内，是平衡LLM任务适配与原有能力保留的高效可落地路径，效果优于正则、梯度投影等传统方案。
