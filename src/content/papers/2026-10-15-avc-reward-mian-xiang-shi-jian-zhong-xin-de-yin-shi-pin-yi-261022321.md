---
title: 'AVC-Reward: Event-Centric Audio-Video Consistency Evaluation'
title_zh: AVC-Reward：面向事件中心的音视频一致性评估
authors:
- Yuruo Wu
- Kaihang Pan
- Kai Shen
- Jiacheng Li
- Shuyuan Tu
- Jisheng Dang
- Li Tuoyu
- Juncheng Li
- Siliang Tang
affiliations:
- Zhejiang University
- HiThink Research
- Fudan University
- Lanzhou University
arxiv_id: '2610.22321'
url: https://arxiv.org/abs/2610.22321
pdf_url: https://arxiv.org/pdf/2610.22321
published: '2026-10-15'
collected: '2026-10-17'
category: Eval
direction: 多模态评估 · 音视频一致性Reward建模
tags:
- Multimodal-Evaluation
- Reward-Model
- Audio-Video-Consistency
- Cross-Modal
- Benchmark
one_liner: 提出事件驱动的三层音视频一致性评估框架及Reward模型，达到SOTA人机对齐效果
practical_value: '- 可复用事件级跨模态拆解方法，优化电商短视频/直播生成的音画匹配校验逻辑，替代高成本人工审核

  - 三层粗到细的一致性评估范式可迁移至多模态内容推荐的质量打分环节，过滤音画不同步的低质素材

  - 可训练Reward模型的设计思路可复用在生成式内容的RLHF优化流程中，提升生成内容的用户感知一致性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有音视频一致性评估多复用早期简单单向任务的指标，整体打分依赖预定义规则，无法适配多事件组合、多层音频混合、非对称跨模态关系等复杂生成场景的评估需求。
### 方法关键点
事件中心的评估框架先在事件粒度解耦音/视事件，独立分析后做跨模态关系校验，聚合为粗到细三层一致性指标：全局叙事协调性、事件级时间同步性、细粒度属性对齐性，基于此实现可训练的Reward模型AVC-Reward，同时配套构建包含多类音视频生成模型正负样本的AVC-Benchmark。
### 关键结果
AVC-Reward与人类判断的对齐度达到现有自动方法SOTA，可输出可解释的错误定位依据，作为在线强化学习信号使用时可提升联合生成模型的音视频一致性。
