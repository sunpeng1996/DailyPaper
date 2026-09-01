---
title: 'MNIST-PRO: MNIST is Back as a Partially Observable World for AI Agents'
title_zh: MNIST-PRO：面向AI Agent的部分可观测感知能力评测基准
authors:
- Vernon Toh
- Navonil Majumder
- Zhengyuan Liu
- Nancy F. Chen
- Soujanya Poria
affiliations:
- Nanyang Technological University, Singapore
- Agency for Science, Technology and Research (A*STAR), Singapore
arxiv_id: '2608.31022'
url: https://arxiv.org/abs/2608.31022
pdf_url: https://arxiv.org/pdf/2608.31022
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: AI Agent · 多模态感知能力评测
tags:
- Agent
- Benchmark
- Multimodal
- Perception
- POMDP
- Partial Observability
one_liner: 将经典MNIST改造为部分可观测序列感知基准，孤立评测多模态Agent的感知状态构建能力
practical_value: '- 做电商导购Agent、界面操作Agent的感知能力迭代时，可借鉴本研究的控制变量思路：先排除导航、交互等干扰，孤立评测核心的片段观测整合能力，快速定位性能瓶颈。

  - 处理片段化视觉信息场景（如用户分段上传的商品截图识别、长图商品信息提取）时，优先采用「先全量采集观测，再离线拼接视觉画布识别」的策略，比边采集边拼接的在线模式准确率高15~30个百分点。

  - Agent感知状态存储需适配任务复杂度：短序列任务保留原始视觉历史效果最优，长序列/多目标任务采用文本状态+结构化坐标网格的混合存储更能避免信息丢失。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多模态Agent评测基准要么是全观测输入无需主动感知，要么融合了导航、物理控制等复杂干扰，无法孤立定位Agent在部分可观测场景下的感知状态构建瓶颈，导致感知能力的迭代优化缺乏明确的评测依据。

### 方法关键点
- 基于经典MNIST数据集构造POMDP任务，Agent只能通过固定大小的glimpse窗口移动观测图像，需主动探索、整合片段观测、构建感知状态后输出识别结果，排除复杂3D环境的控制、导航干扰。
- 设计2级难度任务：Level 1为单数字空间整合，Level 2为多数字序列顺序识别，可灵活调整窗口大小、移动步长控制任务难度。
- 设计5类感知状态存储配置做对照：原始视觉历史、自由文本状态、结构化度量网格图、在线/离线视觉拼接画布。

### 关键结果
- 评测10款主流多模态大模型，全观测下MNIST识别准确率普遍达83%~99%，但在MNIST-PRO部分可观测场景下平均准确率仅6.5%~61%，性能落差极大。
- 离线拼接视觉画布可大幅提升准确率：例如Claude-5-Fable在Level 2任务下准确率从18%提升到69%，验证大部分失败来自观测整合而非信息采集不足。
- 带工具调用的Agent harness可让Gemini-3.7-Flash的Level 2准确率从38%提升到63%，但跨episode的持久记忆对准确率无明显增益。

### 核心结论
大模型的被动视觉识别能力不代表主动感知能力，部分可观测场景下的核心瓶颈不是信息采集，而是感知状态的有效构建与更新。
