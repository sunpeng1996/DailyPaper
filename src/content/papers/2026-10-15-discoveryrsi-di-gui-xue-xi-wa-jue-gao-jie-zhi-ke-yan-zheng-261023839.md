---
title: 'DiscoveryRSI: Recursively Learning to Discover Valuable Hypotheses'
title_zh: DiscoveryRSI：递归学习挖掘高价值可验证研究假设
authors:
- Jianyuan Zhong
- Chenwei Wu
- Zhaochen Yu
- Xixian Jiang
- Xuewei Li
- Hao Xiao
- Xilin Dai
- Junyang Wang
- Jiaru Zou
- Zhiqing Cui
affiliations:
- PhAI Labs
- The Chinese University of Hong Kong
- University of Michigan
- Stanford University
- Harvard Medical School
arxiv_id: '2610.23839'
url: https://arxiv.org/abs/2610.23839
pdf_url: https://arxiv.org/pdf/2610.23839
published: '2026-10-15'
collected: '2026-10-19'
category: Agent
direction: 多智体科研 · 递归自提升
tags:
- MultiAgent
- Recursive Self-Improvement
- Hypothesis Generation
- Credit Assignment
- Scientific Discovery
one_liner: 提出多智体演化+递归自提升框架生成高价值可测试科研假设，性能优于GPT-6等SOTA模型
practical_value: '- 多智体演化搜索+自动评估的框架可直接复用，用于电商推荐场景的新运营策略、召回规则、候选物料生成，自动优化候选池质量

  - 假设信用分配机制可迁移到LLM生成内容的归因，比如推荐文案、搜索Query改写的效果归因，给优质生成路径加权做LoRA微调

  - 生成-评估-归因-优化的递归自提升闭环可套用到LLM4Rec迭代优化，仅用业务效果反馈即可无额外标注持续迭代模型能力'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有科研Agent无法将假设研发、实验执行过程中的经验转化为模型迭代能力，缺乏对生成路径贡献的精准归因，导致输出假设可验证性差、落地价值低，亟需可自主递归优化的假设生成框架。

### 方法关键点
- 多智体演化搜索生成假设树，设置Lead、Generation、Evolution、Critique四类角色，支持演化、修复、交叉、重启四种操作，每个假设绑定主张、研究计划、决策标准、替代解释四大核心要素
- 三层递归自提升机制：假设信用优化用TrueSkill给假设打分，将评估结果精准归因到生成路径的贡献节点，加权训练模型；Harness回放固定模型权重，定位工作流故障点优化调度逻辑；重发现将更新后的模型和工作流应用到新任务生成新经验
- 配套DFM-Bench从假设质量、修订价值、开发路径进展、研究运行质量、科学贡献五个层级全面评估研究进展

### 关键实验
在4个生命科学+4个电池领域数据集测试，对比GPT-6 Luna、GPT-5.6 Sol、Claude Opus 5等SOTA模型：两轮自提升后假设平均质量从4.86提升到5.39，每轮修订的人评得分提升+0.07，生成假设匹配后续已发表研究的比例达6.3%，是GPT-6的2.52倍。

### 核心结论
将评估结果精准归因到生成路径的贡献节点，是实现Agent递归自提升、无需额外标注即可持续优化生成质量的核心
