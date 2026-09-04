---
title: Using Grounded Theory for Agent Behavior Analysis at Scale
title_zh: 基于扎根理论的大规模Agent行为分析框架AutoTraceGT
authors:
- Zhuoran Lu
- Yangyang Yu
- Zhuoyan Li
- Yibo Meng
- Nan Jiang
- Chengxi Zang
- Jie Gao
- Ziang Xiao
affiliations:
- Purdue University
- Stevens Institute of Technology
- Cornell University
- University of Texas at El Paso
- Johns Hopkins University
arxiv_id: '2608.30391'
url: https://arxiv.org/abs/2608.30391
pdf_url: https://arxiv.org/pdf/2608.30391
published: '2026-08-30'
collected: '2026-09-04'
category: Agent
direction: Agent行为分析 · 自动化扎根理论框架
tags:
- Agent
- Grounded Theory
- Behavior Analysis
- Multi-Agent Pipeline
- Trajectory Analysis
one_liner: 首个自动化扎根理论多Agent流水线，可规模化分析Agent轨迹行为模式，覆盖73-91%人工标注失败模式
practical_value: '- 可复用多Agent角色分工架构做大规模业务日志（比如推荐/搜索Agent交互轨迹、客服Agent会话轨迹）的无监督行为模式挖掘，替代人工标注降低成本

  - 可借鉴理论饱和停止准则，做无监督标签体系建设的自动终止判断，无需预设迭代轮次即可保证标签覆盖度

  - 生成的行为codebook可直接作为下游任务（Agent失败预警、用户流失预测、推荐效果归因）的特征输入，实测比few-shot LLM baseline效果提升明显

  - 针对电商导购Agent、客服Agent的故障归因场景，可直接复用该框架挖掘未知失败模式，补充预定义故障分类体系漏判的case'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent行为分析存在三类局限：仅统计步数、重试次数等量化指标无法解释成败根因；人工标注长序列轨迹成本极高无法规模化；预定义行为分类器刚性强，无法适配新任务的未知 emergent 行为，行业缺乏可扩展、可泛化的Agent行为分析方法论。
### 方法关键点
- 引入社会科学扎根理论，设计4角色多Agent流水线：OpenCode Agent标注单条轨迹的细粒度行为标签；AxialCode Agent聚合批次标签为行为分类；Manage Agent迭代维护全局codebook，采用merge-first策略对齐新旧分类；TheoreticalCode Agent在codebook饱和后输出全局行为理论解释
- 实现理论饱和自动停止准则：连续多轮新增分类数低于阈值即终止迭代，无需预设迭代轮次
- 全链路可审计：每个行为分类都关联原始轨迹的证据片段，结果可解释
### 关键结果
- 实验覆盖6个Agent轨迹数据集（含电商WebShop、客服Tau-Bench等场景）共7500+条轨迹，对比少样本/零样本LLM baseline、人工标注分类体系
- 生成的codebook覆盖73-91%人工标注的失败模式，同时挖掘出人工分类体系遗漏的跨模块、细粒度行为模式
- 基于codebook的特征做下游失败预测，ROC AUC较少数样本LLM baseline最高提升12.4个百分点
### 核心洞见
扎根理论的归纳式分析思路，比预定义分类的演绎式分析更适配开放场景下未知行为模式的挖掘需求
