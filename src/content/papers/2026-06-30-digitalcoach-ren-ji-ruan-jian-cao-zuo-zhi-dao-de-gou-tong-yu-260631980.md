---
title: 'DigitalCoach: Communication and Grounding Gaps in Human and Agentic Computer
  Use Coaching'
title_zh: DIGITALCOACH：人机软件操作指导的沟通与落地差距研究
authors:
- Meng Chen
- Anya Ji
- Tsung-Han Wu
- Tobias Maringgele
- David M. Chan
- Alane Suhr
- Amy Pavel
affiliations:
- University of California, Berkeley
- Technical University of Munich
arxiv_id: '2606.31980'
url: https://arxiv.org/abs/2606.31980
pdf_url: https://arxiv.org/pdf/2606.31980
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: Agent 人机协作技能指导优化
tags:
- Multimodal Agent
- GUI Agent
- Human-Agent Collaboration
- Dialogue Dataset
- Coaching Agent
one_liner: 构建28.1小时多模态GUI操作指导数据集，揭示AI教练相比人类的核心能力差距
practical_value: '- 开发电商工具指导类Agent（如教商家用设计工具做主图、用运营后台设置活动）时，可参考论文的教练方法分类，平衡直接指令、原理解释、知识校验的话术比例，避免仅输出步骤，提升用户技能留存

  - 多模态GUI Agent的上下文窗口选10~30s即可，超过30s增益极小，可大幅降低推理成本

  - 上线用户指导类Agent时，需额外增加屏幕状态校验模块，当前SOTA多模态大模型优先依赖文本历史，极易输出和当前界面不匹配的错误指令

  - 设计用户教学交互流程时，可参考人类教练节奏：先确认用户状态、解释原理，再给出操作指令，能显著提升学习效率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前GUI Agent多聚焦自动帮用户完成任务，完全跳过了用户自主学习软件技能的需求；现有教学对话数据集要么是纯文本，要么基于静态内容，没有和实时GUI状态、用户操作行为联动的多模态标注数据，无法支撑有效指导型Agent的开发与评估。

### 方法关键点
- 构建DIGITALCOACH数据集：覆盖Excel、Blender、Figma等5类主流专业软件，包含72组专家-新手指导会话，含22752轮对话、28.1小时录屏、39609个输入事件、36724个文件快照，标注了对话动作和10类教练方法（直接指令、解释、错误诊断、状态确认等）
- 评估范式：对比6款SOTA多模态大模型（GPT-5.4、Gemini系列、Claude、Qwen-3-VL、Llama-4）的教练能力，覆盖自动评估、专家打分、真人交互实验三个维度
- 消融实验：分别验证输入模态（文本/视觉/组合）、上下文窗口长度、prompt类型对生成质量的影响

### 关键结果数字
- 模型生成的直接指令占比超45%，人类仅为30%；模型的解释、知识提问类话术占比不足人类的1/2，语义/词汇多样性比人类低30%以上
- 最优模型Gemini-3.1-Pro在给定教练方法的前提下CLAIR得分41.4，但去掉视觉输入得分几乎无变化，说明模型几乎不利用视觉上下文
- 真人交互实验中，人类教练能让用户任务得分平均提升54.75%，模型仅提升31.67%，且有41.7%的用户无明显技能提升

**最值得记住的一句话：** 有效指导Agent需要平衡直接指令和用户自主性，仅靠prompt无法修复模型和人类教练的行为差距，必须从训练层面强化多模态grounding和教学策略学习。
