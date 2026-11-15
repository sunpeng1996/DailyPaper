---
title: 'GA-HEL: A Knowledge-Driven Expert System for Open-Set, Granularity-Aware Hierarchical
  Event Linking in Social Media'
title_zh: GA-HEL：面向社交媒体的粒度感知开放集分层事件链接专家系统
authors:
- Shengqi Zhou
- Zhigang Liu
- Wenxiang Zhu
- Zhentao Cang
affiliations:
- Northeast Petroleum University
- Heilongjiang Petroleum Big Data and Intelligent Analysis Key Laboratory
- Tongji University
- Northwestern Polytechnical University
arxiv_id: '2611.16194'
url: https://arxiv.org/abs/2611.16194
pdf_url: https://arxiv.org/pdf/2611.16194
published: '2026-11-12'
collected: '2026-11-15'
category: Other
direction: 开放集分层事件链接 · 知识驱动专家系统
tags:
- Event Linking
- Knowledge-Driven System
- Open-Set Recognition
- Hierarchical Reasoning
- Social Media Analytics
one_liner: 提出三阶段漏斗式知识驱动系统GA-HEL，实现社交媒体开放集粒度感知分层事件链接
practical_value: '- 三阶段漏斗架构可复用在分层标签匹配场景（如电商类目关联、用户分层意图识别），先做开放集过滤再层级推理，减少无效计算

  - 分层推理后加确定性合法路径校验的trick，可迁移到生成式推荐的结果校验环节，避免输出不符合类目层级的非法结果

  - 预冻结所有待评估方法输出再做人工标注的评估协议，可用于业务多策略的公平离线对比，规避标注偏见'
score: 4
source: arxiv-cs.IR
depth: abstract
---

### 动机
社交媒体事件智能需要判定帖子是否归属已注册事件空间，匹配到对应层级路径并停在证据支持的最深粒度，现有方案缺乏显式范围控制与层级合法性保障。
### 方法关键点
采用三阶段知识驱动漏斗架构：1）开放集范围控制先过滤非库内样本，缩小候选范围；2）层级感知解码器选择匹配路径与深度；3）确定性合法路径校验后输出符合入库要求的结构化结果。
### 关键结果
在200条帖子试点集完成机制开发，497条标注扩展集（含4个unseen事件线、难负例）上性能与全局全卡推理强基线持平，同时具备显式范围控制能力，输出均符合层级约束。
