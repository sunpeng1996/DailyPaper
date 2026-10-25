---
title: Tokenized Joint Source-Network Coding for Loss-Resilient Video Streaming
title_zh: 面向抗丢包视频流的令牌化联合信源-网络编码
authors:
- Ke Yang
- Sixian Wang
- Kailin Tan
- Guo Lu
- Jincheng Dai
- Wenjun Zhang
- Ping Zhang
arxiv_id: '2610.21166'
url: https://arxiv.org/abs/2610.21166
pdf_url: https://arxiv.org/pdf/2610.21166
published: '2026-10-15'
collected: '2026-10-25'
category: Other
direction: 视频传输 · 抗丢包编码
tags:
- Video Tokenization
- Low-Latency Streaming
- Packet Loss Resilience
- Joint Source-Network Coding
- RTC
one_liner: 提出TokJSNC令牌化编码框架，无需FEC或重传即可在高丢包率下实现低延迟高帧率视频传输
practical_value: '- 若业务涉及电商直播、数字人带货等实时视频流传输，可借鉴TokJSNC根据内容复杂度动态调整token传输速率的思路，平衡带宽占用与播放流畅度

  - 弱网环境下的实时视频交互类Agent（如远程智能导购、直播数字人）可参考其无FEC/重传的抗丢包架构，降低端到端延迟

  - 做视频内容生成-分发全链路优化的团队，可复用视频token时空相关性做丢包后鲁棒重建，减少用户侧卡顿'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
传统实时视频流依赖FEC与重传抗丢包：FEC在时变丢包场景下效率低下，重传会引入过高延迟无法满足严格的播放时效要求；现有DeepJSCC方案与物理层强耦合，难以适配现有分层网络架构与协议。
### 方法关键点
提出TokJSNC令牌化联合信源-网络编码范式，跳过传统「先压缩再加FEC保护」的流程，直接将视频编码为可变长离散令牌流，传输速率同时适配视频内容复杂度与网络状态；利用学习到的视频令牌间的时空相关性，无需显式FEC或重传即可在宽丢包率范围下实现鲁棒视频重建，同时完全兼容现有网络架构与传输协议。
### 关键结果
70%丢包率场景下平均播放帧率仍高于22fps，而同场景下最优基线方案帧率低于12fps
