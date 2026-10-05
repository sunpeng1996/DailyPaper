---
title: Rollout-Marginal Distillation for Long-Horizon Autoregressive Video Generation
title_zh: 面向长时序自回归视频生成的滚动边际蒸馏方法
authors:
- Chenjian Gao
- Zhihao Hu
- Jianqi Ma
- Jun Zhang
- Weidong Zhang
- Tianfan Xue
affiliations:
- MMLab, The Chinese University of Hong Kong
- Tencent AIPD
arxiv_id: '2609.37925'
url: https://arxiv.org/abs/2609.37925
pdf_url: https://arxiv.org/pdf/2609.37925
published: '2026-09-28'
collected: '2026-10-05'
category: Multimodal
direction: 多模态生成 · 长时序自回归蒸馏
tags:
- Autoregressive Generation
- Video Diffusion
- Knowledge Distillation
- Long-Horizon Generation
- Multimodal
one_liner: 提出滚动边际蒸馏RMD方法，解决长时序自回归视频生成误差累积问题，兼顾块质量与时序一致性
practical_value: '- 自回归长序列生成任务可借鉴「分块独立打分+全局一致性校正」的蒸馏范式，平衡局部输出质量和全局连贯性，避免历史误差干扰当前模块的优化方向

  - 无需修改基础模型架构、无额外记忆模块的轻量蒸馏思路，可低成本迁移到生成式推荐、多轮Agent交互的长序列生成场景，降低落地成本

  - 电商营销短视频、商品演示视频的长时序生成场景，可直接复用RMD方法拓展生成时长上限，同时支持低延迟流生成适配短视频分发需求'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
自回归（AR）视频扩散可实现低延迟流生成，但长时序滚动推理时预测误差会持续累积；现有视频级分布匹配蒸馏（DMD）对整段序列联合打分，为保障时序一致性会被迫适配上下文的历史伪影，无法为单块提供清晰的质量优化信号。
### 方法关键点
滚动边际蒸馏（RMD）保留生成历史做AR预测，先对每个视频块单独调用块教师模型打分，确保块质量优化不受不完美时序上下文干扰；后续补加视频级DMD优化，弥补独立块打分丢失的时序关联性，全程无需修改生成器架构、无需新增额外记忆模块。
### 关键结果
仅在5秒时长的训练数据上收敛，即可稳定生成500秒高视觉质量视频，生成时长是训练 horizon 的100倍，效果全面优于视频级DMD基线。
