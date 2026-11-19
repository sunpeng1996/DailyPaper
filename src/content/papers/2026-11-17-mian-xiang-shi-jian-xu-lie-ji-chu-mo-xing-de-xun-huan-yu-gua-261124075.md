---
title: Recurrent Domain Incremental Adaptation of Time-Series Foundation Models
title_zh: 面向时间序列基础模型的循环域增量适配方法
authors:
- Sachith Abeywickrama
- Peiliang Gong
- Emadeldeen Eldele
- Min Wu
- Chau Yuen
affiliations:
- Nanyang Technological University, Singapore
- Institute of Advanced Intelligence and Computing (IAIC), A*STAR, Singapore
- Khalifa University, UAE
arxiv_id: '2611.24075'
url: https://arxiv.org/abs/2611.24075
pdf_url: https://arxiv.org/pdf/2611.24075
published: '2026-11-17'
collected: '2026-11-19'
category: Training
direction: 时序大模型 · 域增量适配
tags:
- TSFM
- Domain Incremental Learning
- Few-shot Adaptation
- Catastrophic Forgetting
- PEFT
one_liner: 提出PACT分块嵌入迁移方法，实现时序大模型少标签域增量适配且无旧知识遗忘
practical_value: '- 电商/推荐场景用户行为时序大模型跨域适配（如不同类目、大促/平日分布漂移）可复用PACT局部分块更新思路，避免全局微调导致旧场景效果下降

  - 少标签新业务场景适配时，可采用「冻结主干+仅学习局部分布残差+门控选通」架构，大幅降低标注数据需求量

  - 应对业务中反复出现的周期性分布（如大促/平日用户行为切换），可保留历史适配残差模块，推理时自动选通无需手动标注场景ID'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
预训练时序基础模型（TSFM）跨域适配时易发生灾难性遗忘，业务场景下通常仅能获取少量新域标注校准数据，且推理时无法提前获知当前域ID，全局适配会破坏原本正确的嵌入表示，导致旧场景效果下降。
### 方法关键点
提出PACT（Piecewise Adaptation via Chart Transport）方法：1）冻结预训练TSFM编码器、分类头与所有历史适配模块，仅针对新域影响的嵌入局部区域学习轻量残差迁移；2）将源嵌入空间划分为局部块，保留恒等映射通路，通过学习的门控为每个输入自动选通恒等映射或任意历史残差迁移模块。
### 关键结果
每个新域仅用5%标注校准数据、推理无需输入域ID的条件下，在4类轴承故障流任务上平均macro-F1保持在0.95以上，多个公开基准均验证其兼顾新域适配与旧知识保留的效果。
