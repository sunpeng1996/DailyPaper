---
title: 'StateFlow: Building, Evolving, and Accessing 3D World States for Previsualization'
title_zh: StateFlow：面向预可视化的3D世界状态构建、演化与访问
authors:
- Yuyang Yin
- Zixiang Li
- Longxuan Deng
- Hongkai Li
- Shifang Zhao
- Junnan Liu
- Weirong Huang
- Mengyu Wang
- Tianxiao Fu
- Yikai Wang
affiliations:
- Beijing Jiaotong University
- Mootion AI
- Beijing Normal University
- Peking University
- Beijing Academy of Artificial Intelligence
arxiv_id: '2608.12314'
url: https://arxiv.org/abs/2608.12314
pdf_url: https://arxiv.org/pdf/2608.12314
published: '2026-08-11'
collected: '2026-08-13'
category: Other
direction: 3D生成式预可视化 · 持久化状态管理
tags:
- 3D Generation
- Previsualization
- State Management
- Controllable Generation
- Video Synthesis
one_liner: 以持久化3D世界状态为核心的预可视化框架StateFlow，支持可控迭代场景编辑与视频生成
practical_value: '- 持久化状态复用思路可迁移到电商3D商品展示、虚拟直播间生成场景，避免修改后全量重生成，降低计算成本

  - 多模态意图转结构化状态变更的机制，可用于Agent驱动的虚拟场景交互、3D广告素材迭代编辑流程

  - 渲染反馈校验可行性的思路，可借鉴到推荐系统多模态内容生成的一致性校验环节，减少逻辑错误'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有生成式预可视化方法依赖简单prompt一次性生成图像/视频，可控性弱，不支持迭代编辑，缺乏显式持久化的世界状态承载场景、相机等可共享复用的元素。
### 方法关键点
框架以结构化持久3D世界状态为核心，包含三个核心阶段：1）状态构建：通过先验引导的冲突感知双视图初始化，将2D生成内容升维为连贯3D世界；2）状态演化：将用户意图转化为结构化状态变更，保留世界记忆无需每次编辑全场景重生成；3）状态访问：通过渲染反馈反思将相机规划优化为视觉可行的轨迹，无需仅依赖VLM语义，同时可调用现成视频模型增强高保真度视觉效果。
### 关键结果
实验验证StateFlow可生成高质量3D世界，支持影视视频创作、可控镜头规划、类游戏交互原型搭建等场景。
