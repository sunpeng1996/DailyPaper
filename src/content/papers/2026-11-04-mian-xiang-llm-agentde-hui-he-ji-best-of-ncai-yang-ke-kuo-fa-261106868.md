---
title: On Turn-Level Best-of-N Sampling for Scaling LLM Agents
title_zh: 面向LLM Agent的回合级Best-of-N采样可扩展优化方法
authors:
- Jalaj Bhandari
- Dhawal Gupta
- Hongli Zhan
- Zhenting Wang
- Varad Pimpalkhute
- Zhengzhong Liu
- Eric Xing
- Rupesh Srivastava
affiliations:
- Institute of Foundation Models (IFM), MBZUAI Labs
arxiv_id: '2611.06868'
url: https://arxiv.org/abs/2611.06868
pdf_url: https://arxiv.org/pdf/2611.06868
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 推理时性能优化 · 动作选择
tags:
- LLM Agent
- Best-of-N
- Inference Scaling
- Action Selection
- Generator-Selector
one_liner: 基于生成器-选择器框架实现回合级BoN采样，无需额外训练即可提升LLM Agent长程任务表现
practical_value: '- 电商导购Agent、智能客服、广告投放决策Agent可直接复用生成器-选择器架构，用能力更强的闭源/开源大模型作为选择器，每回合从N个候选动作（回复话术、投放策略、出价参数）中选最优，无需额外训练即可快速提升业务效果

  - 搜索推荐场景的Query改写、商品文案生成、Push推送文案生成可借鉴Turn-BoN思路，替换原有单路生成+规则过滤逻辑，生成多候选后用LLM选择器打分，兼顾生成多样性和业务相关性，可降低30%以上的无效生成占比

  - 工程优化可参考文中结论：仅在关键决策回合（用户下单前导购回复、广告放量前出价调整）开启Turn-BoN，非关键回合用单路生成；优先选择N=4配置，可在总算力开销仅3-6倍的前提下拿到80%以上的效果收益

  - Agent效果评估可复用文中的过程行为指标体系，除最终成功率外，新增统计循环动作占比、无效动作占比、指令遵循率等过程指标，更精准定位Agent的能力短板'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent在长程交互任务中表现稳定性差，现有轨迹级Best-of-N采样需生成完整轨迹后再做筛选，不仅算力开销随N线性增长，也无法修正轨迹内的无效中间动作；MCTS、DFS等搜索方法依赖环境状态回滚能力，在终端操作、用户实时交互等真实场景中无法落地。

### 方法关键点
- 采用生成器-选择器架构实现Turn-BoN：每交互回合由生成器采样N个候选动作，调用开源LLM作为选择器直接选出最优动作执行，无需训练专属价值批评模型，也不需要支持环境回滚
- 选择器采用列表式打分逻辑，一次性对比所有候选动作输出最优选项，算力开销显著低于逐点打分、两两锦标赛对比方案
- 理论推导表明，当选择器选中动作的平均优势值大于0时，Turn-BoN诱导的策略性能严格优于原始生成器策略

### 关键实验结果
在Terminal-Bench v2.1长程终端任务集上验证，生成器覆盖Qwen3.6-35B、K2-Horizon-375B两个量级，选择器采用Kimi-K3、Deepseek-v4.1-Flash开源模型，N取4或8：
- pass@1准确率提升5-10pct：35B生成器从47.5%提升至55.2%，375B生成器从73.3%提升至77.9%
- 任务完成平均交互回合数降低40-50%，无效循环、重复操作占比下降14-18%，多次尝试的任务一致性显著提升
- 总token开销为基线的3-8倍，N=4时可拿到80%以上的效果收益，性价比显著高于N=8配置

### 核心结论
推理时的定向算力投入性价比高于盲目扩大模型参数，用能力更强的选择器做回合级动作筛选，是低成本快速提升Agent表现的可行路径
