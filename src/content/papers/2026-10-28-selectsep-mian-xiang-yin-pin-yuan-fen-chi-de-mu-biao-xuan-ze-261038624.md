---
title: 'SelectSep: Target-Selective Video Queries for Audio Source Separation'
title_zh: SelectSep：面向音频源分离的目标选择性视频查询方法
authors:
- Suyeon Lee
- Doyeop Kwak
- Joon Son Chung
affiliations:
- Korea Advanced Institute of Science and Technology
arxiv_id: '2610.38624'
url: https://arxiv.org/abs/2610.38624
pdf_url: https://arxiv.org/pdf/2610.38624
published: '2026-10-28'
collected: '2026-10-31'
category: Other
direction: 多模态音频分离 · 轻量目标查询
tags:
- Audio-Separation
- Multimodal-Query
- Target-Selection
- Feature-Distillation
- Visual-Encoder
one_liner: 联合文本与点击坐标实现无需推理分割的高精准视频查询音频分离
practical_value: '- 多模态召回/搜索场景可借鉴「文本+轻量点击交互」组合指定目标的思路，降低用户输入成本的同时大幅提升召回精准度

  - 视觉特征提取模块可复用带多条件约束的目标特征蒸馏方法，无需额外分割模块即可提取细粒度目标特征，降低推理部署开销

  - 同类干扰项的评测场景设计可迁移到推荐系统难例评测pipeline，验证模型对相似item/query的区分能力'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频查询音频分离（VQSS）依赖整段场景视频作为查询输入，当画面内存在多个发声对象、尤其是语义相似干扰源时，查询歧义极高，过往优化方案依赖推理阶段的分割模块，大幅增加部署成本。

### 方法关键点
1. SelectSep框架仅需文本+单次点击坐标两个轻量输入即可指定目标源与实例，推理阶段无需分割模块；
2. 通过文本+点击条件约束的目标特征蒸馏适配视觉编码器，再用适配后的视觉特征微调分离器；
3. 新增同屏干扰评测设置，专门验证模型的目标选择能力。

### 关键结果
在标准基准和同屏干扰设置下，分离质量和目标选择精度均获得一致提升，尤其针对语义相似源混合的场景效果提升更显著。
