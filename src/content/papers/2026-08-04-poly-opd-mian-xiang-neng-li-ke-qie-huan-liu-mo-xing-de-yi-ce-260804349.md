---
title: 'Poly-OPD: Heterogeneous Multi-Teacher On-Policy Distillation for Capability-Selectable
  Flow Models'
title_zh: Poly-OPD：面向能力可切换流模型的异构多教师同策略蒸馏方法
authors:
- Siming Fu
- Haojun Xu
- Ruizhe He
- Zheming Fu
- Hualiang Wang
- Jie Huang
- Xiaoxiao Ma
- Mingchen Zhong
- Weihu Huang
- Xiaoxuan He
affiliations:
- Joy Future Academy
- Zhejiang University
- Beihang University
arxiv_id: '2608.04349'
url: https://arxiv.org/abs/2608.04349
pdf_url: https://arxiv.org/pdf/2608.04349
published: '2026-08-04'
collected: '2026-08-06'
category: Multimodal
direction: 多模态文生图 · 异构多教师蒸馏
tags:
- Knowledge Distillation
- LoRA
- Text-to-Image
- Flow Matching
- Multi-Teacher Distillation
one_liner: 将异构文生图教师的互补能力整合到单个轻量、支持能力切换的流匹配学生模型
practical_value: '- 整合不同文生图模型优势生成电商商品/营销素材时，可复用像素桥+冻结DINOv2空间对齐方案，解决异构模型潜空间不兼容问题

  - 多风格/多要求文生图微调场景，可借鉴「注意力LoRA共享、前馈Adapter分任务专属」的参数拆分设计，既保多能力又避免交叉干扰

  - 多任务蒸馏/微调可复用gap-aware训练课程，优先给模型表现差的任务分配训练资源，提升训练效率与最终效果'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有开源文生图模型各有互补优势（如FLUX审美契合用户偏好但指令遵循弱，Z-Image构图精准但美感差），但异构模型的autoencoder、噪声调度差异导致潜空间不兼容，难以整合能力到单模型。
### 方法关键点
1. 基于像素桥做on-policy蒸馏：学生生成的图像经选中教师的编码器重编码，匹配教师噪声调度对应量级的噪声水平后生成优化目标，再通过冻结DINOv2特征空间对齐实现跨潜空间监督；
2. 用梯度兼容性诊断设计Adapter架构：注意力LoRA模块跨教师共享，前馈Adapter为教师专属，避免不同能力的交叉干扰；
3. 采用gap-aware训练课程，优先给学生与教师差距大的构图类任务分配更多训练资源，差距收窄后切换训练目标。
### 关键结果
将12B FLUX.1-dev、6B Z-Image蒸馏到2.5B SD3.5-Medium学生模型，GenEval从67.3提升至73.3，超过两个大参数教师；DrawBench HPSv3从9.34提升至11.35，同时保留两类优势且支持能力切换。
