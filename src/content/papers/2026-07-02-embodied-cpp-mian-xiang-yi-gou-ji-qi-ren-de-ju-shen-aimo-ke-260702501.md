---
title: 'Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous
  Robots'
title_zh: Embodied.cpp：面向异构机器人的具身AI模型可移植推理运行时
authors:
- Ling Xu
- Chuyu Han
- Borui Li
- Hao Wu
- Shiqi Jiang
- Ting Cao
- Chuanyou Li
- Sheng Zhong
- Shuai Wang
affiliations:
- 东南大学
- 南京大学
- Microsoft Research
- 清华大学人工智能产业研究院(AIR)
arxiv_id: '2607.02501'
url: https://arxiv.org/abs/2607.02501
pdf_url: https://arxiv.org/pdf/2607.02501
published: '2026-07-02'
collected: '2026-07-05'
category: Other
direction: 具身AI · 跨异构设备推理运行时
tags:
- Embodied_AI
- Inference_Runtime
- Heterogeneous_Hardware
- VLA
- Edge_Deployment
one_liner: 提出分层架构的C++具身模型推理运行时，解决异构边缘设备部署碎片化、延迟高问题
practical_value: '- 低延迟batch-1推理优化方案可直接复用在端侧实时推荐、端侧Agent的响应场景，降低端上推理延迟

  - 5层模块化部署架构可迁移到多模态推荐模型的跨端部署框架设计，大幅减少多设备适配的胶水代码量

  - 内存压缩优化方法可复用在边缘设备部署的轻量LLM、小参数量推荐模型，降低硬件资源门槛'
score: 4
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有具身AI（VLA、WAM）部署依赖模型专属Python栈，碎片化严重；通用推理运行时面向请求响应服务设计，无法满足闭环控制多速率执行、异构硬件低延迟batch-1推理、自定义扩展I/O接口的具身部署需求。
### 方法关键点
抽象VLA、WAM两类具身模型的共享执行路径，设计5层模块化架构：输入适配器、序列构建器、主干执行器、头插件、部署适配器，支持多速率执行、低延迟融合推理、算子与I/O扩展，通过统一后端抽象兼容异构设备、机器人、模拟器。
### 关键结果数字
在HY-VLA、pi0.5两个VLA模型上部署的闭环任务成功率分别达100.0%、91.0%；WAM基准测试中Transformer块内存从312.2 MiB降至88.1 MiB，部署效率提升的同时保持模型精度无损。
