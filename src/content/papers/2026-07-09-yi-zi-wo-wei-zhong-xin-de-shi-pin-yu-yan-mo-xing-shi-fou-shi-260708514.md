---
title: Do Egocentric Video-Language Models Capture Both Hand- and Object-Centric Cues?
title_zh: 以自我为中心的视频语言模型是否同时捕捉手部与物体中心线索？
authors:
- Masatoshi Tateno
- Alexandros Stergiou
- Risa Shinoda
- Yoichi Sato
- Dima Damen
affiliations:
- The University of Tokyo
- University of Twente
- University of Bristol
arxiv_id: '2607.08514'
url: https://arxiv.org/abs/2607.08514
pdf_url: https://arxiv.org/pdf/2607.08514
published: '2026-07-09'
collected: '2026-07-11'
category: Multimodal
direction: 多模态视频理解 · 手物交互识别
tags:
- Video-Language Model
- Hand-Object Interaction
- Masked Pre-training
- Action Recognition
- Multimodal Evaluation
one_liner: 提出手物掩码训练与HOI动态感知解码器范式，配套解耦评估基准，提升手物交互识别鲁棒性
practical_value: '- 多模态特征解耦学习可借鉴手物掩码训练思路，直播/AR电商场景中分离用户交互手势、商品本身特征，提升商品识别与交互意图理解准确率

  - 解耦评估范式可复用在多模态推荐效果验证，单独验证用户行为特征、物品特征对推荐结果的贡献，排查模型对伪关联shortcut的依赖

  - 辅助预测增强目标嵌入的方法可迁移到多模态召回，加入物品位置、语义辅助预测任务，提升多模态召回中核心目标的特征敏感性'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有以自我为中心的视频语言模型做手物交互（HOI）识别时，依赖手、物体、环境的伪关联shortcut，而非基于手和物体本身的外观、动态特征推理，鲁棒性差。
### 方法关键点
1. 手物掩码训练范式，支持从部分手/物体观测完成鲁棒推理；
2. HOI动态感知解码器，通过辅助预测手、物体的位置与语义，显式学习两类中心嵌入，提升对两类核心线索的敏感度；
3. 构建CI-HOI评估框架与DEHOI测试集，通过图像补全分离手、物体相关观测，实现解耦的HOI效果评估。
### 关键结果
在DEHOI测试集上表现优于现有基线模型，同时在标准动作识别、物体状态识别、机器人操作动作识别任务上均有增益，HOI理解鲁棒性显著提升。
