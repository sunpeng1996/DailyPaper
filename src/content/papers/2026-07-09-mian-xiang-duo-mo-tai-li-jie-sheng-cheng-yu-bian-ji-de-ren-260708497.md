---
title: Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation,
  and Editing
title_zh: 面向多模态理解、生成与编辑的认知架构多模态Agent
authors:
- Feng Wang
- Canmiao Fu
- Zhipeng Huang
- Chen Li
- Jing Lyu
- Ge Li
affiliations:
- Peking University
- WeChat Vision, Tencent Inc.
arxiv_id: '2607.08497'
url: https://arxiv.org/abs/2607.08497
pdf_url: https://arxiv.org/pdf/2607.08497
published: '2026-07-09'
collected: '2026-07-10'
category: Agent
direction: 多模态Agent · 长会话记忆优化
tags:
- Multimodal Agent
- Episodic Visual Memory
- VLM
- Reinforcement Learning
- Long-context Dialogue
one_liner: 提出带外置情景视觉记忆的认知架构多模态Agent，8B性能超32B基线且推理耗时减半
practical_value: '- 多模态交互类业务（电商AI设计、商品秀生成、图文客服）可复用「结构化视觉记忆+按需检索」架构，避免全量历史视觉token挤占上下文，大幅降低长会话推理成本

  - 可借鉴PAE的结构化视觉记忆设计：给每一张生成/上传的图像存储「缩略图+语义标签+文本描述」三元组，同时兼顾检索的lexical匹配效率和细粒度视觉区分度，比纯文本记忆检索准确率提升超40%

  - 训练阶段可复用「程序化生成带检索标注的多轮对话+分阶段SFT+RL优化」范式，先训检索模块再固定检索优化记忆生成，不需要昂贵的人工标注就能大幅提升长会话性能

  - 电商商品多轮迭代设计、定制化海报生成场景可直接复用MEC的任务分类+工具调度逻辑，自动路由生成、编辑、理解、纯聊天任务，减少prompt工程成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有大一统多模态模型处理长轮次多模态对话时，需要重复投喂全量历史视觉token，不仅导致视觉token爆炸挤占上下文预算，还会因为长上下文隐式注意力不稳定出现跨轮视觉引用错误、语义漂移，单纯扩参数效果极差，32B模型在难例上检索准确率不足3%。

### 方法关键点
- 架构拆分为3个独立可优化模块：Perceptual Abstraction Engine（PAE）将每张图像抽象为「标签+文本描述+压缩缩略图」的结构化记忆存入外置Episodic Visual Memory（EVM）；Cognitive Retrieval Engine（CoRE）根据当前查询从EVM中仅召回相关视觉片段；Multimodal Executive Controller（MEC）负责任务分类、工具调度、生成最终输出
- 训练数据：开发Unified Scenario Engine自动生成带细粒度轮级检索标注的多轮多模态对话，无需人工标注
- 训练策略：分阶段SFT+RL，先用标注数据SFT训练CoRE，再用RL优化CoRE，最后固定CoRE用RL优化PAE的记忆生成效果，奖励直接关联下游检索准确率而非caption指标
- 部署版本CMA-Harness扩展了17种工具调用能力、多会话持久化记忆、OpenAI兼容接口

### 关键实验
自建M2CA-Bench长轮次多模态对话基准（100个20轮会话共2000个标注轮次，分4级难度），对比大一统多模态模型、全上下文Agent基线、未优化多Agent基线：8B参数模型20轮会话检索准确率达91.4%（英文）/89.6%（中文），比32B全上下文基线高8.2%，每轮推理时间从23.1s降到12.7s接近减半；难例集上检索准确率比8B多Agent基线高18.4%。

### 核心结论
结构化记忆+模块化决策比单纯参数缩放更适合构建可扩展、高效率的长轮次多模态Agent。
