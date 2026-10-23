---
title: 'ProactEgoMem: Benchmarking Proactive Memory in Streaming Egocentric Video'
title_zh: ProactEgoMem：流式第一视角视频主动记忆能力评测基准
authors:
- Ruotong Liao
- Meikel Kokowski
- Xiaoxiao Sun
- Yongqin Xian
- Laura Bravo Sánchez
- Shiye Su
- Federico Tombari
- Serena Yeung-Levy
- Volker Tresp
affiliations:
- LMU Munich
- Stanford University
- Google
- Technical University of Munich
arxiv_id: '2610.30089'
url: https://arxiv.org/abs/2610.30089
pdf_url: https://arxiv.org/pdf/2610.30089
published: '2026-10-21'
collected: '2026-10-23'
category: Agent
direction: 多模态主动Agent · 记忆能力评测
tags:
- Proactive Agent
- Multimodal Agent
- Video Agent
- Benchmark
- Egocentric Video
one_liner: 推出流式第一视角视频主动记忆评测基准ProactEgoMem，覆盖双场景3类任务与两级主动度评测协议
practical_value: '- 主动记忆触发逻辑可迁移到电商穿戴式导购Agent：实时识别用户浏览商品的关键行为触发记忆存储，无需用户主动提问

  - 双等级主动度评测协议可复用：电商场景可拆分「仅触达通知」/「全流程主动代操作」两个等级评估Agent主动服务效果

  - 三类记忆任务框架可复用：信息流/直播场景可参考拆分信息捕获、状态追踪、位置追踪三类需求设计记忆模块'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态助手均为被动响应式，无法为用户长期主动记录环境信息、减轻长时记忆负担，缺乏流式第一视角场景下主动记忆能力的标准化评测基准。
### 方法关键点
1. 构建ProactEgoMem基准，覆盖3类核心任务：瞬态视觉信息捕获、物体状态追踪、物体位置追踪；
2. 设计双等级主动度评测协议：Notification Level仅要求按时触发符合用户意图的通知，Intervention Level要求Agent自主完成全生命周期的记忆维护；
3. 包含日常/科研两个赛道，共400条视频片段，配套1500道QA题验证记忆质量。
### 关键结果数字
所有参测的闭源、开源、视频语言、流式基线模型，均无法同时满足主动记忆的时效性与准确性要求。
