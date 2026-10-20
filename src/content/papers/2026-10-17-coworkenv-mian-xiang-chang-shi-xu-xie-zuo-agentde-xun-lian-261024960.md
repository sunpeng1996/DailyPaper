---
title: 'CoworkEnv: Synthesizing Training Environments for Long-Horizon Cowork Agents'
title_zh: CoworkEnv：面向长时序协作Agent的训练环境合成框架
authors:
- Zhongwei Xie
- Yiming Du
- Jiaxin Bai
- Baixuan Xu
- Chunyang Li
- Xiyu Ren
- Wei Fan
- Tianshi Zheng
- Weizhi Du
- Jingqiao Yu
affiliations:
- The Hong Kong University of Science and Technology
- The Chinese University of Hong Kong
- Hong Kong Baptist University
- Independent Researcher
arxiv_id: '2610.24960'
url: https://arxiv.org/abs/2610.24960
pdf_url: https://arxiv.org/pdf/2610.24960
published: '2026-10-17'
collected: '2026-10-20'
category: Agent
direction: 协作Agent · 训练环境合成
tags:
- Agent Training
- Synthetic Environment
- SFT
- RL
- Multi-turn Interaction
one_liner: 提出能力导向的可执行协作Agent训练环境合成框架，同时支持SFT与RL训练
practical_value: '- 可复用「能力导向→任务生成→程序化校验→轨迹筛选」流程，为电商客服、运营类业务Agent合成SFT/RL训练数据，大幅降低人工标注成本

  - 多轮交互类Agent训练优先选SFT+RL组合方案：参考实验结果，SFT可将8B基座多轮任务得分提升31.9分，RL进一步可提升29分，增益远高于通用任务

  - 训练数据规模可按ROI灵活配置：20%训练数据即可获得40%的全量增益，50%数据可获得51%的全量增益，算力有限场景下可优先覆盖核心任务

  - 合规类场景可复用Generator-Discriminator分离设计：生成器构造业务场景，判别器单独定义校验规则与禁止动作，降低安全约束下的训练数据构造难度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长时序协作Agent需要实现跨工具协调、多轮交互、遵循业务流程约束，现有训练数据普遍缺乏连贯的请求上下文、一致的服务记录、标准化工具接口与可执行校验逻辑，人工构造成本极高且一致性差，无法同时支持SFT与RL两类训练范式，限制了端侧小参数协作Agent的性能提升。

### 方法关键点
- 能力导向的任务合成：将目标能力映射为跨服务工作流，生成包含用户请求、初始状态、工具接口、可执行校验规则的标准化任务实例，同时覆盖普通业务场景与安全约束场景
- 程序化校验+反馈修复：自动校验任务的可解析性、服务合法性、校验规则一致性，不合格任务返回生成器迭代修复，确保所有生成环境可稳定执行
- 双训练范式支持：基于Teacher执行生成高质量轨迹用于SFT训练，同时保留完整交互环境支持学生Agent在线交互获得奖励信号用于RL训练，两类范式共享底层环境与校验逻辑

### 关键实验
基于Qwen3-VL-8B-Instruct基座实验，在Claw-Eval基准上，SFT后模型总得分从46.6提升至64.1，其中多轮任务得分提升31.9分；SFT+GDPO RL训练后，多轮任务得分进一步提升至74.9，较基座提升29分；在ClawMark基准上SFT后得分较基座提升7.6分；数据量消融显示20%训练数据即可获得4.2分的总得分提升，50%数据可获得9.0分提升。

### 核心结论
高质量可执行的合成训练环境，是小参数协作Agent在多轮复杂任务上追平大模型效果的核心基础设施。
