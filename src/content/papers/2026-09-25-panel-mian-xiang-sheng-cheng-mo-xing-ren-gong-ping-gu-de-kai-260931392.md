---
title: 'PANEL: An Open-Source, Self-Hosted Web Platform for Human Evaluation of Generative
  Models'
title_zh: PANEL：面向生成模型人工评估的开源自托管Web平台
authors:
- Matteo Spanio
- Andrea Poltronieri
- Martín Rocamora
affiliations:
- University of Padova
- Music Technology Group, Universitat Pompeu Fabra
arxiv_id: '2609.31392'
url: https://arxiv.org/abs/2609.31392
pdf_url: https://arxiv.org/pdf/2609.31392
published: '2026-09-25'
collected: '2026-09-28'
category: Eval
direction: 生成模型人工评估工具开发
tags:
- Human-Evaluation
- Generative-AI
- Open-Source-Tool
- LLM-Evaluation
- Model-Benchmark
one_liner: 开源可自托管的生成模型人工评估平台，支持多模态测试、自动统计分析与合规操作
practical_value: '- 做GenRec/LLM4Rec的人工偏好评估时，可直接部署PANEL替代商用问卷平台，支持文本/商品图/短视频等多模态测试素材，降低自研评估工具成本

  - 可复用其内置的pairwise win rate、Bradley-Terry score计算逻辑，不用重复开发偏好排序统计模块，直接输出A/B测试显著性结果

  - 出海业务场景可复用其GDPR适配的同意书版本管理、用户自助撤回、日志留存能力，降低用户调研类需求的合规风险'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
生成模型自动评估指标与人类感知相关性弱，人工评估是黄金标准，但现有工具存在明显短板：闭源商用平台灵活性不足，公开竞技场不支持自有模型的可控对比测试，单次自研评估工具开发成本高。

### 方法关键点
1. 浏览器端可视化配置评估任务，支持音频/视频/图像/文本多模态刺激，内置7种题型、受试者筛选、逻辑跳转能力，生成单链接即可分发测试
2. 自动输出单题统计、组间显著性检验、pairwise胜率、Bradley-Terry打分，支持预实验功效分析
3. 内置同意书版本管理、用户自助撤回、留存规则强制、审计日志等能力满足GDPR合规要求，任务可导出为机器可读格式

### 关键结果
平台已在GitHub开源，支持私有化部署，无需依赖第三方服务即可完成全链路人工评估流程
