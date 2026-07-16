---
title: 'CD-MED: Cross-Domain Multimodal Emotion Descriptor for Visual Comparison of
  Digital Objects'
title_zh: CD-MED：面向数字对象视觉比较的跨域多模态情感描述符
authors:
- Elnara Kadyrgali
- Muragul Muratbekova
- Pakizar Shamoi
affiliations:
- Kazakh-British Technical University
arxiv_id: '2607.12958'
url: https://arxiv.org/abs/2607.12958
pdf_url: https://arxiv.org/pdf/2607.12958
published: '2026-07-14'
collected: '2026-07-16'
category: RecSys
direction: 跨域多模态推荐 · 统一情感表征
tags:
- Multimodal
- Cross-Domain Recommendation
- Emotion Recognition
- Affective Computing
- Unified Representation
one_liner: 提出跨域多模态情感描述符CD-MED，实现异构数字对象公共情感空间统一表征与跨域比较
practical_value: '- 跨域内容（图文/短视频/直播/书籍）推荐场景可复用公共情感空间映射思路，解决不同模态、不同领域内容的特征异构问题，打通跨域召回通道

  - 商品内容（主图/详情页/短视频/直播切片）的情感标签生成可复用「单模态模型单独推理→统一空间投影」的轻量架构，无需重新训练端到端多模态大模型，大幅降低算力成本

  - 情绪适配型个性化推荐场景，可借鉴valence-arousal二维可视化方案，快速对齐用户情感偏好与内容情感属性，同时提升推荐结果的可解释性'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有情感识别模型多为模态专属，无法直接对电影、歌曲、图文、书籍等异构跨域数字对象做情感维度的比较、检索与推荐，缺乏统一的情感表征框架，限制了情感导向的跨域应用落地。
### 方法关键点
1. 提出CD-MED跨域多模态情感描述符，不同模态先经各自专属的成熟情感识别模型处理，再将输出投影到共享情感空间，既保留单模态情感信息，又生成对象的全局整合情感画像。
2. 设计valence-arousal二维空间可视化规则：位置对应情感坐标、颜色对应情感类别、大小对应情感强度、形状对应模态，大幅提升情感表征的可解释性。
### 关键结果
可直接适配现有各模态成熟的情感识别能力，无需额外端到端训练，支持电影、歌曲、图像、书籍等多领域跨域的情感导向检索、推荐、相似比较任务。
