---
title: 'SkillForge: Self-Distilling Agents for Project-Specific Issue Resolution'
title_zh: SkillForge：面向特定项目问题解决的自蒸馏智能体框架
authors:
- Silin Chen
- Han Li
- Xiaodong Gu
- Yuling Shi
- Haibing Guan
affiliations:
- Shanghai Jiao Tong University
arxiv_id: '2608.18933'
url: https://arxiv.org/abs/2608.18933
pdf_url: https://arxiv.org/pdf/2608.18933
published: '2026-08-18'
collected: '2026-08-20'
category: Agent
direction: Agent 项目特定知识自蒸馏优化
tags:
- LLM Agent
- Self-Distillation
- Cold Start
- Knowledge Retrieval
- Software Engineering
one_liner: 通过主动合成项目问题自蒸馏双层级实体锚定技能，解决软件智能体项目冷启动问题
practical_value: '- 可复用双层级知识蒸馏+分阶段注入架构：先离线从业务现有数据（电商历史订单/搜索点击流/平台规则）合成模拟问题，蒸馏全局（平台规则/类目特征）+局部（单个商品/商家属性）领域知识，再通过全局知识初始化Agent上下文、实时交互中注入对应实体的局部技能，高效解决Agent业务冷启动问题

  - 实体锚定的知识检索设计可直接迁移：放弃纯语义匹配检索逻辑，改为Agent访问到对应业务实体（商品/活动页/商家）时实时注入对应知识，大幅降低检索噪音，适配电商/推荐Agent的实时交互场景

  - 冷启动阶段知识获取方法可借鉴：无需依赖历史用户反馈/问题日志，可从业务本身的测试用例、规则文档、历史交互数据合成模拟问题，低成本预训练Agent的领域知识，适配新业务线/新站点的快速上线需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM驱动的领域Agent在特定业务/项目上执行任务时存在严重冷启动缺陷：缺乏项目专属知识，需要反复试错才能适配项目特定规则；现有自进化方法要么依赖历史问题解决信号、长尾场景覆盖度极低，要么在问题到达后才做在线探索、单问题时间/Token成本极高，无法适配新项目冷启动场景。

### 方法关键点
- 主动合成项目问题：基于项目已有的测试用例执行轨迹定位核心功能代码段，LLM在受限上下文下重写代码生成模拟bug及对应问题描述，完全无需历史问题数据支撑
- 双层级技能蒸馏：从模拟问题的解决轨迹中，蒸馏两类与实体绑定的技能：1）全局诊断技能，包含模块功能、排查流程、关联API等项目级通用知识；2）局部干预技能，包含单实体的修改规则、避坑指南等专属知识
- 分阶段技能适配：新问题到达时先检索全局诊断技能初始化Agent上下文，Agent运行过程中访问到对应实体时，实时注入对应的局部干预技能，避免全量注入引入的上下文噪音

### 关键实验
在SWE-bench Verified、SWE-bench Pro两个通用SWE基准上测试，对比历史驱动、在线探索类所有基线：用DeepSeek-V3.2时SWE-bench Verified Pass@1达72.2%，较基线提升5.8pp，SWE-bench Pro提升5.8pp；用GPT-5-mini时对应提升5.6pp、4.1pp，同时单问题成本远低于在线探索类方法。

**最值得记住的一句话：主动从目标业务系统本身预蒸馏领域知识，而非等待历史反馈积累，是解决Agent业务冷启动的高性价比路径。**
