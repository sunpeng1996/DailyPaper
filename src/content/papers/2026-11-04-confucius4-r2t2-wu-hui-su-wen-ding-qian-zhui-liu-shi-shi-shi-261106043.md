---
title: 'Confucius4-R2T2: A Stable-Prefix Streaming ASR Model for Real Real-Time Transcription'
title_zh: Confucius4-R2T2：无回溯稳定前缀流式实时语音识别模型
authors:
- Daniel Huang
- Qi He
- Shaoxiong Duan
- Yingjie Li
- Qiao Cheng
- Yitao Duan
affiliations:
- 网易有道
arxiv_id: '2611.06043'
url: https://arxiv.org/abs/2611.06043
pdf_url: https://arxiv.org/pdf/2611.06043
published: '2026-11-04'
collected: '2026-11-09'
category: Multimodal
direction: 流式ASR · 大模型无架构改动微调
tags:
- Streaming ASR
- Longest Stable Prefix
- Post-training
- Low Latency
- Stable Output
one_liner: 基于LSP标注微调实现无需改架构的稳定前缀流式ASR，准确率接近全上下文基座且延迟低
practical_value: '- 搭建电商语音导购、语音搜索类Agent时可直接复用该开源ASR，避免输出回溯导致下游任务重复计算或错误响应

  - 需将全上下文大模型改造为流式输出模型时，可借鉴LSP标注方法，无需改动架构仅通过微调即可实现输出前缀稳定不回溯

  - 大模型增量微调时可复用冻结预训练主干、仅微调上层模块的策略，用少量领域数据就能达到接近基座的效果，降低训练成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
流式ASR输出token若后续被修正，会导致下游语音Agent、翻译等模块产生无效计算甚至执行错误操作，现有方案要么需改动模型架构复杂度高，要么输出稳定性差、延迟高。
### 方法关键点
1. 提出Longest Stable Prefix（LSP）概念，证明其满足前缀单调性、与全音频输出一致、是匹配最早输出的最长有效序列三大属性；
2. 基于Qwen3-ASR-1.7B基座，冻结预训练音频编码器与投影层，用1500小时中英音频数据以LSP为标注做后训练，无需修改模型架构即可得到稳定前缀流式模型。
### 关键结果
流式识别效果接近基座全上下文识别质量，输出前缀永不修改，发射延迟极低，且效果可泛化到后训练语种之外的其他语言。
