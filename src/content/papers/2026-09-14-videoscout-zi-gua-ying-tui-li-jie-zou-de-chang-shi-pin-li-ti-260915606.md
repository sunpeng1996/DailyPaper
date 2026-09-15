---
title: 'VideoScout: Learning Agentic Active Exploration with Adaptive Reasoning Pacing
  for Long Video Understanding'
title_zh: VideoScout：自适应推理节奏的长视频理解主动探索智能体
authors:
- Weixin Xu
- Zhenyu Yang
- Bing Wang
- Shengsheng Qian
- Changsheng Xu
arxiv_id: '2609.15606'
url: https://arxiv.org/abs/2609.15606
pdf_url: https://arxiv.org/pdf/2609.15606
published: '2026-09-14'
collected: '2026-09-15'
category: Agent
direction: 多模态Agent · 长视频理解
tags:
- Multimodal LLM
- Video Agent
- Reinforcement Learning
- Long Video Understanding
- SFT
- DAPO
one_liner: 提出支持动态调速、笔记、回看的多轮视频Agent，长视频理解效果超同类开源7B模型
practical_value: '- 电商直播/长短视频内容理解场景可复用自适应节奏设计：无关片段2×/4×快进降本，关键片段1×细看保准确率，支持回看补全漏检信息，解决均匀采样漏关键商品介绍/用户互动片段的问题

  - 多轮Agent训练范式可迁移：先做单轮SFT冷启动教动作格式与基础行为，再用轨迹级DAPO做RL优化，组合奖励同时覆盖准确率、格式合规、与专家行为的时序IoU对齐，解决多轮探索奖励稀疏问题

  - 长时序信息处理场景（如用户长周期行为序列建模、多轮对话推荐）可复用跨轮文本笔记+动态步长设计，用可控大小的记忆缓存关键信息，动态调整序列采样粒度，平衡效率与信息完整度

  - 长内容推理奖励设计可借鉴仅在答案正确时生效的IoU时序对齐奖励，避免模型为凑进度牺牲准确率，引导Agent在获取足够信息的节点输出结果'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有长视频理解方法要么依赖固定均匀采样，要么采用粗到细的Agent缩放策略，都容易遗漏稀疏分布的关键证据；同时MLLM视觉上下文窗口有限，无法直接处理超长视频，亟需能主动探索、动态分配感知资源的框架。

### 方法关键点
- 将长视频理解建模为**Sequential Evidence Acquisition (SEA)** 问题，Agent逐轮与视频交互，支持三类动作：调整播放速度（1×/2×/4×对应不同采样帧率与分辨率）、回看快进过的指定片段、输出答案终止流程
- 维护固定大小的跨轮文本笔记，累积与查询相关的关键证据，避免跨轮信息丢失
- 两阶段训练：先基于66K标注的VideoScout-66K数据集做单轮SFT，教授输出格式与基础动作选择逻辑；再用DAPO算法做轨迹级RL，组合奖励包含答案准确率、输出格式合规性、与教师轨迹观看进度的IoU（仅答案正确时生效）

### 关键结果
在9个长视频理解基准测试中，7B参数的VideoScout在长视频理解类基准平均得分48.0，跨域基准平均得分45.0，均为开源模型最优；比基础Qwen2.5-VL-7B平均高6.2~7.2分，比未经过两阶段训练的同框架Agent高14.9分；推理时间自适应，简单任务比同类Agent更快，复杂任务投入更多算力换取更高准确率。

最值得记住的一句话：长时序理解的核心不是如何被动编码固定输入，而是如何像人一样主动把有限的感知资源分配到高价值信息段。
