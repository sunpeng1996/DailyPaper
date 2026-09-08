---
title: 'Encore: Infinite Audio-Video Generation with Adaptive Signal Routing'
title_zh: Encore：基于自适应信号路由的无限时长音视频生成框架
authors:
- Shaohua Pan
- Junbao Chen
- Shengyi He
- Jingfeng Xue
- Wen Tao
- Haocheng Feng
- Siming Fan
- Dongwei Pan
- Yi Yang
- Wei He
affiliations:
- Baidu, China
- Beijing Institute of Technology, China
arxiv_id: '2609.04249'
url: https://arxiv.org/abs/2609.04249
pdf_url: https://arxiv.org/pdf/2609.04249
published: '2026-08-28'
collected: '2026-09-08'
category: Multimodal
direction: 长时序多模态生成 · 自适应信号路由
tags:
- Audio-Video Generation
- Long-form Generation
- Adaptive Signal Routing
- Cross-modal Synthesis
- Temporal Coherence
one_liner: 提出自适应信号路由驱动的Encore框架，可生成超500秒同步的长时序音视频内容
practical_value: '- 电商商品种草长视频、直播自动剪辑场景可复用「分块迭代+跨块上下文传播」架构，解决长内容时序连贯问题

  - 自适应信号路由（ASR）的可学习注意力偏置、残差缩放设计可迁移至多模态跨条件生成任务，提升条件信号适配效率

  - 带偏移位置嵌入的参考信号约束方案可用于优化音视频同步生成效果，适配短转长内容生成需求'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音视频生成仅能输出短时长同步片段，长视频生成方案普遍缺失同步音频，联合生成需同时满足视频时序连贯、音频时序连贯、跨模态同步三重约束，现有架构难以适配。
### 方法关键点
1. 拆分长时序生成任务：通过分块迭代生成+显式跨块上下文传播保障局部连续性，引入带偏移位置嵌入的参考音视频信号保障全局一致性
2. 核心模块Adaptive Signal Routing（ASR）：在自注意力层加入可学习注意力偏置，交叉注意力输出层加入可学习残差缩放，自适应调节各条件信号的影响权重
3. 端到端训练，推理阶段支持无限时长音频转视频、视频转音频生成
### 关键结果
在扩展的VerseBench长音视频评估集上生成质量、时序连贯性显著优于SOTA，可生成超500秒身份、音频一致的同步音视频内容
