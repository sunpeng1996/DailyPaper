---
title: 'AutoTrainess: Teaching Language Models to Improve Language Models Autonomously'
title_zh: AutoTrainess：支持大语言模型自主迭代训练的智能体框架
authors:
- Zhaojian Yu
- Penghao Yin
- Shuzheng Gao
- Shilin He
- Kai Cai
- Xiao-Ping Zhang
affiliations:
- Tsinghua University
- The Chinese University of Hong Kong
- Simple Agent Lab
arxiv_id: '2606.31551'
url: https://arxiv.org/abs/2606.31551
pdf_url: https://arxiv.org/pdf/2606.31551
published: '2026-06-30'
collected: '2026-07-01'
category: Agent
direction: Agent · 大模型自主训练优化
tags:
- LLM Agent
- Agent-Computer Interface
- Autonomous Training
- Post-training
- AutoML
one_liner: 通过封装人类训练经验的专用ACI接口，实现无需人工干预的LLM自主后训练，性能显著优于CLI基线
practical_value: '- 开发业务Agent时避免开放裸CLI，可参考该思路封装领域专用ACI接口，把推荐/广告场景的特征工程规则、训练范式约束、安全校验等最佳实践内嵌到接口中，大幅降低Agent执行错误率

  - 四阶段闭环流程（规划→数据处理→训练/策略优化→评估→日志沉淀）可直接复用，适合推荐系统自动调优、A/B实验自动迭代、用户增长策略自动优化等场景

  - 数据处理阶段「先对齐基准格式再做生成/增强」的思路可迁移到推荐训练数据构造：先对齐线上推理的prompt模板、样本格式，再做数据清洗、合成，从根源降低训练-线上分布不一致问题

  - 结构化迭代日志设计可直接用到业务实验管理系统，每轮迭代的动机、改动、结果、下一轮计划结构化存储，方便Agent和人工回溯分析，减少实验重复劳动'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前LLM训练高度依赖人工参与，即便现有编码Agent能完成简单开发任务，但直接通过裸CLI执行训练时，会频繁出现数据格式错误、训练流程不稳定、评估结果不可比等问题，缺乏内嵌人类训练经验的专用交互接口，导致自主训练成功率极低，难以实现长周期的模型迭代优化。

### 方法关键点
- 设计训练专用Agent-Computer Interface（ACI）集合AutoTrainHub，把人类训练经验封装为规划&日志、数据处理、训练、评估4个阶段的标准化接口，约束Agent动作空间，避免无意义的自由探索
- 数据处理模块内置数据选择、构造、校验三级流程，强制要求训练样本对齐benchmark的输入输出格式，提前过滤低质量、存在泄露风险的数据，降低训练失败率
- 训练模块固定LlamaFactory作为统一后端，屏蔽框架选择复杂度，要求训练前先做小批量验证，保证流程可复现
- 评估模块强制使用benchmark官方入口，要求输出结构化错误分析，直接指导下一轮迭代；日志模块沉淀每轮迭代的完整上下文，作为长周期决策的记忆基础

### 关键实验
在PostTrainBench上测试，覆盖4个基座模型（Qwen3-1.7B/4B、SmolLM3-3B、Gemma3-4B），10小时H20 GPU时限，对比CLI-only基线：
- GPT-5.4（Codex）作为Agent基座时，AutoTrainess平均得分26.94，比CLI基线的23.21提升16.2%
- DeepSeek-V4-Flash（OpenCode）作为Agent基座时，得分从12.13提升到19.58，相对提升61.4%
- 消融实验显示各模块均有核心贡献：移除数据接口训练失败率提升5.5个百分点，移除评估接口评估失败率提升15.2个百分点

### 核心结论
给Agent开放能力时，内嵌领域最佳实践的约束接口比无限制的自由操作空间，更能提升复杂长周期任务的执行效率和成功率。
