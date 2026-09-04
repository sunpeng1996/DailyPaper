---
title: Small Language Models as Judges for Rubric-Based Reinforcement Learning
title_zh: 面向评分规则型强化学习的小语言模型裁判方法研究
authors:
- Fengyu Xie
- Yilun Zhao
- Bingsen Chen
- Arman Cohan
- Chen Zhao
affiliations:
- New York University
- Yale University
arxiv_id: '2608.30005'
url: https://arxiv.org/abs/2608.30005
pdf_url: https://arxiv.org/pdf/2608.30005
published: '2026-08-29'
collected: '2026-09-04'
category: LLM
direction: LLM对齐 · 高效RL奖励模型
tags:
- SLM
- Reward Model
- LLM-as-Judge
- Reinforcement Learning
- Probe
- GRPO
one_liner: 基于小模型隐藏层探针的评分裁判，效果超8B生成式裁判且耗时低10.7倍
practical_value: '- 生成式推荐/电商Agent的RL对齐场景，可复用「小模型+隐藏层探针」的低成本奖励模型方案，替代大模型生成式裁判，RL训练的奖励计算耗时降低10倍量级，最终策略效果甚至优于大模型裁判方案

  - 电商商品文案、推荐理由、搜索query改写的多维度质量/合规评估场景，无需调用大模型生成判定结果，直接用1-2B小模型隐藏层接线性分类器输出各维度得分，成本低、响应快、可解释性强

  - 跨业务的评分规则适配可复用探针的迁移能力：仅需少量标注数据训练探针头，即可适配不同业务的评分维度，不需要重新微调小模型基座，落地成本极低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
基于评分规则（rubric）的强化学习支持对开放生成任务做多维度质量评估，解决了规则校验无法覆盖复杂场景的问题，但现有方案依赖付费API或7B以上大模型做裁判，奖励计算成本极高，无法规模化落地，而小模型直接生成判定结果的准确率远达不到要求，亟需探索低成本、高准确率的小模型裁判方案。
### 方法关键点
- 构建两个点式评分评估数据集：PointRubric（通用领域）、RaR-Science-Static（科学领域），覆盖多响应、逐维度标注、加权评分规则，完全匹配rubric-based RL的奖励计算需求
- 对比三种小模型判分范式：生成式判定（输出Yes/No结果）、Logprob打分（计算Yes/No token的对数概率差）、探针判定（冻结小模型基座，仅训练轻量线性分类头读取隐藏层特征输出判定概率）
- 选用Qwen3-1.7B探针作为RL奖励模型接入GRPO训练流程，与8B生成式裁判做全链路对齐对比
### 关键结果
- 静态测试集上，1.7B探针的criterion-level macro-F1达0.835，远高于同尺寸生成式裁判的0.443、Logprob裁判的0.449，仅略低于8B探针的0.864
- 用于GRPO训练时，1.7B探针将策略的RaR-Science评分从0.232提升到0.643，超过8B生成式裁判的0.594，且奖励判定耗时仅为后者的1/10.7
- 探针模型具备强迁移性：科学领域训练的探针在医疗领域评分仍达0.718 macro-F1，训练出的策略在GPQA-Diamond数据集上准确率提升0.053

> 最值得记住的结论：小模型隐藏层已蕴含足够的高质量评估信号，用探针读取的效率和效果远优于让小模型直接生成判定结果
