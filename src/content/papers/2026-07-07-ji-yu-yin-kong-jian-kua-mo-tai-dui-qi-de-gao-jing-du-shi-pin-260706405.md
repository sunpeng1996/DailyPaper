---
title: Precise Video-to-Audio Generation with Cross-Modal Alignment in Latent Space
title_zh: 基于隐空间跨模态对齐的高精度视频转音频生成方法
authors:
- Thanh V. T. Tran
- Ngoc-Son Nguyen
- Luong Tran
- Long-Khanh Pham
- Paarth Neekhara
- Shezheen Hussain
- Van Nguyen
affiliations:
- FPT Software AI Center, Vietnam
- NVIDIA Corporation, USA
arxiv_id: '2607.06405'
url: https://arxiv.org/abs/2607.06405
pdf_url: https://arxiv.org/pdf/2607.06405
published: '2026-07-07'
collected: '2026-07-09'
category: Multimodal
direction: 多模态生成 · 视频转音频跨模态对齐
tags:
- Video-to-Audio
- Cross-Modal Alignment
- Cross-Attention
- Generative AI
- Multimodal
one_liner: 提出端到端单阶段V2A架构Flowley与声音感知标注流水线SoundCap，实现SOTA视频音频生成效果
practical_value: '- Progressive Soft-masked Cross-Attention可直接迁移至多模态对齐场景（如电商短视频音视频匹配、商品多模态特征融合），无额外算力开销即可提升时序对齐精度

  - SoundCap面向任务的细粒度标注流水线思路可复用，可用于电商短视频配音、商品素材标注等场景，降低人工标注成本

  - 单阶段端到端多模态生成架构设计可借鉴，用于多模态内容生成类业务（如商品短视频自动配乐/解说），减少多阶段训练的算力损耗'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有Video-to-Audio(V2A)方法存在两类痛点：一是多阶段训练架构算力开销高、推理延迟大；二是将视觉输入转文本调用预训练文生音频模型的方案会丢失细粒度时序同步信号，同时现有V2A基准缺乏面向声音的描述标注，进一步限制生成质量。
### 方法关键点
1. 提出单阶段端到端架构Flowley，直接融合视觉特征与文本提示生成匹配的音频
2. 设计Progressive Soft-masked Cross-Attention，在原生注意力机制内实现音视频时序同步，相比标准注意力无额外计算成本
3. 提出即插即用的SoundCap流水线，自动生成声音感知的细粒度标注引导模型生成
### 关键结果
无预训练音视频对齐模块时，在VGGSound数据集多指标达到SOTA；结合SoundCap后，零样本场景下音频质量超过现有最强闭源方法
