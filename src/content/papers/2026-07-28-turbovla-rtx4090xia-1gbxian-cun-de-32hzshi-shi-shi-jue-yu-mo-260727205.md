---
title: 'TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with
  <1 GB VRAM'
title_zh: TurboVLA：RTX4090下<1GB显存的32Hz实时视觉语言动作模型
authors:
- Hengyi Xie
- Chenfei Yao
- Xianjin Wu
- Xuanyang Xi
- Yiping Tang
- Di Xu
- Yingying Zhu
- Dingkang Liang
- Xiang Bai
- Han Ding
affiliations:
- Huazhong University of Science and Technology
- Huawei Technologies Co. Ltd
arxiv_id: '2607.27205'
url: https://arxiv.org/abs/2607.27205
pdf_url: https://arxiv.org/pdf/2607.27205
published: '2026-07-28'
collected: '2026-07-31'
category: Multimodal
direction: 多模态VLA模型推理与端侧部署优化
tags:
- VLA
- Inference Optimization
- Lightweight Model
- Edge Deployment
- Multimodal Fusion
one_liner: 重构传统LLM中心VLA路径为V+L直连映射，实现低显存低延迟的轻量视觉语言动作模型
practical_value: '- 端侧多模态Agent开发可复用V+L独立编码+轻量双向交互架构，替代LLM中心路径，大幅降低端侧推理显存与延迟

  - 多模态业务任务可借鉴「跳过通用LLM中间层、直接跨模态特征融合输出结果」的思路，压缩推理链路提升效率

  - 消费级硬件部署多模态应用可参考0.2B小参数模型优化方案，实现超实时推理的同时降低部署成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有VLA模型普遍采用LLM中心的V→L→A路径，每次策略调用都会产生极高的计算和显存开销，无法在消费级硬件上实现低延迟本地部署。

### 方法关键点
1. 重构传统VLA路径为直接V+L→A映射，取消LLM作为感知与动作的中间接口；
2. 视觉观测、语言指令分别独立编码，通过轻量双向跨模态交互完成信息交换；
3. 用紧凑型解码器直接预测连续动作块。

### 关键结果
在LIBERO基准上0.2B参数规模实现97.7%平均成功率，RTX4090上推理延迟仅31.2ms、推理显存0.9GB，效果比肩远大于自身规模的VLA模型，推理帧率达32Hz，远超LLM中心方案的11Hz。
