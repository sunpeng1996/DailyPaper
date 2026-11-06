---
title: 'TaoMate-HD: Progressive-Resolution Autoregressive Audio-Video Generation'
title_zh: TaoMate-HD：渐进分辨率自回归音视频生成模型
authors:
- Qijun Gan
- Chenwei Zhang
- Xinyang Li
- Meiguang Jin
- Junfeng Ma
- Shen Qiu
affiliations:
- Alibaba Group
- Nanjing University
arxiv_id: '2611.03394'
url: https://arxiv.org/abs/2611.03394
pdf_url: https://arxiv.org/pdf/2611.03394
published: '2026-11-01'
collected: '2026-11-06'
category: Multimodal
direction: 多模态 · 流式数字人音视频生成
tags:
- Audio-Video Generation
- Streaming Digital Human
- Progressive Resolution
- Autoregressive Generation
- Low Latency Inference
one_liner: 提出渐进分辨率自回归流式音视频生成方案，提速同时降语音错误率支持小时级生成
practical_value: '- 电商直播数字人生成可复用渐进分辨率生成思路，先低分辨率生成粗结构再精细化，平衡生成质量与推理速度

  - 流式生成场景可借鉴跨chunk历史传递机制+非对称文本条件训练方法，解决文本更新导致的语音重复/中断问题

  - 部署阶段可采用阶段并行优化策略，在现有硬件上进一步提升端到端生成速度，降低服务成本'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
流式数字人生成存在两大核心痛点：高分辨率去噪计算成本极高，动态文本更新易引发语音重复、中断，现有方案难以同时满足生成质量、低延迟与语音连续性要求。
### 方法关键点
1. 采用渐进分辨率生成范式：每个音视频chunk先经2步低分辨率去噪生成粗视频结构，最后1步上采样精细化至高分辨率，音视频沿同一轨迹生成；
2. 跨chunk同阶段传递历史预测结果，保留上下文信息避免内容错乱；
3. 引入非对称文本条件连续训练策略，生成、蒸馏模块使用独立文本窗口，适配动态输入场景。
### 关键结果
相同硬件下较直接高分辨率生成提速1.6x，阶段并行部署较串行渐进生成再提速1.9x，语音字符错误率相对基线降低11.18个百分点，支持小时级音视频生成。
