---
title: 'Group-of-Latents: Perceptual Video Compression at Extreme Bitrates via Masked
  Latent Generative Modeling'
title_zh: 基于掩码隐层生成建模的极低位率感知视频压缩框架
authors:
- Shaokang Wang
- Jinchang Xu
- Peidong Jia
- Zhijian Hao
- Siyuan Qian
- Fei Zhao
- Rui Ma
- Xiaozhu Ju
- Jian Tang
- Xiaodong Xie
affiliations:
- 北京大学
- 西安电子科技大学
- X-humanoid（北京）
arxiv_id: '2607.19437'
url: https://arxiv.org/abs/2607.19437
pdf_url: https://arxiv.org/pdf/2607.19437
published: '2026-07-21'
collected: '2026-07-23'
category: Other
direction: 生成式视频编码 · 极低位率感知压缩
tags:
- Video Compression
- Diffusion Transformer
- Latent Generative Modeling
- Perceptual Coding
one_liner: 提出GoL隐层分组策略结合预训练DiT先验，实现<0.005bpp极低位率下SOTA感知质量视频压缩
practical_value: '- 弱网电商短视频/直播分发场景可复用GoL隐层分组策略：仅编码少量关键帧隐层作为锚点，生成预测帧隐层，大幅降低带宽开销，适配下沉市场用户的内容触达需求

  - 推荐系统稀疏行为补全可借鉴该架构思路：仅存储少量用户关键交互隐层作为锚点，用大模型先验生成中间缺失的行为隐层，降低特征存储与传输成本

  - 资源约束场景的大模型落地可复用「预训练大模型先验+轻量化适配模块」范式：无需端到端重训大模型，仅优化小体量编码模块即可拿到SOTA效果，降低落地成本'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有视频压缩多采用变换量化范式，极低位率（<0.005bpp）场景下的感知质量优化严重不足，无法满足弱网环境下的内容分发需求。
### 方法关键点
1. 提出Group-of-Latents（GoL）策略，在因果Tokenizer隐空间将隐流划分为I类关键帧隐层、P类预测帧隐层
2. 用I-DCM深度压缩模块编码I类隐层，以极低开销保留感知锚点
3. 基于预训练DiT的统一隐层去噪模块U-LDM，以I类隐层为锚点优化帧内纹理，从噪声中生成P类隐层，零额外比特成本重建时序动态
### 关键结果
在<0.005bpp的极低位率区间达到SOTA感知保真度，同时具备丰富空间细节与鲁棒时序一致性。
