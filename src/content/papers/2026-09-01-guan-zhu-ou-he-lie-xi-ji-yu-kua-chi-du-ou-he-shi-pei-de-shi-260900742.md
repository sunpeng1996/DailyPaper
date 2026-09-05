---
title: 'Mind the Rift: Cross-Scale Coupling Mismatch for AI-Generated Video Detection'
title_zh: 关注耦合裂隙：基于跨尺度耦合失配的AI生成视频检测
authors:
- Siyu Li
- Jin Yang
- Weiheng Liang
affiliations:
- Sichuan University
- Xizang University
arxiv_id: '2609.00742'
url: https://arxiv.org/abs/2609.00742
pdf_url: https://arxiv.org/pdf/2609.00742
published: '2026-09-01'
collected: '2026-09-05'
category: Other
direction: AIGC内容检测 · 生成视频鉴别
tags:
- AIGC-Detection
- Video-Forensics
- Cross-Scale-Coupling
- Temporal-Modeling
- Encoder-Agnostic
one_liner: 提出基于跨尺度耦合失配的AI生成视频检测框架RIFT，兼具高精度与编码器无关性
practical_value: '- 跨尺度特征耦合校验思路可迁移到电商UGC/AIGC内容风控场景，用于鉴别AI生成的商品宣传视频、营销素材等违规内容

  - 双独立特征流+耦合差异度量的架构可直接复用，无需依赖大参数量编码器即可实现高检测精度，降低工程落地成本

  - 编码器无关特性适配业务侧多模型栈部署需求，可直接对接现有已上线的视觉特征提取链路，无需额外改造'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
AI生成视频逼真度已达电影级，现有检测方法对未知生成器泛化性差，亟需可靠的通用检测方案保障数字内容可信。研究发现自然视频的宏观语义时序动态与微观像素残差模式由物理成像链路天然耦合，而AI生成过程未显式保留该联合分布，存在系统性失配，可作为新型取证信号。
### 方法关键点
提出RIFT正交取证框架：1）宏流基于流形轨迹的微分几何与持续同源建模，构建时序演化动态基线；2）微流通过隐写分析滤波与时序建模实现敏感取证探针；3）耦合差异模块基于Gram-Schmidt正交化保障度量有效性，量化两流的条件依赖偏差。
### 关键结果
在VidProM（120K视频、7个生成器）、GenVidBench（68K视频、4个生成器）上F1分别达99.33%、99.72%；留一法评估下未知生成器检测率达97.87%；编码器无关性优异，ViT-S到ViT-L参数量提升超10倍F1波动<0.1%，切换为DINOv1仅下降0.73pp。
