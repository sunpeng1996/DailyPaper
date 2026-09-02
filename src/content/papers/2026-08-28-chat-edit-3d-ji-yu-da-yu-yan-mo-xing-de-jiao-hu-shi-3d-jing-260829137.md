---
title: 'Chat-Edit-3D++: Interactive 3D and 4D Scene Editing via Large Language Models'
title_zh: Chat-Edit-3D++：基于大语言模型的交互式3D/4D场景编辑
authors:
- Shuangkang Fang
- Yufeng Wang
- Yi-Hsuan Tsai
- Wenrui Ding
- Yi Yang
- Shuchang Zhou
- Ming-Hsuan Yang
arxiv_id: '2608.29137'
url: https://arxiv.org/abs/2608.29137
pdf_url: https://arxiv.org/pdf/2608.29137
published: '2026-08-28'
collected: '2026-09-02'
category: Agent
direction: Agent 视觉工具调度 3D/4D场景编辑
tags:
- LLM
- Agent
- Tool Calling
- 3D Editing
- Vision-Language
one_liner: 提出Hash-Atlas网络与LLM驱动的CE3D++框架，实现灵活交互式3D/4D场景编辑，支持30种视觉工具调度
practical_value: '- 做Agent工具调度时，可参考其构造垂直任务轨迹数据集微调小参数LLM的方案，用小模型实现数十种工具精准调度，降低推理成本

  - 电商3D商品素材制作、虚拟直播间搭建等跨模态任务，可借鉴2D编辑与3D重建流程解耦的思路，降低pipeline维护复杂度

  - 多轮交互类AI工具（如AI设计助手）可复用「用户意图理解-工具自动调度-结果反馈」的闭环逻辑，提升交互流畅度'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有文本驱动3D场景编辑方案存在输入格式固定、灵活性差，编辑能力受限于少量2D视觉模型，3D重建与编辑流程耦合度高、pipeline设计复杂的问题，难以作为交互式设计工具落地。
### 方法关键点
1. 提出Hash-Atlas网络，将3D场景编辑转换为2D atlas图像操作，实现2D编辑与3D重建流程完全解耦
2. 构建以LLM为核心的CE3D++对话式编辑框架，支持用户任意文本输入，自动理解意图并调度对应视觉模型
3. 构造编辑任务专属轨迹数据集微调小参数LLM，新增运动约束扩展支持单目4D场景编辑
### 关键结果
小参数LLM可精准调度最多30种不同视觉工具，具备强场景理解能力与多轮对话能力，可实现多样化视觉编辑效果
