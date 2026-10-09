---
title: 'SuperNav: An Agentic Navigation System for Any Task in Any Scene'
title_zh: SuperNav：适配任意场景任意任务的具身智能导航Agent系统
authors:
- Jinkai Zhang
- Jingyi Xu
- Yuanhong Yu
- Jiarui Guo
- Ruizhen Hu
- Hujun Bao
- Xiaowei Zhou
- Sida Peng
affiliations:
- Zhejiang University
- Shenzhen University
- Causa Robotics
arxiv_id: '2610.12126'
url: https://arxiv.org/abs/2610.12126
pdf_url: https://arxiv.org/pdf/2610.12126
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: 具身Agent · 通用导航系统
tags:
- Embodied Agent
- Navigation
- MLLM
- Tool Calling
- Zero-shot
one_liner: 无需微调预训练MLLM，通过专用Agent Harness实现跨任务跨场景的通用具身导航
practical_value: '- 电商线下导购、门店动线引导Agent可直接复用「MLLM做决策+底层工具执行」的分层架构，无需微调大模型即可适配不同门店场景和用户需求，大幅降低落地成本

  - Agent工具调用设计可借鉴统一视觉点接口，将上层语义决策和底层执行完全解耦，上层仅输出语义化目标，底层支持几何导航、学习型执行器等多种后端，便于多端部署

  - 长会话上下文管理可复用「已处理图片移除payload仅保留路径+文本历史」的裁剪策略，既控制MLLM上下文窗口占用，又支持随时回溯历史证据，可迁移至多轮导购Agent、长会话推荐场景

  - 可复用Navigation Skills设计思路：将通用流程（搜索、纠错、完成判断）封装为markdown文档供MLLM按需读取，比硬编码流程灵活，比微调大模型成本低，适合快速适配业务新场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有服务机器人导航方案存在两类局限：模块化零样本导航依赖硬编码工作流，无法适配多变的用户请求；端到端方法微调MLLM预测导航动作，泛化性受训练数据覆盖度限制，无法同时实现任务通用性（适配不同用户需求）和场景通用性（在未知环境运行）。

### 方法关键点
- 分层解耦架构：预训练MLLM仅负责需求解析、场景理解、决策，所有导航执行逻辑委托给专用工具，完全无需对MLLM做导航领域微调，保留大模型通用能力
- 专用Agent Harness：包含3核心组件：1）Navigation Skills：封装搜索、复检、故障恢复、任务完成判断的通用流程，MLLM按需读取；2）Agent专属工具集：覆盖观测、转向、点导航、进度跟踪、任务终止等操作；3）上下文管理：自动裁剪已处理图片的媒体payload，仅保留文本历史和图片路径，控制上下文长度
- 统一视觉点接口：MLLM直接在观测图像上指定目标点坐标，底层几何导航、学习型导航执行器兼容同一套接口，上层决策逻辑无需修改即可切换执行后端

### 关键结果
- 覆盖单物体、多物体、需求驱动、类别级4类导航任务，对比NaVid、UniNaVid、OmniNav等4个基线
- 单物体导航SR达78.00%，是最强基线UniNaVid的2.29倍；需求驱动导航SR达59.50%，是最强基线OmniNav的1.59倍
- HM3D-OVON unseen数据集1m阈值下SR73.33%、SPL0.4105，0.25m阈值下SR68.33%，优于现有公开方法，已在四足机器人上完成真实场景部署

**最值得记住的一句话**：将大模型的通用理解推理能力与专用工具的执行能力解耦，无需领域微调即可让预训练MLLM适配复杂垂直场景任务
