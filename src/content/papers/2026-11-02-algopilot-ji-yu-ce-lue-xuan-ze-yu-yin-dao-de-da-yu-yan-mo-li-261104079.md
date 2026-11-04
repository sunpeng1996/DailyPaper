---
title: 'AlgoPilot: Cross-Paradigm Reasoning in Language Models via Strategy Selection
  and Guidance'
title_zh: AlgoPilot：基于策略选择与引导的大语言模型跨范式推理框架
authors:
- Yilun Hao
- Ruixiao Yang
- Hudson Hilal
- Yongchao Chen
- Kaizhi Qian
- Yada Zhu
- Yang Zhang
- Chuchu Fan
affiliations:
- Massachusetts Institute of Technology
- Harvard University
- MIT-IBM Watson AI Lab
arxiv_id: '2611.04079'
url: https://arxiv.org/abs/2611.04079
pdf_url: https://arxiv.org/pdf/2611.04079
published: '2026-11-02'
collected: '2026-11-04'
category: Reasoning
direction: 大语言模型 · 跨范式推理优化
tags:
- Cross-Paradigm Reasoning
- SteerLM
- GuideLM
- GRPO
- LLM Reasoning
- Strategy Selection
one_liner: 三模块跨范式推理框架将8B模型推理准确率从38.4%提升至72.9%，超GLM-5基线11.7%
practical_value: '- 可复用「路由层+领域专家引导层+执行层」三模块架构搭建业务Agent：电商场景下可自动路由用户问题到搜索/推荐/客服/履约工具链，先输出结构化引导再调用执行模块，大幅降低小模型执行错误率

  - 训练路由模块（类似SteerLM）时可先用SFT冷启动再用GRPO做RL优化，用下游执行成功率做奖励信号，不需要人工标注策略选择标签，降低训练成本

  - 电商复杂决策类任务（供应链优化、大促资源分配、营销ROI预估）可参考范式选择逻辑，自动匹配CoT/代码/MILP求解器，不需要人工指定求解路径

  - 小模型部署优化：业务受成本限制只能用小模型时，可外接轻量路由+引导模块，不需要大规模微调底座就能提升推理准确率，降低迁移成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM推理方法大多依赖固定提示模板或单一工具，而真实场景问题（规划、优化、逻辑推理等）需要适配完全不同的求解范式，手动指定范式效率低、准确率差，小模型更是难以直接处理复杂跨域推理任务。

### 方法关键点
- 三模块分层解耦架构：1) SteerLM：先SFT后GRPO训练，自适应选择CoT/代码/SMT约束求解/PDDL规划/MILP优化5种范式，同时判断是否需要生成引导；2) 范式专属GuideLM：用SFT训练，为选中的范式生成结构化配方引导（如MILP场景输出变量、约束、目标定义）；3) ExecuteLM：基于选定范式和引导生成最终可执行方案
- 免人工标注数据构造：通过多轮执行过滤生成高价值引导样本，再跨范式打分得到SteerLM的监督信号，避免组合搜索爆炸
- GRPO奖励设计兼顾首位准确率和候选集质量：加权前3位范式的执行成功率，加排序一致性、格式校验惩罚，同时鼓励输出多个可行策略

### 关键结果
- 数据集覆盖5类推理范式、13个基准、66个领域共2.2万样本；基于Qwen3-8B底座，比原生模型准确率从38.4%提升至72.9%，比744B参数的GLM-5最优基线高11.7%
- 模块可迁移：SteerLM和GuideLM可直接迁移到Gemma-4-E4B-it底座，准确率从39%提升至60.5%
- 鲁棒性：问题表述改写后路由决策一致性达98%，仅掉点4.3个百分点

最值得记住的一句话：跨范式推理的核心不是盲目用更大的模型，而是把「选什么解法」和「怎么按解法配方转化问题」两个步骤从执行过程中解耦出来，用极小的微调成本就能大幅提升小模型的复杂任务表现
