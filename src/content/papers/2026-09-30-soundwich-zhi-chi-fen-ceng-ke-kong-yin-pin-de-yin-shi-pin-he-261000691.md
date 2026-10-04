---
title: 'Soundwich: Video Generation with Layered and Controllable Audio'
title_zh: Soundwich：支持分层可控音频的音视频联合生成方法
authors:
- Zhuo Ning
- AmirHossein Naghi Razlighi
- Sagi Polaczek
- Daniel Cohen-Or
- Ali Mahdavi-Amiri
affiliations:
- Simon Fraser University
- University of Cyprus
- CYENS Centre of Excellence
- Tel Aviv University
arxiv_id: '2610.00691'
url: https://arxiv.org/abs/2610.00691
pdf_url: https://arxiv.org/pdf/2610.00691
published: '2026-09-30'
collected: '2026-10-04'
category: Multimodal
direction: 多模态生成 · 音视频分层可控编辑
tags:
- Multimodal Generation
- Training-free
- Audio-Video Synthesis
- Controllable Generation
- Flow Matching
one_liner: 提出免训练框架Soundwich，将冻结音视频流匹配模型改造为支持多独立同步可编辑音轨的生成器
practical_value: '- 免训练改造预训练多模态大模型的思路可复用，无需全量微调即可给现有生成模型新增可控分层输出能力，适合业务快速迭代

  - 跨模态信息路由+共享全局场景表征的设计可迁移至多模态生成式推荐场景，提升商品短视频/直播素材的音画一致性与编辑灵活性

  - 分层独立可控输出的逻辑可适配电商素材生产工作流，支持快速替换广告音频的BGM、旁白、音效等组件，降低素材制作成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音视频联合生成模型仅输出单条混合音频，无法支持源级控制，不符合专业音视频编辑工作流需求。

### 方法关键点
1. 提出免训练框架Soundwich，直接改造冻结的音视频流匹配模型，输出与同一段视频绑定的多条同步独立可编辑音轨；
2. 引入共享场景表征，在保留音轨独立分离的同时传递全局音视频上下文，保证多轨音频的一致性；
3. 路由每条音轨与对应视觉源的跨模态交互，提升音画匹配度，生成的音轨支持独立调速、静音、替换、重混音操作。

### 关键结果
人类评测显示，在时序控制能力、音源分离度、音频自然度上均优于基线方法，同时支持连贯音视频生成下的灵活源级编辑。
