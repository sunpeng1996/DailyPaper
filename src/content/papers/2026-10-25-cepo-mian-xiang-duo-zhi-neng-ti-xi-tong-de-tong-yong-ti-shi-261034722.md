---
title: 'CEPO: A General Framework for Improving Prompt Optimization in Multi-Agent
  Systems'
title_zh: CEPO：面向多智能体系统的通用提示优化框架
authors:
- Jongha Kim
- Seohyun Lee
- Jonathan Minho Chung
- Jinsung Yoon
- Hyunwoo J. Kim
affiliations:
- Korea University
- KAIST
- Google Cloud AI Research
arxiv_id: '2610.34722'
url: https://arxiv.org/abs/2610.34722
pdf_url: https://arxiv.org/pdf/2610.34722
published: '2026-10-25'
collected: '2026-11-02'
category: Agent
direction: 多智能体 · 提示优化框架
tags:
- Multi-Agent
- Prompt Optimization
- Coordinator-Executor
- LLM
- MAS
one_liner: 将多智能体协调与执行提示拆分，配合角色对齐优化，兼容现有提示优化器并稳定提升性能
practical_value: '- 多智能体系统Prompt设计可直接复用拆分思路：将跨角色共享的协作规则（如电商导购多Agent的工单流转、信息同步规范）抽为全局coordinator
  prompt，每个角色的执行指令单独作为executor prompt，避免重复修改多份Prompt

  - Prompt优化阶段可先固定执行Prompt优化全局协调规则，再固定协调规则优化单个高价值角色的执行Prompt，比直接全量优化每个角色的Prompt省30%+优化API调用量，效果更优

  - 协调规则Prompt具备跨任务迁移性，如电商文档审核多Agent的协调Prompt可直接迁移到商品信息质检多Agent场景，仅微调执行Prompt即可达到接近域内优化的效果，降低冷启动成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多智能体系统的Prompt优化将全局协调逻辑与单Agent执行指令耦合在每个角色的Prompt内，修改协调规则需同步调整多份Prompt，优化成本高、效果不稳定，且缺乏可适配所有现有Prompt优化器的通用框架。
### 方法关键点
- 采用协调-执行Prompt拆分结构：全局共享1份coordinator prompt定义跨Agent协作规则（如冲突处理、信息同步规范），每个Agent单独持有executor prompt定义自身任务执行逻辑，调用时拼接两者作为有效Prompt
- 设计角色对齐优化流程：先固定所有executor prompt，用面向协作的meta-instruction优化coordinator prompt；再固定最优coordinator prompt，用面向执行的meta-instruction优化指定Agent的executor prompt
- 完全兼容PE2、OPRO、MASPO等所有现有Prompt优化器，无需修改优化器底层逻辑
### 关键实验结果
在11个基准数据集、4个领域（文档理解、数学推理、代码生成、视频理解）验证，给4种现有Prompt优化器叠加CEPO后，平均性能提升2.7~5.07个百分点；在文档理解任务上，相同API调用预算下CEPO比原生优化器效果高3.6个百分点，系统内Agent数量越多CEPO增益越大，5个Agent时增益达6.9个百分点。
> 最值得记住的结论：多智能体Prompt优化的核心是将全局协作逻辑与局部执行逻辑解耦，优化方向与角色职能对齐才能用更低成本获得更高收益
