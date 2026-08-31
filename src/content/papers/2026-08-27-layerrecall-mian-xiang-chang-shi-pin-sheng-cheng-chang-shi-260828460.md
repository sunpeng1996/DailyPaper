---
title: 'LayerRecall: A State-Conditioned Memory Router for Long-Horizon Consistency
  in Video Generation'
title_zh: LayerRecall：面向长视频生成长时序一致性的状态条件记忆路由器
authors:
- Yixuan Ding
- Jiahao Kong
- Wei Huang
- Ruijie Quan
- Yi Yang
affiliations:
- Zhejiang University
- The University of Hong Kong
arxiv_id: '2608.28460'
url: https://arxiv.org/abs/2608.28460
pdf_url: https://arxiv.org/pdf/2608.28460
published: '2026-08-27'
collected: '2026-08-31'
category: Other
direction: 长视频生成 · KV缓存记忆路由
tags:
- KV Cache
- Memory Router
- Diffusion Model
- Long-Horizon Modeling
- Video Generation
one_liner: 提出层选择记忆路由LayerRecall，提升长视频生成的历史特征召回能力与时序一致性
practical_value: '- 可复用KV缓存分层路由思路，在长序列推荐/Agent记忆模块中，仅将历史状态注入对记忆敏感的网络层，降低推理开销同时提升长时序特征召回准确率

  - CHPM无标注训练方法可直接迁移，无需长序列标注数据，用特权长上下文参考监督有限记忆模块的预测空间，大幅降低长序列场景训练数据门槛

  - 生成式推荐多轮用户交互内容生成场景，可借鉴记忆引导自校正逻辑，保留当前上下文连贯性的同时修正不符合历史用户偏好的生成结果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
自回归视频扩散依赖近期缓存生成分块内容，会丢失历史主体、场景、属性特征，现有记忆机制仅解决历史特征访问问题，未考虑DiT不同层对上下文的偏好差异，无法保证历史特征的有效利用。
### 方法关键点
1. 设计LayerRecall状态感知层选择记忆路由器，检索相关历史K/V状态仅注入对记忆敏感的骨干层，其余层保留本地注意力保障局部连续性
2. 提出跨时序预测匹配（CHPM）训练策略，用特权长上下文参考监督有限记忆路由器，无需高质量长时序标注数据
### 关键结果
在100条多轮测试prompt上，MemoBench、MovieBench综合性能最优，VBench-Long性能与基线相当无局部连续性损失，推理开销可忽略，支持跨骨干网络迁移
