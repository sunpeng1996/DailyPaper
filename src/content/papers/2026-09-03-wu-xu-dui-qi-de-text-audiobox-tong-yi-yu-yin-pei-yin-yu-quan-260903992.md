---
title: Alignment-Free Text-Audiobox for Voice Dubbing and Full-Duplex Dialogue Synthesis
title_zh: 无需对齐的Text-Audiobox：统一语音配音与全双工对话合成框架
authors:
- Sanyuan Chen
- Min-Jae Hwang
- Sho Inoue
- Anna Sun
- Bokai Yu
- David Kant
- Dongmin Hyun
- Dorian Desblancs
- Gregory Antonovsky
- Oleg Repin
affiliations:
- FAIR at Meta
arxiv_id: '2609.03992'
url: https://arxiv.org/abs/2609.03992
pdf_url: https://arxiv.org/pdf/2609.03992
published: '2026-09-03'
collected: '2026-09-05'
category: Multimodal
direction: 多模态生成 · 无对齐文本转语音合成
tags:
- Text-to-Speech
- Diffusion Transformer
- Flow Matching
- Latent Diffusion
- Voice Synthesis
one_liner: 提出基于流匹配Diffusion Transformer的无对齐统一语音合成框架，在多类语音任务上性能大幅优于现有系统
practical_value: '- 无对齐跨模态映射思路可迁移至文本转营销语音、文本转商品短视频场景，省去强制对齐预处理成本

  - 高压缩比DAC-VAE特征编码方案可复用在音频生成类业务，大幅降低推理显存占用与时延

  - 多阶段基于自动指标的重排序策略，可直接套用到所有AIGC生成类任务的后处理环节提升输出质量

  - 框架可直接落地电商AI数字人实时对话、直播内容多语言配音等业务场景'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有语音合成系统依赖强制对齐与显式时长预测，预处理成本高，跨任务适配性差，难以同时覆盖配音、长对话等多场景需求。

### 方法关键点
1. 基于流匹配训练的Diffusion Transformer backbone，采用DAC-VAE特征做潜变量扩散，将48kHz音频编码为25Hz潜序列，压缩率超原有EnCodec方案10倍，同时提升重构质量
2. 无对齐架构：直接调用开源文本编码器，通过交叉注意力自动学习文本-语音对齐，省去强制对齐和显式时长预测步骤
3. 3B参数模型预训练用48万小时单语言语音数据，微调适配3类下游任务；推理支持最长1分钟零样本生成，通过多扩散方案支持任意长文本生成，新增多阶段重排序提升输出质量

### 关键结果
- 真实配音基准上，韵律/音色相似度、自然度、可分享性均大幅优于Meta内部最新配音系统
- 短对话生成效果接近人类录音，长对话拟人度、表现力远超内部最新模型，原生支持话轮转换、反馈词、情感动态建模
- 情感对话任务上情感对齐和交互质量显著优于无情感条件基线
