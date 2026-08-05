---
title: 'SwanTale: Unified Multi-Speaker Speech and Audio Generation for Instruct and
  Zero-Shot Tasks'
title_zh: SwanTale：支持指令与零样本任务的统一多说话人语音音频生成
authors:
- Yu Zhang
- Ruiqi Li
- Changhao Pan
- Ke Lei
- Xiang Yin
- Cheng Yang
affiliations:
- ByteDance
- Zhejiang University
arxiv_id: '2608.02023'
url: https://arxiv.org/abs/2608.02023
pdf_url: https://arxiv.org/pdf/2608.02023
published: '2026-08-02'
collected: '2026-08-05'
category: Multimodal
direction: 多模态生成 · 语音音频零样本/指令生成
tags:
- Speech Generation
- Zero-Shot Learning
- MoE
- Curriculum Learning
- GRPO
- Multimodal Generation
one_liner: 提出统一多说话人语音音频生成框架SwanTale，同时支持零样本克隆和指令驱动生成
practical_value: '- 电商短视频口播、广告配音场景可复用其零样本语音克隆能力，快速生成符合品牌人设的多风格语音内容，无需专业配音演员录制

  - 数据侧的「原始数据清洗+定向合成补全+多级标注」策略可迁移至多模态训练数据构造流程，解决广告旁白、商品讲解等垂类场景训练数据覆盖不足的问题

  - 指令驱动的多说话人+背景音统一生成能力可用于自动生成电商广告、短剧的完整音频轨，大幅降低内容制作成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
广告、短视频、动画配音等内容生产场景，既需要基于少量参考音频的零样本语音克隆，也需要无参考时通过自然语言指令自定义说话人音色、风格、背景音效，现有方案无法同时覆盖两类任务需求。
### 方法关键点
1. 数据侧提出SwanData-Caption：清洗原始语音数据、补充定向合成数据、标注多级精准描述，解决训练数据覆盖不足问题；
2. 模型侧引入SwanVAE支持多音频模态生成，搭配reward-conditioned质量控制、Engram条件控制、Unified MoE做多任务多模态统一建模；
3. 训练采用课程学习+GRPO后训练，逐步提升模型复杂任务能力。
### 关键结果
在零样本、指令生成多类核心指标上领先，两类任务的表现力评分均达SOTA，支持多说话人+背景音的复杂指令生成。
