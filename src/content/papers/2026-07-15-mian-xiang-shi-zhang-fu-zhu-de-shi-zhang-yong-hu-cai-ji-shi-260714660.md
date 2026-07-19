---
title: 'VIABench: A Comprehensive Video Benchmark Collected from Blind Individuals
  for Visual Impairment Assistance'
title_zh: 面向视障辅助的视障用户采集视频评测基准VIABench
authors:
- Yunfeng Liu
- Yuandong Yang
- Jiarui Han
- Zhenpeng Huang
- Yuqing Tang
- Xiangyu Zeng
- Gangshan Wu
- Limin Wang
affiliations:
- Nanjing University
- Shanghai AI Laboratory
arxiv_id: '2607.14660'
url: https://arxiv.org/abs/2607.14660
pdf_url: https://arxiv.org/pdf/2607.14660
published: '2026-07-15'
collected: '2026-07-19'
category: Eval
direction: 多模态大模型 · 视障场景评测基准
tags:
- Multimodal LLM
- Benchmark
- Video Understanding
- VQA
- Assistive AI
one_liner: 推出由视障群体采集的多模态大模型视障辅助场景视频评测基准，覆盖三类任务与双模式评测管道
practical_value: '- 面向特殊人群（如银发、视障用户）的多模态产品开发，可参考其核心需求拆解为可量化评测子任务的思路

  - 实时多模态Agent（如线下导购、导航Agent）开发可复用其在线实时/离线双轨评测管道设计，兼顾效果与性能评测

  - 主动式场景推送（如危险预警、导购提示）场景，可参考其前瞻性事件预判+自然语言生成的评测逻辑，量化推送时效性与相关性'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有Multimodal Large Language Models (MLLMs) 在通用多模态任务表现优异，但面向视障辅助的真实落地场景效果缺乏专项验证，缺少由视障群体自行采集的真实第一视角视频评测基准。
### 方法关键点
1. 数据集全部来自视障用户录制/分享的第一视角视频，定义三类核心评测任务：主动预判导航关键事件并生成口头提醒、视频VQA回答用户关于环境/物品的提问、视觉引导的上下文感知交互推理
2. 支持在线实时、离线两种评测管道，保证评测的公平性和鲁棒性，适配不同落地场景的评估需求
### 关键结果
现有主流MLLM尚无法为视障群体提供完整的辅助支持，其中对预判准确率、实时响应速度要求最高的主动提醒任务表现最差。
