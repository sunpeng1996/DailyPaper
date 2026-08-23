---
title: Personalized Digital Semantic Communication for Image Transmission with Vision-Language
  Models
title_zh: 基于视觉语言模型的个性化数字语义通信图像传输框架
authors:
- Nan Li
- Li Zhou
- Haijun Wang
- Jun Xiong
- Haitao Zhao
- Jibo Wei
affiliations:
- College of Electronic Science, National University of Defense Technology, China
arxiv_id: '2608.14260'
url: https://arxiv.org/abs/2608.14260
pdf_url: https://arxiv.org/pdf/2608.14260
published: '2026-08-14'
collected: '2026-08-23'
category: Other
direction: 个性化语义通信 · 多模态内容传输
tags:
- VLM
- Latent Diffusion Model
- Semantic Communication
- Vector Quantization
- Personalization
one_liner: 融合VLM与隐扩散模型实现带宽受限场景下用户感知的个性化图像语义传输
practical_value: '- 电商个性化商品图渲染场景可借鉴「同时输入源内容+用户历史交互提取个性化语义token」的设计，提升内容与用户偏好匹配度

  - 移动端低带宽场景下商品图推流可参考「语义token向量量化转定长比特流」的压缩方案，降低传输带宽同时保留语义一致性

  - 个性化内容生成的评估指标可复用「源内容保真度+用户偏好对齐度」的联合度量思路，替代单一内容相似度指标'
score: 4
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有语义通信（SC）方案大多无用户感知能力，忽略接收方关联语义，无法满足AR、个性化内容分发等视觉密集型应用的低带宽高匹配传输需求。
### 方法关键点
1. 提出PDSC框架，VLM作为语义编码器同时输入源图像、接收方历史交互，提取融合源信息与用户偏好的个性化语义token，经向量量化转为离散语义索引后编码为定长紧凑比特流，兼容数字传输；
2. 接收端采用LDM作为语义解码器，基于恢复的语义token重建个性化图像；
3. 定义容量约束下的个性化语义率失真问题，设计联合源语义保真度、用户偏好对齐度的语义失真度量。
### 关键结果
带宽受限无线传输场景下，相比CDDM、MoS等SOTA语义通信基线，源语义一致性、个性化效果均表现更优。
