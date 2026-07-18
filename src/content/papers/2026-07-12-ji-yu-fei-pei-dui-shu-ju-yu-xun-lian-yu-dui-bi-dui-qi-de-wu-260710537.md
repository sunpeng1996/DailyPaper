---
title: Dance to Music Generation leveraging Pre-training with Unpaired data and Contrastive
  Alignment
title_zh: 基于非配对数据预训练与对比对齐的舞蹈驱动音乐生成方法
authors:
- Ryota Kimura
- Sangheon Park
- Natalia Polouliakh
- Taketo Akama
affiliations:
- Sony Computer Science Laboratories
- Keio University
- Georgia Institute of Technology
arxiv_id: '2607.10537'
url: https://arxiv.org/abs/2607.10537
pdf_url: https://arxiv.org/pdf/2607.10537
published: '2026-07-12'
collected: '2026-07-18'
category: Multimodal
direction: 跨模态生成 · 非配对数据对齐
tags:
- Cross-Modal Alignment
- Contrastive Learning
- Diffusion Model
- ControlNet
- Unpaired Pre-training
one_liner: 结合非配对数据对比预训练与ControlNet改造预训练扩散模型，实现更高精度的舞蹈驱动音乐生成
practical_value: '- 短视频/直播等电商内容生产场景的跨模态匹配任务（如BGM生成、动作触发音效）可复用「单模态预训练+弱监督对比对齐+ControlNet挂载预训练生成模型」架构，大幅降低对高质量配对标注数据的需求

  - 时序类跨模态对齐任务（如商品展示视频与BGM匹配、直播带货动作与特效/音效联动）可引入节拍/时间戳引导的对比损失，显著提升跨模态特征对齐的时序一致性

  - 垂类条件生成任务适配现有大生成模型时，优先采用ControlNet类轻量化挂载方案，无需全量微调即可实现可控条件注入，大幅降低工程落地成本与训练资源消耗'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
舞蹈驱动音乐生成核心要求动作与音频时序对齐，但高质量同步配对舞蹈-音乐数据采集成本高、受版权限制，仅用配对数据难以训练出效果优异的端到端模型。
### 方法关键点
1. 分别预训练动作、音频单模态编码器，采用节拍引导的对比预训练对齐两者特征空间，可高效利用大量非配对数据降低对标注配对数据的依赖
2. 基于预训练文本转音频扩散模型，挂载ControlNet风格的条件注入模块，将对齐后的动作特征作为生成控制条件，仅需少量配对数据微调即可完成垂类适配
### 关键结果
在AIST++数据集上，相较现有SOTA方法舞蹈-音乐对齐性能更优，音频质量达到可比水平，量化指标与人工评估均验证方案有效性。
