---
title: 'AV-FABLE: Audio-Visual Manipulation Forensics in Long-Form Videos'
title_zh: AV-FABLE：长视频场景下的音视频篡改取证基准与方法
authors:
- Yuesheng Huang
- Hoi Fan Au
- Jiaqi Hou
- Ruicheng Zhang
- Jiarui He
- Haocheng Yang
- Bin Hu
- Kewei Zhang
- Weijian Deng
- Jun Zhou
affiliations:
- Tsinghua University
- Peking University
arxiv_id: '2610.33413'
url: https://arxiv.org/abs/2610.33413
pdf_url: https://arxiv.org/pdf/2610.33413
published: '2026-10-24'
collected: '2026-10-31'
category: Multimodal
direction: 多模态大模型 · 音视频篡改取证
tags:
- AV-LLM
- Multimodal Benchmark
- Video Forensics
- Temporal Localization
- Deepfake Detection
one_liner: 发布998小时长视频音视频篡改双时间线基准与性能最优的NFSR取证方法
practical_value: '- 多模态风控场景优化：电商/短视频平台做UGC内容篡改、违规检测时，无需依赖AV-LLM的零样本prompt输出，可复用其冻结的感知特征加轻量分模态解码器，大幅提升检测性能

  - 多模态时序任务评估：做音视频对齐、长时序多模态定位类任务时，分开评估各模态的时序性能，避免联合时间线评估掩盖单模态的误差

  - 长时序稀疏事件检测参考：长视频/长音频的稀疏目标检测场景，可采用分模态独立时序解码器的设计，降低跨模态干扰，提升跨域迁移能力'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音视频深度伪造基准多聚焦短 talking-head 片段，长视频篡改取证仅侧重视觉模态，且粗粒度视频级分类无法定位篡改位置、区分受影响模态，无法满足细粒度取证需求。
### 方法关键点
1. 构建 AV-FABLE 双时间线基准，包含16650对原始/篡改孪生视频（共998小时），覆盖27种编辑配置，音视频时间线独立，支持分模态时序定位，可暴露联合评估隐藏的误差。
2. 提出 NFSR 架构，直接读取冻结 AV-LLM 的感知特征，用独立的音频、视频时序解码器提取取证信号。
### 关键结果
零样本 prompting AV-LLM 的检测效果接近随机，NFSR 在域内及3种分布外场景均取得最优音视频定位性能，可迁移到外部长视频取证基准的未见过视频。
