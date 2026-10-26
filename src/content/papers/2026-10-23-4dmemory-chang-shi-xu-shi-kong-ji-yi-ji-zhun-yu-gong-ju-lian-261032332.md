---
title: '4DMemory: Benchmarking Long-Horizon Spatiotemporal Memory with Harness-Augmented
  Agents'
title_zh: 4DMemory：长时序时空记忆基准与工具链增强Agent框架
authors:
- Yanhao Jia
- Yi Zhu
- Yiran Zhong
- Weigao Sun
- Feida Zhu
- Pengkun Jiao
- Sihan Yang
- Ming Ma
- Steven Hoi
- Erik Cambria
affiliations:
- Nanyang Technological University
- Token Foundry, Alibaba
- The Chinese University of Hong Kong
- Institute of Neuroscience, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
arxiv_id: '2610.32332'
url: https://arxiv.org/abs/2610.32332
pdf_url: https://arxiv.org/pdf/2610.32332
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: Agent 长时序多模态记忆 benchmark
tags:
- Long-Horizon Agent
- Multimodal Memory
- Benchmark
- RAG
- Tool Use
one_liner: 发布含近900小时长视频的时空推理基准，配套模型无关的记忆增强Agent工具链
practical_value: '- 可复用「任务无关预存记忆+查询触发检索」的架构：给长时序用户行为建模、直播/短视频内容理解场景提供参考，避免重复编码长序列

  - 时空推理任务的分层工具设计：视频处理、视觉定位、文本统计三类专用工具拆分的思路，可迁移到多模态商品内容理解、用户跨会话行为分析任务

  - 长时序任务的评估方法：工具调用成功率、执行顺序合规性、最终答案准确率的多层度量体系，可复用来自建Agent效果评估指标'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有大模型长上下文能力无法支撑小时级跨模态时空推理，现有长视频benchmark大多局限于1-2小时单视频，缺少跨多视频、数十小时级的记忆推理评测能力，无法有效验证多模态Agent的长时序记忆效果。

### 方法关键点
- 构建LongVideo数据集：含1025个独立长视频、2部剧集共402集，总时长887小时，最长单任务覆盖97.98小时视频，配套5214条人工标注QA，覆盖视觉、文本、时空三类推理任务
- 设计4DMemory Harness工具链：模型无关架构，分为任务无关的记忆预构建阶段（离线生成带时间戳的多模态结构化记忆）和查询触发的推理阶段（按需检索+调用三类专用工具），解耦任务时长和模型原生上下文窗口限制
- 评测体系设计：拆分工具调用率、顺序敏感准确率、顺序不敏感准确率、整体准确率4项指标，区分工具执行流程正确性和最终答案正确性

### 关键实验
评测13款SOTA闭源大模型，结果显示：原生模型在4DMemoryBench上的得分比现有同类benchmark平均低10%以上；搭配Harness后所有模型性能提升超50%；最优模型Muse Spark-1.1整体准确率达77.79%，但分布式计数类任务准确率仅47.58%，是当前Agent共通短板。

### 核心结论
长时序多模态推理的瓶颈不是模型上下文窗口长度，而是记忆存储、检索、工具调用、推理全链路的协同准确率。
