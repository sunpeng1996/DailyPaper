---
title: 'SimpleMemVLA: A Simple but Effective Native-Video Memory for Vision-Language-Action
  Models'
title_zh: SimpleMemVLA：面向视觉语言动作模型的高效原生视频记忆方案
authors:
- Cheng Yin
- Wang Xu
- Junpeng Yang
- Sikyuen Tam
- Hanyu Liu
- Yuan Yao
- Xiangrui Zeng
- Junbo Cui
- Yequan Wang
- Zhouping Yin
affiliations:
- 华中科技大学
- 中国人民大学
- 清华大学
- 北京大学
- 北京人工智能研究院
arxiv_id: '2609.05533'
url: https://arxiv.org/abs/2609.05533
pdf_url: https://arxiv.org/pdf/2609.05533
published: '2026-09-01'
collected: '2026-09-09'
category: Multimodal
direction: 多模态VLA · 长时序记忆机制优化
tags:
- VLA
- Long-Horizon Reasoning
- Memory Mechanism
- Prefix Prefill
- Multimodal
- KV Cache
one_liner: 提出无专用记忆模块的VLA方案，输入带时间戳的采样历史，共享前缀prefill降延迟，性能超现有机制达SOTA
practical_value: '- 长会话推荐/多轮Agent场景可放弃复杂的历史压缩/检索模块，直接输入带时序标记的采样完整历史，依托基座预训练能力降低模块开发成本

  - 同一会话内的连续请求（如用户逛商品时的连续推荐、客服Agent多轮对话）可复用prefill阶段的KV cache，显著降低推理延迟

  - 长上下文任务可通过子任务生成的hidden states作为历史信息到下游头的唯一传递通道，过滤无效信息提升效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
长时序任务为部分可观测场景，决策所需信息可能出现在数分钟前的观测中。现有VLA的记忆机制（检索库、学习式压缩器、循环状态）均需提前判断要保留的历史内容，原有假设分钟级历史无法直接处理，但现代VLM基座已突破该限制。
### 方法关键点
1. 无专用记忆模块，保留采样的完整历史，转换为基座预训练适配的带时间戳视频格式直接输入；
2. 生成子任务的hidden states作为历史信息到动作头的唯一传递通道；
3. 连续决策共享大部分历史，在动作执行阶段prefill共享前缀，压缩推理耗时。
### 关键结果
在4个记忆基准上达到新SOTA，无通用控制能力损失；固定基座与训练配置时，性能大幅领先检索、压缩、循环状态记忆机制，因果干预验证模型可有效读取历史信息，推理延迟接近单帧VLA。
