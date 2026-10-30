---
title: 'A-RSI: Adaptive Task Refresh for Zero-Data Multimodal Self-Improvement'
title_zh: A-RSI：面向零数据多模态自改进的自适应任务刷新机制
authors:
- Yu Liu
- Youxing Li
- Yuedong Tan
- Zhiwei Yang
- Zihan Su
- Hanqi Feng
- Shaojie Zhang
- Libin Liao
- Zihao Wan
- Chenxu Wu
affiliations:
- University of Trento
arxiv_id: '2610.38568'
url: https://arxiv.org/abs/2610.38568
pdf_url: https://arxiv.org/pdf/2610.38568
published: '2026-10-27'
collected: '2026-10-30'
category: Training
direction: 大模型自训练 · 零数据多模态自改进
tags:
- Self-Improvement
- Multimodal LLM
- Zero-Data Training
- Task Refresh
- GRPO
one_liner: 零数据多模态自改进框架，靠训练日志触发任务池刷新，无需外部标注/验证集
practical_value: '- LLM微调/RLHF场景可复用任务池饱和判定逻辑：监控训练批次内Reward方差下降幅度+训练准确率提升阈值，无需验证集即可判断是否更换训练数据，降低标注成本

  - 规则明确的垂类场景（电商类目属性识别、优惠券规则计算等）可借鉴程序化任务生成范式：固定模板库+参数采样生成带可校验标准答案的任务，无需人工标注

  - 自改进Agent训练优先采用随机新鲜任务采样，论文验证难度感知、能力感知等复杂采样策略效果不如随机采样，大幅降低工程复杂度

  - 模型效果评估需区分「输出长度达标带来的假性提升」和「实际推理能力提升」，避免把奖励hacking当成真实能力提升，适合电商文案生成、属性抽取等任务的校验'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有递归自改进（RSI）方法普遍存在两个痛点：一是仅关注生成什么新任务，忽略当前任务池学习信号耗尽的时机，容易导致训练停滞或浪费新任务资源；二是大多通过自一致性、多数投票生成监督标签，容易把模型自身的错误预测当成标注，同时依赖验证集判断训练进度，无法适配零标注场景。
### 方法关键点
- 基于训练日志的饱和判定：监控训练窗口内带Reward方差的有效prompt数量Uw、训练准确率aw，当Uw下降到阈值以下或aw提升超过预设阈值时触发任务池刷新，全程不需要访问验证/测试集
- 程序化任务生成范式：预先训练模型生成可执行的任务模板库，通过参数采样生成同一配置下的图像、问题、可校验标准答案，无需人工标注，答案正确性不依赖模型投票
- 轻量化刷新策略：触发刷新时保留模型权重，仅替换整个任务池，采用固定类目配额的随机采样抽取新任务，无需复杂的难度感知、能力感知采样逻辑
### 关键结果
在11个多模态基准测试集上验证，以Qwen3-VL-8B-Instruct为基座：仅用800个新鲜任务就把平均准确率从57.77提升到61.05，比每轮都刷新的策略高0.4个点，新任务用量仅为后者的1/4；相同训练步数下，比不刷新任务池的策略准确率高2.05个点；所有测试的复杂采样策略效果均不如随机采样。
### 最值得记住的结论
零数据自改进场景下，最简单的「训练日志判饱和+随机刷新任务」策略，效果优于各类复杂的自适应采样策略，工程成本更低收益更高。
