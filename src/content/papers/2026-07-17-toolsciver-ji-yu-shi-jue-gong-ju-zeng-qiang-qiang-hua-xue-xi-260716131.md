---
title: 'ToolSciVer: Multimodal Scientific Claim Verification with Visual Tool Augmented
  Reinforcement Learning'
title_zh: ToolSciVer：基于视觉工具增强强化学习的多模态科学主张验证
authors:
- Binglin Zhou
- Peng Shi
- Ryo Kamoi
- Nan Zhang
- Rui Zhang
affiliations:
- The Pennsylvania State University
- University of Waterloo
arxiv_id: '2607.16131'
url: https://arxiv.org/abs/2607.16131
pdf_url: https://arxiv.org/pdf/2607.16131
published: '2026-07-17'
collected: '2026-07-20'
category: Agent
direction: Agent 工具增强多模态事实校验
tags:
- VLM
- GRPO
- Tool Augmentation
- Reinforcement Learning
- Multimodal Reasoning
one_liner: 为VLM配备三类科学视觉专用工具，基于GRPO训练实现多模态科学主张验证最优性能
practical_value: '- 电商/广告场景中针对商品参数表、销量/转化趋势图、多图组合详情页的信息提取，可直接复用三类工具设计：表格行/列聚焦提取、图表转结构化文本、高分辨率区域放大，大幅降低VLM理解复杂视觉内容的误差

  - 训练工具调用Agent时可复用GRPO的复合奖励设计，将最终任务正确性、格式合规、工具调用效率、错误调用惩罚结合，比纯prompt工具调用的稳定性提升显著

  - 工具效率系数（OTC）的设计可直接迁移到任意工具调用Agent场景，能在不损失效果的前提下减少30%冗余工具调用，同时降低50%左右的推理token消耗，适合业务降本

  - 无需为工具调用标注大量监督数据，用GRPO的在线采样相对优势训练即可让模型学会选择合适工具，大幅降低落地的数据成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
多模态科学主张验证（MSCV）需结合论文中的表格、图表、配图与文本判断主张真伪，现有VLM普遍存在关键视觉证据定位难、结构化科学视觉内容解析误差大、多模态推理不可靠的问题；纯prompt工具调用稳定性差，通用视觉工具也不适配科学场景的定向证据提取需求，亟需专门的工具增强框架提升MSCV性能。
### 方法关键点
- 设计三类领域专属视觉工具：Table Focus基于OCR将表格转为结构化格式，支持返回指定行/列的局部证据；Chart Parse将图表内容转为JSON格式结构化文本，包含轴标签、数值、趋势等信息；Region Zoom对多面板配图指定区域做高分辨率裁剪，坐标归一化到0-1000实现分辨率无关
- 采用GRPO做策略训练，复合奖励包含5部分：答案正确性、输出格式合规性、长度惩罚、工具调用效率系数（OTC）、错误调用惩罚；其中OTC系数奖励以最少工具调用得到正确结果的轨迹，抑制冗余调用
- 单轮仅允许调用1个工具或输出最终答案，缩小动作空间，工具返回结果直接加入上下文供后续推理
### 关键实验
在SCIVER、MUSCICLAIMS两个MSCV基准数据集测试，覆盖Qwen、InternVL、Gemma三个家族共5款开源VLM，对比非工具CoT、纯prompt工具调用、VTOOL-R1、OPENTHINKIMG四个基线：平均准确率较非工具CoT高8-12pp，较纯prompt工具调用高7-10pp，较现有RL工具调用基线高2-4pp；工具调用效率提升30%，平均推理token消耗降低51%。
### 核心结论
为特定领域工具调用Agent设计专属工具套件+任务对齐的复合奖励，效果远优于直接套用通用工具+Prompt的方案。
