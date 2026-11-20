---
title: 'HiUni: Harmonizing Understanding and Generation in Shared Visual Space'
title_zh: HiUni：共享视觉空间下统一视觉理解与生成能力
authors:
- Jiahao Hu
- Jingdong Du
- Yichen Zhang
- Yi Song
- Zhenyu Zhang
- Jiaxin Niu
- Ruihang Li
- Xiangzhao Hao
- Yiqian Zhang
- Yong Huang
affiliations:
- ERNIE Team, Baidu Inc.
arxiv_id: '2611.26107'
url: https://arxiv.org/abs/2611.26107
pdf_url: https://arxiv.org/pdf/2611.26107
published: '2026-11-18'
collected: '2026-11-20'
category: Multimodal
direction: 多模态大模型 · 理解生成统一架构
tags:
- Multimodal LLM
- Vision-Language Model
- Parameter Sharing
- Image Generation
- Visual Understanding
one_liner: 基于预训练VLM单主干实现高参数共享的视觉理解+生成统一多模态架构
practical_value: '- 电商多模态内容生产场景可复用高参数共享架构思路，无需单独维护理解、生成两套主干，大幅降低训练与部署成本

  - 商品图生成/修图需求可借鉴「Pixel Diffusion Head+轻量HiGate通路」设计，不改动预训练VLM主干即可提升生成细节质量

  - 多模态商品检索、图文理解等下游任务可直接复用统一主干的多模态表征，无需额外对齐两套特征空间，减少适配工作量'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前统一多模态模型大多为视觉理解、生成任务分设独立视觉表征或主干网络，参数复用率低，任务对齐成本高，限制统一架构的落地效率。
### 方法关键点
1. 复用预训练VLM的同一语言对齐ViT与密集Transformer主干支撑理解、生成双任务，仅在输出侧保留任务特化计算，最大化参数共享率
2. 设计Pixel Diffusion Head适配像素空间生成的优化需求，解决生成任务收敛难问题
3. 新增轻量HiGate通路在输出阶段补全预训练ViT丢失的细粒度空间细节，提升生成图的清晰度与还原度
### 关键结果
理解任务平均得分与原有预训练VLM持平，图像生成、编辑性能达到当前主流模型的可比水平，验证了单主干无任务特化计算即可有效支撑双任务的可行性
