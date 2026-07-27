---
title: 'MoE$^2$-LoRA: When MoE Models Meet MoE-style Low-Rank Adaptation'
title_zh: MoE²-LoRA：面向MoE大模型的MoE风格低秩适配方法
authors:
- Qingyu Yang
- Haonan He
- Minglei Li
- Jingqi Ye
- Tao Chen
- Lei Bai
- Peng Ye
affiliations:
- Shanghai Artificial Intelligence Laboratory
- KTH Royal Institute of Technology
- University of Science and Technology of China
- Fudan University
- The Chinese University of Hong Kong
arxiv_id: '2607.21978'
url: https://arxiv.org/abs/2607.21978
pdf_url: https://arxiv.org/pdf/2607.21978
published: '2026-07-24'
collected: '2026-07-27'
category: Training
direction: MoE大模型参数高效微调方法
tags:
- MoE
- LoRA
- PEFT
- Parameter-Efficiency
- Fine-tuning
one_liner: 提出耦合预训练MoE路由先验与全局共享LoRA专家池的PEFT方法，效果超现有SOTA且保留通用能力
practical_value: '- 业务中使用MoE架构LLM做推荐文案生成、Query理解/改写场景，可直接替换原有LoRA方案，相同参数量下域内效果最高提2.56个点，同时避免灾难性遗忘保留通用能力

  - RCP模块设计可复用：复用大模型原生路由信号+低秩任务校正通道，无需从零学习路由，大幅降低路由模块训练成本，适合小算力/端侧场景的MoE模型微调

  - 全局共享LoRA专家池设计无需手动配置每层LoRA容量，可自动适配不同层适配需求，参数利用率远高于分层配置，适合多任务微调场景下的跨层知识共享'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前MoE架构LLM已在推理效率、缩放性能上追平稠密模型，成为大模型落地的主流选择，但针对MoE的参数高效微调（PEFT）方法研究不足：现有方案要么静态选择部分专家挂载LoRA，导致推理时激活的未适配专家效果劣化，要么分层独立配置适配模块，忽略跨层专家协作与特征交互，参数冗余度高；此外现有MoE风格LoRA未复用原生MoE的路由先验，需要从零学习路由，训练成本高、泛化性差。

### 方法关键点
- 双通道路由条件投影（RCP）模块：主通道复用原生MoE的路由logits作为预训练先验，辅助通道用低秩矩阵投影隐藏状态注入任务校正信号，联合映射生成LoRA专家的路由权重，既继承预训练路由模式，又支持任务自适应调整
- 全局共享LoRA专家池：所有MoE层共用同一个LoRA专家池，每层独立训练路由矩阵，自动学习层专属的LoRA专家选择偏好，无需手动配置每层适配容量，实现跨层知识共享，降低参数冗余

### 关键实验
在OLMoE-1B-7B、DeepSeek-V2-Lite、Qwen3-30B-A3B、Qwen3.5-35B-A3B四个不同规模MoE backbone上测试，覆盖数学、代码、多模态医疗VQA等任务，对比PERFT-E、MoELoRA、MoLA、DAS-LoRA等SOTA PEFT基线，相同参数预算下，域内平均准确率最高提升2.56个点，通用能力保留率也优于所有基线，参数规模扩展时效果线性提升，缩放效率显著高于MoELoRA。

### 核心结论
针对MoE架构的PEFT设计不需要割裂原生MoE机制与适配模块，深度耦合原生路由先验+跨层共享适配参数，可同时实现效果提升、参数高效、通用能力保留三大目标。
