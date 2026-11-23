---
title: 'Omo: Giving Continuing AI-Agent Work a Place to Return To'
title_zh: 《Omo：为持续运行的AI Agent任务提供可回溯的固定工作空间》
authors:
- Kaviru Hapuarachchi
- Harrison Edwards
affiliations:
- Omo Research
arxiv_id: '2611.27107'
url: https://arxiv.org/abs/2611.27107
pdf_url: https://arxiv.org/pdf/2611.27107
published: '2026-11-20'
collected: '2026-11-23'
category: Agent
direction: Agent任务中断恢复 · 空间交互设计
tags:
- AI Agents
- Task Resumption
- Spatial IDE
- Persistent Workspace
- Human-Agent Interaction
one_liner: 提出两款基于空间记忆的Agent任务管理工具，解决工作中断后恢复任务的上下文丢失问题
practical_value: '- 多Agent并行任务管理可借鉴「空间锚定」思路，给不同业务线Agent（比如文案生成、选品、投放优化Agent）分配固定可视化空间，降低多任务切换的上下文恢复成本

  - Agent会话生命周期管理可复用「会话生命周期独立于视图」的设计，前端页面关闭不终止后端Agent执行，避免用户误操作丢失任务进度，适合电商大促期间长时间运行的投放Agent场景

  - 给Agent状态展示设计做参考：仅将状态标签作为提示入口，核心执行结果、变更diff等证据直接绑定到对应空间入口，用户点击即可直达，减少信息查找成本'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
AI Agent已支持用户离线时持续运行任务，但用户中断工作回归后，仅靠会话列表无法快速回忆任务初衷、Agent变更内容与后续指令。现有工具仅解决了会话保活的执行连续性问题，未覆盖工作空间识别、上下文恢复两类核心需求，非专业开发者使用Agent时更缺乏快速找回上下文的路径，多Agent并行场景下任务管理成本极高。

### 方法关键点
- 拆分Agent任务中断恢复三类需求：执行连续性（会话保活）、工作空间识别（快速定位任务）、上下文恢复（还原目标与变更），核心解决后两类未被覆盖的需求；
- 推出两款共享后端的实现：Omo Space是开源Minecraft mod，用户可自定义搭建房间，房间内方块对应本地终端会话，关闭游戏不终止Agent运行；Omo Theia是基于Eclipse Theia的空间IDE，每个项目对应独立房间，桌面绑定终端，支持一键跳转Git变更与代码编辑页；
- 沉淀4条可复用落地经验：会话生命周期独立于视图、状态标签仅作提示而非结论、每个空间入口直接关联任务证据、不基于猜测的Agent状态自动执行操作。

### 实验设计
当前尚未完成正式用户实验，计划采用被试内设计，对比命名会话列表、2D固定布局、Omo空间三种方案的任务恢复准确率，指标包含原目标复述准确率、变更说明准确率、后续指令合理性三类，覆盖新手与非专业开发者群体，分别测试短时间中断与次日回归两种场景。

### 最值得记住的一句话
用户对任务的记忆和空间场景强绑定，给固定任务分配固定空间，可大幅降低上下文恢复的认知成本。
