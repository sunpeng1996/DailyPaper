---
title: 'SG-UMP: Sequence-Guided Universal Multimodal Prioritization Calculation Framework'
title_zh: SG-UMP：序列引导的通用多模态优先级计算框架
authors:
- Xinyi Zhang
- Yutong Li
- Peijie Sun
affiliations:
- Imperial College London
- University College London
- Nanjing University of Posts and Telecommunications
arxiv_id: '2608.28503'
url: https://arxiv.org/abs/2608.28503
pdf_url: https://arxiv.org/pdf/2608.28503
published: '2026-08-28'
collected: '2026-08-31'
category: RecSys
direction: 多模态序列推荐 · 可插拔增强插件
tags:
- Multimodal Recommendation
- Sequential Recommendation
- Plug-and-Play
- Module Routing
- MoE
one_liner: 提出可插拔多模态序列推荐插件，同时适配用户偏好异质性与数据集模态偏置
practical_value: '- 可直接将SG-UMP作为插件集成到现有SASRec、STOSA等序列推荐主干，无需重构全模型，即可获得18%-25%的性能提升

  - 多模态模块参数可直接复用：频率过滤层设1层、模态专属专家4个、共享专家2个、互信息损失权重α=0.5，平衡效果与效率

  - 针对不同业务场景（如图像主导的电商、文本主导的本地生活），用Module Router动态调整模块执行顺序，效果优于固定流程

  - 条件互信息损失设计可迁移至多模态路由类任务，避免路由退化为固定路径'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多模态序列推荐（MSR）依赖预训练编码器提取通用特征，存在两大核心缺陷：一是无法捕捉用户级偏好异质性（不同用户对模态的关注度差异大，如部分用户关注商品图、部分用户关注参数文本），二是忽略数据集级模态偏置（不同场景模态优先级不同，如电商场景图像更重要、本地生活点评场景文本更重要），固定的多模态处理流程泛化性差，限制推荐效果。

### 方法关键点
- 整体为可插拔插件，不替换原有SR主干，仅增强多模态信息处理能力
- Module Combiner集成三类功能模块：频率过滤层（去噪提取稳定低频偏好模式）、层级注意力层（自适应加权不同模态信号，对齐用户偏好）、多尺度融合层（基于MoE架构，分模态专属专家和共享专家，兼顾模态独有特征与跨模态交互）
- Module Router根据输入和数据集模态特征，动态决定三类模块的执行顺序，加入条件互信息损失正则，避免路由退化，适配不同场景特性

### 关键实验
在4个真实数据集（Amazon Home/Beauty/Office、Yelp）上测试，集成到SASRec、STOSA、Oracle4Rec三个主流主干，比原有主干平均提升18.91%-24.93%，比最优多模态基线平均提升7%-17%，仅带来5%-17%的epoch耗时增加。

多模态推荐没有通用的固定处理流程，同时适配用户级偏好异质性和数据集级模态偏置，才能在不同场景下获得稳定的效果提升
