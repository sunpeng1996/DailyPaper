---
title: 'AdaptVPR: Route-Aware Hard Positive Generation for Robust Visual Place Recognition'
title_zh: AdaptVPR：面向鲁棒视觉位置识别的路径感知难正样本生成
authors:
- Shunpeng Chen
- Jingyi Zhang
- Changwei Wang
- Shengpeng Xu
- Yukun Song
- Xingtian Pei
- Jinzhou Lin
- Li Guo
- Shibiao Xu
arxiv_id: '2609.04369'
url: https://arxiv.org/abs/2609.04369
pdf_url: https://arxiv.org/pdf/2609.04369
published: '2026-09-02'
collected: '2026-09-07'
category: Other
direction: 视觉位置识别 · 难正样本生成
tags:
- VPR
- Hard Positive Generation
- Data Augmentation
- Diffusion Models
- Domain Shift
one_liner: 提出路径感知难正样本生成框架AdaptVPR，提升跨域场景下视觉位置识别鲁棒性
practical_value: '- 跨域图像召回（如电商同款识别、线下到线上场景匹配）场景可复用分层难正样本生成思路，拆分全局风格、局部遮挡双路径扩增训练数据，提升模型抗域偏移能力

  - 生成式数据扩增的校验逻辑可直接复用，通过几何一致性+特征多样性双重校验，避免生成样本语义漂移，降低无效训练数据占比

  - 难正样本生成调度策略可参考，根据样本可编辑性和风险约束动态选择生成路径，平衡扩增效率与样本质量'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
VPR任务受光照、天气、季节变化、动态遮挡等域偏移影响性能易退化，核心原因是现有训练数据中同地点样本的外观多样性不足。
### 方法关键点
1. 提出路径感知生成扩增框架AdaptVPR，先通过视觉语言模型解析场景属性、评估编辑可行性，规则调度器根据编辑得分和风险约束选择生成路径；
2. 拆分三条互补生成路径：全局外观路径修改天气/光照/时段，局部遮挡路径插入合理动态遮挡物，双路径结合生成更高难度外观偏移样本；
3. 配套基于几何一致性和外观多样性的VPR定向校验机制，全局样本校验失败直接丢弃，局部/双路径样本可根据校验反馈微调prompt重生成，避免结构漂移。
### 关键结果
生成16万条校验通过的合成难正样本数据集AdaptCities，多VPR基准模型和视觉骨干上测试均获稳定提升，强域偏移场景下R@1最高提升9.2%。
