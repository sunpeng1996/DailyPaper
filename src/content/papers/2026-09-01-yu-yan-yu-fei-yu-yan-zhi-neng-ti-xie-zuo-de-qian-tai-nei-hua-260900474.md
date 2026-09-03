---
title: Exploring Collaboration between a language and a non-language agent
title_zh: 语言与非语言智能体协作的潜态内化范式研究
authors:
- Harini S I
- Somesh Singh
- Yaman K Singla
- Rajiv Ratn Shah
- David Doermann
- Balaji Krishnamurthy
affiliations:
- Adobe Media and Data Science Research
- IIIT-Delhi
- IIT Kanpur
- SUNY at Buffalo
arxiv_id: '2609.00474'
url: https://arxiv.org/abs/2609.00474
pdf_url: https://arxiv.org/pdf/2609.00474
published: '2026-09-01'
collected: '2026-09-03'
category: Agent
direction: 异构Agent协作范式优化
tags:
- LLM-Agent Collaboration
- Latent State Internalization
- Verbalization Debt
- DAPO
- Multi-Agent
one_liner: 提出潜态内化范式绕过语言转写瓶颈，实现LLM与非语言专业Agent高效协同推理
practical_value: '- 异构业务系统对接LLM时不要局限于文本tool call：可将召回/排序/销量预测等非语言业务模型的隐层输出，通过轻量MLP投影为LLM
  embedding空间的连续token，替代传统特征转文本的有损方案，大幅提升个性化文案生成、营销活动决策等任务效果

  - 两阶段训练策略可直接复用：先冻结LLM训练投影层完成隐态分布对齐，再用RL联合微调LLM与投影层，既避免LLM灾难性遗忘原有能力，又能端到端优化协作效果，适合业务场景中LLM快速对接存量业务模型

  - 明确verbalization debt是结构性瓶颈：不会随LLM参数量增大消失，业务做Agent协作时要优先做信号层打通，不要盲目堆大模型参数，例如搜索场景下Query理解模型的隐态直接对接排序模块的效果远好于转成文本标签

  - 可根据业务latency要求灵活调整投影token数：论文验证32个token即可达到效果饱和，业务侧可在效果和耗时之间做tradeoff，平衡推理成本与业务指标'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM作为编排器与专业子Agent协作时普遍依赖自然语言转写，但游戏、机器人、推荐等场景的最优Agent均为非语言模型，其丰富的连续隐态转成文本会损失大量核心信息，形成结构型转写瓶颈，现有方案既未量化该瓶颈的影响，也缺乏有效的解法。

### 方法关键点
- 提出**latent state internalization**范式：将非语言Agent的隐层激活通过3层轻量MLP（LatentBridge）投影为k个连续态token，直接插入LLM的token流，与语言、动作token混合输入，LLM自主决定调用子Agent的时机获取最新隐态
- 两阶段训练：第一阶段冻结LLM，用子Agent的状态-策略对训练LatentBridge完成分布对齐；第二阶段用DAPO RL算法联合微调LLM与LatentBridge，子Agent全程冻结
- 构建LLAMIA-BENCH：包含6种国际象棋协作任务（行为克隆、谜题评估、自然语言解释等），均为单独LLM或单独象棋引擎无法独立解决的任务

### 关键结果
对比GPT-5.1+Lc0（工具调用）、Qwen3-14B+Lc0（工具调用）、任务专项微调模型、仅文本转写的LLAMIA-Verb等基线：14B参数的LLAMIA在所有6个任务上均超过所有基线，平均得分59，比GPT-5.1+Lc0高12分；无文本转写代理的谜题兴趣度任务上，所有文本转写方案得分≤12，LLAMIA达到52；verbalization debt随训练步、任务复杂度增大而扩大，LLM规模从4B提升到14B也无法消除该差距。

> 最值得记住的结论：LLM与非语言专业Agent的协作瓶颈是结构性的语言转写损失，而非LLM推理能力不足，潜态直接注入是比文本工具调用更高效的协作路径
