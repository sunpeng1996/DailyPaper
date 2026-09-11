---
title: 'A Voice-Interactive Multi-Agent System for Smart Operating Rooms: Architecture
  Design and Key Technologies'
title_zh: 面向智能手术室的语音交互多智能体系统架构设计与关键技术
authors:
- Tianxiang Zhou
affiliations:
- Wuhan United Imaging Surgical Co., Ltd. (UIS)
arxiv_id: '2609.11231'
url: https://arxiv.org/abs/2609.11231
pdf_url: https://arxiv.org/pdf/2609.11231
published: '2026-09-10'
collected: '2026-09-11'
category: Agent
direction: Agent 实时交互架构与性能优化
tags:
- Multi-Agent
- KV Cache
- LLM Inference Optimization
- Voice Interaction
- Task Planning
one_liner: 提出适配手术室低时延要求的语音交互多智体系统，融合多项推理优化技术实现实时多设备控制
practical_value: '- KV Cache前缀预热优化可直接复用在推荐/广告端实时Agent服务：将动态参数置于prompt末尾，通过字节级LCP复用缓存，状态变更场景下可将prefill时延从数百ms降至几十ms

  - 流式局部JSON解析+提前执行设计可迁移到电商导购Agent、搜索实时query理解场景：无需等LLM完整输出，检测到完整任务/意图字段即可启动下游执行，端到端时延降低约30%

  - 渐进式技能prompt披露适配短上下文模型场景：按用户角色、当前场景、可用功能动态过滤冗余prompt，可节省15%-20%token占用，缓解上下文膨胀

  - DAG任务调度+拓扑排序逻辑可复用在多工具调用Agent系统：支持带依赖的多任务自动分层并行，总执行时间从多任务累加变为最长单任务耗时'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
传统手术室设备控制依赖物理按键、触控屏，存在无菌区污染风险、操作延迟、多设备协调难等痛点，现有LLM驱动的医疗语音助手未针对实时交互做低时延优化，无法满足毫秒级设备控制要求。
### 方法关键点
- 分层架构设计：拆分语音交互流水线与Agent核心模块，语音流水线支持唤醒、ASR、LLM推理、TTS全链路实时处理，Agent核心内置技能注册、任务规划、设备管理等能力
- KV Cache前缀预热：将用户输入字段置于prompt末尾，通过字节级LCP复用预计算的公共前缀缓存，仅增量计算用户输入部分
- 流式局部JSON解析：LLM输出过程中实时检测完整任务数组，无需等待全量输出即可启动并行任务执行
- 渐进式技能prompt披露：按用户角色、可用设备、当前场景三层过滤冗余prompt内容，压缩token占用
- DAG任务调度：基于Kahn拓扑排序实现无依赖任务并行执行，DFS三色法检测循环依赖
### 关键结果
基于Qwen3-27B-FP8模型、16384 token上下文窗口部署：
- 设备状态变更场景prefill开销从~500ms降至50-80ms，优化幅度83%-90%
- 首token时延从~600ms降至150-200ms，优化幅度67%-75%
- 流式提前执行降低端到端时延约30%，渐进式prompt披露可减少15%-20%的token消耗
### 核心经验
面向低时延要求的Agent系统，可通过工程化分层优化在不更换模型的前提下实现数倍的性能提升。
