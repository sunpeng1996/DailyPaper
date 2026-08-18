---
title: 'VideoGAIA: A Benchmark for General AI Assistants on Agentic Video Understanding'
title_zh: VideoGAIA：面向通用AI助手的智能体视频理解基准
authors:
- Fan Zhang
- Guangming Yao
- Jinyang Wu
- Hao Wu
- Zheng Lian
- Xinyu Geng
- Jingdong Chen
- Yi Yuan
- Pheng-Ann Heng
affiliations:
- The Chinese University of Hong Kong
- Ant Group
- Tsinghua University
- Tongji University
- The Hong Kong University of Science and Technology
arxiv_id: '2608.14718'
url: https://arxiv.org/abs/2608.14718
pdf_url: https://arxiv.org/pdf/2608.14718
published: '2026-08-11'
collected: '2026-08-18'
category: Agent
direction: 多模态Agent · 视频理解评测
tags:
- Multimodal Agent
- Video Understanding
- Benchmark
- Tool Use
- MLLM Evaluation
one_liner: 推出多轮工具增强的agentic视频理解基准，20款前沿MLLM准确率均不足60%
practical_value: '- 做电商商品短视频解析Agent时，可复用该基准的工具调用框架：搭配「视频片段重查+网页检索+内容提取」三类工具，解决单轮视频理解无法覆盖的跨模态信息补全需求（比如从短视频里识别商品型号再查参数）

  - 多模态Agent的评测体系可参考其质量控制pipeline：先用模型粗筛任务，再用3轮人工标注校验，同时做单模态消融（仅用视频/仅用文本能解的任务直接剔除），保证评测样本的有效性

  - 优化视频Agent时可优先解决视频感知错误：该基准显示36.8%-48%的错误来自视觉锚点识别错误，电商场景下可针对性优化商品logo、型号、规格的OCR+视觉识别融合模块，降低上游错误传导'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有单轮视频理解基准已接近饱和，前沿MLLM在Video-MME等榜单上准确率接近90%，无法满足下一代多模态智能体的能力评估需求；当前视频智能体的开发与评测缺乏统一、高难度的真实场景测试集，难以衡量模型多轮交互、工具调用、跨模态信息整合的实际能力。
### 方法关键点
- 采用人机协同构建数据集：从10万条公开视频出发，经过帧级字幕生成、锚点提取、任务生成、多轮质量控制，每个任务经过3名专家独立校验，最终保留271条高质量样本
- 任务设计要求至少2个视频锚点、3步推理、2次工具调用，必须同时依赖视频证据与外部网络信息，剔除仅用单模态/世界知识可解的样本，覆盖文化、地理、日常生活等6大类真实场景
- 采用统一ReAct框架评测：提供网页搜索、页面内容提取、视频片段重查三类工具，每轮仅允许调用1次工具，最多40步交互，采用语义匹配的自动判分规则
### 关键实验结果
评测20款前沿MLLM，最高准确率仅58.3%（Seed2.0-Pro），远低于传统单轮视频理解基准的性能；错误分析显示36.8%-48%的错误来自视频感知环节，其次是网页检索（20.3%-31%）与证据推理（14.2%-28.6%），工具调用数量与准确率无正相关，盲目增加调用次数不会提升效果。
> 最值得记住的结论：通用模型能力的提升不会自动转化为可靠的多模态工具使用能力，视频智能体的核心瓶颈是细粒度视频grounding、定向检索与跨源信息融合的协同优化
