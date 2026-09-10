---
title: 'TRACE: Training Reasoning Agents for Causal Exploration with Synthesized Rewards'
title_zh: TRACE：基于合成奖励训练广告诊断场景的因果推理Agent
authors:
- Rui Sun
- Zhan Shi
- Bing He
affiliations:
- Independent Researchers
arxiv_id: '2609.10315'
url: https://arxiv.org/abs/2609.10315
pdf_url: https://arxiv.org/pdf/2609.10315
published: '2026-09-09'
collected: '2026-09-10'
category: Agent
direction: Agent 因果诊断 · 合成奖励训练
tags:
- Reinforcement Learning
- Causal Reasoning
- Root Cause Analysis
- Synthetic Reward
- Ad Diagnostic
- Agent
one_liner: 通过模拟干预生成合成奖励训练因果推理Agent，在广告异常诊断任务上超越前沿闭源模型
practical_value: '- 广告/电商效果异动根因诊断Agent可复用「模拟器注入已知干预→生成观测数据→隐藏干预作为Oracle标签做RL训练」的pipeline，无需人工标注或LLM-as-judge即可生成客观奖励

  - 多维度归因的奖励设计可直接复用：用Jaccard相似度给部分正确的归因打部分分，叠加全匹配二进制奖励，平衡训练梯度密度和精准归因激励，尤其适合定位多维度人群/资源位的场景

  - 训练流程优先采用SFT暖启动教Agent工具调用格式和基本诊断逻辑，再上RL优化，比直接从基模型启动RL效果提升更显著，还能大幅降低格式错误率

  - 广告/推荐的异动归因业务可参考TRACE的12类根因分类（campaign级、流量结构级、细分segment级、无信号）搭建内部诊断基准测试集'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有带可验证奖励的强化学习（RLVR）在数学、代码领域进展显著，但广告/复杂系统的异常诊断场景没有天然可验证标注，根因标注成本高且结论模糊，LLM-as-judge还存在奖励黑客风险，缺乏可扩展的客观训练信号。

### 方法关键点
- 设计模拟器-Oracle-RL合成奖励范式：先在受控模拟器中采样隐藏干预（根因、影响segment、生效时间），生成带噪声、混淆因子的真实观测数据，用隐藏干预作为Oracle标签生成客观奖励，完全无需人工标注
- 构建TRACE广告诊断环境，覆盖12类根因（campaign级、流量结构级、细分segment级、无信号4大类），支持Python/SQL工具调用，Oracle先验证样本可解、有区分度再纳入训练/测试集
- 奖励由三部分组合：分级归因奖励（原因正确前提下用Jaccard给segment匹配度打分，提供部分credit）、全匹配二进制奖励、格式奖励；训练流程先做SFT暖启动（1200条专家轨迹）再做GRPO RL优化

### 关键实验
测试集为235个独立holdout诊断样本，基线包括Claude Opus 5、GPT-5.6、Qwen3.5-122B等。SFT将Qwen3.5-35B的FullAttr@1从0.159提升到0.637，叠加RL后提升到0.757，超过Claude Opus 5的0.686，也远超提示词版Qwen3.5-122B的0.283，同时工具调用次数比提示词版35B减少近一半（11.73 vs 22.05）。

### 核心结论
对诊断类推理任务，可扩展的高质量训练信号约束，比单纯的模型规模更重要。
