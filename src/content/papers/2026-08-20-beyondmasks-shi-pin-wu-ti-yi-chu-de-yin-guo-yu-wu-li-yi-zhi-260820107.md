---
title: 'BeyondMasks: Evaluating Causal and Physical Consistency in Video Object Removal'
title_zh: BeyondMasks：视频物体移除的因果与物理一致性评估
authors:
- Yigit Ekin
- Enes Sanli
- Aykut Erdem
- Erkut Erdem
- Aysegul Dundar
affiliations:
- Bilkent University
- Koç University
- Hacettepe University
- KUIS AI Center
arxiv_id: '2608.20107'
url: https://arxiv.org/abs/2608.20107
pdf_url: https://arxiv.org/pdf/2608.20107
published: '2026-08-20'
collected: '2026-08-21'
category: Other
direction: 视频生成编辑 · 因果一致性评估
tags:
- Video Editing
- Causal Consistency
- Evaluation Benchmark
- Vision-Language Model
- Generative Video
one_liner: 提出因果一致性视频物体移除基准与多模态评估协议，填补现有评估仅关注局部保真的缺陷
practical_value: '- 做电商短视频商品擦除、背景改稿时，不能仅校验擦除区域视觉一致性，需同步处理阴影、倒影、光照等附属效应，降低用户感知违和感

  - 做AIGC编辑效果自动评估时，可借鉴CORE的多模态评估框架，结合「物体消失+附属效应一致性」双维度，比单像素相似度指标更贴近人类判断

  - 搭建指令驱动视频编辑工具时，可复用BeyondMasks的数据集结构构建测试集，覆盖不同物理交互场景的边界case，提升工具鲁棒性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有视频物体移除评估仅聚焦掩码区域局部填充保真，忽略物体移除作为因果干预需同步消除阴影、倒影、光照变化、动态痕迹等物理附属效应，且缺乏对齐的真实场景基准支撑因果一致性系统评估。

### 方法关键点
1. 构建BeyondMasks配对基准，包含时序对齐的合成+真实世界视频对，带干净背景参考，覆盖光度、几何、体积、动态交互等多类场景，支持掩码驱动、指令驱动两种编辑模式
2. 提出CORE结构化视觉语言模型评估协议，联合度量物体消失一致性、附属效应一致性两个维度

### 关键结果
现有SOTA方法即使掩码区域保真度极高，仍普遍存在次级物理效应移除失败问题；CORE评估结果与人类判断的对齐度显著优于传统指标，暴露了视觉合理性与因果正确性之间的显著差距
