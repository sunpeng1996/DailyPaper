---
title: 'ROWBench: Do Video Models Render What the Program Specifies?'
title_zh: PROWBench：视频生成模型是否符合程序定义的世界规则？
authors:
- Zheng-Hui Huang
- Guixu Lin
- Yu-Ju Tsai
- Jian-Kai Zhu
- Fengbo Lan
- Yu-Lun Liu
- Yung-Yu Chuang
- Kaipeng Zhang
- Zhixiang Wang
affiliations:
- Alaya Lab
arxiv_id: '2610.02205'
url: https://arxiv.org/abs/2610.02205
pdf_url: https://arxiv.org/pdf/2610.02205
published: '2026-10-01'
collected: '2026-10-03'
category: Eval
direction: 可编程世界模型 · 生成保真度评测
tags:
- Video Generation
- Benchmark
- Evaluation
- Programmable World Model
- VLM
one_liner: 提出PROWBench评测基准，可量化视频生成对程序定义世界事件的保真度
practical_value: '- 电商多模态商品/营销场景生成任务可复用「规则-渲染对齐」评测思路，用预设程序化事件校验生成结果的业务合规性，避免出现不符合商品规格、促销规则的错误生成

  - Agent交互场景的多模态轨迹生成评测可参考带时间戳的实体状态日志校验法，精准定位长序列交互中的逻辑错误

  - 可控内容生成场景可直接复用Logic-Render Alignment、Interaction Success Rate两个VLM评测指标，大幅降低人工标注成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
可编程世界模型是下一代游戏引擎的核心技术底座，现有评测仅覆盖视觉质量、可控性、物理规则一致性等维度，缺失对细粒度程序指定事件的生成保真度校验能力。
### 方法关键点
1. 构建PROWBench基准，包含170个程序构造的交互片段、600个代理视频，覆盖多场景、多交互类型，全量记录带时间戳的实体状态、跨视域事件作为可回放真值
2. 设计可扩展框架支持多模态代理表示（粗3D、bounding box等）、第一/第三人称视角、多视角同步渲染
3. 提出两个VLM驱动的自动化评测指标：Logic-Render Alignment、Interaction Success Rate，可量化生成视频与程序定义事件时序、交互逻辑的对齐度
### 关键结果
基准已开源数据集与评测框架，可有效检测生成视频的实体控制精度、长时序记忆能力、程序规则对齐度三类核心能力
