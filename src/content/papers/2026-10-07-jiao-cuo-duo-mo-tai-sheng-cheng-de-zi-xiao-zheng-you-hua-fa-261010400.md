---
title: Self-correction Optimization for Interleaved Multimodal Generation
title_zh: 交错多模态生成的自校正优化方法
authors:
- Xin You
- Zhiwei Ning
- Zukai Chen
- Minghui Zhang
- Xuanke Shi
- Hanxiao Zhang
- Jingsong Liu
- Jie Yang
- Quan Wang
- Yun Gu
affiliations:
- Shanghai Jiao Tong University
- SenseTime Research
- Technical University of Munich
arxiv_id: '2610.10400'
url: https://arxiv.org/abs/2610.10400
pdf_url: https://arxiv.org/pdf/2610.10400
published: '2026-10-07'
collected: '2026-10-08'
category: Multimodal
direction: 多模态大模型 · 交错图文生成优化
tags:
- MLLM
- Multimodal Generation
- Training-free
- Self-correction
- Temporal Consistency
one_liner: 提出免训练自校正优化方法SCO，大幅提升交错图文生成的时序一致性与视觉主体保留能力
practical_value: '- 电商商品图文种草、多轮生成式内容创作场景可直接复用SCO免训练优化逻辑，无需额外标注数据即可提升生成内容的主体一致性、时序连贯性，避免图文脱节、主体漂移问题

  - 可将新事件+状态保留的双约束思想迁移到生成式推荐的多轮内容生成链路，如用户多轮交互下的推荐理由生成、商品秀图序列生成，保证前后生成内容逻辑自洽

  - 该方法可扩展到商品演示短视频生成场景，优化短视频内商品主体一致性与操作流程的物理合理性，降低生成内容违和感'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
当前MLLM在交错图文生成场景存在明显短板：现有方案大多依赖增广数据做额外训练，算力成本高，且生成内容普遍存在视觉主体漂移、时序一致性差、物理合理性不足问题，无法适配多轮多模态内容生成的落地需求。
### 方法关键点
提出免训练的自校正优化（SCO）框架，以无分类器引导更新为参考基准，在双互补约束下执行最小程度自校正：1）新事件约束提升图文序列的跨模态时序一致性；2）状态保留约束保证后续生成步骤中视觉主体的连贯性。
### 关键结果
在交错多模态生成基准测试中，时序一致性、视觉主体保留效果均获得显著提升；可扩展到视频生成、机器人操作、长流程手工制作等场景的物理过程建模优化。
