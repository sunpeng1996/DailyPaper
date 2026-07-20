---
title: 'Audio-Visual Flamingo: Open Audio-Visual Intelligence for Long and Complex
  Videos'
title_zh: AV-Flamingo：面向长复杂视频的开放音视频智能
authors:
- Sreyan Ghosh
- Arushi Goel
- Kaousheik Jayakumar
- Lasha Koroshinadze
- Nishit Anand
- Siddharth Gururani
- Hanrong Ye
- Pritam Biswas
- Yuanhang Su
- Ehsan Hosseini-Asl
affiliations:
- NVIDIA, USA
- University of Maryland, USA
arxiv_id: '2607.16107'
url: https://arxiv.org/abs/2607.16107
pdf_url: https://arxiv.org/pdf/2607.16107
published: '2026-07-16'
collected: '2026-07-20'
category: Multimodal
direction: 多模态大模型 · 长视频音视频理解推理
tags:
- Multimodal-LLM
- Video-Understanding
- Chain-of-Thought
- Long-Context
- Cross-Modal-Reasoning
one_liner: 开源音视频大模型AV-Flamingo，支持长视频跨模态时序推理，性能优于同类开源模型
practical_value: '- 三阶段课程式训练策略可复用在长上下文多模态推荐模型训练上，从短序列感知逐步过渡到长序列行为推理，降低训练难度

  - 带时间戳的跨模态思维链推理框架可迁移到短视频/直播内容理解场景，精准定位商品出现时段、用户互动高光片段，提升内容标签准确性

  - 7M量级跨模态标注数据集构建思路可借鉴到电商直播/短视频素材标注流程，重点覆盖时序、组合类推理样本，提升模型泛化性'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有音视频大模型多聚焦短片段处理，无法适配长复杂真实场景音视频理解需求，而当前视频占全球互联网流量82%，用户日均观看时长超2.5小时，长视频跨模态推理能力存在明显缺口。
### 方法关键点
1. 构建Audio-Visual-Skills数据集，包含约7M真实视频字幕、问答训练样本，针对性覆盖时序、组合、跨模态推理任务；
2. 采用三阶段课程训练策略，从短程感知逐步进阶到长时序多事件推理，降低长序列任务训练难度；
3. 提出时序音视频交错思维链框架，将推理中间步骤与音视频流时间戳绑定，提升时序对齐能力与可解释性。
### 关键结果
在15+音视频、全模态、单模态基准上，性能显著优于同规模开源模型，部分指标超过更大规模的开源/闭源模型，长复杂场景任务优势突出。
