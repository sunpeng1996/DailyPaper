---
title: 'AVSCap: Orchestrating Audio-Visual Synergy for Omni-modal Video Captioning'
title_zh: AVSCap：调度音视频协同的全模态视频字幕生成框架
authors:
- Yanghai Wang
- Jiahao Wang
- Jiafu Tang
- Yuanxing Zhang
- Zhe Cao
- Hanyan Bian
- Zijie Zhang
- Weiliang Luo
- Zhiyu Pan
- Zixuan Dong
affiliations:
- Nanjing University
- Kuaishou Technology
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2607.12820'
url: https://arxiv.org/abs/2607.12820
pdf_url: https://arxiv.org/pdf/2607.12820
published: '2026-07-14'
collected: '2026-07-16'
category: Multimodal
direction: 多模态视频理解 · 音视频协同字幕生成
tags:
- Multimodal LLM
- Video Captioning
- Audio-Visual Fusion
- Reinforcement Learning
- Benchmark
one_liner: 构建音视频显式事件绑定的全模态字幕框架，配套训练语料、评测基准及开源7B模型
practical_value: '- 短视频电商内容打标等多模态理解场景，可复用「先解耦锚定各模态证据再融合生成描述」的pipeline，提升标签的跨模态一致性

  - 多模态生成模型训练可借鉴两阶段策略，SFT打底后用混合奖励的小样本RL优化特定目标，性价比高于单纯扩充SFT数据

  - 多模态生成任务评测可复用细粒度事件拆解召回指标，替代笼统的文本匹配指标，更贴合业务对内容完整性的要求'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有多模态大模型做全模态视频字幕时，将音视频流视为松耦合输入，过度依赖ASR，忽略非语音音效与视觉事件的关联，无法刻画多模态事件的协同演化关系。
### 方法关键点
1. 构建AVSCap-130K三模态训练语料，采用先解耦锚定音视觉证据、再融合生成grounded字幕的流水线制作
2. 两阶段训练7B参数的AVSCap-7B：SFT阶段打基础，再用混合奖励的低样本RL优化音频完整性和音视频协同性
3. 开源AVSCapBench基准，将字幕拆解为视觉、音频、协同事件三类，用细粒度事件召回做评测
### 关键结果
RL优化带来的效果增益远高于增加SFT数据规模，AVSCap-7B在自有及公开基准上均为开源模型最优，非语音音频覆盖率、跨模态绑定能力显著提升
