---
title: 'EviRover: Reinforcing Agentic Perception Beyond a Glance'
title_zh: EviRover：支持主动证据检索的多模态感知智能体
authors:
- Kaixuan Fan
- Kaituo Feng
- Tianshuo Peng
- Yilei Jiang
- Manyuan Zhang
- Junke Wang
- Xiangyu Yue
affiliations:
- MMLab, The Chinese University of Hong Kong
- Fudan University
arxiv_id: '2609.40230'
url: https://arxiv.org/abs/2609.40230
pdf_url: https://arxiv.org/pdf/2609.40230
published: '2026-09-29'
collected: '2026-10-01'
category: Agent
direction: 多模态感知Agent · 主动证据检索
tags:
- Multimodal Agent
- Reinforcement Learning
- SFT
- Visual Perception
- Tool Use
one_liner: 基于SFT+RL训练的首个主动检索图像内外证据的多模态感知Agent，4B参数追平头部闭源模型
practical_value: '- 电商细粒度商品识别、同款检索、图像小目标检测场景，可复用其「局部放大裁剪+外部多模态搜索」的工具链设计，替代单步MLLM预测，降低识别幻觉

  - 多模态Agent训练可复用两阶段范式：先SFT学习工具调用格式与基础交互逻辑，再用GRPO做RL优化，奖励直接对齐业务最终指标（如识别准确率、匹配度），效果优于人工prompt编排

  - 训练难例构造可复用多跳实体替换方法，将简单直接的用户query改写为需要多步检索的复杂query，提升模型处理真实场景复杂需求的能力

  - Agent RL训练可直接复用「序列平均token均值」的损失聚合trick，避免长交互轨迹权重过高，解决多步场景下的梯度偏差问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统视觉感知默认采用单步一次性预测范式，假设输入图像内容与模型参数知识足以解决查询，但真实场景中大量存在证据不足的情况：要么目标占比极低（<0.1%）无法看清，要么需要外部领域/时效性知识才能识别，现有方法要么依赖人工设计prompt调用工具，泛化性差，要么仅能支持单一感知任务，无法适配复杂需求。

### 方法关键点
- 数据层面：设计两类数据生成 pipeline，分别覆盖「图像内证据不足（小目标、找不同、I-spy场景）」和「需外部知识（群体人物识别）」场景，通过多跳实体替换将简单query改写为需要检索的难例，产出EviRover-SFT-5K、EviRover-RL-12K训练集，以及人工校验的688实例EviLens基准。
- 训练层面：采用两阶段范式，先基于Qwen3-VL-4B做SFT，学习10种工具（局部裁剪放大、多模态搜索、SAM3分割、Python解释器等）的调用逻辑；再用EMA-GRPO做RL优化，奖励直接对齐感知任务最终指标，损失采用序列平均聚合避免长轨迹权重偏差。

### 关键结果
- EviLens基准上较backbone平均提升30个点，4B参数性能追平Gemini-3.5-Flash、Seed-2.1-Turbo等头部闭源模型。
- WebEyes基准上grounding IoU达40，超过所有对比模型，分割gIoU较8B参数的Pixel-Searcher高10.4。
- 泛化性优异：常规感知基准RefCOCOg、ReasonSeg全指标涨点，BrowseComp-VL准确率从9.5提升至24.8，涨幅超160%。

> 最值得记住的结论：感知无需局限于单次输入的信息，让模型学会主动判断何时、如何获取缺失证据，不仅能提升感知精度，还能泛化到更广泛的多模态推理任务
