---
title: 'Hy-Nomas: Towards Free-form Interactive World Generation'
title_zh: Hy-Nomas：支持自由形式交互的虚拟世界生成框架
authors:
- Qiaoling Chen
- Jiaxiang Cheng
- Xueqing Deng
- Tiankai Hang
- Ji Hou
- Jiaqi Li
- Yifan Liu
- Tao Lu
- Junshu Tang
- Yu Tang
affiliations:
- Tencent Hy
- Tencent Hy Visual Generation Team
arxiv_id: '2610.36729'
url: https://arxiv.org/abs/2610.36729
pdf_url: https://arxiv.org/pdf/2610.36729
published: '2026-10-26'
collected: '2026-10-29'
category: Multimodal
direction: 多模态交互 · 视频世界生成
tags:
- World_Model
- Diffusion_Model
- Multimodal_Interaction
- Video_Generation
- Prompt_Engineering
one_liner: 提出搭载8B扩散骨干的交互视频世界模型Hy-Nomas，支持多轮自由文本指令与连续相机控制
practical_value: '- 动作感知因果注意力的设计思路可直接迁移至多轮对话式推荐：将长期用户偏好设为全轮可见，当前查询指令仅作用于当前推荐轮次，既保留历史一致性又避免旧指令干扰

  - 多阶段课程训练策略可复用在LLM4Rec多任务训练场景：按任务难度从基础生成、单轮交互到多轮交互逐步叠加训练目标，降低训练难度的同时提升最终效果

  - 多模态Prompt Enhancer的思路可迁移至电商Agent交互模块：将用户历史行为、上下文对话、当前查询统一转换为推荐系统可识别的结构化检索条件，提升跨模态输入的处理效率'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有交互世界生成方案难以平衡多轮指令遵循、历史上下文留存、动作后果一致性三大要求，且多数无法同时支持自由文本指令与连续相机控制。
### 方法关键点
- 以8B参数扩散Transformer为骨干，基于KV cache缓存历史上下文，支持可变长度视频片段生成
- 核心采用动作感知因果注意力机制：全局描述性上下文跨片段可见，动作指令仅作用于对应时间窗口
- 新增视觉语言Prompt Enhancer，将用户请求、多模态交互历史转换为下一片段的结构化生成条件
- 采用多阶段课程训练流程，依次覆盖因果生成、文本交互、相机控制、自生成历史训练，最后完成扩散蒸馏
### 关键结果
人类评估效果显著优于现有世界模型，已开源模型权重、代码、基准数据集与轻量适配工作流
