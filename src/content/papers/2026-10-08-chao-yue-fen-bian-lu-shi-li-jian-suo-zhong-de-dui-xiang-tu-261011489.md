---
title: 'Beyond Resolution: Object-to-Image Ratio Mismatch in Instance Retrieval'
title_zh: 超越分辨率：实例检索中的对象-图像占比不匹配问题
authors:
- Boaz Meivar
- Ofir Kedem
- Amit Edenzon
- Gal Chechik
- Shai Avidan
affiliations:
- Tel Aviv University
- Bar-Ilan University
arxiv_id: '2610.11489'
url: https://arxiv.org/abs/2610.11489
pdf_url: https://arxiv.org/pdf/2610.11489
published: '2026-10-08'
collected: '2026-10-09'
category: Other
direction: 视觉实例检索 · 鲁棒性优化
tags:
- Instance Retrieval
- O2I Ratio Mismatch
- Scale Augmentation
- LoRA
- OWLv2
one_liner: 发现实例检索跨尺寸性能下降主因是O2I占比不匹配，提出无需修改库索引的SOTA优化方案
practical_value: '- 电商同款商品检索场景，可优先排查query与库图的商品占比不匹配问题，无需盲目提升图像分辨率浪费算力

  - 存量检索系统无需修改预构建的商品图库索引，仅在query侧新增尺度增强+OWLv2裁剪重排即可大幅提准

  - 高吞吐线上场景可对检索模型做LoRA微调学习O2I鲁棒性，单轮前向即可匹配query侧增强效果，延迟增量极低'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
视觉实例检索中相同对象在query与库图表观尺寸不同时性能骤降，过往普遍归因于分辨率损失，根因未得到明确量化验证。
### 方法关键点
1. 构建3021个Objaverse对象的受控渲染基准，拆分分辨率与O2I（对象-图像占比）的独立影响；
2. 提出无库索引修改的优化方案：query侧尺度增强+OWLv2裁剪重排；
3. 用LoRA微调模型学习O2I鲁棒性，单前向即可获得增益，适配高吞吐场景。
### 关键结果
12个预训练骨干中9个的跨距离性能下降80%以上来自O2I不匹配，多尺度架构仅能缓解分辨率影响，对O2I问题无改善；优化方案在ILIAS 100M基准上mAP@1000从29.2提升至42.0，达到SOTA；LoRA微调效果与query侧增强完全持平。
