---
title: Task Context Shapes Component Roles in Language Models
title_zh: 任务上下文对大语言模型内部组件功能角色的调控机制
authors:
- Sovesh Mohapatra
- Dani S Bassett
affiliations:
- University of Pennsylvania
- Yale University
arxiv_id: '2610.13895'
url: https://arxiv.org/abs/2610.13895
pdf_url: https://arxiv.org/pdf/2610.13895
published: '2026-10-09'
collected: '2026-10-12'
category: LLM
direction: LLM机制解释 · 组件功能动态性
tags:
- LLM Interpretability
- Attention Head
- Task Context
- Mechanistic Interpretability
- Activation Intervention
one_liner: 揭示任务上下文调控LLM共享注意力头的响应偏好与下游影响路径的机制
practical_value: '- 做LLM驱动的推荐/Agent任务时，可通过任务向量激活编辑快速切换任务，无需修改prompt或微调，适合多任务场景下的轻量调度

  - 做LLM推理优化时，可根据当前任务上下文动态裁剪指定注意力头的计算，降低推理延迟，尤其适配多轮推荐对话场景

  - 做RAG/多事实推理类推荐（如组合搭配推荐）时，可通过干预早期激活控制模型关注的事实，避免无关信息干扰，提升推荐理由准确性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM电路分析仅发现不同任务会共享注意力头，但无法解释相同组件在不同任务下的功能差异，无法支持精准的模型干预和行为调控，亟需明确任务上下文如何改变共享组件的作用模式。

### 方法关键点
- 覆盖5款1.5B~14B参数的开源LLM（Gemma-2-9B、Qwen3-14B、Llama3.1-8B、Falcon-H1 1.5B/7B），设计两类使用相同图事实但任务规则不同的推理任务，控制输入事实不变仅改变任务指令或内部激活状态
- 通过激活扰动测量组件间影响力（前层头输出变化对后层激活的影响）和组件重要性（替换组件激活对答案logit的影响），构建不同任务下的组件交互图谱
- 采用任务向量激活编辑技术，在不改变输入prompt和模型权重的前提下切换内部任务状态，观测相同组件的响应变化

### 关键结果
- 任务切换会大幅改变组件间的影响力分布，影响力模式的跨任务旋转角度比重要性模式高11.98°~30.17°，说明组件交互比单独组件的贡献更易受任务调控
- 仅编辑早期层激活即可让Gemma-2-9B、Qwen3-14B切换关注的事实，目标事实响应份额最高提升97.1个百分点，下游影响模式完全匹配目标任务
- 任务匹配的响应地图预测下游头激活的MSE比平均地图低53.6%（Gemma）和5.0%（Qwen），事实相关时相同扰动的下游响应强度提升40%~53%

### 核心结论
LLM共享组件的功能不是固定的，而是由其所处的任务上下文和下游网络的状态共同决定的
