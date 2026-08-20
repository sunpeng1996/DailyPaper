---
title: 'AnyTalk: Speech Animation for Arbitrary Characters Leveraging a Video Generation
  Model'
title_zh: AnyTalk：基于视频生成模型的任意角色3D语音动画生成
authors:
- Kwan Yun
- Serin Yoon
- Sunjin Jung
- Jung Eun Yoo
- Inyup Lee
- Junyong Noh
arxiv_id: '2608.16143'
url: https://arxiv.org/abs/2608.16143
pdf_url: https://arxiv.org/pdf/2608.16143
published: '2026-08-17'
collected: '2026-08-20'
category: Other
direction: 多模态生成 · 3D语音动画生成
tags:
- Video Diffusion Model
- 3D Animation
- Audio-driven Generation
- Real-time Inference
- Fine-tuning
one_liner: 无需角色专属动画数据，用预训练视频扩散模型生成任意角色3D语音动画并支持实时推理
practical_value: '- 虚拟主播定制可复用零动画数据微调思路：仅用目标虚拟人渲染图+置零音频嵌入微调预训练视频扩散模型，无需标注口型动画数据，大幅降低虚拟人定制成本

  - 实时交互场景可参考蒸馏优化方案：将复杂生成模型蒸馏为轻量实时网络，适配电商直播、AR试穿虚拟人交互等低延迟场景需求

  - 2D生成转3D资产的思路可迁移：先通过生成模型产出2D唇动视频，再优化反推blendshape参数，解决3D虚拟人资产生成的标注依赖问题'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音频驱动3D语音动画方案依赖角色专属训练数据或繁琐的绑定/重网格化流程，人力和数据成本高，无法低成本快速定制任意角色的口型动画，无法满足游戏、VR/AR、虚拟主播等场景的批量需求。
### 方法关键点
1. 提出Character-specific Fine-tuning（CsF）技术，用3D角色渲染图搭配置零音频嵌入（代表无运动）微调预训练视频扩散模型，既保留大规模视频模型的运动先验，又无需专属动画数据
2. 生成对口型的2D talking-head视频后，通过优化流程估计blendshape参数，升维得到3D语音动画
3. 蒸馏得到轻量版AnyTalk_RT，支持实时推理
### 关键结果
覆盖多种人脸网格和blendshape配置，大幅降低人工工作量和数据需求，实时版可落地低延迟交互场景
