---
title: 'TurboBias 2.0: Streaming Context-Biasing for Production-Efficient ASR Systems'
title_zh: TurboBias 2.0：面向生产高效ASR系统的流式上下文偏置框架
authors:
- Vladimir Bataev
- Lilit Grigoryan
- Andrei Andrusenko
- Nikolay Karpov
- Vitaly Lavrukhin
- Boris Ginsburg
affiliations:
- NVIDIA
arxiv_id: '2608.21343'
url: https://arxiv.org/abs/2608.21343
pdf_url: https://arxiv.org/pdf/2608.21343
published: '2026-08-21'
collected: '2026-08-24'
category: Other
direction: 生产级ASR流式上下文偏置优化
tags:
- ASR
- context-biasing
- streaming-inference
- Transducer
- GPU-acceleration
- low-latency
one_liner: 提出支持多用户独立上下文、低延迟高吞吐的生产级Transducer ASR流式上下文偏置框架
practical_value: '- 电商语音搜索、智能客服类Agent的ASR模块可复用per-stream批解码思路，为不同用户/会话独立加载专属上下文词表（如用户收藏商品名、品牌专属术语），完全避免不同用户上下文串扰

  - 低延迟语音交互场景可借鉴GPU加速+不区分大小写的boosting graph设计，在提升专有名词识别准确率的同时，保障推理耗时和吞吐性能达标

  - 高并发生产环境可复用流式+离线双支持的架构设计，同时适配实时语音交互、离线语音内容质检两类业务场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有ASR上下文偏置方法普遍无法满足生产级系统核心要求：不支持流式推理、批解码效率低、无法实现多用户独立上下文配置、运行时开销过高，难以适配低延迟高并发的语音交互类业务需求。
### 方法关键点
1. 基于Transducer架构的ASR扩展GPU加速的TurboBias框架，新增不区分大小写的boosting graph、per-stream批解码能力，批内每个语句可独立配置上下文偏置规则，支持多用户同时个性化偏置且上下文列表完全隔离；
2. 同时兼容离线/流式推理、greedy/束搜索两类解码策略，无需修改ASR模型结构或重训。
### 关键结果
在显著提升上下文短语识别准确率的同时，完全保持原有低延迟与高吞吐的生产级性能指标
