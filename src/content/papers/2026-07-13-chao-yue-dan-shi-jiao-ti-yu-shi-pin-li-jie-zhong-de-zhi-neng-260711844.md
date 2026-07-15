---
title: 'Beyond the Single Camera: Agentic Multi-View Reasoning in Sports Video Understanding'
title_zh: 超越单视角：体育视频理解中的智能体多视角推理方案
authors:
- Kerui Chen
- Jinglu Wang
- Xiaoyi Zhang
- Yan Lu
affiliations:
- Zhejiang University
- Microsoft Research Asia
arxiv_id: '2607.11844'
url: https://arxiv.org/abs/2607.11844
pdf_url: https://arxiv.org/pdf/2607.11844
published: '2026-07-13'
collected: '2026-07-15'
category: Agent
direction: 多模态Agent · 多视角视频理解推理
tags:
- MLLM
- Agent
- Multimodal
- Video Understanding
- Benchmark
one_liner: 提出多视角体育视频理解基准与主动选源Agent推理框架，相对最强基线提升14.46%
practical_value: '- 多源互补信息场景可复用「主动选源→工具调用→证据链推理」的Agent迭代架构，可迁移到电商商品多模态内容（主图/详情图/短视频）理解、多渠道用户行为融合等任务

  - 垂直领域评测集构建可复用「LLM生成标注→MLLM校验→人工过滤」三级流水线，在控制人力成本的前提下保证标注一致性与质量

  - 多模态推理系统优化可参考结论：优先解决细粒度感知、主动信息选择瓶颈，而非堆砌逻辑推理/领域知识库，可指导电商内容审核、短视频理解等系统迭代'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有MLLM在单视角视频理解任务表现优异，但体育视频存在遮挡密集、运动快速、交互复杂等问题，单视角难以精准分析，且业界缺乏专门的多视角体育视频理解评测基准。
### 方法关键点
1. 构建SportMV-Bench：通过LLM生成标注、MLLM校验、人工过滤的流水线，共包含787组多视角视频包、2592条问答对，覆盖感知识别、规则事件解读、判罚推理三类任务
2. 提出SportMV-Agent框架：迭代执行主动视角选择、感知工具调用、证据支撑推理三个步骤，解决现有MLLM多视角信息利用不足的问题
### 关键结果
- 现有MLLM的多视角推理瓶颈在细粒度视觉感知、视角选择能力，而非逻辑推理或领域知识
- 提出的Agent框架相对最强MLLM基线获得14.46%的相对性能提升
