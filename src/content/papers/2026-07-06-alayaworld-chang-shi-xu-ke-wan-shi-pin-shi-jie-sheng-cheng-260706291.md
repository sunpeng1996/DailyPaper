---
title: 'AlayaWorld: Long-Horizon and Playable Video World Generation'
title_zh: AlayaWorld：长时序可玩视频世界生成框架
authors:
- AlayaWorld Team
- Kaipeng Zhang
- Chuanhao Li
- Yifan Zhan
- Yongtao Ge
- Yuanyang Yin
- Jiaming Tan
- Kang He
- Liaoyuan Fan
- Ruicong Liu
affiliations:
- Alaya Lab
arxiv_id: '2607.06291'
url: https://arxiv.org/abs/2607.06291
pdf_url: https://arxiv.org/pdf/2607.06291
published: '2026-07-06'
collected: '2026-07-09'
category: Other
direction: 生成式交互虚拟世界构建
tags:
- Generative World Model
- Open-Source Framework
- Interactive Simulation
- Video Generation
- Embodied AI
one_liner: 开源全栈模块化生成式交互世界构建框架，覆盖完整研发链路并配套全套落地工具
practical_value: '- 可复用其模块化全栈研发架构思路，搭建Embodied Agent交互仿真测试环境，降低Agent训练、评测的虚拟环境构建成本

  - 其基于当前状态+用户输入自回归生成后续场景的逻辑，可迁移到电商虚拟试逛、3D互动营销场景的实时内容生成链路

  - 参考其推理加速优化方案，优化实时互动类生成应用的响应延迟，提升用户交互体验'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
传统虚拟/游戏世界依赖重度人工生产管线，开发成本高、定制灵活性差、部署后迭代修改代价大，现有视频世界模型已具备交互生成能力，但缺乏完整的工程化落地框架。
### 方法关键点
1. 采用模块化可扩展全栈架构，统一覆盖数据预处理、模型搭建、训练、推理加速、部署全研发链路；
2. 支持开放实时交互，兼容自由导航、战斗、施法、召唤怪物等多元用户操作，适配真实/游戏/合成域、室内/室外、一/三人称等多场景需求。
### 关键结果
配套开源可复现研发管线、参考实现、评测工具与完整文档，可直接支撑生成式世界模型相关研究与实时交互类应用落地。
