---
title: 'Class Activation Mapping in Explainable Computer Vision: A Method-Centered
  Review of CNN, Transformer, and Foundation-Model-Era Visual Explanations'
title_zh: 可解释计算机视觉中的类激活映射：CNN、Transformer及大模型时代方法综述
authors:
- AmirHossein Eshghi
- Hamid Saadatfar
- Seyyed Ali Hoseini
- AmirMohsen Eshghi
- Siavash Arjomand Bigdel
affiliations:
- University of Birjand, Iran
- Technical University of Denmark, Denmark
arxiv_id: '2608.12299'
url: https://arxiv.org/abs/2608.12299
pdf_url: https://arxiv.org/pdf/2608.12299
published: '2026-08-12'
collected: '2026-08-13'
category: Other
direction: 可解释CV · 类激活映射方法综述
tags:
- CAM
- Explainable AI
- Computer Vision
- CNN
- Transformer
- Foundation Model
one_liner: 系统梳理2016年来57篇类激活映射相关论文，搭建分类体系并总结领域趋势与现存研究缺口
practical_value: '- 多模态商品/广告推荐的可解释性需求，可借鉴CAM的特征归因逻辑，定位视觉内容中影响CTR/CVR的核心区域

  - 弱监督视觉相关业务（如商品主图卖点区域识别、瑕疵检测）可直接复用综述梳理的无梯度CAM类轻量方法

  - 多模态大模型在推荐场景的可解释性评估，可参考综述整理的faithfulness、robustness等多维度评估框架'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
类激活映射（CAM）是可解释AI领域应用最广泛的视觉解释方法族，可输出高亮模型决策关键区域的热力图，但2016年以来相关方法迭代快、适配架构分散，缺乏体系化梳理。
### 方法关键点
严格筛选2016年后发表的57篇方法类核心论文，按照归因机制、架构依赖、评估目标三个维度搭建分类体系，分三类梳理方法：梯度类CAM、混合类CAM、架构感知类CAM，覆盖CNN、Transformer、CLIP/DINO/SAM等大模型时代适配方案。
### 关键结果
领域整体从单CNN层单类别解释，向多层对比、概率化、Token感知、大模型适配的方向演进；当前评估体系高度碎片化，不同研究在忠实度、定位能力、鲁棒性、计算成本、人类信任度等维度的评估协议不统一，存在大量待填补缺口。
