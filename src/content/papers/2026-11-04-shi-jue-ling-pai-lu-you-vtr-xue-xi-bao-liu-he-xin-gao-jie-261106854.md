---
title: 'Visual Token Routing: Learning to keep tokens that matter'
title_zh: 视觉令牌路由（VTR）：学习保留核心高价值视觉令牌
authors:
- Pranjal Aggarwal
- Sean Welleck
affiliations:
- Carnegie Mellon University
arxiv_id: '2611.06854'
url: https://arxiv.org/abs/2611.06854
pdf_url: https://arxiv.org/pdf/2611.06854
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: 多模态Agent · 视觉令牌稀疏化加速
tags:
- Visual Token Routing
- Computer-use Agent
- Multimodal LLM
- Sparse Representation
- Inference Acceleration
one_liner: 提出轻量时空路由方案，动态裁剪多模态Agent无效视觉令牌，降3.3倍算力且性能无损
practical_value: '- 电商GUI自动化运营、客服类多模态Agent可直接复用VTR时空路由逻辑，裁剪多轮截图的重复/无关视觉令牌，相比直接降分辨率方案性能高10个点以上，同时降低2-3倍推理成本。

  - 直播、短视频等跨模态推荐的内容理解场景，可借鉴自适应约束优化方案，无需预设令牌保留比例，动态适配不同内容的算力需求，低动效内容可省6倍以上视觉计算开销。

  - 长上下文多模态模型推理优化可复用锚点帧+滑动路由设计，每隔固定步长保留一帧全量信息作为锚点，其余帧仅保留高价值区域，可降低KV cache占用2倍以上且精度几乎无损。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
多模态计算机使用Agent（CUA）处理长时序任务、实时场景时，单张1080P截图就产生2000+视觉令牌，100步任务累计超过20万视觉令牌，上下文爆炸导致推理成本高、延迟大；现有固定比例降分辨率、删令牌的方案易丢失按钮、文本框等关键小区域信息，性能下降严重。

### 方法关键点
- 轻量时空路由模块：3层MLP仅23.3M参数（占大模型1%参数量），拼接当前与历史K帧同一位置的视觉令牌，预测每个令牌的保留概率，丢弃令牌直接从输入移除，保留令牌维持原位置编码。
- 双目标联合训练：最小化保留令牌占比+约束动作预测性能损失不超过阈值，通过全量模型、仅锚点模型的损失差自适应调整目标权重，无需预设固定令牌保留比例。
- 锚点帧机制：每B帧保留1张全量截图作为锚点，避免信息长期丢失；路由初始先用SAM分割的变化区域预训练，再联合大模型微调。

### 关键实验
在OSWorld、CUA-World桌面Agent基准、视频游戏动作预测三个数据集测试，对比降分辨率、像素差删帧、H.264运动检测等基线：仅2000步训练就和全分辨率模型性能持平，视觉令牌数减少2.5-5.8倍，推理成本最高降3.3倍，prefill速度最高提2.9倍；比固定规则基线在OSWorld上最高领先12.8个点，联合训练比单独训练路由高13.2个点。

### 核心结论
多模态时序任务中大多数视觉令牌要么语义无关要么时序冗余，通过任务驱动的动态路由裁剪，可在几乎无损性能的前提下大幅降低算力开销。
