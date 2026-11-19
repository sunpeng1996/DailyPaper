---
title: 'RoughCut-Bench: A Benchmark for Automatic Video Rough-Cut with Large Vision-Language
  Models'
title_zh: RoughCut-Bench：面向大视觉语言模型的自动视频粗剪基准
authors:
- Ruisi Zhao
- You Li
- Sihan Chen
- Aosong Cheng
- Chixiang Ma
- Sen Pei
- Zhen Yang
- Hehe Fan
- Dongliang He
- Yi Yang
affiliations:
- Zhejiang University
- ByteDance
- Peking University
- ReLER, CCAI
arxiv_id: '2611.24098'
url: https://arxiv.org/abs/2611.24098
pdf_url: https://arxiv.org/pdf/2611.24098
published: '2026-11-17'
collected: '2026-11-19'
category: Multimodal
direction: 多模态大模型 · 视频内容生产基准
tags:
- LVLM
- Video Processing
- Benchmark
- Agentic Workflow
- Multimodal Evaluation
one_liner: 发布首个LVLM自动视频粗剪基准，配套Agent工作流与人类对齐评估体系
practical_value: '- 电商短视频内容生产场景可复用「视觉+ASR双驱动粗剪框架」，批量处理UGC素材快速生成短视频初稿，降低内容生产成本

  - 多模态内容质量评估可参考「规则标注+Agent对齐人类评估」的双轨方案，平衡自动化评估效率与主观效果一致性

  - 复杂多模态内容生成任务可采用Agentic workflow引导LVLM输出结构化可执行指令，降低输出不可控性'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
LVLM在视频相关任务进展迅速，但自动视频粗剪领域缺乏统一评估基准与成熟的可执行剪辑方案生产工作流，行业落地无参考标准。
### 方法关键点
1. 构建RoughCut-Bench，覆盖两类实用场景：视觉驱动（亮点检测、片段排序、适配用户需求）、语音驱动（填充词去除、重复表达删除、低价值内容裁剪）；
2. 基准包含101个视觉驱动案例（831条原始视频、1476个亮点标注）、84个语音驱动案例（带清理标注的ASR转录文本）；
3. 配套人类对齐的Agent化评估器，同时提出引导LVLM输出结构化剪辑方案的Agent工作流。
### 关键结果数字
实验验证当前主流LVLM生成的剪辑方案与专业人工对齐度仍有较大差距，基准已开源代码、prompt与全量数据集。
