---
title: Bridging VideoQA and Video-Guided Agentic Tasks via Generalized Keyframe Extraction
title_zh: 通过通用关键帧提取桥接视频问答与视频引导智能体任务
authors:
- Sunqi Fan
- Qingle Liu
- Runqi Yin
- Meng-Hao Guo
- Shuojin Yang
affiliations:
- Tsinghua University
arxiv_id: '2606.29445'
url: https://arxiv.org/abs/2606.29445
pdf_url: https://arxiv.org/pdf/2606.29445
published: '2026-06-27'
collected: '2026-06-30'
category: Agent
direction: 视频理解 · GUI Agent 关键帧提取
tags:
- Keyframe Extraction
- VideoQA
- GUI Agent
- Multimodal LLM
- Agentic Tasks
one_liner: 推出新基准VG-GUIBench，提出兼顾任务与场景的TASKER通用关键帧提取算法
practical_value: '- 做直播/短视频内容理解类多模态Agent时，关键帧提取可复用TASKER思路：同时建模任务相关性+场景动态，在降低KV cache计算量的同时提升效果

  - 针对视频引导的GUI操作类Agent（比如智能界面操作助手），可复用VG-GUIBench作为测评基准，评估模型从教程学习技能的泛化能力

  - 通用关键帧提取可同时适配多类视频下游任务，无需针对不同任务单独开发模块，降低工程落地成本'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有Multimodal Large Language Models（MLLMs）在VideoQA基准已取得不错效果，但现有评估仅聚焦浅层次视觉感知能力，极少检验MLLM能否从视频教程学习深层知识、流程技能，并泛化到长周期下游agentic任务；同时发现VideoQA与视频引导agent任务的性能都高度依赖有效的关键帧提取，现有方法缺乏兼顾任务与场景的通用设计。

**方法关键点**：1. 构建新基准VG-GUIBench，专门用于评估MLLM-based GUI agents遵循视频教程完成GUI交互任务的能力；2. 提出TASKER关键帧提取算法，联合建模任务相关性与场景动态，筛选高信息含量的关键帧。

**关键结果**：TASKER在多个公开基准取得显著提升，在EgoSchema fullset超出最优基线2.0%，在NExT-QA超出最优基线1.8%，验证了通用关键帧提取对多类视频理解任务的增益。
