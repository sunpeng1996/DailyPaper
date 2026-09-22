---
title: 'PrismGPT: Proxy-Guided Learning for Region-Aware Photo Editing with Self-Synthesized
  Reasoning'
title_zh: PrismGPT：基于自合成推理的区域感知图像编辑代理引导学习框架
authors:
- Ke Zhao
- Hue Nguyen
- Abhijith Punnappurath
- Zhongling Wang
- Iqbal Mohomed
- Michael S. Brown
affiliations:
- AI Center-Toronto, Samsung Electronics
arxiv_id: '2609.24768'
url: https://arxiv.org/abs/2609.24768
pdf_url: https://arxiv.org/pdf/2609.24768
published: '2026-09-21'
collected: '2026-09-22'
category: Other
direction: 多模态大模型 · 区域感知图像编辑
tags:
- VLM
- Image Editing
- Proxy Task
- Curriculum Learning
- Self-Synthesized Reasoning
one_liner: 提出带自合成推理的VLM区域感知图像编辑框架，仅用6%训练数据达到SOTA
practical_value: '- 多任务训练可复用代理任务+能力感知动态调度范式：先训练简单子任务打基础，随技能掌握度逐步切换主任务权重，可适配LLM4Rec多目标优化、多模态推荐模型训练场景

  - 自合成推理轨迹做SFT的方案可直接复用：无需依赖外部更强的教师模型，能大幅降低垂类场景（如电商商品文案生成、推荐理由生成）的微调标注成本

  - 小样本达SOTA的训练思路可迁移到样本稀缺的垂类业务：如小众品类推荐、定制化广告素材生成，用代理任务预训练打底+少量目标域数据微调即可拿到不错效果'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
专业图像修图需要结合全局调整与基于语义掩码的区域局部编辑，现有自动化方法仅能覆盖部分工作流；直接训练VLM同时完成全局+局部审美缺陷诊断、精准编辑参数预测，面临组合决策空间过大的挑战。

### 方法关键点
1. 推出PrismGPT VLM框架，单张输入图像即可输出结构化区域感知编辑计划，无需依赖商业黑盒工具
2. 采用代理引导学习：设计操作分解、区域感知审美排序两个简单代理任务训练基础能力，搭配基于能力的动态调度器，随技能掌握程度逐步将训练权重从代理任务转移到主编辑任务
3. 所有SFT所用推理轨迹均由同个基模型自合成，无需外部强教师模型

### 关键结果
在MIT-Adobe FiveK和新提出的专业修图基准SPIRE上达到SOTA，训练数据用量仅为之前最优方法的6%
