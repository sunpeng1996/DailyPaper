---
title: 'SatNav: A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation
  from Satellite Imagery'
title_zh: SatNav：基于卫星影像的长航时无人机视觉语言导航可扩展基准
authors:
- Jiajun Jiang
- Chunliang Hua
- Zichun Chen
- Yanxing Wu
- Zeyuan Yang
- Jie Song
- Xiao Hu
affiliations:
- 香港科技大学（广州）
- 国际数字经济研究院（IDEA）低空空间经济研究中心
- 香港科技大学
arxiv_id: '2609.31507'
url: https://arxiv.org/abs/2609.31507
pdf_url: https://arxiv.org/pdf/2609.31507
published: '2026-09-24'
collected: '2026-10-11'
category: Agent
direction: 具身Agent · VLN基准构建
tags:
- Vision-Language Navigation
- Embodied Agent
- Benchmark
- LVLM
- Cross-domain Transfer
one_liner: 构建覆盖18城118K样本的城市级UAV VLN基准SatNav及模块化导航框架SwiftVLN
practical_value: '- 模块化可切换记忆组件的框架设计思路，可直接迁移到长会话导购Agent、长序列用户行为推荐系统的记忆模块选型与消融实验

  - 基于公开低成本数据源自动化生成大规模评测/训练样本的流水线方案，可复用在推荐冷启动样本构造、用户交互行为模拟数据集生成场景

  - 跨域迁移验证方法（卫星预训练→真实UAV推理）可借鉴到离线训练的推荐/Agent模型上线前的跨域效果预验证，降低线上试错成本'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
现有长航时UAV视觉语言导航（VLN）基准依赖高成本3D重建资产，地理覆盖范围、样本规模均受限，无法支撑城市级导航Agent的长时记忆、地理空间推理能力评测。
### 方法关键点
1. 提出SatNav可扩展基准，用高分辨率卫星影像裁剪近似无人机正摄视图作为观测输入，通过自动化cue-to-episode流水线批量生成任务样本
2. 定义Boundary、Landmark、Route三类任务，分别测试循环进度追踪、地标空间对齐、带计数提示的路线跟随能力
3. 开源SwiftVLN模块化框架，支持可插拔记忆组件替换，方便系统对比不同记忆设计的效果
### 关键结果
构建覆盖18个城市59个场景的118K条任务样本，平均轨迹长度达379m；评测显示现有经典VLN Agent、LVLM基Agent在城市级导航任务上表现仍存在明显短板；卫星预训练的导航模型可直接迁移到真实UAV飞行观测数据上执行任务
