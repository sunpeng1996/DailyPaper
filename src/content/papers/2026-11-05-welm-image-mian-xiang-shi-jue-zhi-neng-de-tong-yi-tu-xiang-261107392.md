---
title: 'WeLM-Image: A Unified Image Generation Model towards Visual Intelligence'
title_zh: WeLM-Image：面向视觉智能的统一图像生成基础模型
authors:
- Canmiao Fu
- Chen Li
- Guohui Zhang
- Hao Lu
- Hongyang Wei
- Huadong Wu
- Huaisong Zhang
- Hubery Yin
- Liyuan Cui
- Qixin Yan
affiliations:
- Tencent Inc. WeChat Vision
arxiv_id: '2611.07392'
url: https://arxiv.org/abs/2611.07392
pdf_url: https://arxiv.org/pdf/2611.07392
published: '2026-11-05'
collected: '2026-11-06'
category: Multimodal
direction: 多模态生成 · 统一架构图像生成与编辑
tags:
- MoE
- Text-to-Image
- Image Editing
- Multimodal Foundation Model
- Single GPU Deployment
one_liner: 腾讯微信团队提出MoT-MoE架构统一图像生成模型，支持单GPU部署，覆盖文生图、指令编辑、多参考合成
practical_value: '- 电商商品图生成、营销海报设计、商品图编辑场景可复用MoT-MoE双路径架构，将语义理解与生成任务解耦减少优化冲突，同时通过MoE稀疏激活降低推理参数量，适配单GPU部署的成本要求

  - 知识驱动视觉词汇+大规模视觉聚类的数据集平衡方法，可迁移到生成式推荐的素材库构建，解决头/长尾素材语义覆盖不均问题，提升生成素材的多样性和prompt对齐率

  - 多任务分别RL优化再通过噪声感知蒸馏合并的策略，可复用在电商多场景生成（主图/详情页/营销配图）的模型训练，兼顾不同任务的效果指标，避免多任务优化冲突

  - Turbo版本的少步蒸馏方法可直接复用在高吞吐量实时生成场景（搜索推荐个性化配图、直播实时素材生成），单H20 GPU上1024×1024图5s内生成的性能可满足线上时延要求'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有图像生成模型普遍存在语义理解与生成任务优化冲突、参数量大部署成本高、多任务（文生图/指令编辑/多参考合成）能力难以兼顾的问题，微信生态大规模C端应用需要低单请求成本、支持单GPU部署的统一视觉生成模型，同时满足多场景的效果要求。
### 方法关键点
- 架构：设计MoT-MoE双路径骨干，理解路径（UND）处理文本、参考图语义特征，生成路径（GEN）处理图像隐层表征，两路通过共享注意力实现跨模态交互，各自独立配置MoE模块，总存储参数量31.7B，每生成token仅激活5.4B参数，大幅降低推理计算量。
- 位置编码：提出文本兼容的统一3D RoPE，完全保留预训练文本位置编码逻辑的同时为图像隐层增加空间结构，无需额外适配模块。
- 数据：搭建生成导向的数据引擎，通过知识 grounded 视觉词汇+大规模视觉聚类平衡语义覆盖和任务分布，配套训练时评估反馈迭代优化数据配比。
- 训练：先对生成、编辑任务分别用打分规则/任务专属checklist做RL优化，再通过噪声感知同策略蒸馏合并为统一模型，最后用MeanFlow少步蒸馏得到低时延Turbo版本。
### 关键结果
- 1536分辨率版本在PRISM-Bench、Qwen-Image-Bench、UnicBench三个开源基准上排名所有参评开源模型第一。
- Turbo版本在单NVIDIA H20 GPU上仅需8步无引导采样即可生成1024×1024图像，耗时4.98s，较50步基础模型提速11.4倍；1-4张参考图的编辑任务耗时仅6.78-13.17s，完全适配单GPU部署要求。
### 核心洞见
多模态生成模型可通过任务路径解耦+稀疏激活的架构设计，在不损失效果的前提下大幅降低部署成本，同时兼顾多场景能力。
