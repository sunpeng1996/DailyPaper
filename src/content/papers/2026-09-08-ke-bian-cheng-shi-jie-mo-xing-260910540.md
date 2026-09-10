---
title: Programmable World Model
title_zh: 可编程世界模型
authors:
- Zheng-Hui Huang
- Guixu Lin
- Jiacheng Lin
- Yi-Chuan Huang
- Ruihan Yu
- Muyao Niu
- Siqi Yang
- Yu-Lun Liu
- Yung-Yu Chuang
- Kaipeng Zhang
affiliations:
- Alaya Lab
arxiv_id: '2609.10540'
url: https://arxiv.org/abs/2609.10540
pdf_url: https://arxiv.org/pdf/2609.10540
published: '2026-09-08'
collected: '2026-09-10'
category: Agent
direction: Agent 交互世界模型构建
tags:
- World Model
- Agent Simulation
- State Tracking
- Video Generation
- Program Synthesis
one_liner: 提出解耦状态演化与视觉生成的可编程世界模型，支持长程高一致性交互虚拟场景生成
practical_value: '- 虚拟导购、试玩类广告场景可复用状态-渲染解耦架构，用显式状态维护商品/角色属性，解决长交互下属性漂移问题

  - 可迁移自然语言转可执行规则的Agent设计，将用户对虚拟场景的自定义需求转化为结构化规则，降低可控内容生成成本

  - 用结构化中间表示桥接规则引擎与生成模型的思路，可用于商品展示短视频生成，规避生成内容与商品属性不匹配问题'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
现有视频世界模型在长时交互场景下，缺乏稳定的持久世界状态维护机制，也无法支持自定义规则控制实体交互逻辑，难以满足可控虚拟场景生成需求。
## 方法关键点
1. 架构上解耦世界状态演化与视觉生成流程，由Agent将自然语言指令转换为定义实体属性、状态转移规则的可执行程序
2. 轻量引擎执行程序维护显式全局持久状态，覆盖屏外实体、非视觉属性等全量信息
3. 设计状态增强的3D OBB作为中间表示，结合相机轨迹编译为像素对齐的时空条件信号，输入预训练视频模型完成渲染
## 关键结果
在自建CombatStateBench基准上实现94% Count Accuracy、98% State Accuracy，性能远超现有交互视频世界模型，同时支持长程连贯场景生成。
