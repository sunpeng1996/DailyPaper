---
title: 'Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon
  Real-Time Game Agent'
title_zh: Gamer：面向长时程实时游戏的通用视觉-语言-动作基座Agent
authors:
- Run Luo
- Kuan Zhang
- Qi Deng
- Yukun Chen
- Zhihao Yang
- Yufei Zhang
- Renrong Hu
- Yi Zhang
- Guiyu Ma
- Tianyu Fan
affiliations:
- miHoYo Honkai AI R&D Team
arxiv_id: '2611.18397'
url: https://arxiv.org/abs/2611.18397
pdf_url: https://arxiv.org/pdf/2611.18397
published: '2026-11-12'
collected: '2026-11-16'
category: Agent
direction: 多模态游戏Agent · VLA长时程实时交互
tags:
- VLA
- Game Agent
- Long-Horizon Reasoning
- KV Cache
- Reinforcement Learning
one_liner: 基于Qwen3系列的端到端VLA游戏Agent，支持跨品类游戏键鼠级交互，性能媲美熟练人类玩家
practical_value: '- 稀疏推理+内存压缩的长上下文处理思路，可迁移到电商导购Agent、用户长会话推荐场景，解决有限上下文窗口下的历史信息留存问题

  - Streaming-vLLM的状态化KV缓存复用、FSM引导投机解码+动作早发的工程方案，可直接复用在低延迟实时交互Agent场景，比如直播带货实时助理、搜索实时query补全

  - 三阶段训练（CPT→SFT→RL）+随机键重映射/重复感知损失衰减的轨迹去偏思路，可迁移到交互类推荐系统的用户行为建模，降低高频重复行为的训练偏差

  - TA-GRPO的内存分段+时序信用分配机制，适合长周期推荐任务（比如用户复购引导、月活提升）的RL优化，解决稀疏奖励下的信用分配问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有游戏Agent多依赖游戏专属API、定制化动作空间，跨域泛化性差，且长时程任务存在上下文窗口限制、推理延迟高、稀疏奖励难优化等问题，无法适配无API开放的复杂3D游戏场景，也难以支撑实时交互需求。

### 方法关键点
- 统一键鼠动作表示：将屏幕观测+键盘鼠标操作映射为统一序列化格式，无需游戏专属API，支持跨2D/3D游戏交互
- 三阶段训练范式：① 持续预训练（CPT）：基于数万小时跨游戏轨迹，用随机键重映射、重复感知损失衰减解决数据偏差，学习通用控制先验；② 稀疏推理SFT：基于LLM标注的三级指令数据（操作/子目标/完整任务），训练模型自适应生成推理/内存摘要/动作，解决长上下文记忆问题；③ TA-GRPO强化学习：将长轨迹按内存压缩分段，用环境可验证奖励+时序信用分配优化策略，解决稀疏奖励问题
- Streaming-vLLM推理引擎：通过状态化KV缓存复用、FSM引导投机解码、动作流早发，降低推理延迟，支持高并发实时交互

### 关键实验
训练数据含2.4K小时跨游戏轨迹、6.3B多模态token、1K小时《崩坏：星穹铁道》标注数据；对比VPT、Open-P2P、SIMA等基线，在3D开放世界游戏任务上性能媲美熟练人类玩家，2D游戏基准上取得SOTA成绩；H200上部署支持单卡同时服务数十个游戏实例，端到端推理延迟满足30Hz实时控制要求。

**最值得记住的结论**：即使是重复的键鼠交互轨迹，通过数据规模缩放和适配的学习算法，也能支撑通用交互Agent的能力大幅提升。
