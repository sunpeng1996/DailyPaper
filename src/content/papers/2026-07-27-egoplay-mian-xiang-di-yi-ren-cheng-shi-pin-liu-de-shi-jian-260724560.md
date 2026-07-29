---
title: 'EgoPlay: Event-Triggered Video Editing for Egocentric Streams'
title_zh: EgoPlay：面向第一人称视频流的事件触发式编辑方法
authors:
- Jinjie Mai
- Gordon Guocheng Qian
- Willi Menapace
- Arpit Sahni
- Chaoyang Wang
- Ashkan Mirzaei
- Runjia Li
- Sergey Tulyakov
- Bernard Ghanem
- Peter Wonka
affiliations:
- Snap Inc.
- King Abdullah University of Science and Technology (KAUST)
arxiv_id: '2607.24560'
url: https://arxiv.org/abs/2607.24560
pdf_url: https://arxiv.org/pdf/2607.24560
published: '2026-07-27'
collected: '2026-07-29'
category: Other
direction: 第一人称视频 · 事件触发式生成编辑
tags:
- Video Editing
- Diffusion Transformer
- Egocentric Video
- Event Detection
- Generative AI
one_liner: 提出端到端事件触发第一人称视频编辑模型，效果超SOTA且显存占用减半
practical_value: '- 端到端融合事件检测+下游生成任务的架构思路，可迁移到电商触发式营销场景（如用户浏览行为触发优惠券/专属文案生成），相比级联方案降本提效

  - 分维度评估方案可复用：将触发准确性、触发生成质量、误触发鲁棒性拆分评估，适合推荐/广告系统的触发式投放效果评测

  - 流式分块推理的因果变体设计，可借鉴到实时推荐、AR电商场景的低延迟触发式内容生成链路'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有第一人称视频编辑方案多采用级联事件检测器+编辑器的架构，显存占用高、时序一致性差，缺少针对指定事件触发的定向编辑能力，且缺乏适配触发场景的评估体系。

### 方法关键点
1. 构建106K规模的事件触发剪辑-提示对数据集，覆盖正触发、虚构负触发、多事件三类场景；
2. 微调预训练V2V扩散Transformer，端到端联合学习事件识别、时序约束、像素级编辑能力，原生支持多事件、负触发类提示；
3. 设计因果推理变体支持逐块流式推理，配套提出事件感知评估协议，分别评估触发前内容保留、触发后编辑质量、误触发鲁棒性三个维度。

### 关键结果数字
在Ego4D基准上，编辑质量、视觉质量、背景一致性指标相对SOTA基线EgoEdit分别提升17.7%、16.9%、16.4%；相对VLM引导的级联基线分别提升15.7%、14.5%、13.5%，同时显存占用不到级联方案的1/2。
