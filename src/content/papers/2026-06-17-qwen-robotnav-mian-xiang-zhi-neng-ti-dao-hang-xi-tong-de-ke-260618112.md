---
title: 'Qwen-RobotNav Technical Report: A Scalable Navigation Model Designed for an
  Agentic Navigation System'
title_zh: Qwen-RobotNav：面向智能体导航系统的可扩展导航模型技术报告
authors:
- Jiazhao Zhang
- Gengze Zhou
- Hale Yin
- Yiyang Huang
- Zixing Lei
- Qihang Peng
- Haoqi Yuan
- Jie Zhang
- Xudong Guo
- Xiaoyue Chen
affiliations:
- Qwen Team
arxiv_id: '2606.18112'
url: https://arxiv.org/abs/2606.18112
pdf_url: https://arxiv.org/pdf/2606.18112
published: '2026-06-17'
collected: '2026-06-30'
category: Agent
direction: 智能体导航 · 可重配置大模型
tags:
- Agentic Navigation
- LLM
- Vision-Language
- Scalable Model
- Task Planning
one_liner: 为智能体导航设计带可重配置参数接口的可扩展导航模型，刷新多项基准SOTA
practical_value: '- 多任务共享backbone + 训练时参数随机化方案，推理无需改结构即可动态切换行为模式，可借鉴用来构建Agent统一底层基座，降低电商导购、搜索多任务的部署成本

  - 联合图文数据训练避免纯轨迹训练的策略退化，可复用在推荐系统、Agent交互策略训练中，缓解纯交互轨迹训练导致的泛化能力下降

  - 上层规划器动态调整底层基座任务模式、token预算的分层架构，适合长程用户交互任务（如多轮导购、复杂需求搜索），可直接借鉴解决长路径任务的分解调度问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
智能体导航系统中，指令跟随、目标搜索、自动驾驶等多任务共享感知规划backbone，但不同任务对视觉流的处理策略存在本质差异，现有模型不支持推理时外部重配置观测策略。

### 方法关键点
基于Qwen3-VL构建Qwen-RobotNav，设计双维度可参数化接口：多任务模式选择导航行为，可控观测参数（token budget、相机权重等）控制视觉历史编码；训练时对所有参数做随机化，推理时任意配置无需修改backbone结构；使用15.6M样本训练，加入视觉语言数据联合训练，避免纯轨迹训练导致模型退化为反应式动作映射器；支持上层规划器在长程任务中分解目标，动态切换模型配置，复用同一模型组合复杂行为。

### 关键结果
在多个主流导航基准取得新SOTA：VLN-CE RxR成功率76.5%，EVT-Bench跟踪率90.0%，NAVSIM PDMS 91.4；基于该模型构建的智能体导航系统在HM-EQA提升10.8%、EXPRESS-Bench提升15.4%，同时减少77%导航步骤；模型从2B到8B参数缩放效果良好，可零样本泛化到真实世界机器人。
