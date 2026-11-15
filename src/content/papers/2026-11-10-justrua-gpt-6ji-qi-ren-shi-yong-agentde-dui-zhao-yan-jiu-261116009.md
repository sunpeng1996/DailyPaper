---
title: 'JustRUA: A Controlled Study of GPT-6 Robot-Use Agents'
title_zh: JustRUA：GPT-6机器人使用Agent的对照研究
authors:
- Zefan Wang
- Yufan Dang
- Xuanwei Shi
- Mingqi Gao
- Cheng Yin
- SikYuen Tam
- Hanyu Liu
- Yasheng Wang
- Yaxi Lu
- Songyang Zhang
affiliations:
- Tsinghua University
- ModelBest
- Huazhong University of Science and Technology
- Peking University
- Tencent
arxiv_id: '2611.16009'
url: https://arxiv.org/abs/2611.16009
pdf_url: https://arxiv.org/pdf/2611.16009
published: '2026-11-10'
collected: '2026-11-15'
category: Agent
direction: 大模型驱动机器人Agent架构优化
tags:
- Agent
- LLM
- Harness Optimization
- Benchmarking
- Multimodal
- Control
one_liner: 拆分GPT-6驱动机器人的各设计模块增益，提出精简调度框架将RoboDojo基准分从29.7提至50.3
practical_value: '- 做Agent调度框架（如导购Agent、推荐决策Agent）时可参考「保留全会话历史+提前终止无效动作」的精简设计思路，避免过度堆叠无增益功能

  - 多模块迭代优化时优先采用单变量对照测试，明确每个组件的真实增益，解决多设计同时调整无法归因的问题

  - 给多模态Agent输入时优先补充结构化场景/上下文特征（如电商场景商品属性、用户行为结构化序列），收益远高于经验复用类trick'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
当前GPT-6驱动机器人的Agent系统普遍同时调整多个设计模块，无法明确各模块的真实增益，性能归因困难
### 方法关键点
1. 构建统一对照测试框架，拆分调度harness、动作接口、经验复用、场景几何输入四大类维度逐一测试
2. 基于官方L3框架做精简，仅保留核心有效设计，移除无增益组件
### 关键结果
1. 增益贡献排序：场景几何输入（仅从RGB预测深度也有显著收益）> 保留全episode历史+动作提前终止的精简调度框架
2. 经验复用需付出额外成本，无免费增益
3. 最终JustRUA无需额外训练、自优化循环或任务微调，RoboDojo基准分从29.7大幅提升至50.3
