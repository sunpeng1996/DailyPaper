---
title: 'StreamPI: Streaming Multimodal Temporal Modeling for Vision-Language-Action
  Models'
title_zh: StreamPI：面向视觉-语言-动作模型的流式多模态时序建模
authors:
- Zhe Liu
- Jinghua Hou
- Yuxiang Lu
- Zhenya Yang
- Xianzhe Fan
- Junwei Luo
- Junyi Li
- Ruihua Han
- Zhi Hou
- Hengshuang Zhao
affiliations:
- The University of Hong Kong
- ACE Robotics
arxiv_id: '2608.26067'
url: https://arxiv.org/abs/2608.26067
pdf_url: https://arxiv.org/pdf/2608.26067
published: '2026-08-25'
collected: '2026-08-28'
category: Multimodal
direction: 多模态时序建模 · VLA模型优化
tags:
- VLA
- Multimodal Modeling
- Temporal Reasoning
- Streaming Inference
- Robotics
one_liner: 无额外参数量的流式多模态时序框架，为单帧VLA模型赋予时序推理能力，适配异步部署
practical_value: '- 时序序列建模可复用「指令锚定」设计：将用户query/系统指令作为跨时间步语义锚，用户行为序列每个时间步做内部模态融合、跨时间步做因果注意力，既保留指令一致性又支持流式推理，适配短视频/直播流推荐场景

  - 线上异步部署可借鉴随机间隔训练策略：多步行为序列训练时加入随机采样间隔，提升模型对实时流延迟、数据丢帧/时间抖动的鲁棒性，适配推荐系统大流量下的异步数据链路

  - 存量模型升级可参考无参增量适配方案：基于LLM backbone的长度外推能力直接复用预训练权重，无需新增参数就能扩展单输入到多时序输入的推理能力，降低大模型迭代的训练/部署成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有SOTA VLA模型（如pi0.5）采用单帧范式，无法保留历史观测信息，空间感知精度受限，且同步训练和真实场景异步部署存在适配gap。

### 方法关键点
1. 提出无额外参数量的流式多模态时序建模框架StreamPI，引入指令锚定时序建模：将（视觉观测、语言指令）对作为原子时序单元，单元内双向注意力实现跨模态融合，单元间因果注意力保留流式推理能力，指令全程作为语义锚；
2. 提出随机间隔流式训练策略：固定帧间隔（如每3帧）可加速动作执行，随机间隔可提升对帧时序扰动的鲁棒性，适配异步部署需求；
3. 基于LLM backbone的长度外推能力，直接复用单帧预训练权重，支持单/多帧灵活切换推理。

### 关键结果
在记忆依赖、高精度感知类真实机器人任务，以及仿真基准LIBERO上，性能全面优于pi0.5。
