---
title: 'Evaluating Multimodal LLMs as Generalist Vision-Language-Action Agents for
  Drone Control: Commanding, Approaching, Tracking and Searching'
title_zh: 多模态大模型作为无人机控制通用视-语-动作Agent的评估：指挥/接近/跟踪/搜索
authors:
- Jaewoo Park
- Minyoung Lee
- Sukmin Seo
- Moonbin Yim
- Hyunwook Yoon
- Dohoon Ryu
- Daehee Kim
- Myungseo Song
- Jihyuk Byun
- Seunggyu Chang
affiliations:
- NAVER Cloud Drone AI Team
arxiv_id: '2609.01404'
url: https://arxiv.org/abs/2609.01404
pdf_url: https://arxiv.org/pdf/2609.01404
published: '2026-08-31'
collected: '2026-09-02'
category: Agent
direction: 多模态大模型 · 具身Agent性能评估
tags:
- MLLM
- Embodied Agent
- Drone Control
- Benchmark
- Edge Deployment
one_liner: 提出可插拔MLLM的无人机Agent架构与基准，揭示边缘具身Agent核心瓶颈为动作协议遵守而非空间感知
practical_value: '- 端侧/边缘Agent落地可先验证小模型核心感知能力，再针对性对齐动作协议规则，无需盲目选用大参数模型，大幅降低算力成本

  - Agent系统可设计为核心大模型可插拔架构，方便快速切换不同量级基座，适配不同业务的算力约束与性能要求

  - 评估Agent性能时需重点覆盖终止条件判断、多实例指令一致性等边界场景，避免核心任务达标但逻辑错误导致整体失效'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
现有具身Agent系统普遍压缩MLLM决策权限，无法验证MLLM直接作为控制节点的真实能力，同时缺少针对边缘场景小参数MLLM的具身能力评估基准。

### 方法关键点
1. 推出DroneCATS-Agent架构，MLLM作为可插拔组件，仅通过Prompt定义动作空间，无需微调或function call即可完成无人机偏航、搜索、自主判定到达等全流程控制；
2. 发布DroneCATS基准，覆盖接近可见目标、跟踪移动目标、视野外搜索、多无人机编队指挥4类核心任务，评估范围覆盖前沿大模型到2B参数边缘小模型。

### 关键结果
小参数开源模型导航进入成功半径的可靠性优于前沿大模型，但70%以上失败来自提前/延迟判定到达、多无人机场景盲目复制坐标等动作协议错误，边缘模型落地核心瓶颈不是感知能力，而是动作规则遵守度。
