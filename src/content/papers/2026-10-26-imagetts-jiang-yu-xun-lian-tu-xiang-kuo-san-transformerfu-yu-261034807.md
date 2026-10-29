---
title: 'ImageTTS: Repurposing Pretrained Image Diffusion Transformers for Speech Synthesis'
title_zh: ImageTTS：将预训练图像扩散Transformer复用至语音合成任务
authors:
- Hanchen Pei
- Shujie Liu
- Yayue Deng
- Fangyun Wei
- Yanqing Liu
- Jianwei Yu
- Gongping Huang
affiliations:
- Wuhan University
- Microsoft Corporation
- The Chinese University of Hong Kong
arxiv_id: '2610.34807'
url: https://arxiv.org/abs/2610.34807
pdf_url: https://arxiv.org/pdf/2610.34807
published: '2026-10-26'
collected: '2026-10-29'
category: Multimodal
direction: 跨模态模型复用 · 语音合成
tags:
- Diffusion Transformer
- Cross-modal Transfer
- TTS
- VAE
- Flow Matching
one_liner: 复用预训练图像扩散模型FLUX.2的VAE与DiT，跨模态迁移实现高保真可控语音合成
practical_value: '- 跨模态预训练模型复用思路可迁移到生成式推荐：将图像/文本预训练扩散模型轻量适配生成商品图文、短视频文案，无需从零训练模态专属模型，降低训练成本

  - 「冻结主干预训练权重+仅微调少量适配层」范式可复用：在Agent多模态理解/生成模块冻结大模型主干，仅适配电商场景语音/图像输出需求，保障生成质量同时提升收敛速度

  - 伪模态转换技巧可借鉴：将推荐场景用户行为序列转为伪图像输入预训练图像DiT，利用视觉预训练的长序列建模能力做用户兴趣建模'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
预训练图像生成模型的表征与生成先验能否跨模态迁移到非视觉任务尚未被验证，尤其是对语言保真度、说话人特征保留要求高的语音合成场景。
### 方法关键点
将log-mel语谱图转换为伪RGB格式，输入冻结的FLUX.2图像VAE完成编码，仅采用条件潜流匹配微调预训练Diffusion Transformer（DiT）层，解耦表征迁移（VAE路径）与生成先验迁移（DiT初始化路径）两个独立的跨模态迁移过程。
### 关键结果
- 冻结图像VAE可实现0.99 STOI、0.95说话人相似度，保留语音可懂度与身份特征
- 预训练DiT初始化相比随机初始化，100k训练步时WER从4.2%降至2.7%，收敛更快、语言准确率更高
- 10万小时语音数据训练后，Seed-TTS英文测试集WER达1.12%，CapSpeech风格准确率0.66，优于同数据量训练的语音原生基线
