---
title: Self-Evolving Coding Agents via Harness-Policy Optimization
title_zh: 基于Harness-Policy联合优化的自进化代码Agent框架
authors:
- Zhepei Wei
- Wenlin Yao
- Baolin Peng
- Danqing Wang
- Qianhui Wu
- Hao Cheng
- Yu Meng
- Jianfeng Gao
affiliations:
- Microsoft Research
- University of Virginia
- Carnegie Mellon University
arxiv_id: '2610.22791'
url: https://arxiv.org/abs/2610.22791
pdf_url: https://arxiv.org/pdf/2610.22791
published: '2026-10-15'
collected: '2026-10-20'
category: Agent
direction: Agent 自进化 · Harness-策略联合优化
tags:
- LLM Agent
- Self-Improvement
- Harness Optimization
- Policy Optimization
- Reinforcement Learning
one_liner: 交替优化Agent交互Harness与LLM策略，实现无外部依赖的代码Agent自进化
practical_value: '- 电商/推荐Agent可复用这套交替优化框架：先固定策略，让Agent分析bad case优化Prompt、工具调用逻辑等Harness组件，再固定Harness做RL微调，收益高于单模块优化

  - Harness搜索集可动态替换为每次RL训练中未解决的hard case，无需固定验证集，优化始终对准当前策略短板，适合新场景、冷启动任务快速迭代

  - 有可量化reward信号时，RL策略优化的收益显著高于SFT/RFT，导购、客服、搜索query理解类Agent微调时优先选择GRPO这类RL方法，泛化性更好

  - 优化后的Harness和策略各自都有独立收益，组合收益超过两者之和，业务迭代时可先上线优化后的Harness获取即时收益，再逐步上线微调模型降低风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent优化分为两个割裂方向：固定策略优化Harness（提示词、工作流、工具调用逻辑等交互脚手架），或固定Harness微调策略。二者单独优化存在明显短板：Harness仅适配旧策略的失效模式，对更新后的策略增益有限；策略只能学到固定Harness覆盖的轨迹，无法突破能力边界，在代码、多步工具调用等高复杂度任务上天花板明显。

### 方法关键点
- 提出Self-HPO交替优化框架，循环执行H-step与P-step实现自进化
- H-step：冻结当前策略，让策略自行分析失败轨迹，提出Harness改进候选，在当前hard任务集上筛选最优Harness
- P-step：冻结优化后的Harness，用GRPO+BAR做RL微调更新策略，筛选本轮未解决的hard任务作为下一轮H-step的搜索集
- 无需外部大模型作为Harness提案者，完全依赖自身迭代即可完成优化

### 关键实验
基于Qwen3.5-35B-A3B基线，在SWE-Bench的Verified、Multilingual、Pro三个基准上测试，对比单优化Harness、单优化策略的基线：自进化模式下平均解决率从57.8%提升至64.8%，比单RL微调基线高2.9个百分点；用Opus 4.8作为外部提案者时，SWE-Verified解决率进一步提升到71.6%；优化后的Harness单独用于基线模型提3.5个点，优化后的策略单独用于原始Harness提3.4个点，组合提升8.5个点，超过两者收益之和。

**最值得记住的一句话**：Agent的交互Harness和底层策略是强互补关系，联合交替优化的收益远高于单模块优化的线性叠加
