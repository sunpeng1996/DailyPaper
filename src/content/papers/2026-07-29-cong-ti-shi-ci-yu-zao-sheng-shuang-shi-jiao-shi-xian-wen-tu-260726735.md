---
title: 'Dual Inversion for Text-to-Image Diffusion Models: From Both Prompt and Noise
  Perspectives'
title_zh: 从提示词与噪声双视角实现文生图扩散模型的双向反转
authors:
- Xiaolong Liu
- Junjian Li
- Yuan Xiao
- Jiaqi Deng
- Dayong Ye
- Tianqing Zhu
- Huan Huo
affiliations:
- University of Technology Sydney
- Geely
- City University of Hong Kong
- City University of Macau
arxiv_id: '2607.26735'
url: https://arxiv.org/abs/2607.26735
pdf_url: https://arxiv.org/pdf/2607.26735
published: '2026-07-29'
collected: '2026-08-01'
category: Multimodal
direction: 多模态 · 文生图扩散模型反转与可控编辑
tags:
- Diffusion Model
- Prompt Inversion
- Text-to-Image
- Controllable Generation
- Latent Noise
one_liner: 提出双阶段Dualin方法联合反演目标图像的语义提示词与隐噪声，大幅提升文生图保真度与可控性
practical_value: '- 电商商品图复刻、改款场景可复用双阶段反转逻辑：先反演可解释提示词保证语义对齐，再反演隐噪声保证结构一致，避免生成图失真

  - 可控AI作图工具开发可直接复用无监督DDIM反演模块，无需重新优化即可实现同结构下的风格、元素编辑，降低工程实现成本

  - 素材库生成场景可通过该方法批量反演现有素材的标准提示词，构建高质量素材-提示词平行语料库，用于后续生成模型微调'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有文生图扩散模型的Prompt Inversion方法存在明显缺陷：梯度类方法不稳定、生成图伪影严重；无梯度类方法能生成可读提示词，但无法对齐细粒度细节，保真度不足。核心原因是仅将提示词反演作为充分条件，忽略了编码结构信息的隐空间噪声的关键作用。

### 方法关键点
提出双阶段Dualin方法：第一阶段融合CLIP与LLM反演得到忠实、可解释的硬提示词，保证语义对齐；第二阶段通过无监督DDIM反演重建目标图像的精确隐空间噪声，保证结构信息一致性。理论证明反演得到的噪声无需重新优化即可支持灵活图像编辑。

### 关键结果
在多数据集上的实验表明，Dualin同时生成高质量可解释反演提示词，图像保真度达到SOTA，为精准可控图像编辑提供了可靠基础。
