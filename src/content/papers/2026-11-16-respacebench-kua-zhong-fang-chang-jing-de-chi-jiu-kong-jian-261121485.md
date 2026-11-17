---
title: 'Lost in the Hallway: Benchmarking Persistent Spatial Memory Across Revisits'
title_zh: ReSpaceBench：跨重访场景的持久空间记忆能力评测基准
authors:
- Henry Zheng
- Weibo Gong
- Yang Yue
- Rui Huang
- Yang Zhang
- Gao Huang
affiliations:
- Tsinghua University
- PICO, ByteDance
arxiv_id: '2611.21485'
url: https://arxiv.org/abs/2611.21485
pdf_url: https://arxiv.org/pdf/2611.21485
published: '2026-11-16'
collected: '2026-11-17'
category: Agent
direction: Embodied Agent · 空间记忆评测
tags:
- Spatial Memory
- Embodied Agent
- Benchmark
- MLLM
- Video Reasoning
one_liner: 提出跨重访持久空间记忆评测基准ReSpaceBench及30k无重叠训练样本集
practical_value: '- 做AR逛店/线下导购Agent时可复用覆盖感知采样策略：每个货架/房间入口保留至少1帧观察+过渡段帧，避免相似空间混淆，提升空间关联准确率

  - 多轮会话/跨次推荐的用户记忆建模可参考本文错误分析逻辑：优先解决相似物品/场景的身份绑定错误，而非仅优化证据检索效率

  - 长视频/多轮交互Agent的记忆模块可复用9项任务的设计思路，拆解记忆关联、状态追踪、下游推理三类能力分阶段优化

  - 小样本提升MLLM跨场景记忆能力时，可复用无重叠场景针对性微调范式：仅用合成场景训练就能提升真实场景14.8%的关联准确率'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有MLLM与Embodied Agent的空间记忆评测未针对受控重访场景设计，无法衡量模型在视角变化、同类型空间干扰、环境状态变更下的持久空间关联能力，导致服务机器人、AR导购等落地场景中Agent频繁出现空间混淆、状态更新错误问题。
### 方法关键点
- 构建ReSpaceBench基准：覆盖590个合成+真实家庭场景、3244个问题，拆解为关联、持久状态追踪、下游推理3大类9项任务，严格定义重访为物理进入房间而非视觉瞥见，刻意加入同类型房间作为干扰项
- 配套发布RS-30K训练集：共30k样本，与评测集无场景、路线、视频重叠，避免数据泄露
- 统一评测协议：默认1fps视频采样，按任务类型采用选项匹配、数值精确匹配两种评分规则，设置盲测、随机、频率三类基线
### 关键实验
- 评测32个MLLM及3个Agent视频理解框架，最优零样本模型GPT-5.6 Sol整体准确率仅50.5%，人类准确率达90.1%，存在近40pp性能差
- 三类Agent框架（AVP/DVD/VideoAgent）相比同底座直接推理无任何性能提升，核心错误来自证据遗漏、跨重访房间身份关联错误
- 用RS-30K微调Qwen3-VL-8B，整体准确率从35.5%提升至60.4%，真实场景准确率同步提升14.8pp
### 核心结论
迭代式证据检索不足以保证Agent的空间记忆一致性，跨重访的相似空间身份绑定是当前最核心的性能瓶颈。
