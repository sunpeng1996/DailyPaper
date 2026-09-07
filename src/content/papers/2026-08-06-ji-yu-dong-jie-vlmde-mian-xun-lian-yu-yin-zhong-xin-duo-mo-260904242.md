---
title: Training-Free Speech-Centric Omni Understanding with Frozen VLMs
title_zh: 基于冻结VLM的免训练语音中心多模态理解框架
authors:
- Ankan Deria
- Hanoona Rasheed
- Xilin He
- Fahad Shahbaz Khan
- Salman Khan
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2609.04242'
url: https://arxiv.org/abs/2609.04242
pdf_url: https://arxiv.org/pdf/2609.04242
published: '2026-08-06'
collected: '2026-09-07'
category: Multimodal
direction: 多模态理解 · 免训练跨模态适配
tags:
- Multimodal Understanding
- VLM
- Training-Free
- Speech Processing
- Plug-and-Play
one_liner: 提出免训练即插即用框架TFO，可将任意冻结VLM转换为语音中心多模态理解模型，无需改架构或重训练
practical_value: '- 业务侧新增语音等模态能力时，可优先采用「单模态工具转文本+冻结原有大模型接口」的免训练方案，避免重训导致原有能力退化，大幅降低迭代成本

  - 语音转文本预处理环节可加入置信度过滤、时间戳对齐的trick，提升跨模态任务输入质量，适配直播内容理解、音视频商品检索等电商场景需求

  - 多模态系统选型无需盲目追求原生全模态预训练大模型，模块化拼接成熟单模态组件的方案多数场景性能比肩原生方案，落地门槛更低'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有多模态理解模型需新增专用音频编码器+大规模音视频文本联合训练，与特定VLM backbone紧耦合，还会削弱原有视觉、推理能力，训练成本极高。
### 方法关键点
提出即插即用免训练框架TFO，无需修改VLM架构或做跨模态重对齐：1）用Whisper提取带置信度过滤、时间戳的语音转写文本；2）直接将转写文本输入冻结VLM的原有语言接口，视觉通路完全保留不变。
### 关键结果数字
在56个基准、21种语言上对比原生多模态模型，音视理解性能持平，5种模型设置下纯音频任务平均性能提升，多语言语音理解收益显著；冻结的VLM在图像/视频理解、visual grounding、编码、数学推理等能力上均强于原生多模态checkpoint。
