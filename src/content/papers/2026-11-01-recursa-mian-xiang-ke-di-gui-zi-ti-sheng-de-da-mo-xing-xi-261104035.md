---
title: 'Recursa: Toward Recursively Self-Improving Foundation Model Systems'
title_zh: Recursa：面向可递归自提升的大模型系统
authors:
- Erkang Zhu
- Yin Lin
- Xiaorong Shi
- Xuanrui Lin
- Jingren Zhou
affiliations:
- Alibaba Research
arxiv_id: '2611.04035'
url: https://arxiv.org/abs/2611.04035
pdf_url: https://arxiv.org/pdf/2611.04035
published: '2026-11-01'
collected: '2026-11-04'
category: Agent
direction: Agent 递归自提升领域适配
tags:
- Self-Improving Agent
- Multi-Agent System
- Domain Adaptation
- Knowledge Repository
- Agent Harness
one_liner: 无需人类专家或更强教师模型，通过多Agent递归迭代优化知识仓库实现新领域自适应
practical_value: '- 电商垂域大模型适配可复用两阶段方案：先从领域语料Bootstrap生成导航结构+技能，再用业务任务迭代优化知识仓库，无需额外标注成本

  - Agent harness设计可直接迁移：用持久化Python REPL做工具编排、程序式上下文管理（事件日志外置按需查询），能大幅降低长链路Agent的token消耗和出错率

  - 多Agent拆分训练任务策略可复用到推荐冷启动适配：按任务类型/失败case分组并行优化，合并后泛化性优于单Agent全量训练，提升迭代效率

  - 自生成练习任务思路可优化RAG效果：从领域语料自动生成QA对做自练习，把检索、验证逻辑沉淀为技能，提升知识召回准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
大模型落地陌生领域时普遍缺少专家标注数据或可靠监督信号用于继续训练，现有方法大多仅针对知识缺口或行为缺口单一优化，且依赖更强教师模型驱动，无法实现无外部干预的闭环自迭代，难以适配法律、金融、电商垂域等高知识密度、高自定义规则的场景。

### 方法关键点
- 两阶段适配流程：先从领域语料Bootstrap知识仓库，生成领域导航结构、可复用技能，再通过递归自迭代优化仓库，同时覆盖知识缺口和行为缺口
- 统一Agent Harness：基于持久化Python REPL实现工具编排、程序式上下文管理（全量交互日志外置按需查询）、多Agent并行调度，大幅降低长链路任务的token消耗
- 递归自迭代逻辑：多Learner并行拆分处理任务子集，诊断Solver执行失败case后修订知识仓库，验证无回归后合并修订结果，全程无需人类专家或更强模型介入

### 关键实验
在Harvey LAB法律领域基准（含9288份文件、250个长链路任务）上测试：对比无学习的基线系统，搭载DeepSeek-V4.1-Flash的测试集全通过率从30.0%提升至55.0%，搭载Qwen3.8-Flash从35.0%提升至46.0%；Bootstrap阶段可降低20%以上的交互轮次和输入token消耗，多Learner并行方案效果显著优于单Learner全量训练。

优先优化文本形态的可解释知识组件，再反哺模型权重与架构迭代，是低标注成本下大模型领域适配的最高效路径之一
