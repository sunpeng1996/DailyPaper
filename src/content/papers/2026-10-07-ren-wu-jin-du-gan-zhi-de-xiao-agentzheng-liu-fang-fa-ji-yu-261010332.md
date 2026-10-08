---
title: 'Learning to Act with Task Progress: Distilling Small Agents from Compact Teacher
  Supervision'
title_zh: 任务进度感知的小Agent蒸馏方法：基于紧凑教师监督训练
authors:
- Wenxi Gan
affiliations:
- City University of Hong Kong
- Shenzhen Loop Area Institute
arxiv_id: '2610.10332'
url: https://arxiv.org/abs/2610.10332
pdf_url: https://arxiv.org/pdf/2610.10332
published: '2026-10-07'
collected: '2026-10-08'
category: Agent
direction: Agent小模型蒸馏 · 任务进度监督
tags:
- Agent Distillation
- Task Progress
- Small LLM
- Offline SFT
- ALFWorld
one_liner: 提出任务进度蒸馏（TPD）方法，少量演示下即可高效训练性能优异的小参数任务Agent
practical_value: '- 电商/广告场景下的重复性流程Agent（如客服工单处理、商品上新审核）可参考TPD思路，给多步任务打阶段标签，少量演示样本下就能快速训练出小参数执行Agent，大幅降低推理成本

  - 小样本Agent训练时优先采用「动作模仿+候选集约束选择」方案，比同时学习推理+动作的方案效果高20%以上，还能避免推理输出不可解析的问题

  - 当训练样本量有限（如少于500条演示轨迹）时，加入任务阶段标签能带来15%+的效果提升，样本量充足后可简化为纯动作模仿降低训练复杂度

  - Agent执行阶段用「候选集打分」代替自由生成，能大幅降低输出错误率，适合电商推荐/搜索等可控性要求高的场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
大模型作为Agent执行多步任务时推理成本高、延迟高，面向高频重复性任务，从大模型演示轨迹蒸馏小Agent是主流降本方案，但现有方法要么需要学习长推理链导致样本利用率低，要么纯动作模仿在小样本下子目标切换容易出错，亟需兼顾小样本效率和最终效果的蒸馏方案。

### 方法关键点
- 提出Task-Progress Distillation（TPD）框架，离线为每条大模型演示动作标注任务阶段标签（分为定位目标、转换处理、交付三类），学生模型同时学习阶段标签和对应动作
- 执行阶段学生模型对所有可行的「阶段-动作」对联合打分，选择得分最高的动作执行，阶段仅用于打分不传入下一轮推理，避免累积错误
- 基线方案包含纯动作模仿蒸馏、学习推理+动作的蒸馏两类，所有方法均基于固定演示数据集做离线SFT，无在线交互训练

### 关键实验结果
在ALFWorld多步任务基准测试，学生模型采用Qwen3-1.7B：
- 404条演示时，TPD和纯动作模仿的unseen任务成功率均达72.4%，比「学习推理+动作+约束选择」基线高24.1pp，比自由生成的推理基线高67.4pp
- 200条小样本演示时，TPD成功率达67.7%，比纯动作模仿高19.7pp，优势主要来自子目标切换（如拿到需加热物品后直接去微波炉而非继续搜索）的准确率提升
- 808条演示时两种紧凑蒸馏方案成功率均达76.9%，和大模型教师的88.1%仅差11.2pp，推理输出token量仅为学习推理基线的1/33

> 最值得记住的一句话：少量样本训练小Agent时，先把大模型推理压缩成「阶段+动作」的紧凑标签，比让小模型直接学完整推理链的效率和效果都高得多
