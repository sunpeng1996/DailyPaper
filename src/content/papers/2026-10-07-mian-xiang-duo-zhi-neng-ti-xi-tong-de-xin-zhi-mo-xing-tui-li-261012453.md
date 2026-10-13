---
title: Mental-Models for Multi-Agent Systems
title_zh: 面向多智能体系统的心智模型推理框架
authors:
- Hanan Gani
- Lulu Shao
- Manmohan Chandraker
affiliations:
- University of California, San Diego
arxiv_id: '2610.12453'
url: https://arxiv.org/abs/2610.12453
pdf_url: https://arxiv.org/pdf/2610.12453
published: '2026-10-07'
collected: '2026-10-13'
category: MultiAgent
direction: 多智能体协作 · 心智模型推理
tags:
- MultiAgent
- Theory of Mind
- LLM Agent
- Reinforcement Learning
- LoRA
one_liner: 提出带递归心智状态表征的多智能体框架，显式建模伙伴隐藏状态提升决策性能
practical_value: '- 电商客服/议价多Agent场景可复用递归ToM建模思路，显式抽取用户/交互方的信念、意图隐向量，优化回复策略提升转化

  - 工程上可复用「心智状态+奖励模型联合训练→蒸馏到端侧轻量策略」的范式，推理时仅部署优化后的策略，避免复杂心智推理的性能开销

  - 低资源场景下仅需25%的心智状态标注即可获得显著增益，可在现有对话/推荐标注数据中补充少量用户意图/信念标注，低成本提升效果

  - 多模态导购/推荐场景可复用该框架的多模态心智建模能力，结合用户行为、对话、浏览内容建模隐藏需求，优化推荐话术与物品排序'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前基于LLM的多智能体系统大多仅通过prompt、记忆或行为塑造优化，未显式建模交互伙伴的隐藏目标、信念、约束等心智状态，在部分可观测场景下容易误判意图、策略鲁棒性差，缺乏可跨任务复用的伙伴状态表征。

### 方法关键点
- 递归心智状态编码器：将交互历史编码为分层隐向量，一阶表征伙伴的信念、意图、思考过程，二阶表征伙伴对当前智能体的认知，保留不确定性建模
- 心智感知奖励模型：联合训练心智编码器与奖励模型，基于推断的伙伴状态评估候选动作的收益，确保心智表征服务于决策
- 策略蒸馏：用心智感知奖励作为监督信号训练独立策略，推理时仅需部署策略即可，无需额外心智推理模块，降低部署开销
训练基于LoRA适配7B级开源LLM/VLM backbone，支持纯语言、多模态场景。

### 关键实验结果
在纯语言（SOTOPIA、CRAIGSLIST-BARGAIN、BIGTOM、TOMI）和多模态（MMROLE）基准上测试，对比base LLM、SFT、GRPO等baseline：
1. SOTOPIA上Qwen2.5-7B相对base整体得分提升17.2%，跨伙伴类型平均提升7.7%
2. BIGTOM上配对TB/FB准确率平均提升26.7pp
3. Craigslist议价场景无额外微调下，walkaway率最高降低6个百分点
4. MMROLE跨域场景相对基线整体得分提升3.9%

**最值得记住的一句话**：显式的结构化伙伴心智建模是提升多智能体交互鲁棒性的有效归纳偏置，可通过训练注入策略，无需推理时额外开销。
