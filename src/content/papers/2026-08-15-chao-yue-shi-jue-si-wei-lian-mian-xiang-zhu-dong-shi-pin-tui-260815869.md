---
title: 'Beyond Visual CoT: Internalized Visual Thinking for Proactive Video Reasoning'
title_zh: 《超越视觉思维链：面向主动视频推理的内化视觉思考框架IVT》
authors:
- Xiaoyu Zhu
- Xinke Deng
- Suresh Taddewadikar
- Arnab Kumar Mondal
- Zhongyu Jiang
- Ian Fasel
- Joerg Liebelt
affiliations:
- Apple
arxiv_id: '2608.15869'
url: https://arxiv.org/abs/2608.15869
pdf_url: https://arxiv.org/pdf/2608.15869
published: '2026-08-15'
collected: '2026-08-18'
category: Multimodal
direction: 多模态推理 · 视觉思维链优化
tags:
- Multimodal LLM
- Visual CoT
- Video Reasoning
- Latent Prediction
- Inference Efficiency
one_liner: 训练时通过未来帧隐向量监督内化视觉推理，推理无额外开销，性能超Visual CoT同时延迟降5倍以上
practical_value: '- 直播电商内容实时理解、短视频时序预判等低延时多模态场景，可借鉴IVT思路，将未来状态预测从推理端迁移到训练端做辅助监督，无需显式生成中间图像，大幅降低推理延迟

  - 多目标辅助训练时，建议采用主任务（比如文本生成/推荐打分）和辅助预测任务1:1的均衡数据配比，联合训练效果优于两阶段训练，避免主任务优化冲掉辅助任务学到的predictive信号

  - 涉及未来状态预判的Agent（比如直播场控Agent、用户内容消费时序预测Agent），可优先选择Flux-VAE这类重构导向的隐向量作为预测目标，相比DINOv2等语义特征能提供更有效的监督信号

  - 延迟敏感的多模态推理场景不要盲目上显式Visual CoT，优先评估内化式隐空间监督方案，性价比远高于显式生成中间结果的方案'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Visual CoT通过生成中间图像作为推理桥梁，能有效提升主动视频推理（早事件预测、下事件预测）效果，但推理时需生成、重编码像素级图像，开销暴涨5~6倍，延迟过高无法适配直播实时理解、事件预判等对时效性要求高的落地场景，亟需兼顾效果和推理效率的优化方案。
### 方法关键点
- 提出Internalized Visual Thinking (IVT)后训练框架，训练时同时优化文本预测损失、未来帧隐向量预测损失，推理时仅保留文本生成路径，无额外计算开销
- 目标表示优先选择Flux-VAE隐向量（效果优于DINOv2、SigLIP等语义特征），预测头将MLLM隐状态映射到目标空间做监督，梯度不回传目标编码器
- 架构可选共享参数的Dense decoder（适合1~2帧短预测horizon）或MoE decoder（预测、理解任务用独立专家，对长horizon更鲁棒）
- 训练采用文本/预测任务1:1均衡数据配比、全程联合训练而非两阶段训练，预测目标用直接回归或流匹配均可
### 关键结果
在Ego-Exo4D、Ego4D、EPIC-KITCHENS-100三个公开数据集的早事件预测、下事件预测共6个任务上，IVT全面优于纯文本SFT基线，4个任务效果超过显式Visual CoT，所有场景下平均端到端延迟比Visual CoT降低5倍以上。
### 核心结论
显式推理时生成像素级中间结果不是获得视觉推理能力的必要条件，完全可以在训练时通过隐空间预测监督把视觉预判能力内化到模型参数中，兼顾效果和推理效率
