---
title: Stable Autoregressive Speech Generation with Low-Frame-Rate High-Dimensional
  Continuous Tokens
title_zh: 基于低帧率高维连续Token的稳定自回归语音生成
authors:
- Yi Luo
- Rongzhi Gu
- Jixun Yao
affiliations:
- ByteDance Seed
- Columbia University
arxiv_id: '2607.29363'
url: https://arxiv.org/abs/2607.29363
pdf_url: https://arxiv.org/pdf/2607.29363
published: '2026-07-31'
collected: '2026-08-04'
category: Other
direction: 自回归生成 · 连续Token表示优化
tags:
- Autoregressive Generation
- Continuous Token
- Codec
- Flow Matching
- Speech Synthesis
one_liner: 提出Locodec编码与MP-ELD流匹配框架，实现无预训练依赖的稳定高保真长序列语音生成
practical_value: '- 高维连续Token的表示空间优化思路可复用在Semantic ID生成场景，通过提升流形插值性改善序列预测的稳定性

  - 多路径信息路由+残差CFG的抗误差累积方案，可迁移到长序列生成式推荐、Agent长对话的自回归建模中降低分布漂移

  - 低帧率高带宽的Token设计思路，可用于优化多模态召回的特征压缩，平衡序列长度与信息保留度，降低推理耗时'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
自回归语音生成长期存在序列长度、表示容量、长序列稳定性的三重权衡：高帧率高容量表示易引发分布漂移、自回归误差累积，低压缩率表示带宽不足会丢弃关键信息，限制生成保真度上限。
### 方法关键点
1. 提出Locodec本地编码Codec，优化表示空间的低维核心流形插值性与原生高维坐标可识别性，提升高带宽Token的可预测性
2. 提出MP-ELD单Token自回归流匹配框架，通过多路径信息路由、残差classifier-free guidance缓解误差累积
3. 无需依赖外部SSL/ASR模型、预训练文本LLM或后训练阶段
### 关键结果
基于8Hz、768维Token实验验证：重建质量无损失，单Token可预测性显著提升，WER达到业内可比水平，长序列合成稳定性优异
