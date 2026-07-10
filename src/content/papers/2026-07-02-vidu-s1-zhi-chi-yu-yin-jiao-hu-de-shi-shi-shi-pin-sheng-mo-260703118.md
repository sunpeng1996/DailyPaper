---
title: 'Vidu S1: A Real-Time Interactive Video Generation Model'
title_zh: Vidu S1：支持语音交互的实时视频生成模型
authors:
- Jintao Zhang
- Kai Jiang
- Jintao Chen
- Xu Wang
- Yang Luo
- Yuji Wang
- Dechuang Chen
- Jungang Li
- Chengyang Ye
- Marco Chen
affiliations:
- Tsinghua University
- Shengshu Technology
arxiv_id: '2607.03118'
url: https://arxiv.org/abs/2607.03118
pdf_url: https://arxiv.org/pdf/2607.03118
published: '2026-07-02'
collected: '2026-07-10'
category: Other
direction: 实时交互视频生成 · 语音控制
tags:
- Video Generation
- Real-time Inference
- Diffusion Model
- Voice Control
- TurboDiffusion
one_liner: 提出支持语音控制、无限时长无畸变的实时视频生成模型，消费级GPU可达42FPS 540p输出
practical_value: '- 电商直播/短视频场景可复用TurboDiffusion+TurboServe低延迟推理架构，用消费级GPU落地实时生成式内容，大幅降低部署成本

  - 虚拟主播场景可借鉴语音实时控制视频生成逻辑，实现用户语音互动驱动主播动作/表情的实时交互直播

  - 个性化短广告生成可复用自定义角色上传+多音色选择能力，快速生成适配不同用户偏好的定制化广告素材'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有主流视频生成模型均采用离线一次性生成范式，用户提交prompt后需等待数分钟至数十分钟才能拿到完整视频，生成过程无法主动交互，无法适配实时互动场景需求。
### 方法关键点
1. 底层基于TurboDiffusion实现高效视频生成，搭配TurboServe推理调度框架优化端到端延迟；
2. 支持用户通过语音指令随时控制生成内容，可上传真人/动漫/宠物自定义角色，支持多音色选择适配个性化需求；
3. 优化无限时长生成逻辑，避免长期生成出现的模糊、内容漂移、视觉畸变问题。
### 关键结果
普通消费级GPU上可输出540p分辨率实时视频，最高帧率达42FPS，所有测试指标均达到SOTA，完全满足实时推理要求，已上线可交互Demo。
