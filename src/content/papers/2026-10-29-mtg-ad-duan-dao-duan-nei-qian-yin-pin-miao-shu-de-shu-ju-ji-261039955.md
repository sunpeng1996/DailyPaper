---
title: 'Mind The Gap (MTG-AD): Dataset and Fine-grained Evaluation for End-to-End
  Inline Audio Descriptions'
title_zh: MTG-AD：端到端内嵌音频描述的数据集与细粒度评估
authors:
- Subhashini Venugopalan
- Jenny Tan
- Taylor Roper
- Jimmy Tobin
- Anton Kast
- Alicia Martin
- Sam Sepah
- Amy Pavel
affiliations:
- Google Research
- UC Berkeley
arxiv_id: '2610.39955'
url: https://arxiv.org/abs/2610.39955
pdf_url: https://arxiv.org/pdf/2610.39955
published: '2026-10-29'
collected: '2026-10-31'
category: Multimodal
direction: 多模态音频描述 · 数据集与评估
tags:
- MLLM
- Dataset
- Evaluation
- Accessibility
- Audio Description
- UGC
one_liner: 发布专业标注的内嵌音频描述数据集MTG-AD及无参考端到端细粒度评估框架
practical_value: '- 做需适配原有内容时间间隙的生成任务（如短视频插播旁白、直播间智能口播文案）时，可复用「生成内容转音频后校验时间适配性」的端到端评估逻辑，避免生成内容和原有语音重叠

  - 面向特殊人群的内容生成任务，可参考「残障领域专家+健全专家配对标注」的数据集构建方法，大幅提升标注的实际可用性

  - 无参考自动评估指标设计可借鉴「对齐专家规范+验证与用户打分相关性」的思路，降低业务侧高频评估的人力成本'
score: 7
source: arxiv-cs.HC
depth: abstract
---

### 动机
内嵌音频描述（AD）需嵌入视频原生静默间隙，是视障用户获取UGC视频信息的核心可访问性能力，但现有MLLM在该任务上的表现缺乏专业基准与可指导优化的细粒度评估体系。
### 方法关键点
1. 构建MTG-AD数据集：包含36小时视频、8k+条专业标注，由视障+明眼AD专家配对共创，覆盖多样化UGC场景
2. 提出MTG-AD-Eval无参考评估框架：端到端将生成脚本转音频后校验静默间隙适配性，基于专家规范输出多维度可落地的优化指标
### 关键结果
自动指标与明眼用户、7名视障用户的人工打分显著相关；SOTA MLLM生成的AD视觉描述准确率高、语音重叠率低，但叙事节奏流畅度仍有差距；视障用户认为MLLM生成的AD对内容理解帮助度高，仅略逊于人工创作的AD
