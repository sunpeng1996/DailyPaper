---
title: 'SkillOpt-Lite: Better and Faster Agent Self-evolution via One Line of Vibe'
title_zh: SkillOpt-Lite：极简流水线实现更优更快的Agent技能自进化
authors:
- Yifei Shen
- Bo Li
- Xinjie Zhang
affiliations:
- LMMs-Lab
- NTU MMLab
- Microsoft
arxiv_id: '2607.03451'
url: https://arxiv.org/abs/2607.03451
pdf_url: https://arxiv.org/pdf/2607.03451
published: '2026-07-02'
collected: '2026-07-08'
category: Agent
direction: Agent 技能自进化 · 极简流水线优化
tags:
- Agent-Self-Evolution
- Skill-Optimization
- Zeroth-Order-Optimization
- Harness-Optimization
- LLM-Agent
one_liner: 提出仅含3个核心模块的极简Agent技能自优化流水线，性能和收敛速度均优于复杂基线
practical_value: '- 电商导购/客服Agent技能迭代可复用极简设计：将每个执行轨迹存为独立文件，用文件系统工具遍历挖掘共性问题，移除mini-batch合并、慢更新等冗余模块，大幅降低优化复杂度、提升迭代速度

  - 小模型落地Agent场景可借鉴HarnessOpt思路：无需盲目升级大模型，同时优化prompt技能与执行脚手架（工具调用逻辑、错误fallback策略等），可让小模型性能超过配置不佳的大模型，压低推理成本

  - 所有业务Agent迭代流程可直接复用验证原则：必须使用严格独立于训练集的验证集做门控，避免在训练失败样本上验证导致的过拟合、泛化能力下降问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent技能优化方案过度堆砌复杂模块，不仅工程开销大，还会模糊离散文本空间的优化信号，拖慢收敛速度、降低最终性能；业界缺少经理论验证的最小可行技能优化流水线，导致Agent自进化落地门槛高、效率低。

### 方法关键点
- 基于零阶优化（ZO）和PAC学习理论，推导3个核心设计原则：跨轨迹共识挖掘、独立验证门控、基于文件系统的轨迹探索，移除所有无理论/经验支撑的冗余模块
- SkillOpt-Lite流水线仅保留4步：轨迹落盘为独立文件、用基础文件工具自主探索日志、挖掘共性失败模式生成最小修改补丁、独立验证集门控决定是否更新技能
- 扩展出HarnessOpt支持优化Agent执行脚手架（工具调用、控制流等），新增启动阶段人工校验、沙箱验证、可回滚编辑等安全机制

### 关键实验
在SearchQA、Spreadsheet、LiveMath等6个基准测试，对比原SkillOpt基线：
- LiveMath任务上GPT-5.5提分8.8，GPT-5.4-nano提分25.4，优化后的小模型性能超过原SkillOpt优化后的标准GPT-5.4
- Spreadsheet任务平均提分12.6，ALFWorld任务上GPT-5.4-nano提分9.5，收敛速度比基线快3倍以上
- HarnessOpt在SpreadsheetBench上让GPT-5.4-nano准确率达0.7758，超过运行标准流水线的更大参数的GPT-5.5（0.7620）

### 核心洞察
随着基础模型能力提升，为Agent优化设计的复杂专用算法往往不如将所有系统 artifact 视作普通文件、授予模型基础文件系统操作工具的极简方案效果好
