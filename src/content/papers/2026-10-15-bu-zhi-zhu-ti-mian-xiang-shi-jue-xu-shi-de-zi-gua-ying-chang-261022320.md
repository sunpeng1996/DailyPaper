---
title: 'Not Just a Subject: Capturing Adaptive Scene-Specific Variance for Visual
  Storytelling'
title_zh: 不止主体：面向视觉叙事的自适应场景特定方差捕捉方法
authors:
- SeungJu Cha
- Ye-Chan Kim
- Kwanyoung Lee
- Dong-Jin Kim
affiliations:
- Hanyang University
arxiv_id: '2610.22320'
url: https://arxiv.org/abs/2610.22320
pdf_url: https://arxiv.org/pdf/2610.22320
published: '2026-10-15'
collected: '2026-10-17'
category: Multimodal
direction: 多模态生成 · 视觉叙事文生图优化
tags:
- Diffusion Model
- Text-to-Image
- Visual Storytelling
- Identity Preservation
- Training-free
one_liner: 提出无需训练的EOS-Story框架，平衡视觉叙事生成的主体一致性与场景适配性
practical_value: '- 电商商品场景化图生成可复用prompt解耦思路，将商品特征与场景子提示拆分避免信息稀释，结合外观残差注入保留商品辨识度，无需微调即可生成适配不同营销场景的商品素材

  - 多模态生成类Agent的身份一致性需求可借鉴Adaptive Identity Preservation方案，解决不同场景下主体特征尺度不匹配导致的生成伪影问题

  - 训练免优化的跨模态特征注入思路可大幅降低落地成本，无需重新微调大模型即可快速适配特定垂类生成任务'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有面向视觉叙事的文生图方法过度聚焦主体身份保留，无法适配多样场景变化，易出现语义错位、结构僵化、生成伪影问题，且大多需要额外训练成本。
### 方法关键点
1. 提出训练免优化的EOS-Story框架，跨文本、视觉双空间平衡身份一致性与场景适配性；
2. 文本空间将叙事解耦为身份、场景子提示，通过跨上下文桥接将短语级外观残差软注入场景<EOS>嵌入，解决场景侧无外观线索问题；
3. 视觉空间引入自适应身份保留机制，通过身份锚定将身份特征对齐到场景特定尺度，再经身份感知自注意力融合，解决尺度不匹配导致的结构伪影。
### 关键结果
在原有Consistory+及新增的多构图场景拓展基准Consistory+_+上，性能达到可比或业界最优水平
