---
title: 'UniVOE: A Removal-Driven Framework for Interaction-Aware Universal Video Object
  Editing'
title_zh: UniVOE：面向交互感知的通用视频对象编辑的移除驱动框架
authors:
- Shuzhou Yang
- Lanqing Guo
- Lingen Li
- Weiqi Li
- Zhao Zhong
- Liefeng Bo
- Jian Zhang
affiliations:
- Peking University
- Tencent Hunyuan
- The Chinese University of Hong Kong
arxiv_id: '2610.31641'
url: https://arxiv.org/abs/2610.31641
pdf_url: https://arxiv.org/pdf/2610.31641
published: '2026-10-22'
collected: '2026-10-24'
category: Multimodal
direction: 多模态视频对象编辑框架
tags:
- Video Editing
- Multimodal Generation
- Data Generation
- Reward Model
- Transfer Learning
one_liner: 利用视频物体移除模型生成配对训练数据，解决注入任务标注稀缺问题，实现两类编辑SOTA
practical_value: '- 针对难收集标注的生成类任务（如电商商品视频特效合成），可先用易训练的反向任务生成大规模配对训练数据，大幅降低标注成本

  - 生成类任务可采用「迁移领域预训练先验做基础训练+奖励模型后对齐」的 pipeline，平衡训练效率和人类感知效果

  - 互逆业务任务（如内容生成/擦除、用户行为的正向/反向建模）可联合训练共享数据和先验，降低整体研发成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
视频对象移除与注入是互逆编辑操作，移除可通过视频补全预训练先验快速落地，但注入任务需要大规模精准对齐的配对标注，真实配对数据采集难度极高，合成数据的真实度和多样性无法满足要求。

### 方法关键点
1. 先迁移视频补全预训练先验，在小范围「有目标物体/无目标物体」配对数据上微调，得到可感知物体交互效果（阴影、形变、光照等）的移除模型；
2. 用训练好的移除模型将真实有物体视频转换为对应无物体版本，生成大规模配对标注，反向训练注入模型，还原物体及对应的交互效果；
3. 引入自有奖励模型做基于偏好的后训练，解决像素级重构无法匹配人类感知的问题。

### 关键结果
对比开源及商业SOTA系统，在物体移除、注入两类任务上均达到最优性能，复杂交互效果场景下优势尤其突出。
