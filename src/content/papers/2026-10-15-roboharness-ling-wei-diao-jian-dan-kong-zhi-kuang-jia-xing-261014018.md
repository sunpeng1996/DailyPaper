---
title: 'RoboHarness: A Simple Harness Outperforms VLA and World Action Models'
title_zh: RoboHarness：零微调简单控制框架性能超越VLA与世界动作模型
authors:
- Bince Qu
- Wei Chen
- Bo Zhang
affiliations:
- Zhejiang University
arxiv_id: '2610.14018'
url: https://arxiv.org/abs/2610.14018
pdf_url: https://arxiv.org/pdf/2610.14018
published: '2026-10-15'
collected: '2026-10-27'
category: Agent
direction: 具身Agent · LLM机器人控制接口设计
tags:
- Embodied AI
- LLM Agent
- Robot Control
- VLA
- Zero-Finetune
one_liner: 为通用LLM提供几何约束式机器人控制接口，零微调性能超越SOTA VLA/WAM
practical_value: '- 设计Agent工具链时优先采用最小正交原子工具集，而非预定义大量场景化功能，可大幅降低LLM适配成本，该思路可直接复用在电商运营Agent、搜推策略调优Agent的工具设计中

  - 复杂任务可采用「上层LLM推理决策+底层原子执行接口」的分层架构，避免让LLM直接生成低层次执行指令，降低训练/微调数据需求，可参考优化搜推系统的大模型调度模块

  - 对涉及空间/实体匹配的多模态搜推场景（如AR试穿、线下履约点位推荐、智能货柜交互），可引入统一坐标体系+实时关键点状态追踪机制，给LLM提供闭环反馈提升匹配准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有VLA、WAM方案需大量机器人动作训练数据，采集成本高、泛化性受限；LLM调用预定义机器人技能的方案又受限于预定义功能覆盖范围，无法灵活适配新任务、新物体，难以释放LLM本身的推理与规划能力。
### 方法关键点
- 设计统一相机坐标系的几何状态追踪机制：LLM可通过`track_object`工具标记物体关键点，经光流追踪+深度反投影得到实时3D坐标，解决LLM空间感知不足的问题
- 最小完备动作工具集：分为两类，一类是封装了touch/共线/共面等常用几何约束的keypoint-constraint工具，自动求解并执行符合约束的运动轨迹；另一类是直接控制机器人自由度的adjustment微调工具
- 理论证明工具集完备性：任意抓取姿态、任意手持物体与目标物体的空间关系都可通过2-3个关键点约束表示，无需额外扩展工具
### 关键实验结果
- BEHAVIOR 2025前10项长周期家务任务：Qwen3.8-Flash-Next零微调平均q-score达44.54%，超出SOTA VLA G0.5的34.84%、WAM基线的28.08%
- 100种未知物体抓取泛化测试：零机器人训练数据前提下成功率达68%-86%，超过所有需要上千小时训练数据的VLA/WAM基线
### 核心结论
LLM的落地瓶颈往往不在自身推理能力，而在于是否有足够简单、完备的接口连接其知识与真实执行环境
