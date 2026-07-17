---
title: 'Plover: Steering GUI Agents through Plan-Centric Interaction'
title_zh: Plover：以计划为中心的交互实现GUI Agent可控引导
authors:
- Madhumitha Venkatesan
- Shicheng Wen
- Jiajing Guo
- Jorge Piazentin Ono
- Liu Ren
- Dongyu Liu
affiliations:
- University of California, Davis
- Bosch Research North America
arxiv_id: '2607.15193'
url: https://arxiv.org/abs/2607.15193
pdf_url: https://arxiv.org/pdf/2607.15193
published: '2026-07-16'
collected: '2026-07-17'
category: Agent
direction: GUI Agent 人机协同交互优化
tags:
- GUI Agent
- Human-AI Interaction
- Mixed-Initiative
- Task Planning
- Automation Repair
one_liner: 提出以计划为核心的GUI Agent交互框架，支持可编辑外部化计划与本地化故障修复
practical_value: '- 电商运营类RPA/Agent可复用计划外部化设计：将执行步骤暴露为可编辑的持久化对象，故障修复仅修改待执行步骤，无需全流程重跑，降低长流程任务的干预成本

  - Agent故障修复可参考分层干预机制：无空间歧义场景用自然语言修正，复杂界面（比如商家后台、报表系统）操作故障用截图标注+区域约束做本地化修复，平衡干预效率与准确性

  - 可直接复用Agent卡顿检测逻辑：结合最近操作序列重复度+界面感知哈希相似度双重判断执行停滞，主动触发重规划，减少无效执行的算力与时间浪费'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有自治式GUI Agent的规划、重规划过程完全黑盒，用户无法监督执行逻辑、定位故障点，出错后要么全量重跑丢失已有进度，要么无法通过纯自然语言修正解决空间歧义问题，在长流程、高风险的GUI自动化场景（如电商后台操作、企业级RPA）中，故障扩散会带来极高的重复劳动成本。
### 方法关键点
- 采用规划器-执行器分离架构，将任务计划作为全局共享的持久化状态，强制拆分已执行不可变步骤、待执行可编辑步骤，所有重规划操作仅修改待执行片段，完整保留已执行进度与操作历史
- 支持两类智能重规划：用户驱动型提供自然语言指导、截图多模态标注、直接编辑计划三种干预入口；系统驱动型结合行为序列重复度检测+界面感知哈希相似度判断执行停滞，主动触发局部重规划
- 配套交互界面支持计划版本分支管理、执行进度可视化、变更diff对比，降低用户监督与故障定位成本
### 关键实验结果
- 基准故障修复实验：基于OSWorld-Verified数据集的38个高难度任务，纯自治执行下共26个任务失败/部分成功，引入计划为中心的人机协同机制后，88%的故障任务得到改善，其中17个转为完全成功、6个转为部分成功，平均每个任务仅需2.04次轻量干预
- 自治执行稳定性实验：覆盖5类真实场景的25条执行轨迹，浏览器类任务自治执行后界面SSIM>0.98，桌面办公类任务SSIM仅0.61~0.69，验证桌面/复杂界面场景的自治执行漂移率更高，更依赖计划级干预
### 核心结论
GUI Agent的可靠性提升不依赖完美自治能力，而是通过计划级可见性把潜在的执行漂移转化为可协作修复的交互过程。
