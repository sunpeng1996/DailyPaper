---
title: Online Neural Space Time Memory for Dynamic Novel View Synthesis
title_zh: 面向动态新视角合成的在线神经时空记忆框架
authors:
- Baback Elmieh
- Lynn Tsai
- Zeman Li
- Srinivas Kaza
- Tiancheng Sun
- Gabor Csapo
- Ali Behrouz
- Yuan Deng
- Stephen Lombardi
- Steven M. Seitz
affiliations:
- University of Washington
- Google
arxiv_id: '2607.15271'
url: https://arxiv.org/abs/2607.15271
pdf_url: https://arxiv.org/pdf/2607.15271
published: '2026-07-16'
collected: '2026-07-18'
category: Other
direction: 动态新视角合成 · 实时记忆优化
tags:
- Novel View Synthesis
- Test-Time Training
- Memory Mechanism
- Real-Time Inference
- Cross-View Attention
one_liner: 通过解耦记忆更新与推理频率，引入记忆损失与缓存机制实现实时动态新视角合成
practical_value: '- 「记忆更新与推理频率解耦」的设计思路可直接复用在流数据实时推荐场景，无需每步更新用户长期记忆，大幅降低推理延迟

  - 辅助Memory Loss+权重缓存防灾难性漂移的方案，可迁移到需要在线增量更新的LLM推荐/Agent记忆模块，避免历史用户/物品特征遗忘

  - 低频率梯度更新+高频率特征读取的架构，可适配实时广告投放系统的用户兴趣建模，平衡效果与算力成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
在线多视角流视频新视角合成面临核心权衡：既要维护长期记忆重建临时遮挡区域，又要满足严格实时约束；传统逐帧梯度更新的测试时训练（TTT）方案算力成本过高，长序列下不稳定，无法落地实时场景。

### 方法关键点
1. 解耦记忆更新与推理的执行频率：仅周期性执行梯度更新，每帧直接读取记忆做推理，通过跨视图注意力对齐历史记忆与当前帧的形变；
2. 引入辅助Memory Loss强制模型持久内化场景信息；
3. 新增Memory Caching策略正则化活跃权重，避免灾难性漂移。

### 关键结果数字
内存复杂度为O(1)，在单张H100 GPU上256×256分辨率下实现摊销实时推理；动态人体动作场景下精度达SOTA，支持分钟级在线记忆；仅1FPS的记忆更新频率即可支撑30FPS的输入与合成输出。
