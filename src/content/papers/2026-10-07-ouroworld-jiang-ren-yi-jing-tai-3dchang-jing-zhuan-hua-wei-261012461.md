---
title: 'OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs'
title_zh: OuroWorld：将任意静态3D场景转化为无限循环3D动态 Cinemagraph
authors:
- You-Zhe Xie
- Ting-Wei Chou
- Yu-Hsuan Li
- Kaipeng Zhang
- Zhixiang Wang
- Yu-Lun Liu
affiliations:
- National Yang Ming Chiao Tung University
- Alaya Lab
arxiv_id: '2610.12461'
url: https://arxiv.org/abs/2610.12461
pdf_url: https://arxiv.org/pdf/2610.12461
published: '2026-10-07'
collected: '2026-10-10'
category: Other
direction: 3D动态场景生成 · 4D高斯喷溅
tags:
- 3D Gaussian Splatting
- 4D Generation
- Dynamic Scene
- Video Synthesis
- Vision-Language Model
one_liner: 提出无掩码框架将静态3D Gaussian Splatting场景转为任意视角无缝循环的动态3D Cinemagraph
practical_value: '- 电商3D商品展示、虚拟直播间场景可直接复用该框架生成无缝循环动态效果，提升用户停留时长

  - 傅里叶级数形变场构造周期一致性的思路可迁移至生成式推荐的短视频/直播片段循环生成场景，避免内容跳变

  - 无真值的多维度AIGC效果评估方案可借鉴到内容类推荐的内容质检环节，降低人工标注成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有3D世界模型生成的高逼真可探索场景均为静态，无动态变化；已有动态3D生成方法仅支持流体类运动，跨视角一致性差、循环衔接存在明显断层。
### 方法关键点
1. 无掩码端到端框架：输入任意静态3D Gaussian Splatting场景，由VLM推理符合常识的动态逻辑，引导视频模型生成参考视频后升维补全为多视角视频；
2. 提出不一致鲁棒周期4DGS：用Fourier-series形变场从构造上保证循环一致性，锚定参考视角的Grounded Drift Field吸收跨视角生成误差，支持通用形变、物体运动、光照变化等多种动态效果。
### 关键结果
在39个重建/生成场景上性能超过所有基线，用户研究偏好胜率达70.8%~99.0%
