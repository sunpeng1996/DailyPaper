---
title: 'MusicLayout: Explicit Structural Planning for Controllable Text-to-Music Generation'
title_zh: MusicLayout：面向可控文本生成音乐的显式结构规划方法
authors:
- Shuyu Li
- Kejun Zhang
- Jiahe Lei
- Shulei Ji
- Zihao Wang
- Jiaxing Yu
- Wanying Wu
- Lei Wang
affiliations:
- Zhejiang University
- The Chinese University of Hong Kong
- Shandong University
- Ant Group
arxiv_id: '2608.09035'
url: https://arxiv.org/abs/2608.09035
pdf_url: https://arxiv.org/pdf/2608.09035
published: '2026-08-10'
collected: '2026-08-13'
category: Multimodal
direction: 多模态生成 · 可控文本到音乐生成
tags:
- Text-to-Music
- Controllable Generation
- Intermediate Representation
- Autoregressive Model
- Multimodal Generation
one_liner: 提出显式中间表示MusicLayout，实现可预编辑、结构可控的文本到音乐生成
practical_value: '- 生成类任务可引入显式中间规划层，代替端到端黑盒生成，支持用户干预中间结果后再生成最终产物，可迁移到电商文案、Banner生成等场景

  - 统一autoregressive框架下先规划结构再生成内容的范式，可复用在长文本生成、多片段组合的商品种草内容生成等任务中

  - 中间表示可解释、可编辑的设计思路，能降低生成结果的badcase率，减少内容审核成本，适合电商UGC/PGC内容生产链路'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有文本到音乐生成系统仅依赖全局文本prompt，音乐结构组织过程隐式黑盒化，无法在音频生成前完成结构的检查、调整与修正，长片段生成的结构一致性与可控性较差。

### 方法关键点
1. 提出MusicLayout显式中间表示，将音乐拆解为时间对齐的段落、织体、重复变奏、乐器编排要素，作为文本意图与生成音频之间的可解释规划层
2. 基于统一自回归范式搭建生成框架，单序列内先生成MusicLayout表示，再基于该表示预测音频token
3. 支持生成音频前对MusicLayout进行人工编辑，实现布局级的结构可控性

### 关键结果
通过布局条件生成、布局修改、匹配数据消融三类实验验证：显式布局规划可有效提升长程音乐结构组织效果，布局级结构控制能力得到落地支持，无公开具体量化指标
