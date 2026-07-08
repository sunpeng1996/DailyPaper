---
title: Parallelized Autoregressive Decoding for Omni-Modal Dense Video Captioning
title_zh: 面向全模态密集视频字幕生成的并行自回归解码方法
authors:
- Wenzheng Zeng
- Siyi Jiao
- Chen Gao
- Hwee Tou Ng
- Mike Zheng Shou
affiliations:
- National University of Singapore
arxiv_id: '2607.02963'
url: https://arxiv.org/abs/2607.02963
pdf_url: https://arxiv.org/pdf/2607.02963
published: '2026-07-03'
collected: '2026-07-08'
category: Multimodal
direction: 多模态生成 · 并行自回归解码优化
tags:
- Parallel Decoding
- Dense Video Captioning
- Multimodal LLM
- Autoregressive Generation
- Causal Dependency Graph
one_liner: 通过重构跨事件因果依赖图实现全模态密集视频字幕无损并行解码，同步提升效率与生成性能
practical_value: '- 做短视频/直播商品文案批量生成场景时，可借鉴跨弱依赖事件并行解码思路，同一视频下不同商品片段的描述可并行生成，大幅提升推理效率

  - 生成式推荐多候选item文案批量生成任务，可复用因果依赖图重构方法，对无依赖的item文案实现无损并行解码，降低推理成本

  - 多模态Agent处理长时序多事件理解任务时，可引入latent global planning模块预提取事件间因果关系，平衡全局感知与局部语义一致性'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
自回归视频大模型生成密集字幕采用逐token解码范式，推理效率随视频长度、事件密度上升急剧下降，扩展性受限，且难以兼顾全局事件因果关联与局部语义一致性。
### 方法关键点
基于跨时间独立事件的弱局部依赖重构因果依赖图，实现无损并行生成：跨事件弱依赖token并行解码，同事件内强耦合token保留串行解码维持语义连贯；配套两个核心组件：
1. 隐式全局规划模块：自动学习事件级结构，生成编码全局事件因果的紧凑token，自适应聚合事件级音视频语义，指导依赖重构与并行解码
2. 事件因子化并行解码机制：平衡局部语义聚焦与全局事件感知
### 关键结果
多基准测试中，全模态事件定位与字幕生成任务的效率、性能均显著优于现有基线方案
