---
title: StepAudio 3 Gen Technical Report
title_zh: StepAudio 3 Gen 通用音频生成模型技术报告
authors:
- Bin Lin
- Bo Zhao
- Boyang Wang
- Boyang Zhang
- Boyong Wu
- Chao Yan
- Chen Geng
- Chen Wu
- Cheng Yi
- Chengli Feng
affiliations:
- StepFun-Audio Team
arxiv_id: '2609.12945'
url: https://arxiv.org/abs/2609.12945
pdf_url: https://arxiv.org/pdf/2609.12945
published: '2026-09-10'
collected: '2026-09-14'
category: Other
direction: 通用音频生成 · 离散自回归建模
tags:
- Audio Generation
- Autoregressive Model
- RVQ
- TTS
- LLM Adaptation
one_liner: 提出基于离散自回归的通用音频生成框架，统一支持多类型音频生成，性能达SOTA
practical_value: '- 电商短视频/直播内容生产场景可复用该统一音频生成框架，一次性覆盖商品口播配音、背景音效、BGM生成需求，无需对接多套独立模型，降低研发与运维成本

  - 对话Agent的语音交互模块可借鉴其RVQ Adaptor+离散自回归的轻量生成架构，降低语音生成推理延迟，提升多轮语音交互的流畅度

  - 多模态内容推荐系统的多模态内容生成链路可复用其干扰感知渐进式预训练思路，扩展模态能力时保留原有大模型的文本理解能力，避免灾难性遗忘'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有音频生成模型按语音、音效、音乐等赛道独立优化，存在表示不兼容、多类型音频混合生成困难的问题，主流扩散Transformer范式推理延迟高，无法适配低时延场景需求。
### 方法关键点
1. 抛弃主流扩散Transformer架构，采用离散自回归生成范式，直接基于RVQ token建模音频；
2. StepAudio Tokenizer在16×2048共享残差码空间联合量化语义与波形级声学特征，采样率12.5Hz，每个码层同时保留两类信息；
3. 主干AR模型沿时间轴预测首个码本，轻量因果Transformer沿码本轴补全剩余15个码本；
4. 采用三大核心设计：干扰感知渐进式预训练（保留LLM文本能力）、RVQ Adaptor适配多码本声学表示、跨音频域共享表示的离散自回归建模。
### 关键结果
经过渐进式预训练、多任务指令训练、SFT后，在TTS、语音设计任务上达到SOTA水平，同时保留语音、人声、音效、音乐的强生成能力
