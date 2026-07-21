---
title: 'TimeLens2: Generalist Video Temporal Grounding with Multimodal LLMs'
title_zh: TimeLens2：基于多模态大模型的通用视频时序定位框架
authors:
- Yuhan Zhu
- Changlian Ma
- Xiangyu Zeng
- Xinhao Li
- Zhiqiu Zhang
- Songze Li
- Jun Zhang
- Tianxiang Jiang
- Yuandong Yang
- Ziang Yan
affiliations:
- 南京大学
- 上海人工智能实验室
- 上海交通大学
- 浙江大学
- 中国科学技术大学
arxiv_id: '2607.17423'
url: https://arxiv.org/abs/2607.17423
pdf_url: https://arxiv.org/pdf/2607.17423
published: '2026-07-18'
collected: '2026-07-21'
category: Multimodal
direction: 多模态大模型·视频时序定位
tags:
- MLLM
- Video Temporal Grounding
- Wasserstein Reward
- Weak Annotation
- Reinforcement Learning
one_liner: 提出时序证据区间集优化范式，性能超同规模及397B参数级开源视频时序定位基线
practical_value: '- 电商种草视频检索、短视频内容推荐场景可复用temporal Wasserstein reward设计，解决预测片段与标注数量不匹配的优化、评估问题

  - 弱标注视频数据集构建可复用TimeLens2-93K的pipeline：字幕生成候选+独立定位+跨Agent共识+语义校验+边界修正，大幅降低人工标注成本

  - 多模态搜索推荐系统做视频片段召回时，可复用区间集建模思路，适配任意长度多模态视频的query时序定位需求'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有视频MLLM仅能输出视频内容描述，无法准确定位对应事件的发生时间区间，现有训练策略与时序定位的集合值任务存在错位：长视频单轮标注鲁棒性差，强化学习奖励无法适配预测、标注片段数量不一致的场景。
### 方法关键点
1. 全流程将时序证据作为区间集开展监督与优化；
2. 构建TimeLens2-93K数据集，通过字幕生成候选、独立定位、跨Agent共识、语义校验、边界修正五步生成可靠多跨度标注；
3. 设计时序Wasserstein奖励，计算合并区间均匀分布的一维W1距离，提供无需片段匹配的密集反馈，搭配temporal IoU补充重叠度精准反馈。
### 关键结果
2B/4B/8B版本分别较Qwen3-VL基线提升14.2/13.0/18.1 mIoU，8B版本达到SOTA，超过参数规模达397B的开源模型，7个基准测试均优于同规模基线。
