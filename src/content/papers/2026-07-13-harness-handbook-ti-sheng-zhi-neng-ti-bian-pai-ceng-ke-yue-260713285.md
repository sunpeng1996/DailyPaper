---
title: 'Harness Handbook: Making Evolving Agent Harnesses Readable,Navigable, and
  Editable'
title_zh: Harness Handbook：提升智能体编排层可阅读、可导航与可编辑性
authors:
- Ruhan Wang
- Yucheng Shi
- Zongxia Li
- Zhongzhi Li
- Yue Yu
- Junyao Yang
- Kishan Panaganti
- Haitao Mi
- Dongruo Zhou
- Leoweiliang
affiliations:
- Tencent HY LLM Frontier
- Indiana University
- University of Maryland, College Park
- University of Georgia
- National University of Singapore
arxiv_id: '2607.13285'
url: https://arxiv.org/abs/2607.13285
pdf_url: https://arxiv.org/pdf/2607.13285
published: '2026-07-13'
collected: '2026-07-16'
category: Agent
direction: Agent 编排层自动化迭代优化
tags:
- Agent Harness
- Behavior Localization
- Static Program Analysis
- LLM for SE
- Automated Code Editing
one_liner: 提出行为中心化的智能体harness知识库，自动关联行为与源代码，降低harness迭代的行为定位成本
practical_value: '- 自研推荐/广告Agent系统时，可复用三层分级（系统概览-组件概览-单元深钻）的行为-代码映射架构，降低大模型驱动的Agent代码迭代的定位成本

  - 静态程序分析+LLM辅助行为结构化的构建流程可直接迁移到内部代码库的知识库建设中，替代纯人工维护的系统文档，减少新人上手和迭代改造成本

  - Behavior-Guided Progressive Disclosure（BGPD）的粗到细定位逻辑，可复用在大模型代码修改场景，减少token消耗同时提升定位准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
生产级Agent的harness（编排层）负责prompt构造、状态管理、工具调用、执行协调，是Agent能力落地的核心。但harness迭代时需要先定位行为对应的代码位置，而现有代码搜索、长上下文处理方案都是按文件/函数组织信息，无法直接关联自然语言描述的行为需求与分散在多模块、多执行阶段的实现代码，行为定位成为harness迭代的核心瓶颈。

### 方法关键点
- 提出三层分级的Harness Handbook表示：L1系统概览（架构、执行模型、主流程）→ L2组件概览（各阶段职责、输入输出、依赖）→ L3单元深钻（关联具体源代码位置），同时配套跨阶段状态关联视图
- 自动化构建流程：先通过静态程序分析提取代码调用图、状态读写等事实，再通过LLM辅助将代码单元映射到执行阶段，最终合成层级化的行为知识库
- 提出BGPD（行为引导渐进式披露）修改流程：从粗到细定位目标行为对应的代码位置，验证后生成修改方案，代码变更后自动增量同步Handbook，无需全量重建

### 关键实验
在两个开源Agent harness（Terminus-2、Codex）的共60个真实修改请求上测试，对比直接探索仓库的基线：整体方案质量胜率提升10~18.9个百分点，规划token消耗降低8.6%~12.7%；符号级行为定位F1最高提升18.8个百分点，完全定位失败率最高降低25.9个百分点；弱规划器配合Handbook的定位效果可匹配远强于自身的大模型的输出。

最值得记住的一句话：复杂智能体系统的迭代不仅取决于生成修改代码的能力，更取决于精准定位修改位置的能力。
