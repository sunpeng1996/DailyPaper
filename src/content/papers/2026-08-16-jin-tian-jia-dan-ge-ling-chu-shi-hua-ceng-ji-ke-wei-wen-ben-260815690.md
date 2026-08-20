---
title: Adding Voice Cloning to Text-to-Audio-Video Models with a Single Zero-Initialised
  Layer
title_zh: 仅添加单个零初始化层即可为文本转音视频模型集成声音克隆能力
authors:
- Ivan Mikheev
- Viacheslav Vasilev
- Anna Dmitrienko
- Alexey Letunovskiy
- Ivan Kirillov
- Kirill Chernyshev
- Denis Dimitrov
affiliations:
- Kandinsky Lab, Moscow, Russia
arxiv_id: '2608.15690'
url: https://arxiv.org/abs/2608.15690
pdf_url: https://arxiv.org/pdf/2608.15690
published: '2026-08-16'
collected: '2026-08-20'
category: Multimodal
direction: 多模态音视频生成 · 个性化声音克隆
tags:
- Text-to-Audio-Video
- Voice Cloning
- Diffusion Model
- Zero-Initialization
- Inference Optimization
- Personalized Generation
one_liner: 在文本转音视频模型音频骨干上加单零初始化层，短微调即可实现高性能可控声音克隆
practical_value: '- 电商虚拟主播/商品短视频生成场景可复用单零初始化层微调方案，无需重新训练全量T2AV大模型，仅少量训练即可为通用音视频生成能力接入定制化声音功能，大幅降低个性化改造的成本

  - 推理阶段可单独运行音频路径获得30倍提速的特性，可用于批量生成音视频素材前先快速验证声音匹配度，再生成完整音视频，提升内容生产效率

  - 参考语音双路注入（diffusion潜变量前置+全局说话人嵌入调制）的条件融合方法，可迁移到其他多模态个性化生成任务，比如数字人形象+声音同步定制场景'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有文本转音视频（T2AV）生成模型无法控制输出音频的说话人身份，限制了个性化内容创作、虚拟主播配音、特定人物音视频渲染等场景的落地。

### 方法关键点
1. 仅在基础T2AV模型的音频骨干顶部添加1个零初始化线性层，经过短周期微调即可实现声音克隆能力；
2. 推理时通过双路信号注入参考语音信息：将参考语音的diffusion潜变量前置到音频流，同时用全局说话人嵌入调制目标音频的token；
3. 架构天然支持推理阶段单独运行音频路径，无需加载视频分支。

### 关键结果数字
在30个说话人共674组说话人-文本对的基准上，5B参数增强模型在ECAPA-TDNN、WavLM-SV、Resemblyzer三个独立验证网络上的说话人编码器余弦相似度（SECS）均为最高，显著优于5个强基线TTS声音克隆模型；单独运行音频路径时推理速度比完整音视频扩散循环快~30x，且完全保留声音克隆能力。
