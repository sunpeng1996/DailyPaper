---
title: Persona Learning from Feedback for Personalized AI Assistants
title_zh: 基于反馈学习的个性化AI助手Persona适配框架
authors:
- Yiran Shen
- Yu Xia
- Liuyi Yao
- Prithviraj Ammanabrolu
affiliations:
- UC San Diego
- Alibaba Group
arxiv_id: '2610.38561'
url: https://arxiv.org/abs/2610.38561
pdf_url: https://arxiv.org/pdf/2610.38561
published: '2026-10-28'
collected: '2026-10-30'
category: Agent
direction: Agent个性化 · 反馈驱动LoRA适配
tags:
- LoRA
- Persona Learning
- Feedback Alignment
- Agent Personalization
- Context Routing
one_liner: 通过反馈训练独立LoRA persona适配器结合上下文路由，实现无用户微调的AI助手个性化
practical_value: '- 电商客服/导购Agent可直接复用该框架：将常见用户偏好（简洁/详细/热情/专业）训练为独立LoRA适配器，无需逐用户微调，大幅降低个性化落地成本

  - 可直接复用反馈门控机制：仅对不符合偏好的响应执行梯度更新，既提升训练效率，又避免破坏模型通用能力，适合多风格输出场景的训练

  - 多偏好组合的LoRA权重拼接方法可直接落地：无需训练复合偏好的专用适配器，通过预调权重系数即可实现多风格融合，满足用户「热情+简洁」这类复合需求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有AI助手个性化依赖persona prompt或固定微调方案，仅靠persona描述无法定位单条响应的具体调整点，也无法灵活适配用户动态变化、组合式的偏好需求，逐用户微调的成本过高无法规模化落地，还易损伤模型通用能力。

### 方法关键点
- 每个persona对应独立LoRA适配器，共享冻结基座大模型，训练时不给学生模型传入persona提示，直接通过反馈习得对应行为模式
- 冻结自教师模型基于persona规范+单条响应的反馈，对学生生成的前缀提供token级监督；新增反馈门控，仅当响应不符合偏好时才更新对应适配器，提升训练效率
- 部署阶段训练轻量化监督路由器，从请求/对话上下文识别偏好，可选择单个适配器或通过固定权重拼接多个适配器实现复合偏好适配，全程无需用户侧微调

### 关键结果
单轮场景基于PRISM请求数据集测试，PLF相对persona prompt的偏好匹配胜率达61.7%；多轮辅导场景基于教育对话数据集测试，学生满意度达76.7%，仅比已知偏好的oracle低2.5个百分点；在IFEval、GSM8K、MMLU-Pro、MT-Bench通用基准上，性能相比基座无显著下降。

### 核心结论
将个性化行为拆分为可复用LoRA适配器+上下文路由的架构，可在不损失通用能力的前提下低成本规模化实现多偏好适配。
