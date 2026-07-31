---
title: 'Ripple: Real-Time Streaming Audio-Video Generation With Cross-Modal Recurrent
  Memory'
title_zh: Ripple：带跨模态循环记忆的实时流式音视频生成系统
authors:
- Yanbo Ding
- Zhizhi Guo
- Quanyue Song
- Yishan He
- Zhixiang He
- Yongxiang Li
- Yali Wang
affiliations:
- 中国科学院深圳先进技术研究院
- 中国电信人工智能科技（北京）有限公司
- 上海人工智能实验室
- 中国科学院大学
- 西安交通大学
arxiv_id: '2607.26818'
url: https://arxiv.org/abs/2607.26818
pdf_url: https://arxiv.org/pdf/2607.26818
published: '2026-07-29'
collected: '2026-07-31'
category: Multimodal
direction: 跨模态生成 · 流式推理优化
tags:
- Streaming Generation
- Cross-Modal
- Recurrent Memory
- Knowledge Distillation
- Reinforcement Learning
one_liner: 提出带跨模态循环记忆的流音视频生成框架，实现低延迟长序列生成，速度超教师模型15倍
practical_value: '- 流式推理的滑动窗口+模态专属记忆架构可迁移到长视频/直播流实时内容生成场景，大幅降低生成延迟

  - 三阶段训练范式可复用在大模型流式推理轻量化改造任务，平衡推理效率与生成质量

  - 跨模态记忆交互机制可借鉴到电商商品展示音视频生成、直播数字人音画同步优化场景'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有音视频生成模型延迟高，已有的流生成方案计算成本高且不支持长序列生成，无法适配实时应用场景。
### 方法关键点
1. 架构融合定长滑动窗口注意力与模态专属循环记忆，持续聚合音视频上下文，新增跨模态记忆交互模块提升音画同步性；
2. 采用三阶段训练范式：先将双向音视频教师模型适配为带模拟记忆的块级因果注意力，再通过端到端蒸馏优化记忆构建与交互流程，最后针对流生成场景做在线强化后训练。
### 关键结果
480P分辨率下推理速度达~28FPS，比教师模型快15倍以上，长短视频基准测试性能均优于现有离线/在线音视频生成方案，支持连贯长序列生成。
