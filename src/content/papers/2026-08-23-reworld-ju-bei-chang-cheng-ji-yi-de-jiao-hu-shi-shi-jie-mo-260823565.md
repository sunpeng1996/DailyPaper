---
title: 'ReWorld: An Interactive World Model with Long-Horizon Memory'
title_zh: ReWorld：具备长程记忆的交互式世界模型
authors:
- Zhifei Chen
- Luozhou Wang
- Guibao Shen
- Dongyu Yan
- Shuai Yang
- Tianshuo Xu
- Yihua Du
- Wei Wang
- Tianyi Gui
- Lianghua Huang
affiliations:
- HKUST(GZ)
- Alibaba
arxiv_id: '2608.23565'
url: https://arxiv.org/abs/2608.23565
pdf_url: https://arxiv.org/pdf/2608.23565
published: '2026-08-23'
collected: '2026-08-25'
category: Agent
direction: Agent 交互式世界模型优化
tags:
- World_Model
- KV_Cache
- LoRA
- Interactive_Agent
- Memory_Optimization
one_liner: 通过训练控制-记忆解耦、推理定长KV缓存优化，实现长时序低延迟交互式世界生成
practical_value: '- 电商3D虚拟卖场、虚拟试穿等Agent交互场景可复用「定长KV缓存+姿态索引landmark检索+冗余度淘汰」方案，解决长时序交互OOM、场景记忆丢失问题

  - 多目标训练冲突场景（如生成质量/响应速度/记忆一致性兼顾）可借鉴「混合注意力窗口+随机头路由」方案，能力不绑定特定头，部署无需拆分模块，降低工程复杂度

  - 需兼顾高保真和低延迟的生成场景，可复用「主模型冻结+仅LoRA做少步蒸馏」方案，一套底座同时支持高保真多步、实时低延迟两种模式，无需维护两套模型

  - 多源异构数据训练统一交互模型时，可借鉴「全局度量尺度对齐+回文轨迹增强」方法，解决动作映射不一致、长程记忆缺乏监督的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
交互式世界模型需同时满足动作跟随精准、长程场景记忆一致、实时流式生成三个核心要求，但三者存在结构性矛盾：控制需要短上下文窗口响应实时指令，记忆需要无边界长窗口存储历史场景，现有方案联合训练时会出现控制精度提升但记忆一致性下降的问题，且推理时KV缓存随时序线性增长极易OOM，无法支撑分钟级长交互。

### 方法关键点
- 训练解耦：采用混合注意力窗口+随机头路由设计，18个本地头仅关注最近12帧学习控制能力，6个全局头关注全历史学习记忆能力，每步随机切换全局头集合，避免能力绑定特定头，部署时所有头共享统一缓存即可
- 记忆优化：训练时随机丢弃历史KV块，让模型适配稀疏非连续上下文；推理时用固定大小为12的KV缓存，仅保留锚点块、最近5个块、按当前姿态检索的6个landmark块，老化块按移动距离阈值存入landmark库，满库时淘汰姿态最冗余的块，缓存大小不随时序增长
- 工程&数据优化：仅用LoRA做4步分布匹配蒸馏，主模型冻结，一套底座同时支持高保真多步、实时低延迟两种模式；构建8源多模态数据集，统一度量尺度对齐，加入回文轨迹提供重访监督

### 关键结果
对比6个SOTA交互式世界模型，旋转误差低至11.95°，控制保真度最优；64s长时序重访任务中，固定12块缓存仍能准确复现初始视角，而滑动窗口方案早已丢失历史、全量KV缓存已OOM；VBench视频质量综合得分0.850，位列第一。

### 核心结论
多目标能力联合训练存在冲突时，优先在训练阶段做能力解耦而非推理阶段做模块拆分，可大幅降低部署复杂度同时保留核心性能。
