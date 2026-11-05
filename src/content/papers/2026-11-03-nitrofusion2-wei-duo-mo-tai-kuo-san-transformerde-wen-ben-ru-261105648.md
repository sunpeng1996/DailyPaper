---
title: 'NitroFusion2: Bringing Adversarial Loss to the Text Stream of Multimodal Diffusion
  Transformers'
title_zh: NitroFusion2：为多模态扩散Transformer的文本流引入对抗损失
authors:
- Dar-Yen Chen
- Yi-Zhe Song
affiliations:
- University of Surrey
- Turing Elite Research Labs
arxiv_id: '2611.05648'
url: https://arxiv.org/abs/2611.05648
pdf_url: https://arxiv.org/pdf/2611.05648
published: '2026-11-03'
collected: '2026-11-05'
category: Multimodal
direction: 多模态扩散Transformer · 对抗蒸馏加速
tags:
- Multimodal Diffusion
- Adversarial Training
- Distillation
- MMDiT
- Generation Acceleration
one_liner: 提出文本流对抗蒸馏与维度提示判别方法，将多模态扩散蒸馏步数压缩到1-2步且质量相当
practical_value: '- 电商商品图、营销素材等多模态生成场景可复用TSAD思路，用文本中间特征做判别信号，大幅降低扩散模型推理步数，提升实时生成效率

  - ACD维度提示判别机制可迁移到可控生成场景，指定生成内容的风格、材质、文字排版等属性，精准匹配业务对生成结果的要求

  - 1-2步轻量生成方案可落地到高实时性场景，比如直播实时素材生成、推荐流个性化配图、Agent实时内容创作等，降低算力依赖'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统对抗扩散蒸馏仅使用图像特征作为判别依据，多模态扩散Transformer（MMDiT）的文本流通过联合注意力已与图像信息深度绑定，该表征此前未被用于对抗判别。
### 方法关键点
1. 提出Text-Stream Adversarial Distillation（TSAD），将MMDiT中间文本token状态作为新的对抗表征，兼顾文本条件与图像关联信息
2. 提出Aspect-Cued Discrimination（ACD），给判别器输入排版、物体、风格等维度提示，定向强化训练过程中对特定属性的优化
3. 基于NitroFusion的专家判别器架构，整合TSAD与ACD得到NitroFusion2
### 关键结果
将传统4-8步的少步蒸馏压缩到1-2步，生成质量与原 regime 相当；1步生成即可输出清晰渲染文字与丰富细粒度细节，2步生成在所有测试基准上保持竞争力。
