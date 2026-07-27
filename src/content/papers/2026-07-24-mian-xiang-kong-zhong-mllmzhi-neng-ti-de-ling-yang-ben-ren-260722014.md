---
title: Zero-Shot Mission-Level Evaluation for Aerial MLLM Agents
title_zh: 面向空中MLLM智能体的零样本任务级评估基准MissionBench
authors:
- Suman Navaratnarajah
- Taehyoung Kim
- Jona Ruthardt
- Ishaan Bhimwal
- Ryousuke Yamada
- Yannik Blei
- Wolfram Burgard
- Yuki M Asano
affiliations:
- University of Technology Nuremberg
- Fraunhofer IVI
- THWS
- AIST
arxiv_id: '2607.22014'
url: https://arxiv.org/abs/2607.22014
pdf_url: https://arxiv.org/pdf/2607.22014
published: '2026-07-24'
collected: '2026-07-27'
category: Agent
direction: 具身Agent · MLLM任务级评估
tags:
- MLLM
- Embodied Agent
- UAV
- Zero-shot Evaluation
- Benchmark
one_liner: 提出含120个真实无人机任务的MissionBench，评估通用MLLM零样本执行长航时空中任务的能力
practical_value: '- 长周期闭环任务评估思路可迁移：面向电商导购Agent、线下服务机器人等场景，放弃单步准确率的片面评估，设计覆盖感知/规划/交互/交付全链路的成功指标，可拆解导航失败、最后一步感知失败、提前终止等不同错误模式，精准定位问题

  - 结构化输出设计可直接复用：prompt中要求Agent输出中间推理过程、目标定位、动作、完成标志的范式，能大幅提升长序列任务稳定性，实验显示移除推理字段会让成功率下降65%，该技巧可直接用于电商Agent、客服Agent的prompt工程

  - 时序上下文最优长度结论可落地：对于需要连续记忆的任务（如带浏览历史的推荐Agent、多轮交互客服），保留最近3条历史的效果优于1条或5条，过长上下文会稀释关键信息，可直接指导工程中的上下文窗口设计'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前MLLM已成为具身智能体的核心推理模块，但现有基准大多仅评估路径导航、单步技能等单一能力，无法衡量通用MLLM零样本完成需要感知、规划、控制、报告多能力协同的长周期任务的表现；尤其是空中UAV任务对视角敏感、动作自由度高，缺乏对应的闭环任务级评估基准，无法验证通用预训练带来的具身能力增益。

### 方法关键点
- 构建MissionBench基准：包含120个真实UAV任务，覆盖报告、巡检、操控、巡逻4大类，分布在5个高保真3D仿真环境中，每个任务仅用1条自然语言指令定义，无细分步骤提示
- 闭环评估框架：Agent仅接收第一人称RGB图像、最近3帧历史观测、动作历史，输出结构化内容（推理过程、目标边界框、带幅度的动作、报告内容、DONE完成标志），支持连续4自由度动作控制
- 多维度评估指标：设计成功率SR、Oracle成功率OSR（是否到达过目标附近）、任务进度MP、碰撞率CR、步骤效率Eff，可拆解不同错误模式

### 关键实验
在30个任务的测试集上评估22款开源/闭源MLLM，所有模型均无无人机领域微调：最强模型Gemini 3.1 Pro的零样本成功率仅34.8%，远低于人类键盘操作的84.4%；模型性能随参数量提升整体呈上升趋势，但静态空间感知能力与任务成功率仅中度相关（皮尔逊系数0.463）；消融实验显示采样温度0.7、1080P输入、3帧历史、强制输出推理字段的配置效果最优。

### 核心结论
通用MLLM的具身任务能力不能仅靠单步感知指标衡量，闭环任务级评估才能暴露长序列决策中的漂移、提前终止等真实问题。
