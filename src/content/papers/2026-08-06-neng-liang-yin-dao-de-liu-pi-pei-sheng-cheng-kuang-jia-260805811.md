---
title: Energy-Guided Flow Matching
title_zh: 能量引导的流匹配生成框架
authors:
- Haoyang Tong
- Yu He
- Fang Li
- Lichen Ma
- Jingling Fu
- Dong Chen
- Zhen Chen
- Junshi Huang
- Jie Cao
affiliations:
- MAIS & NLPR, CASIA
- JD.com
- Xi'an Jiaotong University
arxiv_id: '2608.05811'
url: https://arxiv.org/abs/2608.05811
pdf_url: https://arxiv.org/pdf/2608.05811
published: '2026-08-06'
collected: '2026-08-19'
category: Training
direction: 生成模型训练 · 流匹配优化
tags:
- Flow Matching
- Generative Model
- Image Generation
- Energy Guided
- Dynamic Endpoint
one_liner: 通过动态演化的热核过滤端点优化流匹配，无骨干改动前提下提升图像生成质量与训练效率
practical_value: '- 电商商品图/营销素材生成场景可直接复用EG-FM，无需改动现有生成模型骨干，几乎无额外成本即可提升生成质量、缩短训练周期

  - 多分辨率商品图生成场景可借鉴动态端点的粗到细生成思路，仅需少量高分辨率适配训练即可得到高质量大尺寸生成结果，降低训练成本

  - 生成式推荐的图文内容生成任务可复用能量引导调度策略，平衡全局结构合理性与细粒度细节生成优先级，提升用户接受度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
像素空间生成模型避免了隐空间压缩的信息损失，可保留细粒度细节，但需在高维空间同时学习全局结构与细粒度特征，训练难度大；标准流匹配采用固定干净图像作为插值端点，频谱演化需隐式学习，收敛慢、效果上限低。

### 方法关键点
提出EG-FM框架：1. 用热核过滤的动态端点替代固定端点，端点从低频图像平滑演化到干净图像；2. 采用图像专属的能量引导调度逐步释放高频信号，重定向流匹配的速度向量；3. 无需修改骨干网络与训练数据，训练推理额外成本可忽略。

### 关键结果
256×256 ImageNet类条件生成任务：200epoch FID达1.55，600epoch达1.45；512×512分辨率生成仅需40个适配epoch，FID达1.58；文本到图像生成任务GenEval得分0.85、DPG-Bench得分83.9，全面优于基线。
