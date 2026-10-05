---
title: 'Moving Forward with Video Saliency: A New Dataset and Benchmark where Motion
  Matters'
title_zh: 面向运动感知的视频显著性新数据集SalTempto及基准测试
authors:
- Susmit Agrawal
- Rebecca Wanner
- Juliane Verwiebe
- Matthias Tangemann
- Matthias Bethge
- Matthias Kümmerer
affiliations:
- Tübingen AI Center, University of Tübingen
- IMPRS-IS
- Optocycle
- University of Toronto
- Vector Institute
arxiv_id: '2610.03276'
url: https://arxiv.org/abs/2610.03276
pdf_url: https://arxiv.org/pdf/2610.03276
published: '2026-10-02'
collected: '2026-10-05'
category: Other
direction: 视频显著性预测 · 数据集构建
tags:
- Video Saliency
- Dataset
- Benchmark
- Temporal Modeling
- Gaze Prediction
one_liner: 构建高动态视频显著性基准数据集SalTempto，可有效验证时序模型相对静态基线的性能增益
practical_value: '- 做短视频电商广告素材优化时，可参考SalTempto的高动态内容标注逻辑，采集用户gaze数据构建素材吸引力评估模型，提升广告点击率

  - 开发短视频内容理解类Agent（如电商短视频卖点自动提取、违规内容检测）时，可基于该数据集训练时序显著性模型，优先处理用户关注的视频区域，降低计算成本同时提升准确率

  - 构建业务算法基准时，可借鉴其「先验证静态/简单基线的性能上限，再优化基准动态性」的思路，避免自家业务数据集无法区分不同复杂度模型的优劣'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有主流视频显著性基准LEDOV时序模式不足，静态基线即可覆盖超一半可解释gaze信息，时序模型相对静态基线无明显增益，无法区分是模型缺陷还是基准本身问题。
### 方法关键点
构建高动态视频显著性基准SalTempto：从HACS-Segments选取224条1分钟动态视频片段，每条包含完整事件的前因后果，采集最多16名受试者的gaze标注，提供训练拆分支持预训练模型适配。
### 关键结果
- SalTempto上静态基线仅能覆盖centerbias之上13%的性能上限，远低于LEDOV的50%+
- 微调后的SOTA时序模型相比静态基线有显著性能增益，验证了时序信息的价值
- 目前SOTA模型仍有近一半的SalTempto性能上限未被挖掘，时序建模空间充足
