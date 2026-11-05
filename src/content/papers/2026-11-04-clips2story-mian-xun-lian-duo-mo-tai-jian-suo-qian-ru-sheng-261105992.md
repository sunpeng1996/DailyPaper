---
title: 'Clips2Story: Training-Free Video Storyboarding and Editing Using Multimodal
  Retrieval-Embedded Generation'
title_zh: Clips2Story：免训练多模态检索嵌入生成的视频分镜创作框架
authors:
- Junnuo Wang
- Weihan Xu
- Hao-Wen Dong
affiliations:
- New York University
- University of Washington
- University of Michigan
arxiv_id: '2611.05992'
url: https://arxiv.org/abs/2611.05992
pdf_url: https://arxiv.org/pdf/2611.05992
published: '2026-11-04'
collected: '2026-11-05'
category: Multimodal
direction: 多模态视频编辑 · LLM检索生成结合
tags:
- Multimodal Generation
- Video Editing
- Training-Free
- Retrieval-Augmented Generation
- LLM Agent
one_liner: 免训练LLM驱动框架支持从无序视频片段库按用户关键词生成连贯可编辑分镜
practical_value: '- 免训练多模态素材组装范式可直接复用在电商商品短视频自动剪辑场景：将商品素材片段、用户评论、卖点文本统一映射为文本描述符，用LLM按推广关键词生成剪辑脚本，降低短视频生产门槛

  - 「关键词检索预过滤候选集+LLM排序规划」的两段式架构可迁移到长尾内容推荐场景：先通过语义召回缩小候选池，再用LLM做个性化序列编排，平衡效果与推理成本

  - 多模态素材的文本化代理表示方法可复用在跨模态推荐的特征对齐环节：将非文本模态（视频、图片、音频）统一转换为结构化文本描述，降低LLM处理多模态内容的复杂度

  - 面向非结构化素材库的序列规划评估指标（OPC、KR）可直接复用在个性化Feed流的效果评估环节，衡量序列连贯性与主题匹配度'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
现有视频编辑/摘要方法依赖有序输入视频，无法支持从无序碎片化素材库按用户自定义主题生成全新叙事的视频，而专业视频编辑人工筛选编排素材成本极高，免训练的AI辅助剪辑方案存在明显缺口。

### 方法关键点
- 多模态描述符提取：对每个视频片段用WhisperX提取语音转录、BLIP生成中间帧字幕、GroundingDINO+CLIP提取实体和背景信息，统一转为结构化文本描述
- 关键词导向候选检索：用Sentence-Transformer计算关键词与片段文本描述的相似度，召回总时长15分钟以内的候选集，降低LLM上下文压力
- 双Pipeline设计：Narration-Free版仅做片段选择排序，适合粗剪；Narration-Driven版生成过渡 narration 并匹配对应素材，提升叙事连贯性
- 全流程免训练，所有组件均用开源预训练模型，输出可编辑分镜支持人工干预

### 关键实验
基于100条跨5类体裁的长视频构造合成评估数据集，将原视频切分打乱为无序片段库，对比A2Summ、TeaserGen、REGen三个基线；客观指标上Clips2Story-ND的关键词相关性（KR-Narration）比基线最高提升38.9%，Clips2Story-NF的顺序保留系数（OPC）达0.56是基线的3倍以上；人工评估中Clips2Story-ND在叙事连贯性、关键词匹配度、真实感上均显著优于REGen，5分制下得分分别达4.43、4.42、4.28。

### 核心结论
将非结构化多模态素材统一转换为文本代理表示，用「检索过滤+LLM规划」的免训练范式，可低成本实现复杂的序列编排类任务，无需端到端微调。
