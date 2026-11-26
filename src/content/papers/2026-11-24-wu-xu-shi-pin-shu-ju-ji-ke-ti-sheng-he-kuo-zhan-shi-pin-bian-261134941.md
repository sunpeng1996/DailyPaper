---
title: Improving and Expanding Video Editing Capabilities Without Videos
title_zh: 无需视频数据即可提升和扩展视频编辑能力
authors:
- Ji Xie
- Yanhao Jia
- Xiangpeng Yang
- Martin Q. Ma
- Sihan Xu
- Erik Cambria
- Louis-Philippe Morency
affiliations:
- Carnegie Mellon University
- Nanyang Technological University
- University of Technology Sydney
- University of Michigan
arxiv_id: '2611.34941'
url: https://arxiv.org/abs/2611.34941
pdf_url: https://arxiv.org/pdf/2611.34941
published: '2026-11-24'
collected: '2026-11-26'
category: Multimodal
direction: 多模态 · 图像到视频能力迁移
tags:
- Video Editing
- Knowledge Distillation
- Diffusion Model
- Multimodal Generation
- Benchmark
one_liner: 提出I2VT图像到视频能力迁移框架，仅用图像数据升级视频编辑模型，开源OpenVE++评测基准
practical_value: '- 电商短视频素材生产场景可复用I2VT的跨模态迁移思路，仅用图文素材训练即可扩展短视频编辑能力，大幅降低配对视频数据采集成本

  - 扩散模型的单帧引导训练范式可迁移到生成式推荐的多帧/多模态内容一致性优化场景，无需修改原有模型架构即可实现能力升级

  - 内容生产类Agent可集成该思路，仅需维护更易获取的图文编辑能力库，即可自动拓展短视频编辑技能栈'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
视频编辑模型效果远落后于图像编辑模型，核心瓶颈是配对编辑视频数据集采集成本极高，无法快速规模化扩展新编辑任务。

### 方法关键点
1. 提出I2VT迁移框架，无需修改视频编辑器原有架构、无需新增配对视频数据，仅用单张图像即可完成高效 post-training
2. 训练阶段将单张图像作为单帧视频输入视频编辑器，每一步去噪过程由预训练图像编辑器提供监督信号引导训练
3. 训练完成后模型可直接处理完整视频剪辑，自动保留时序一致性
4. 开源OpenVE++评测基准，新增动作变更、表情调整、肢体移动、场景重打光4类视频生产实用任务

### 关键结果
在3款不同的预训练视频编辑器上验证适配性，在OpenVE-Bench和OpenVE++两个基准上均达到SOTA性能。
