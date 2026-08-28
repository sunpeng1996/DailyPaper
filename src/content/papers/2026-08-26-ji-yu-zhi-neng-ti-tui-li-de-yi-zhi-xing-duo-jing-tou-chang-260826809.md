---
title: 'Thinking on Shots: Consistent Multi-Shot Video Editing with Agentic Reasoning'
title_zh: 基于智能体推理的一致性多镜头长视频编辑方法
authors:
- Chenyang Wu
- Fuchen Long
- Binyuan Huang
- Xinlong Sun
- Xi Chen
- Chun-Le Guo
- Chongyi Li
affiliations:
- 南开大学计算机学院VCIP
- 腾讯在线视频BU智能创作平台部
arxiv_id: '2608.26809'
url: https://arxiv.org/abs/2608.26809
pdf_url: https://arxiv.org/pdf/2608.26809
published: '2026-08-26'
collected: '2026-08-28'
category: Agent
direction: Agent 多模态长内容编辑优化
tags:
- LLM
- VLM
- Agent
- Video Editing
- Evaluation Benchmark
one_liner: 提出面向多指令多镜头长视频编辑的智能体框架及配套评测基准，效果超现有闭源SOTA
practical_value: '- 处理长序列多指令任务时，可借鉴基于LLM+VLM协同的细粒度分段（替代固定时长分段）思路，避免实体碎片化和时序一致性问题，适配长视频商品种草剪辑、直播切片自动编辑场景

  - 多模态多任务评测体系设计可复用：针对复杂多指令任务，从一致性、指令匹配度、原始结构破坏度三个维度设计评估指标，适配AIGC内容生产的效果校验

  - 多指令解耦的智能体工作流可迁移至多轮用户意图的内容生成场景，比如电商个性化短视频批量生成、按用户要求定制广告素材的Agent链路'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有生成式视频编辑方法仅支持单镜头/短视频剪辑，长视频多指令编辑采用固定时长分段会导致实体碎片化、编辑幻觉、时序连续性断裂问题，缺乏统一任务定义与评测基准。
### 方法关键点
1. 定义多指令多镜头长视频编辑（MMLVE）任务，核心目标为跨镜头编辑一致性、多指令解耦、时空结构零破坏；
2. 推出MMLVE-Agent框架，通过LLM与VLM协同实现镜头级视频解耦、精准指令解析；
3. 构建含真实复杂时空动态、高密度异质指令的MMLVE-Bench评测数据集，配套3项专属评估指标。
### 关键结果
MMLVE-Agent性能优于现有闭源SOTA方法Seedance 2.0，可消除编辑幻觉，保障跨镜头编辑一致性，实现无缝时空过渡。
